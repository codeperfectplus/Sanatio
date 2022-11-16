import sys
import unittest
sys.path.append('.')
from src.main import Validator

validator = Validator()


class PassportTest(unittest.TestCase):
    def test_passport_true_IN(self):
        self.assertTrue(validator.isPassportNumber('A1234567', 'IN'))
        self.assertTrue(validator.isPassportNumber('A9876543', 'IN'))
        self.assertTrue(validator.isPassportNumber('C1234564', 'IN'))
        
    def test_passport_false_IN(self):
        self.assertFalse(validator.isPassportNumber('123456789', 'IN'))
        self.assertFalse(validator.isPassportNumber('987654321', 'IN'))
        self.assertFalse(validator.isPassportNumber('342143556', 'IN'))
        self.assertFalse(validator.isPassportNumber('12345678', 'IN'))
    
    def test_passport_true_US(self):
        self.assertTrue(validator.isPassportNumber('123456789', 'US'))
        self.assertTrue(validator.isPassportNumber('987654321', 'US'))
        self.assertTrue(validator.isPassportNumber('342143556', 'US'))
        
    def test_passport_false_US(self):
        self.assertFalse(validator.isPassportNumber('A1234567', 'US'))
        self.assertFalse(validator.isPassportNumber('A9876543', 'US'))
        self.assertFalse(validator.isPassportNumber('12345678', 'US'))
        self.assertFalse(validator.isPassportNumber('1234567890', 'US'))
        
    
        
if __name__ == '__main__':
    unittest.main()