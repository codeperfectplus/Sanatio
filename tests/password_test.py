import sys
import unittest
sys.path.append('.')
from src.main import Validator

validator = Validator()


class StrongPasswordTest(unittest.TestCase):
    def test_strong_password_true(self):
        self.assertTrue(validator.isStrongPassword('Foo@1234'))
        self.assertTrue(validator.isStrongPassword('Bar@1234'))
        self.assertTrue(validator.isStrongPassword('FooBar@1234'))
        self.assertTrue(validator.isStrongPassword('FooBar@1234'))
        
    def test_strong_password_false(self):
        self.assertFalse(validator.isStrongPassword('foo'))
        self.assertFalse(validator.isStrongPassword('foo123'))
        self.assertFalse(validator.isStrongPassword('foo@123'))
        self.assertFalse(validator.isStrongPassword('FOO@123'))
        

if __name__ == '__main__':
    unittest.main()
