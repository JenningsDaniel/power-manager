from smbus import SMBus 
from logging import getLogger
from logging.config import fileConfig 

SMBUS_NUMBER = 1
LINE_POWER = 1
BATTERY_POWER = 2

fileConfig('logging_config.ini')
log = getLogger()

i2c = SMBus(SMBUS_NUMBER)



def getPowerMode():
   rawdata = i2c.read_byte_data(0x69, 0x00)
   data = rawdata & ~(1 << 7)
   log.debug("raw: %s, data: %s", rawdata, data)

   return data

def isBatteryPower():
    if (getPowerMode() == BATTERY_POWER):
        return True
    
    return False


    
