import sys
sys.path.append('.')

import unittest
from sanatio.utils.checksum_algorithms.verhoeff_algorithm import VerhoeffAlgorithm
from sanatio.utils.checksum_algorithms.luhn_algorithm import LuhnAlgorithm

verhoeff = VerhoeffAlgorithm()
luhn = LuhnAlgorithm()

class CheckSumTest(unittest.TestCase):
    def test_verhoeff_True(self):
        self.assertTrue(verhoeff.verify('9284 9436 2499'))
    
    def test_luhn_True(self):
        self.assertTrue(luhn.verify('4569403961014710'))
        
if __name__ == '__main__':
    unittest.main()