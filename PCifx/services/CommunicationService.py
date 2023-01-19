import json
import serial
import sys


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class CommunicationService(metaclass=Singleton):

    def __init__(self):
        self.serial = serial.Serial()
        self.serial.baudrate = 9600

        self.directory = ""

        self.injectionSettings = {
            "numInj": 0,
            "Qmin": 0,
            "Qmax": 0,
            "numSteps": 0
        }
        self.globalMatrixConfig = {
            "cd25": 0,
            "cd50": 0,
            "leakage": 0
        }
        self.customScanSettings = {
            "start": 0,
            "end": 0,
            "isSinglePixel": False
        }

    def serialConnect(self, port):
        self.serial.port = port
        self.serial.open()

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

    def sendChargeScan(self):
        data = {}
        data["operation"] = "CHARGE_SCAN"
        data = json.dumps(data)

        if not self.serial.isOpen():
            print("serial port is closed")

        self.serial.write(data.encode('ascii'))
        try:
            while(True):
                incoming = self.serial.readline().strip().decode("utf-8")
                print(incoming)
                if(incoming == "EOC"):
                    print("Closing serial communication")

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

    def setCustomStart(self, num):
        self.customScanSettings["start"] = num

    def setCustomEnd(self, num):
        self.customScanSettings["end"] = num

    def setCustomSinglePixel(self, flag):
        self.customScanSettings["isSinglePixel"] = flag

    def printCustomScanSettings(self):
        print(self.customScanSettings)
