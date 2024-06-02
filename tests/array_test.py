import sys
import unittest
sys.path.append('.')
from sanatio import Validator
validator = Validator()


class ArrayTest(unittest.TestCase):
    def test_isArray_True(self):
        self.assertTrue(validator.isArray([]))
        self.assertTrue(validator.isArray([1, 2, 3]))
        self.assertTrue(validator.isArray(['a', 'b', 'c']))

    def test_isArray_False(self):
        self.assertFalse(validator.isArray('abc'))
        self.assertFalse(validator.isArray(123))

    def test_isLength_True(self):
        self.assertTrue(validator.isLength([1, 2, 3], 1, 3))
        self.assertTrue(validator.isLength([1, 2, 3], 3, 3))
        self.assertTrue(validator.isLength([1, 2, 3], 3, 3))

    def test_isLength_False(self):
        self.assertFalse(validator.isLength([1, 2, 3], 1, 2))
        self.assertFalse(validator.isLength([1, 2, 3], 4, 5))
        self.assertFalse(validator.isLength([1, 2, 3], 1, 2))

    def test_isContains_True(self):
        self.assertTrue(validator.isContains([1, 2, 3], 1))
        self.assertTrue(validator.isContains([1, 2, 3], 2))
        self.assertTrue(validator.isContains([1, 2, 3], 3))

    def test_isContains_False(self):
        self.assertFalse(validator.isContains([1, 2, 3], 4))
        self.assertFalse(validator.isContains([1, 2, 3], 5))
        self.assertFalse(validator.isContains([1, 2, 3], 6))

    def test_isUnique_True(self):
        self.assertTrue(validator.isUnique([1, 2, 3]))
        self.assertTrue(validator.isUnique(['a', 'b', 'c']))
        self.assertTrue(validator.isUnique([1, 'a', 3]))

    def test_isUnique_False(self):
        self.assertFalse(validator.isUnique([1, 2, 2]))
        self.assertFalse(validator.isUnique(['a', 'b', 'b']))
        self.assertFalse(validator.isUnique([1, 'a', 3, 3]))
    

if __name__ == '__main__':
    unittest.main()
