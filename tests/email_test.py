import sys
import unittest
sys.path.append('.')
from sanatio import Sanatio

validator = Sanatio()


class EmailTest(unittest.TestCase):
    def test_isEmail_True(self):
        self.assertTrue(validator.isEmail('test@gmail.com'))
        self.assertTrue(validator.isEmail('test@live.com'))
        self.assertTrue(validator.isEmail('test@yahoo.in'))
        self.assertTrue(validator.isEmail('test@test.org'))
        
    def test_isEmail_False(self):
        self.assertFalse(validator.isEmail('abc.gmail'))
        self.assertFalse(validator.isEmail('abc.gmail.'))
        

if __name__ == '__main__':
    unittest.main()