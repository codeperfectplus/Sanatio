import sys
import unittest
sys.path.append('.')
from src.main import Validator

validator = Validator()


class LicensePlateTest(unittest.TestCase):
    def test_isLicensePlate_IN(self):
        self.assertTrue(validator.isLicensePlate('KA01HH1234', 'IN'))
        self.assertTrue(validator.isLicensePlate('Up21C1234', 'IN'))
        
    # def test_isLicensePlate_US(self):
    #     self.assertTrue(validator.isLicensePlate('CA 1234', 'US'))
        
        
if __name__ == '__main__':
    unittest.main()