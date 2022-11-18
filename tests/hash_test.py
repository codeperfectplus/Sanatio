import sys
import unittest
sys.path.append('.')
from sanatio.main import Validator

validator = Validator()


class HashTest(unittest.TestCase):
    def test_hash(self):
        pass
        

if __name__ == '__main__':
    unittest.main()