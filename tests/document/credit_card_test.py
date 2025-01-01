import sys
import unittest
from sanatio import Sanatio
sys.path.append('.')

validator = Sanatio()


class CreditCardTest(unittest.TestCase):
    def test_credit_card_true(self):
        self.assertTrue(validator.isCreditCard('4578423013769219'))
        self.assertTrue(validator.isCreditCard('4569403961014710'))
        self.assertTrue(validator.isCreditCard('6011000990139424'))

    def test_credit_card_false(self):
        self.assertFalse(
                validator.isCreditCard('370341378581368')
            )   # checksome false


if __name__ == '__main__':
    unittest.main()
