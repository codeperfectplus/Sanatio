import sys
import unittest
sys.path.append('.')
from sanatio import Sanatio

validator = Sanatio()


class HashTest(unittest.TestCase):
    def test_hash(self):
        pass
        

if __name__ == '__main__':
    unittest.main()