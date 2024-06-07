import sys
import datetime
import unittest
sys.path.append('.')
from sanatio import Sanatio

validator = Sanatio()


class BaseTest(unittest.TestCase):

    def test_isvalidString(self):
        self.assertTrue(validator.isvalidString('hello'))
        self.assertFalse(validator.isvalidString(123))
        self.assertFalse(validator.isvalidString(''))

    def test_isvalidNumber(self):
        self.assertTrue(validator.isvalidNumber(123))
        self.assertFalse(validator.isvalidNumber('hello'))

    def test_isvalidBoolean(self):
        self.assertTrue(validator.isvalidBoolean(True))
        self.assertTrue(validator.isvalidBoolean(False))
        self.assertFalse(validator.isvalidBoolean('hello'))

    def test_removeSpaces(self):
        self.assertEqual(validator.removeSpaces('hello world'), 'helloworld')
        self.assertEqual(validator.removeSpaces(' hello world '), 'helloworld')
        self.assertEqual(validator.removeSpaces(''), None)

    def test_boolConversion(self):
        self.assertTrue(validator.boolConversion('True'))
        self.assertTrue(validator.boolConversion('true'))
        self.assertTrue(validator.boolConversion('TRUE'))
        self.assertTrue(validator.boolConversion('1'))
        self.assertTrue(validator.boolConversion(1))
        self.assertTrue(validator.boolConversion(True))
        self.assertFalse(validator.boolConversion('False'))
        self.assertFalse(validator.boolConversion('false'))
        self.assertFalse(validator.boolConversion('FALSE'))
        self.assertFalse(validator.boolConversion('0'))
        self.assertFalse(validator.boolConversion(0))
        self.assertFalse(validator.boolConversion(False))

    def test_boolConversion_with_output(self):
        self.assertTrue(validator.boolConversion('yes', [1, 0]))
        self.assertTrue(validator.boolConversion('y', [1, 0]))
        self.assertTrue(validator.boolConversion('YES', [1, 0]))
        self.assertTrue(validator.boolConversion('Y', [1, 0]))
        self.assertFalse(validator.boolConversion('no', [1, 0]))
        self.assertFalse(validator.boolConversion('n', [1, 0]))
        self.assertFalse(validator.boolConversion('NO', [1, 0]))
        self.assertFalse(validator.boolConversion('N', [1, 0]))
        self.assertTrue(validator.boolConversion('t', [1, 0]))


if __name__ == '__main__':
    unittest.main()