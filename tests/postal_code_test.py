import sys
import unittest
sys.path.append('.')
from src.main import Validator

validator = Validator()


class PostalCodeTest(unittest.TestCase):
    def test_isPostalCode_IN_True(self):
        self.assertTrue(validator.isPostalCode('560037', 'IN'))
        self.assertTrue(validator.isPostalCode('110016', 'IN'))
        self.assertTrue(validator.isPostalCode('110001', 'IN'))
        self.assertTrue(validator.isPostalCode('244242', 'IN'))
        
    def test_isPostalCode_IN_False(self):
        self.assertFalse(validator.isPostalCode('560037-1234', 'IN'))
        self.assertFalse(validator.isPostalCode('56003', 'IN'))
        self.assertFalse(validator.isPostalCode('12345', 'IN'))
        self.assertFalse(validator.isPostalCode('5600371234', 'IN'))
    
    def test_isPostalCode_US_True(self):
        self.assertTrue(validator.isPostalCode('56003', 'US'))
        self.assertTrue(validator.isPostalCode('56003-1234', 'US'))
        self.assertTrue(validator.isPostalCode('95100-4223', 'US'))
        
    def test_isPostalCode_US_False(self):
        self.assertFalse(validator.isPostalCode('56003-12345', 'US'))
        self.assertFalse(validator.isPostalCode('56003 1234', 'US'))
        self.assertFalse(validator.isPostalCode('56003-123', 'US'))
        self.assertFalse(validator.isPostalCode('5600', 'US'))
        self.assertFalse(validator.isPostalCode('56003-12345', 'US'))
        
    def test_isPostalCode_AF_True(self):
        self.assertTrue(validator.isPostalCode('1043', 'AF'))
        self.assertTrue(validator.isPostalCode('1390', 'AF'))
        self.assertTrue(validator.isPostalCode('1001', 'AF'))
    
    def test_isPostalCode_AF_False(self):
        self.assertFalse(validator.isPostalCode('104', 'AF'))
        self.assertFalse(validator.isPostalCode('4410', 'AF'))
        self.assertFalse(validator.isPostalCode('10001', 'AF'))
    
    def test_isPostalCode_SA_True(self):
        self.assertTrue(validator.isPostalCode('12345', 'SA'))
        self.assertTrue(validator.isPostalCode('12345-1234', 'SA'))
        self.assertTrue(validator.isPostalCode('24424-4232', 'SA'))
        
    def test_isPostalCode_SA_False(self):
        self.assertFalse(validator.isPostalCode('1234', 'SA'))
        self.assertFalse(validator.isPostalCode('123456', 'SA'))
        self.assertFalse(validator.isPostalCode('12345-12345', 'SA'))
    
    def test_isPostalCode_SG_True(self):
        self.assertTrue(validator.isPostalCode('123456', 'SG'))
        self.assertTrue(validator.isPostalCode('436723', 'SG'))
        
    def test_isPostalCode_SG_False(self):
        self.assertFalse(validator.isPostalCode('12345', 'SG'))
        self.assertFalse(validator.isPostalCode('1234567', 'SG'))
        
    def test_isPostal_ZA_True(self):
        self.assertTrue(validator.isPostalCode('1234', 'ZA'))
        self.assertTrue(validator.isPostalCode('4321', 'ZA'))
        self.assertTrue(validator.isPostalCode('8764', 'ZA'))

    def test_isPostalCode_ZA_False(self):
        self.assertFalse(validator.isPostalCode('123', 'ZA'))
        self.assertFalse(validator.isPostalCode('12345', 'ZA'))
        self.assertFalse(validator.isPostalCode('123456', 'ZA'))
        
    def test_isPostalCode_PK_True(self):
        self.assertTrue(validator.isPostalCode('12345', 'PK'))
        self.assertTrue(validator.isPostalCode('54321', 'PK'))
        self.assertTrue(validator.isPostalCode('87654', 'PK'))
        
    def test_isPostalCode_PK_False(self):
        self.assertFalse(validator.isPostalCode('1234', 'PK'))
        self.assertFalse(validator.isPostalCode('123456', 'PK'))
        self.assertFalse(validator.isPostalCode('110016', 'PK'))
        self.assertFalse(validator.isPostalCode('110001', 'PK'))
        
    def test_isPostalCode_AM_True(self):
        self.assertTrue(validator.isPostalCode('1234', 'AM'))
        self.assertTrue(validator.isPostalCode('4321', 'AM'))
        self.assertTrue(validator.isPostalCode('8764', 'AM'))
        
    def test_isPostalCode_AM_False(self):
        self.assertFalse(validator.isPostalCode('123', 'AM'))
        self.assertFalse(validator.isPostalCode('12345', 'AM'))
        self.assertFalse(validator.isPostalCode('123456', 'AM'))
        
    def test_isPostalCode_AR_True(self):
        self.assertTrue(validator.isPostalCode('B1636FDA', 'AR'))
        self.assertTrue(validator.isPostalCode('C1636ABC', 'AR'))
        self.assertTrue(validator.isPostalCode('Y5900FNF', 'AR'))
    
    def test_isPostalCode_AR_False(self):
        self.assertFalse(validator.isPostalCode('B1636FD', 'AR'))
        self.assertFalse(validator.isPostalCode('B1636FDAA', 'AR'))
        self.assertFalse(validator.isPostalCode('B1636FDA1', 'AR'))
        self.assertFalse(validator.isPostalCode('B1636FDA1', 'AR'))
        self.assertFalse(validator.isPostalCode('B1636FDA1', 'AR'))
        
    def test_isPostalCode_AT_True(self):
        self.assertTrue(validator.isPostalCode('1234', 'AT'))
        self.assertTrue(validator.isPostalCode('4321', 'AT'))
        self.assertTrue(validator.isPostalCode('8764', 'AT'))
        
    def test_isPostalCode_AT_False(self):
        self.assertFalse(validator.isPostalCode('123', 'AT'))
        self.assertFalse(validator.isPostalCode('12345', 'AT'))
        self.assertFalse(validator.isPostalCode('123456', 'AT'))
    
    def test_isPostalCode_AU_True(self):
        self.assertTrue(validator.isPostalCode('1234', 'AU'))
        self.assertTrue(validator.isPostalCode('4321', 'AU'))
        self.assertTrue(validator.isPostalCode('5678', 'AU'))
    
    def test_isPostalCode_AU_False(self):
        self.assertFalse(validator.isPostalCode('123', 'AU'))
        self.assertFalse(validator.isPostalCode('12345', 'AU'))
        self.assertFalse(validator.isPostalCode('123456', 'AU'))
        
    def test_isPostalCode_AZ_True(self):
        self.assertTrue(validator.isPostalCode('1234', 'AZ'))
        self.assertTrue(validator.isPostalCode('4321', 'AZ'))
        self.assertTrue(validator.isPostalCode('8764', 'AZ'))
        
    def test_isPostalCode_AZ_False(self):
        self.assertFalse(validator.isPostalCode('123', 'AZ'))
        self.assertFalse(validator.isPostalCode('12345', 'AZ'))
        self.assertFalse(validator.isPostalCode('123456', 'AZ'))
        
    def test_isPostalCode_BD_True(self):
        self.assertTrue(validator.isPostalCode('1234', 'BD'))
        self.assertTrue(validator.isPostalCode('4321', 'BD'))
        self.assertTrue(validator.isPostalCode('8764', 'BD'))
        
    def test_isPostalCode_BD_False(self):
        self.assertFalse(validator.isPostalCode('123', 'BD'))
        self.assertFalse(validator.isPostalCode('12345', 'BD'))
        self.assertFalse(validator.isPostalCode('123456', 'BD'))
        
    def test_isPostalCode_BY_True(self):
        self.assertTrue(validator.isPostalCode('220050', 'BY'))
        self.assertTrue(validator.isPostalCode('290010', 'BY'))
        self.assertTrue(validator.isPostalCode('260000', 'BY'))
        
    # def test_isPostalCode_BY_False(self):  # TODO: fix this test
    #     self.assertFalse(validator.isPostalCode('22005', 'BY'))
    #     self.assertFalse(validator.isPostalCode('29001', 'BY'))
    #     self.assertFalse(validator.isPostalCode('26000', 'BY'))
        
    # def test_isPostalCode_BR_True(self):
    #     self.assertTrue(validator.isPostalCode('40301–140', 'BR'))
    #     self.assertTrue(validator.isPostalCode('20501–820', 'BR'))
    #     self.assertTrue(validator.isPostalCode('80801–460', 'BR'))
    
    def test_isPostalCode_CA_True(self):
        self.assertTrue(validator.isPostalCode('A1A 1A1', 'CA'))
        self.assertTrue(validator.isPostalCode('H3Z 2Y7', 'CA'))
        self.assertTrue(validator.isPostalCode('V6Z 2B6', 'CA'))
        
    def test_isPostalCode_CA_False(self):
        self.assertFalse(validator.isPostalCode('2B6 V6Z', 'CA'))
        self.assertFalse(validator.isPostalCode('2Y7 H3Z', 'CA'))
        self.assertFalse(validator.isPostalCode('ABC 126', 'CA'))
    
    def test_isPostalCode_CH_True(self):
        self.assertTrue(validator.isPostalCode('1234', 'CH'))
        self.assertTrue(validator.isPostalCode('4321', 'CH'))
        self.assertTrue(validator.isPostalCode('8764', 'CH'))
        
    def test_isPostalCode_CH_False(self):
        self.assertFalse(validator.isPostalCode('123', 'CH'))
        self.assertFalse(validator.isPostalCode('12345', 'CH'))
        self.assertFalse(validator.isPostalCode('123456', 'CH'))
        
    def test_isPostalCode_CN_True(self):
        self.assertTrue(validator.isPostalCode('266033', 'CN'))
        self.assertTrue(validator.isPostalCode('465040', 'CN'))
        self.assertTrue(validator.isPostalCode('362682', 'CN'))
        
    def test_isPostalCode_CN_False(self):
        self.assertFalse(validator.isPostalCode('26603', 'CN'))
        self.assertFalse(validator.isPostalCode('46504', 'CN'))
        self.assertFalse(validator.isPostalCode('36268', 'CN'))
        
    def test_isPostalCode_CY_True(self):
        self.assertTrue(validator.isPostalCode('2008', 'CY'))
        self.assertTrue(validator.isPostalCode('2009', 'CY'))
        self.assertTrue(validator.isPostalCode('2010', 'CY'))
        
    def test_isPostalCode_CY_False(self):
        self.assertFalse(validator.isPostalCode('200', 'CY'))
        self.assertFalse(validator.isPostalCode('20099', 'CY'))
        self.assertFalse(validator.isPostalCode('20100', 'CY'))
    
    def test_isPostalCode_CZ_True(self):
        self.assertTrue(validator.isPostalCode('123 45', 'CZ'))
        self.assertTrue(validator.isPostalCode('432 10', 'CZ'))
        self.assertTrue(validator.isPostalCode('876 45', 'CZ'))
    
    def test_isPostalCode_CZ_False(self):
        self.assertFalse(validator.isPostalCode('1234', 'CZ'))
        self.assertFalse(validator.isPostalCode('12345', 'CZ'))
        self.assertFalse(validator.isPostalCode('123456', 'CZ'))
        
    def test_isPostalCode_DE_True(self):
        self.assertTrue(validator.isPostalCode('12345', 'DE'))
        self.assertTrue(validator.isPostalCode('43210', 'DE'))
        self.assertTrue(validator.isPostalCode('87645', 'DE'))
        
    def test_isPostalCode_DE_False(self):
        self.assertFalse(validator.isPostalCode('1234', 'DE'))
        self.assertFalse(validator.isPostalCode('123456', 'DE'))
        self.assertFalse(validator.isPostalCode('1234567', 'DE'))
        
    def test_isPosalCode_DZ_True(self):
        self.assertTrue(validator.isPostalCode('16000', 'DZ'))
        self.assertTrue(validator.isPostalCode('26000', 'DZ'))
        self.assertTrue(validator.isPostalCode('36000', 'DZ'))
        
    def test_isPostalCode_DZ_False(self):
        self.assertFalse(validator.isPostalCode('1600', 'DZ'))
        self.assertFalse(validator.isPostalCode('2600', 'DZ'))
        self.assertFalse(validator.isPostalCode('3600', 'DZ'))

    def test_isPostalCode_FR_True(self):
        self.assertTrue(validator.isPostalCode('12345', 'FR'))
        self.assertTrue(validator.isPostalCode('43210', 'FR'))
        self.assertTrue(validator.isPostalCode('87645', 'FR'))
        
    def test_isPostalCode_FR_False(self):
        self.assertFalse(validator.isPostalCode('1234', 'FR'))
        self.assertFalse(validator.isPostalCode('123456', 'FR'))
        self.assertFalse(validator.isPostalCode('1234567', 'FR'))
    
    def test_isPostalCode_GB_True(self):
        self.assertTrue(validator.isPostalCode('M2 5BQ', 'GB'))
        self.assertTrue(validator.isPostalCode('M34 4AB', 'GB'))
        self.assertTrue(validator.isPostalCode('CR0 2YR', 'GB'))
        self.assertTrue(validator.isPostalCode('DN16 9AA', 'GB'))
        self.assertTrue(validator.isPostalCode('W1A 4ZZ', 'GB'))
        self.assertTrue(validator.isPostalCode('EC1A 1BB', 'GB'))
        
    
                                                        
        
    
if __name__ == '__main__':
    unittest.main()