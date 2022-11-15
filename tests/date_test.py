import sys
import unittest
sys.path.append('.')
from src.main import Validator

validator = Validator()


class DateTest(unittest.TestCase):
    def test_isDate_true(self):
        self.assertTrue(validator.isDate('2017-01-01'))
        self.assertTrue(validator.isDate('2017-01-31'))
    
    def test_isAfter_true(self):  # if date1 is after date2
        self.assertTrue(validator.isAfter('2020-01-01', '2019-01-01'))
        self.assertTrue(validator.isAfter('2021-01-01', '2019-01-01'))
    
    def test_isAfter_false(self):
        self.assertFalse(validator.isAfter('2017-01-01', '2018-01-01'))
        self.assertFalse(validator.isAfter('2017-01-01', '2019-01-02'))

    def test_isBefore_true(self):
        self.assertTrue(validator.isBefore('2017-01-01', '2018-01-01'))
        self.assertTrue(validator.isBefore('2017-01-01', '2019-01-02'))
        
    def test_isBefore_false(self):
        self.assertFalse(validator.isBefore('2020-01-01', '2019-01-01'))
        self.assertFalse(validator.isBefore('2021-01-01', '2019-01-01'))

if __name__ == '__main__':
    unittest.main()