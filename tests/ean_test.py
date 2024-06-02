
import sys
import random
import unittest
sys.path.append('.')
from sanatio import Sanatio
validator = Sanatio()

def generate_ean13_number():
    """ generate ean13 number """
    ean_number = ''.join(random.choices('0123456789', k=12))
    total_sum = sum(int(ean_number[i]) * 3 if i % 2 != 0 else \
                    int(ean_number[i]) for i in range(len(ean_number)))
    unit_digit = 0 if total_sum % 10 == 0 else 10 - (total_sum % 10)
    return ean_number + str(unit_digit)

class EANTest(unittest.TestCase):        
    def test_isEAN_true(self):
        self.assertTrue(validator.isEAN13(generate_ean13_number()))
        self.assertTrue(validator.isEAN13(generate_ean13_number()))
        self.assertTrue(validator.isEAN13(generate_ean13_number()))
        self.assertTrue(validator.isEAN13(generate_ean13_number()))
        self.assertTrue(validator.isEAN13(generate_ean13_number()))
        self.assertTrue(validator.isEAN13(generate_ean13_number()))

    def test_isEAN_false(self):
        self.assertFalse(validator.isEAN13('890103067921'))
        self.assertFalse(validator.isEAN13('8901030679215'))

    
if __name__ == '__main__':
    unittest.main()
