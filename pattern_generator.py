import os, pyvisa
from contextlib import contextmanager



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
    gpib_device = resource_manager.open_resource('GPIB0::29::INSTR', write_termination='\n')
    gpib_device.write("*RST") #Resets instrument to factory default state
    gpib_device.write("*CLS") #Clears the event registers in all register groups
    print(gpib_device.query("*IDN?"))
    
    # A block is a container for the pattern data to be output
    gpib_device.write("GROup:DELete:ALL")
    gpib_device.write("BLOCk:DELete:ALL")
    
    gpib_device.write("BLOCk:NEW \"Block1\",10000")  
    gpib_device.write("BLOCk:SELect \"Block1\"")
        
    gpib_device.write("GROup:NEW \"Group1\",2")
    gpib_device.write("SIGNal:ASSign \"Group1[1]\",\"1A1\"")
    gpib_device.write("SIGNal:ASSign \"Group1[0]\",\"1A2\"")
    
    pattern1 = ""
    pattern0 = ""
    for i in range(0,5000):
        pattern1 += "1"
        pattern0 += "0"
    
    
    gpib_device.write("SIGNal:DATa \"Group1[1]\",0,10000,\""+pattern1+pattern0+"\"")
    gpib_device.write("SIGNal:DATa \"Group1[0]\",0,10000,\""+pattern1+pattern0+"\"")
    
    gpib_device.write("SIGNal:HIGH \"Group1[1]\",0.9")    
    gpib_device.write("SIGNal:LOW \"Group1[1]\",0")    
    #gpib_device.write("SIGNal:LOW \"Group1[1]\",0")
    gpib_device.write("SIGNal:OFFSet \"Group1[1]\", 0")  
  
    
    #gpib_device.write("SIGNal:AMPLitude \"Group1[0]\",2")
    gpib_device.write("SIGNal:OFFSet \"Group1[0]\", 0")
    gpib_device.write("SIGNal:HIGH \"Group1[0]\",0.9")    
    gpib_device.write("SIGNal:LOW \"Group1[0]\",0")    

    
    #gpib_device.write("PGENA:CH2:LDELay 4ns")
    
    # Grouping is to collect the logical channels on the pattern data into a group.
    
    #gpib_device.write("TBAS:FREQuency 40MHZ")
    
    #gpib_device.write("TBAS:RUN 1")
    
    # CLOCK SETTINGS
    gpib_device.write("OUTPut:CLOCk:AMPLitude 0.9") #set clock voltage to 900mV    
    gpib_device.write("OUTPut:CLOCk:OFFSet 0.45")     
    gpib_device.write("OUTPut:CLOCk:STATe ON") # This command turns on or off the clock output.
    gpib_device.write("OUTPut:CLOCk:TIMPedance 50") # sets clock output termination impedance to 50 ohm
    gpib_device.write("TBAS:FREQuency 40MHZ")
    
    
    #Start Sequencer
    gpib_device.write("TBAS:RUN ON") # start sequencer      
    gpib_device.write("OUTPut:STATe:ALL ON") # This command turns on or off all of the outputs (all assigned outputs, clock output,DC output).



