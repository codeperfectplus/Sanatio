import sys
import unittest
sys.path.append('.')
from sanatio import Sanatio

validator = Sanatio()


class StrongPasswordTest(unittest.TestCase):
    def test_strong_password_true(self):
        self.assertTrue(validator.isStrongPassword('Foo@1234'))
        self.assertTrue(validator.isStrongPassword('Bar@1234'))
        self.assertTrue(validator.isStrongPassword('FooBar@1234'))
        self.assertTrue(validator.isStrongPassword('FooBar@1234'))
        self.assertTrue(validator.isStrongPassword('FooBar1234', special_chars=False))
        self.assertTrue(validator.isStrongPassword('foobar@1234', uppercase=False))
        self.assertTrue(validator.isStrongPassword('1234', min_length=4,
                                                   uppercase=False, 
                                                   lowercase=False, 
                                                   special_chars=False))
        
        
    def test_strong_password_false(self):
        self.assertFalse(validator.isStrongPassword('foo'))
        self.assertFalse(validator.isStrongPassword('foo123'))
        self.assertFalse(validator.isStrongPassword('foo@123'))
        self.assertFalse(validator.isStrongPassword('FOO@123'))
        self.assertFalse(validator.isStrongPassword('Foo@1234', min_length=13))
        
        

if __name__ == '__main__':
    unittest.main()
