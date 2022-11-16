import sys
import unittest
sys.path.append('.')
from src.main import Validator

validator = Validator()


class PostalCodeTest(unittest.TestCase):
    def test_isPostalCode_IN(self):
        self.assertTrue(validator.isPostalCode('560037', 'IN'))
        self.assertFalse(validator.isPostalCode('560037-1234', 'IN'))
    
    def test_isPostalCode_US(self):
        self.assertTrue(validator.isPostalCode('56003', 'US'))
        self.assertTrue(validator.isPostalCode('56003-1234', 'US'))
        self.assertTrue(validator.isPostalCode('95100-4223', 'US'))
        self.assertFalse(validator.isPostalCode('56003 1234', 'US'))
        self.assertFalse(validator.isPostalCode('56003-12345', 'US'))
        
    def test_isPostalCode_AF(self):
        self.assertTrue(validator.isPostalCode('1043', 'AF'))
        self.assertTrue(validator.isPostalCode('1390', 'AF'))
        self.assertTrue(validator.isPostalCode('1001', 'AF'))
        
        self.assertFalse(validator.isPostalCode('104', 'AF'))
        self.assertFalse(validator.isPostalCode('4410', 'AF'))
        self.assertFalse(validator.isPostalCode('10001', 'AF'))
        
        
if __name__ == '__main__':
    unittest.main()