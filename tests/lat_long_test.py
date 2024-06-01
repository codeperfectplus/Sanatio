import sys
import unittest
sys.path.append('.')
from sanatio import Validator

validator = Validator()


class LatLongTest(unittest.TestCase):
    def test_lat_long_true(self):
        self.assertTrue(validator.isLatLong('40.689247, -74.044502'))
        self.assertTrue(validator.isLatLong('+90.0, -127.554334'))
        self.assertTrue(validator.isLatLong('-90.0, +180.0'))
        self.assertTrue(validator.isLatLong('47.1231231, 179.99999999'))
        self.assertTrue(validator.isLatLong('28.838648, 78.773331'))
        
if __name__ == '__main__':
    unittest.main()