
import sys
import unittest
sys.path.append('.')
from sanatio.main import Validator
validator = Validator()


class EANTest(unittest.TestCase):        
    def test_isEAN_true(self):
        self.assertTrue(validator.isEAN13('8901030679216'))
        self.assertTrue(validator.isEAN13('0067238891190'))
        self.assertTrue(validator.isEAN13('6921815600015'))

    def test_isEAN_false(self):
        self.assertFalse(validator.isEAN13('890103067921'))
        self.assertFalse(validator.isEAN13('8901030679215'))

    
if __name__ == '__main__':
    unittest.main()
