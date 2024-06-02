import sys
import unittest
sys.path.append('.')
from sanatio import Sanatio

validator = Sanatio()

class IPTest(unittest.TestCase):
    def test_isIP_True(self):
        self.assertTrue(validator.isIPV4('10.10.10.10'))
        self.assertTrue(validator.isIPV4('0.0.0.0'))
        self.assertTrue(validator.isIPV4('255.255.255.255'))
    
    def test_isIP_False(self):
        self.assertFalse(validator.isIPV4('2001:db8:0000:1:1:1:1:1'))
        self.assertFalse(validator.isIPV4('2001:0db8:85a3:0000:0000:8a2e:0370:7334'))
        self.assertFalse(validator.isIPV4('256.256.256.256'))
        
    def test_isIPV6_True(self):
        self.assertTrue(validator.isIPV6('2001:db8:0000:1:1:1:1:1'))
        self.assertTrue(validator.isIPV6('2001:0db8:85a3:0000:0000:8a2e:0370:7334'))
        self.assertTrue(validator.isIPV6('FE80:0000:0000:0000:0202:B3FF:FE1E:8329'))
        self.assertTrue(validator.isIPV6('FE80:0000:0000:0000:0202:B3FF:FE1E:8329'))
        
    def test_isIPV6_False(self):
        pass
        
    
if __name__ == '__main__':
    unittest.main()
