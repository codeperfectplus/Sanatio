import sys
import unittest
sys.path.append('.')
from src.main import Validator

validator = Validator()

class IPTest(unittest.TestCase):
    def test_isIP_True(self):
        self.assertTrue(validator.isIP('10.10.10.10'))
        self.assertTrue(validator.isIP('0.0.0.0'))
        self.assertTrue(validator.isIP('255.255.255.255'))
    
    def test_isIP_False(self):
        self.assertFalse(validator.isIP('2001:db8:0000:1:1:1:1:1'))
        self.assertFalse(validator.isIP('2001:0db8:85a3:0000:0000:8a2e:0370:7334'))
        self.assertFalse(validator.isIP('256.256.256.256'))
        
    
if __name__ == '__main__':
    unittest.main()
