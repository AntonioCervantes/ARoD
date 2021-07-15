from smbus import SMBus
import time

def expression(value):
    addr = 0x8 # bus address
    bus = SMBus(1) # indicates /dev/ic2-1
    bus.write_byte(addr, value)
    

### For expression testing ###
    
#while True:
    #expression(2)
    #time.sleep(5)