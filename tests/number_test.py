import sys
import unittest
sys.path.append('.')
from sanatio import Validator

validator = Validator()


class NumberTest(unittest.TestCase):
    def test_isDivisibleBy_true_positive(self):
        self.assertTrue(validator.isDivisibleBy(10, 2))
        self.assertTrue(validator.isDivisibleBy(10, 5))
        self.assertTrue(validator.isDivisibleBy(10, 10))
        self.assertTrue(validator.isDivisibleBy(10, 1))
    
    def test_isDivisibleBy_true_negative(self):
        self.assertTrue(validator.isDivisibleBy(10, -1))
        self.assertTrue(validator.isDivisibleBy(10, -5))
        self.assertTrue(validator.isDivisibleBy(10, -10))
        self.assertTrue(validator.isDivisibleBy(-10, 2))
            
    def test_isDivisibleBy_false(self):
        self.assertFalse(validator.isDivisibleBy(10, 3))
        self.assertFalse(validator.isDivisibleBy(10, 7))
        self.assertFalse(validator.isDivisibleBy(10, 0))
        self.assertFalse(validator.isDivisibleBy("foo", "bar"))
        self.assertFalse(validator.isDivisibleBy("foo", 1))
        
    def test_toInt(self):
        self.assertEqual(validator.toInt("10"), 10)
        self.assertEqual(validator.toInt("10.0"), 10)
        self.assertEqual(validator.toInt("10.1"), 10)
        self.assertEqual(validator.toInt(10.9), 10)
        

if __name__ == '__main__':
    unittest.main()