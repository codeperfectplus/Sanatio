import sys
sys.path.append('.')

import unittest
from sanatio.utils.checksum import VerhoeffAlgorithm
from sanatio.utils.checksum import LuhnAlgorithm


class CheckSumTest(unittest.TestCase):
    def test_verhoeff_True(self):
        verhoeff = VerhoeffAlgorithm('9284 9436 2499')
        self.assertTrue(verhoeff.verify())
    
    def test_luhn_True(self):
        luhn = LuhnAlgorithm('4569403961014710')
        self.assertTrue(luhn.verify())
        
if __name__ == '__main__':
    unittest.main()