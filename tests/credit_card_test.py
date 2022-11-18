import sys
import unittest
sys.path.append('.')
from sanatio.main import Validator

validator = Validator()


class CreditCardTest(unittest.TestCase):
    def test_credit_card_true(self):
        self.assertTrue(validator.isCreditCard('5191914942157165'))
        self.assertTrue(validator.isCreditCard('4569403961014710'))
        self.assertTrue(validator.isCreditCard('6011000990139424'))
        self.assertTrue(validator.isCreditCard('370341378581367'))


if __name__ == '__main__':
    unittest.main()