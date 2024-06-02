import sys
import unittest
sys.path.append('.')
from sanatio import Sanatio

validator = Sanatio()


class SSNTest(unittest.TestCase):
    def test_ssn_true(self):
        self.assertTrue(validator.isSSN('123-45-6789'))
        self.assertTrue(validator.isSSN('333-22-4444'))
        
    def test_ssn_false(self):
        self.assertFalse(validator.isSSN('aaa-bbb-cccc'))
        self.assertFalse(validator.isSSN('900-58-4564'))


if __name__ == '__main__':
    unittest.main()
        