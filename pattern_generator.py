import os, pyvisa
from contextlib import contextmanager
import time




@contextmanager
def _stopVerboseLogging():
    original_stderr = os.dup(2) #stderr stream is linked to file descriptor 2
    blackhole = os.open(os.devnull, os.O_WRONLY) # anything written to /dev/null is discarded
    os.dup2(blackhole,2) # duplicate the blackhole to file descriptor 2, which the C library uses as stderr
    os.close(blackhole) #bh was dupòcated
    yield
    os.dup2(original_stderr, 2) #restoring the original stderr
    os.close(original_stderr)


def printConnectedDevices():
    '''
    Get GPIB devices connected
    Returns a tuple (address, IDN)
    '''
    resource_manager = pyvisa.ResourceManager()
    

    print("DEVICES CONNECTED:")


    address_list = resource_manager.list_resources()
    for address in address_list:
        if("GPIB" in address):
            gpib_device = resource_manager.open_resource(address, write_termination='\n')
            gpib_device.write("*RST") #Resets instrument to factory deffault state
            gpib_device.write("*CLS") #Clears the event registers in all register groups
            print(address)
            print(gpib_device.query("*IDN?"))
            
    


with _stopVerboseLogging():
    #printConnectedDevices()
    resource_manager = pyvisa.ResourceManager()
    gpib_device = resource_manager.open_resource('GPIB0::25::INSTR', write_termination='\n')
    gpib_device.write("*RST") #Resets instrument to factory default state
    gpib_device.write("*CLS") #Clears the event registers in all register groups
    print(gpib_device.query("*IDN?"))
    
    
    # CLOCK SETTINGS
    gpib_device.write("TBAS:LDELay ON")
    gpib_device.write("TBAS:CRANge 12") # clock range between 50MHz - 100MHz
    gpib_device.write("TBAS:DOFFset 0")
    gpib_device.write("TBAS:FREQuency 80MHZ")
    
    # A block is a container for the pattern data to be output
    gpib_device.write("GROup:DELete:ALL")
    gpib_device.write("BLOCk:DELete:ALL")
    
    gpib_device.write("BLOCk:NEW \"Block1\",80000")  
    gpib_device.write("BLOCk:SELect \"Block1\"")
        
    gpib_device.write("GROup:NEW \"Group1\",2")
    gpib_device.write("SIGNal:ASSign \"Group1[0]\",\"1A1\"") # 40Mhz clock signal
    gpib_device.write("SIGNal:ASSign \"Group1[1]\",\"1A2\"") # injection signal
    
   
    #gpib_device.write("SIGNal:AMPLitude \"Group1[0]\",2")
    gpib_device.write("SIGNal:OFFSet \"Group1[0]\", 0")
    gpib_device.write("SIGNal:HIGH \"Group1[0]\",0.9")    
    gpib_device.write("SIGNal:LOW \"Group1[0]\",0")
    #gpib_device.write("SIGNal:HLIMit \"Group1[0]\",0") 
    #gpib_device.write("SIGNal:LLIMit \"Group1[0]\",0")
    #gpib_device.write("SIGNal:LIMit \"Group1[0]\",0") 
    gpib_device.write("SIGNal:LDELay \"Group1[0]\",0") 

    
    injectionAmplitude = "0.8"
    gpib_device.write("SIGNal:OFFSet \"Group1[1]\", 0")
    gpib_device.write("SIGNal:HIGH \"Group1[1]\","+injectionAmplitude)    
    gpib_device.write("SIGNal:LOW \"Group1[1]\",0")
    #gpib_device.write("SIGNal:HLIMit \"Group1[1]\",0") 
    #gpib_device.write("SIGNal:LLIMit \"Group1[1]\",0")
    #gpib_device.write("SIGNal:LIMit \"Group1[1]\",0") 
    delay = "0ns"
    gpib_device.write("SIGNal:LDELay \"Group1[1]\","+delay+"") 
    
    patternClock = ""
    patternInjection1 = ""
    patternInjection0 = ""
    for i in range(0,40000):
        patternClock += "01"
        patternInjection1 += "1"
        patternInjection0 += "0"
    
    #print(patternInjection1+patternInjection0)
    
    gpib_device.write("SIGNal:DATa \"Group1[0]\",0,80000,\""+patternClock+"\"")
    gpib_device.write("SIGNal:DATa \"Group1[1]\",0,80000,\""+patternInjection1+patternInjection0+"\"")
    
    

    
    #gpib_device.write("PGENA:CH2:LDELay 4ns")
    
    # Grouping is to collect the logical channels on the pattern data into a group.
    
    #gpib_device.write("TBAS:FREQuency 40MHZ")
    
    #gpib_device.write("TBAS:RUN 1")
    

    
    
    #Start Sequencer
    gpib_device.write("TBAS:RUN ON") # start sequencer      
    gpib_device.write("OUTPut:STATe:ALL ON") # This command turns on or off all of the outputs (all assigned outputs, clock output,DC output).

    #time.sleep(5)
    

    #delays = ["0ns", "2ns", "4ns", "10ns", "12ns", "18ns", "20ns", "25ns"]
    
    #for t in delays:
    #    time.sleep(5)
    #    print(t)
    #    gpib_device.write("SIGNal:LDELay \"Group1[1]\","+t) 
     
    
    
    amplitudes = ["0.8", "0.7","0.6","0.5","0.1", "0.05", "0.03"]
    
    for x in amplitudes:
        time.sleep(8)
        print(x)
        gpib_device.write("SIGNal:HIGH \"Group1[1]\","+x)    
   
    




   


 

