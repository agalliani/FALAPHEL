import os, pyvisa
from contextlib import contextmanager
import time


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]




class DTGService(metaclass=Singleton):
 
    def __init__(self):
        self.conversionQV = 0.02/1000.0 #vth 20mV at 1000 electrons
        self.resource_manager = pyvisa.ResourceManager()
        self.gpib_device = self.resource_manager.open_resource('GPIB0::25::INSTR', write_termination='\n')
        self.gpib_device.write("*RST") #Resets instrument to factory default state
        self.gpib_device.write("*CLS") #Clears the event registers in all register groups
        print("CONNECTED TO INSTRUMENT:")
        print(self.gpib_device.query("*IDN?"))
        
        
        
    def sendSettings(self, initChargeAmplitude):
        # CLOCK SETTINGS
        self.gpib_device.write("TBAS:LDELay ON")
        self.gpib_device.write("TBAS:CRANge 12") # clock range between 50MHz - 100MHz
        self.gpib_device.write("TBAS:DOFFset 0")
        self.gpib_device.write("TBAS:FREQuency 80MHZ")
        
        
   
        # A block is a container for the pattern data to be output
        self.gpib_device.write("GROup:DELete:ALL")
        self.gpib_device.write("BLOCk:DELete:ALL")
    
        self.gpib_device.write("BLOCk:NEW \"Block1\",80000")  
        self.gpib_device.write("BLOCk:SELect \"Block1\"")
        
        self.gpib_device.write("GROup:NEW \"Group1\",2")
        self.gpib_device.write("SIGNal:ASSign \"Group1[0]\",\"1A1\"") # 40Mhz clock signal
        self.gpib_device.write("SIGNal:ASSign \"Group1[1]\",\"1A2\"") # injection signal
    
   
        #self.gpib_device.write("SIGNal:AMPLitude \"Group1[0]\",2")
        self.gpib_device.write("SIGNal:OFFSet \"Group1[0]\", 0")
        self.gpib_device.write("SIGNal:HIGH \"Group1[0]\",0.9")    
        self.gpib_device.write("SIGNal:LOW \"Group1[0]\",0")
        #self.gpib_device.write("SIGNal:HLIMit \"Group1[0]\",0") 
        #self.gpib_device.write("SIGNal:LLIMit \"Group1[0]\",0")
        #self.gpib_device.write("SIGNal:LIMit \"Group1[0]\",0") 
        self.gpib_device.write("SIGNal:LDELay \"Group1[0]\",0") 


        self.gpib_device.write("SIGNal:OFFSet \"Group1[1]\", 0")
        self.gpib_device.write("SIGNal:HIGH \"Group1[1]\","+str(initChargeAmplitude*self.conversionQV)) #set qmax at signal startup   
        self.gpib_device.write("SIGNal:LOW \"Group1[1]\",0")
        #self.gpib_device.write("SIGNal:HLIMit \"Group1[1]\",0") 
        #self.gpib_device.write("SIGNal:LLIMit \"Group1[1]\",0")
        #self.gpib_device.write("SIGNal:LIMit \"Group1[1]\",0") 
        delay = "0ns"
        self.gpib_device.write("SIGNal:LDELay \"Group1[1]\","+delay+"") 
        
        # PATTERN DATA SETTINGS
        patternClock = ""
        patternInjection1 = ""
        patternInjection0 = ""
        for i in range(0,40000):
            patternClock += "01"
            patternInjection1 += "1"
            patternInjection0 += "0"
        self.gpib_device.write("SIGNal:DATa \"Group1[0]\",0,80000,\""+patternClock+"\"")
        self.gpib_device.write("SIGNal:DATa \"Group1[1]\",0,80000,\""+patternInjection1+patternInjection0+"\"")
    
        
    def startSequencer(self):
        #Start Sequencer
        self.gpib_device.write("TBAS:RUN ON") # start sequencer      
        self.gpib_device.write("OUTPut:STATe:ALL ON") # This command turns on or off all of the outputs (all assigned outputs, clock output,DC output).

    def stopSequencer(self):
        #Start Sequencer
        self.gpib_device.write("TBAS:RUN OFF") # start sequencer      
        self.gpib_device.write("OUTPut:STATe:ALL OFF") # This command turns on or off all of the outputs (all assigned outputs, clock output,DC output).

  
    def setInjectionAmplitude(self,Qin):
        
        amplitude = str(round(Qin*self.conversionQV,6))
        print(amplitude, " V")
        self.gpib_device.write("SIGNal:HIGH \"Group1[1]\","+amplitude)    

        
  