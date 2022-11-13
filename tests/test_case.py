import sys
import unittest
sys.path.append('.')
from src.main import Validator

validator = Validator()


class ValidatorTest(unittest.TestCase):
    """ """

    def test_equals(self):
        self.assertTrue(validator.equals('foo', 'foo'))


if __name__ == '__main__':
    unittest.main()
