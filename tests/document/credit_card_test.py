import sys
import unittest
sys.path.append('.')
from sanatio import Validator

validator = Validator()


class CreditCardTest(unittest.TestCase):
    def test_credit_card_true(self):
        self.assertTrue(validator.isCreditCard('4578423013769219'))
        self.assertTrue(validator.isCreditCard('4569403961014710'))
        self.assertTrue(validator.isCreditCard('6011000990139424'))
        
    def test_credit_card_false(self):
        self.assertFalse(validator.isCreditCard('370341378581367'))   # checksome false


if __name__ == '__main__':
    unittest.main()