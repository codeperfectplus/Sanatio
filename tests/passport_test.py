import sys
import unittest
sys.path.append('.')
from src.main import Validator

validator = Validator()


class PassportTest(unittest.TestCase):
    def test_passport_true_IN(self):
        self.assertTrue(validator.isPassportNumber('A1234567', 'IN'))
        self.assertTrue(validator.isPassportNumber('A9876543', 'IN'))
        
    def test_passport_true_US(self):
        pass
        
if __name__ == '__main__':
    unittest.main()