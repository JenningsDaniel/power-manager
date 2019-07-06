from smbus import SMBus 
from logging import StreamHandler, getLogger

SMBUS_NUMBER = 1
LINE_POWER = 1
BATTERY_POWER = 2

i2c = SMBus(SMBUS_NUMBER)


handler = StreamHandler()
#handler.setFormatter(logging.BASIC_FORMAT)
root = getLogger()
root.setLevel("DEBUG")
root.addHandler(handler)

log = getLogger("test1")

def getPowerMode():
   rawdata = i2c.read_byte_data(0x69, 0x00)
   data = rawdata & ~(1 << 7)
   log.debug("raw: %s, data: %s", rawdata, data)

   return data

def isBatteryPower():
    if (getPowerMode() == BATTERY_POWER):
        return True
    
    return False


    
