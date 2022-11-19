import sys
import unittest
sys.path.append('.')
from sanatio.main import Validator

validator = Validator()


class AadharCardTest(unittest.TestCase):
    def test_isAadharCard_True(self):
        self.assertTrue(validator.isAadharCard('9284 9436 2499'))
        self.assertTrue(validator.isAadharCard(' 9284 9436 2499 '))
    
    def test_isAadharCard_False(self):
        self.assertFalse(validator.isAadharCard('9284 9436 2493'))  # last digit is wrong
        self.assertFalse(validator.isAadharCard('9284 9436 249'))  # too short
        self.assertFalse(validator.isAadharCard('9284 9436 24999'))  # too long
        self.assertFalse(validator.isAadharCard('1234 5678 9012'))  # starts with 0/1
        self.assertFalse(validator.isAadharCard('9284 9436 249a'))  # contains non-digit
        
if __name__ == '__main__':
    unittest.main()