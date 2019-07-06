import unittest
from power_mode import getPowerMode, isBatteryPower
from mock import patch

class TestPowerMode(unittest.TestCase):
    
    @patch('power_mode.i2c')
    def test_line_power_mode(self, mock_i2c):
        i2c = mock_i2c
        i2c.read_byte_data.return_value =  1

        self.assertEqual(getPowerMode(), 1)

    @patch('power_mode.i2c')
    def test_battery_power_mode(self, mock_i2c):
        i2c = mock_i2c
        i2c.read_byte_data.return_value =  2

        self.assertEqual(getPowerMode(), 2)

    @patch('power_mode.i2c')
    def test_isBatteryPower(self, mock_i2c):
        i2c = mock_i2c
        i2c.read_byte_data.return_value =  2

        self.assertTrue(isBatteryPower())

if __name__ == '__main__':
    unittest.main()
