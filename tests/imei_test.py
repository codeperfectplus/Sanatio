import sys
import unittest
sys.path.append('.')
from src.main import Validator

validator = Validator()


class IMEITest(unittest.TestCase):
    def test_isIMEI_true(self):
        self.assertTrue(validator.isIMEI('123456789012345'))
        self.assertTrue(validator.isIMEI('123456789012345'))
        self.assertTrue(validator.isIMEI('123456789012345'))
        self.assertTrue(validator.isIMEI('123456789012345'))
        
    def test_isIMEI_false(self):
        self.assertFalse(validator.isIMEI('12345678901234'))
        self.assertFalse(validator.isIMEI('1234567890123456'))
        self.assertFalse(validator.isIMEI('123456789012345a'))
        self.assertFalse(validator.isIMEI('123456789012345A'))
        self.assertFalse(validator.isIMEI('123456789012345213'))
        self.assertFalse(validator.isIMEI('1234567890123452'))

  
if __name__ == '__main__':
    unittest.main()
