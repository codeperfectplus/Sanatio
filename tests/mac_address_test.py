import sys
import unittest
sys.path.append('.')
from sanatio import Validator

validator = Validator()


class MacAddressTest(unittest.TestCase):
    def test_macAddress(self):
        self.assertTrue(validator.isMACAddress('00:00:00:00:00:00'))
        self.assertTrue(validator.isMACAddress('00-00-00-00-00-00'))
        self.assertTrue(validator.isMACAddress('00:24:17:b1:cc:cc'))
        self.assertTrue(validator.isMACAddress('20:89:86:9a:86:24'))
        
if __name__ == '__main__':
    unittest.main()