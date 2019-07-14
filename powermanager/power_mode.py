from ConfigParser import SafeConfigParser
from smbus import SMBus 
from logging import getLogger
from logging.config import fileConfig 

LINE_POWER = 1
BATTERY_POWER = 2

parser = SafeConfigParser()
parser.read('config.ini')

fileConfig(parser.get('DEFAULT', 'LoggingConfigFile'))

log = getLogger()

i2c = SMBus(parser.getint('DEFAULT', 'SMBusNumber'))



def getPowerMode():
   rawdata = i2c.read_byte_data(0x69, 0x00)
   data = rawdata & ~(1 << 7)
   log.debug("raw: %s, data: %s", rawdata, data)

   return data

def isBatteryPower():
    if (getPowerMode() == BATTERY_POWER):
        return True
    
    return False


    
