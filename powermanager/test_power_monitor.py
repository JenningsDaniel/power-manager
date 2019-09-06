import unittest
from power_monitor import monitorPower
from mock import patch
from time import gmtime

class TestPowerMonitor(unittest.TestCase):

    @patch('power_mode.isBatteryPower')
    def testLingPowerFiveSeconds(self, mock_isBatteryPower):
        isBatteryPower = mock_isBatteryPower
        isBatteryPower.return_value = False 

        monitorPower()

        
if __name__ == '__main__':
    unittest.main()

