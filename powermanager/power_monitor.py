from ConfigParser import SafeConfigParser
from logging import getLogger
from logging.config import fileConfig 
from power_mode import isBatteryPower
from time import sleep

parser = SafeConfigParser()
parser.read('config.ini')

fileConfig(parser.get('DEFAULT', 'LoggingConfigFile'))

log = getLogger()

def monitorPower():
    while not isBatteryPower():
        sleep(parser.getint('DEFAULT', 'LinePowerSleepTimeSeconds'))

