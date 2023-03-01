from glob import glob
import json
import serial
import sys

from services.DTGService import DTGService

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class CommunicationService(metaclass=Singleton):

    def __init__(self):
        self.DTGService = DTGService()
        
        
        self.serial = serial.Serial()
        self.serial.baudrate = 9600

        self.directory = ""

        self.injectionSettings = {
            "numInj": 200,
            "Qmin": 400,
            "Qmax": 1600,
            "numSteps": 50
        }
        self.globalMatrixConfig = {
            "cd25": 0,
            "cd50": 0,
            "leakage": 0,
        }
        self.customScanSettings = {
            "start": 0,
            "end": 0,
            "isSinglePixel": False
        }

        # 10bit config mask with LKG, C0 and C1 disabled.
        self.mask = 0b1000111111

    def serialConnect(self, port):
        #print("Connection request")
        self.serial.port = port
        self.serial.open()
        
        data = {
            "operation": "START"
        }

        self.sendJsonData(data)        

    def getSerialPorts(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cynwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    def sendJsonData(self, data):
        data = json.dumps(data)

        if not self.serial.isOpen():
            print("serial port is closed")
        
        #print(data)

        self.serial.write(data.encode('ascii'))
        try:
            while(True):
                incoming = self.serial.readline().strip().decode("utf-8")
                print(incoming)
                if("FCS1" in incoming):
                    initChargeAmplitude = float(incoming.split("-")[1])
                    self.DTGService.sendSettings(initChargeAmplitude)
                    self.DTGService.startSequencer()
                if("UPAMP" in incoming):
                    self.DTGService.setInjectionAmplitude(float(incoming.split("-")[2]))
                if(incoming == "EOC"):
                    #print("Closing serial communication")

                    break
        except Exception as e:
            print(e)

            pass

    def sendStop(self):
        if self.serial.is_open:
            data = {}
            data["operation"] = "STOP"
            data = json.dumps(data)

            self.serial.write(data.encode('ascii'))
            # serialPort.flush()
            
            self.DTGService.stopSequencer()
            try:
                while(True):
                    incoming = self.serial.readline().strip().decode("utf-8")
                    print(incoming)
                    if("EOC" in incoming):
                        self.serial.close()
                        break
            except Exception as e:
                print(e)
                pass
        else:
            print("Attempting a connection that does not exist")
            
    

    def setNumInjection(self, num):
        self.injectionSettings["numInj"] = num

    def setQmin(self, num):
        self.injectionSettings["Qmin"] = num

    def setQmax(self, num):
        self.injectionSettings["Qmax"] = num

    def setNumSteps(self, num):
        self.injectionSettings["numSteps"] = num

    def printInjSet(self):
        print(self.injectionSettings)

    def setCD25(self, num):
        self.globalMatrixConfig["cd25"] = num

    def setCD50(self, num):
        self.globalMatrixConfig["cd50"] = num

    def setLeakage(self, num):
        self.globalMatrixConfig["leakage"] = num

    def printGlobalMatrixConfig(self):
        print(self.globalMatrixConfig)
        #self.sendFullScanRequest()

    def setCustomStart(self, num):
        self.customScanSettings["start"] = num

    def setCustomEnd(self, num):
        self.customScanSettings["end"] = num

    def setCustomSinglePixel(self, flag):
        self.customScanSettings["isSinglePixel"] = flag

    def printCustomScanSettings(self):
        print(self.customScanSettings)

    def sendFullScanRequest(self):
        setup = self.mask

        if(self.globalMatrixConfig["leakage"] == 1):
            setup = self.set_bit(setup, 8, 1)

        if(self.globalMatrixConfig["cd25"] == 1):
            setup = self.set_bit(setup, 7, 1)

        if(self.globalMatrixConfig["cd50"] == 1):
            setup = self.set_bit(setup, 6, 1)

        body = {
            "operation": "CHARGE_SCAN_FULL_MATRIX",
            "setup": bin(setup),
            "numInj": self.injectionSettings["numInj"],
            "numStep": self.injectionSettings["numSteps"],
            "Qmin": self.injectionSettings["Qmin"],
            "Qmax": self.injectionSettings["Qmax"]
        }

        print(body)

        self.sendJsonData(body)

    def set_bit(self, v, index, x):
        """
        If x is True, set the bit at index in v to 1. If x is False, set the bit at index in v to 0.
        Set the index:th bit of v to 1 if x is truthy, else to 0, and return the new value.

        :param v: the value to be modified
        :param index: the index of the bit you want to set
        :param x: The value to set the bit to. If x is anything other than 0, the bit is set. Otherwise,
        it's cleared
        :return: The value of v with the bit at index set to x.
        """

        # Compute mask, an integer with just bit 'index' set.
        mask = 1 << index
        # Clear the bit indicated by the mask (if x is False)
        v &= ~mask
        if x:
            # If x was True, set the bit indicated by the mask.
            v |= mask
        return v            # Return the result, we're done.
