import sys
import unittest
sys.path.append('.')
from src.main import Validator

validator = Validator()


class MobilePhoneTest(unittest.TestCase):
    def test_mobilePhone_IN(self):
        self.assertTrue(validator.isMobilePhone('9876543210', 'IN'))
        self.assertTrue(validator.isMobilePhone('9876543210', 'IN'))
        self.assertTrue(validator.isMobilePhone('+919876543210', 'IN'))
    
    def test_mobilePhone_US(self):
        self.assertTrue(validator.isMobilePhone('9876543210', 'US'))
        self.assertTrue(validator.isMobilePhone('+19876543210', 'US'))
        self.assertTrue(validator.isMobilePhone('19876543210', 'US'))
    
    
        
if __name__ == '__main__':
    unittest.main()