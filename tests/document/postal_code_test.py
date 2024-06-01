import sys
import unittest
sys.path.append('.')
from sanatio import Validator

validator = Validator()


class PostalCodeTest(unittest.TestCase):
    def test_isPostalCode_IN_True(self):
        self.assertTrue(validator.isPostalCode('590037', 'IN'))
        self.assertTrue(validator.isPostalCode('110019', 'IN'))
        self.assertTrue(validator.isPostalCode('110001', 'IN'))
        self.assertTrue(validator.isPostalCode('344343', 'IN'))
        
    def test_isPostalCode_IN_False(self):
        self.assertFalse(validator.isPostalCode('590037-1934', 'IN'))
        self.assertFalse(validator.isPostalCode('59003', 'IN'))
        self.assertFalse(validator.isPostalCode('19345', 'IN'))
        self.assertFalse(validator.isPostalCode('5900371934', 'IN'))
    
    def test_isPostalCode_US_True(self):
        self.assertTrue(validator.isPostalCode('59003', 'US'))
        self.assertTrue(validator.isPostalCode('59003-1934', 'US'))
        self.assertTrue(validator.isPostalCode('95100-4333', 'US'))
        
    def test_isPostalCode_US_False(self):
        self.assertFalse(validator.isPostalCode('59003-19345', 'US'))
        self.assertFalse(validator.isPostalCode('59003 1934', 'US'))
        self.assertFalse(validator.isPostalCode('59003-193', 'US'))
        self.assertFalse(validator.isPostalCode('5900', 'US'))
        self.assertFalse(validator.isPostalCode('59003-19345', 'US'))
        
    def test_isPostalCode_AF_True(self):  # TODO: review this test
        self.assertTrue(validator.isPostalCode('1043', 'AF'))
        self.assertTrue(validator.isPostalCode('1290', 'AF'))
        self.assertTrue(validator.isPostalCode('1001', 'AF'))
    
    def test_isPostalCode_AF_False(self):
        self.assertFalse(validator.isPostalCode('104', 'AF'))
        self.assertFalse(validator.isPostalCode('4410', 'AF'))
        self.assertFalse(validator.isPostalCode('10001', 'AF'))
    
    def test_isPostalCode_SA_True(self):
        self.assertTrue(validator.isPostalCode('19345', 'SA'))
        self.assertTrue(validator.isPostalCode('19345-1934', 'SA'))
        self.assertTrue(validator.isPostalCode('34434-4333', 'SA'))
        
    def test_isPostalCode_SA_False(self):
        self.assertFalse(validator.isPostalCode('1934', 'SA'))
        self.assertFalse(validator.isPostalCode('193459', 'SA'))
        self.assertFalse(validator.isPostalCode('19345-19345', 'SA'))
    
    def test_isPostalCode_SG_True(self):
        self.assertTrue(validator.isPostalCode('193459', 'SG'))
        self.assertTrue(validator.isPostalCode('439733', 'SG'))
        
    def test_isPostalCode_SG_False(self):
        self.assertFalse(validator.isPostalCode('19345', 'SG'))
        self.assertFalse(validator.isPostalCode('1934597', 'SG'))
        
    def test_isPostal_ZA_True(self):
        self.assertTrue(validator.isPostalCode('1934', 'ZA'))
        self.assertTrue(validator.isPostalCode('4331', 'ZA'))
        self.assertTrue(validator.isPostalCode('8794', 'ZA'))

    def test_isPostalCode_ZA_False(self):
        self.assertFalse(validator.isPostalCode('193', 'ZA'))
        self.assertFalse(validator.isPostalCode('19345', 'ZA'))
        self.assertFalse(validator.isPostalCode('193459', 'ZA'))
        
    def test_isPostalCode_PK_True(self):
        self.assertTrue(validator.isPostalCode('19345', 'PK'))
        self.assertTrue(validator.isPostalCode('54331', 'PK'))
        self.assertTrue(validator.isPostalCode('87954', 'PK'))
        
    def test_isPostalCode_PK_False(self):
        self.assertFalse(validator.isPostalCode('1934', 'PK'))
        self.assertFalse(validator.isPostalCode('193459', 'PK'))
        self.assertFalse(validator.isPostalCode('110019', 'PK'))
        self.assertFalse(validator.isPostalCode('110001', 'PK'))
        
    def test_isPostalCode_AM_True(self):
        self.assertTrue(validator.isPostalCode('1934', 'AM'))
        self.assertTrue(validator.isPostalCode('4331', 'AM'))
        self.assertTrue(validator.isPostalCode('8794', 'AM'))
        
    def test_isPostalCode_AM_False(self):
        self.assertFalse(validator.isPostalCode('193', 'AM'))
        self.assertFalse(validator.isPostalCode('19345', 'AM'))
        self.assertFalse(validator.isPostalCode('193459', 'AM'))
        
    def test_isPostalCode_AR_True(self):
        self.assertTrue(validator.isPostalCode('B1939FDA', 'AR'))
        self.assertTrue(validator.isPostalCode('C1939ABC', 'AR'))
        self.assertTrue(validator.isPostalCode('Y5900FNF', 'AR'))
    
    def test_isPostalCode_AR_False(self):
        self.assertFalse(validator.isPostalCode('B1939FD', 'AR'))
        self.assertFalse(validator.isPostalCode('B1939FDAA', 'AR'))
        self.assertFalse(validator.isPostalCode('B1939FDA1', 'AR'))
        self.assertFalse(validator.isPostalCode('B1939FDA1', 'AR'))
        self.assertFalse(validator.isPostalCode('B1939FDA1', 'AR'))
        
    def test_isPostalCode_AT_True(self):
        self.assertTrue(validator.isPostalCode('1934', 'AT'))
        self.assertTrue(validator.isPostalCode('4331', 'AT'))
        self.assertTrue(validator.isPostalCode('8794', 'AT'))
        
    def test_isPostalCode_AT_False(self):
        self.assertFalse(validator.isPostalCode('193', 'AT'))
        self.assertFalse(validator.isPostalCode('19345', 'AT'))
        self.assertFalse(validator.isPostalCode('193459', 'AT'))
    
    def test_isPostalCode_AU_True(self):
        self.assertTrue(validator.isPostalCode('1934', 'AU'))
        self.assertTrue(validator.isPostalCode('4331', 'AU'))
        self.assertTrue(validator.isPostalCode('5978', 'AU'))
    
    def test_isPostalCode_AU_False(self):
        self.assertFalse(validator.isPostalCode('193', 'AU'))
        self.assertFalse(validator.isPostalCode('19345', 'AU'))
        self.assertFalse(validator.isPostalCode('193459', 'AU'))
        
    def test_isPostalCode_AZ_True(self):
        self.assertTrue(validator.isPostalCode('1934', 'AZ'))
        self.assertTrue(validator.isPostalCode('4331', 'AZ'))
        self.assertTrue(validator.isPostalCode('8794', 'AZ'))
        
    def test_isPostalCode_AZ_False(self):
        self.assertFalse(validator.isPostalCode('193', 'AZ'))
        self.assertFalse(validator.isPostalCode('19345', 'AZ'))
        self.assertFalse(validator.isPostalCode('193459', 'AZ'))
        
    def test_isPostalCode_BD_True(self):
        self.assertTrue(validator.isPostalCode('1934', 'BD'))
        self.assertTrue(validator.isPostalCode('4331', 'BD'))
        self.assertTrue(validator.isPostalCode('8794', 'BD'))
        
    def test_isPostalCode_BD_False(self):
        self.assertFalse(validator.isPostalCode('193', 'BD'))
        self.assertFalse(validator.isPostalCode('19345', 'BD'))
        self.assertFalse(validator.isPostalCode('193459', 'BD'))
        
    def test_isPostalCode_BY_True(self):
        self.assertTrue(validator.isPostalCode('330050', 'BY'))
        self.assertTrue(validator.isPostalCode('390010', 'BY'))
        self.assertTrue(validator.isPostalCode('390000', 'BY'))
        
    # def test_isPostalCode_BY_False(self):  # TODO: fix this test
    #     self.assertFalse(validator.isPostalCode('33005', 'BY'))
    #     self.assertFalse(validator.isPostalCode('39001', 'BY'))
    #     self.assertFalse(validator.isPostalCode('39000', 'BY'))
        
    # def test_isPostalCode_BR_True(self):
    #     self.assertTrue(validator.isPostalCode('40301–140', 'BR'))
    #     self.assertTrue(validator.isPostalCode('30501–830', 'BR'))
    #     self.assertTrue(validator.isPostalCode('80801–490', 'BR'))
    
    def test_isPostalCode_CA_True(self):
        self.assertTrue(validator.isPostalCode('A1A 1A1', 'CA'))
        self.assertTrue(validator.isPostalCode('H3Z 3Y7', 'CA'))
        self.assertTrue(validator.isPostalCode('V9Z 3B9', 'CA'))
        
    def test_isPostalCode_CA_False(self):
        self.assertFalse(validator.isPostalCode('3B9 V9Z', 'CA'))
        self.assertFalse(validator.isPostalCode('3Y7 H3Z', 'CA'))
        self.assertFalse(validator.isPostalCode('ABC 199', 'CA'))
    
    def test_isPostalCode_CH_True(self):
        self.assertTrue(validator.isPostalCode('1934', 'CH'))
        self.assertTrue(validator.isPostalCode('4331', 'CH'))
        self.assertTrue(validator.isPostalCode('8794', 'CH'))
        
    def test_isPostalCode_CH_False(self):
        self.assertFalse(validator.isPostalCode('193', 'CH'))
        self.assertFalse(validator.isPostalCode('19345', 'CH'))
        self.assertFalse(validator.isPostalCode('193459', 'CH'))
        
    def test_isPostalCode_CN_True(self):
        self.assertTrue(validator.isPostalCode('399033', 'CN'))
        self.assertTrue(validator.isPostalCode('495040', 'CN'))
        self.assertTrue(validator.isPostalCode('393983', 'CN'))
        
    def test_isPostalCode_CN_False(self):
        self.assertFalse(validator.isPostalCode('39903', 'CN'))
        self.assertFalse(validator.isPostalCode('49504', 'CN'))
        self.assertFalse(validator.isPostalCode('39398', 'CN'))
        
    def test_isPostalCode_CY_True(self):
        self.assertTrue(validator.isPostalCode('3008', 'CY'))
        self.assertTrue(validator.isPostalCode('3009', 'CY'))
        self.assertTrue(validator.isPostalCode('3010', 'CY'))
        
    def test_isPostalCode_CY_False(self):
        self.assertFalse(validator.isPostalCode('300', 'CY'))
        self.assertFalse(validator.isPostalCode('30099', 'CY'))
        self.assertFalse(validator.isPostalCode('30100', 'CY'))
    
    def test_isPostalCode_CZ_True(self):
        self.assertTrue(validator.isPostalCode('193 45', 'CZ'))
        self.assertTrue(validator.isPostalCode('433 10', 'CZ'))
        self.assertTrue(validator.isPostalCode('879 45', 'CZ'))
    
    def test_isPostalCode_CZ_False(self):
        self.assertFalse(validator.isPostalCode('1934', 'CZ'))
        self.assertFalse(validator.isPostalCode('19345', 'CZ'))
        self.assertFalse(validator.isPostalCode('193459', 'CZ'))
        
    def test_isPostalCode_DE_True(self):
        self.assertTrue(validator.isPostalCode('19345', 'DE'))
        self.assertTrue(validator.isPostalCode('43310', 'DE'))
        self.assertTrue(validator.isPostalCode('87945', 'DE'))
        
    def test_isPostalCode_DE_False(self):
        self.assertFalse(validator.isPostalCode('1934', 'DE'))
        self.assertFalse(validator.isPostalCode('193459', 'DE'))
        self.assertFalse(validator.isPostalCode('1934597', 'DE'))
        
    def test_isPosalCode_DZ_True(self):
        self.assertTrue(validator.isPostalCode('19000', 'DZ'))
        self.assertTrue(validator.isPostalCode('39000', 'DZ'))
        self.assertTrue(validator.isPostalCode('39000', 'DZ'))
        
    def test_isPostalCode_DZ_False(self):
        self.assertFalse(validator.isPostalCode('1900', 'DZ'))
        self.assertFalse(validator.isPostalCode('3900', 'DZ'))
        self.assertFalse(validator.isPostalCode('3900', 'DZ'))

    def test_isPostalCode_FR_True(self):
        self.assertTrue(validator.isPostalCode('19345', 'FR'))
        self.assertTrue(validator.isPostalCode('43310', 'FR'))
        self.assertTrue(validator.isPostalCode('87945', 'FR'))
        
    def test_isPostalCode_FR_False(self):
        self.assertFalse(validator.isPostalCode('1934', 'FR'))
        self.assertFalse(validator.isPostalCode('193459', 'FR'))
        self.assertFalse(validator.isPostalCode('1934597', 'FR'))
    
    def test_isPostalCode_GB_True(self):
        self.assertTrue(validator.isPostalCode('M3 5BQ', 'GB'))
        self.assertTrue(validator.isPostalCode('M34 4AB', 'GB'))
        self.assertTrue(validator.isPostalCode('CR0 3YR', 'GB'))
        self.assertTrue(validator.isPostalCode('DN19 9AA', 'GB'))
        self.assertTrue(validator.isPostalCode('W1A 4ZZ', 'GB'))
        self.assertTrue(validator.isPostalCode('EC1A 1BB', 'GB'))
        
    # def test_isPostalCode_IE_True(self):  # TODO: REGEX for IE is not working
    #     self.assertTrue(validator.isPostalCode('D03 E5F3', 'IE'))
    #     self.assertTrue(validator.isPostalCode('D03 E5F3', 'IE'))
    #     self.assertTrue(validator.isPostalCode('D03 E5F3', 'IE'))
    
    def test_isPostalCode_ID_True(self):
        self.assertTrue(validator.isPostalCode('19345', 'ID'))
        self.assertTrue(validator.isPostalCode('43310', 'ID'))
        self.assertTrue(validator.isPostalCode('87945', 'ID'))
        
    def test_isPostalCode_ID_False(self):
        self.assertFalse(validator.isPostalCode('1934', 'ID'))
        self.assertFalse(validator.isPostalCode('193459', 'ID'))
        self.assertFalse(validator.isPostalCode('1934597', 'ID'))
    
    def test_isPostalCode_IR_True(self):
        self.assertTrue(validator.isPostalCode('1193953471', 'IR'))
        self.assertTrue(validator.isPostalCode('4331098795', 'IR'))
        self.assertTrue(validator.isPostalCode('8795433187', 'IR'))
        
    def test_isPostalCode_IR_False(self):
        self.assertFalse(validator.isPostalCode('19345978901', 'IR'))
        self.assertFalse(validator.isPostalCode('1934597890193', 'IR'))
        self.assertFalse(validator.isPostalCode('19345978901934', 'IR'))
        
    def test_isPostalCode_IT_True(self):
        self.assertTrue(validator.isPostalCode('00193', 'IT'))
        self.assertTrue(validator.isPostalCode('43310', 'IT'))
        self.assertTrue(validator.isPostalCode('87945', 'IT'))
        
    def test_isPostalCode_IT_False(self):
        self.assertFalse(validator.isPostalCode('1934', 'IT'))
        self.assertFalse(validator.isPostalCode('193459', 'IT'))
        self.assertFalse(validator.isPostalCode('1934597', 'IT'))
        
    def test_isPostalCode_JP_True(self):
        self.assertTrue(validator.isPostalCode('001-0934', 'JP'))
        self.assertTrue(validator.isPostalCode('433-1098', 'JP'))
        self.assertTrue(validator.isPostalCode('879-5433', 'JP'))
        
    def test_isPostalCode_JP_False(self):
        self.assertFalse(validator.isPostalCode('1934', 'JP'))
        self.assertFalse(validator.isPostalCode('193459', 'JP'))
        self.assertFalse(validator.isPostalCode('1934597', 'JP'))
        
    def test_isPostalCode_MY_True(self):
        self.assertTrue(validator.isPostalCode('00193', 'MY'))
        self.assertTrue(validator.isPostalCode('43310', 'MY'))
        self.assertTrue(validator.isPostalCode('87945', 'MY'))
        
    def test_isPostalCode_MY_False(self):
        self.assertFalse(validator.isPostalCode('1934', 'MY'))
        self.assertFalse(validator.isPostalCode('193459', 'MY'))
        self.assertFalse(validator.isPostalCode('1934597', 'MY'))
    
    
    def test_isPostalCode_MX_True(self):
        self.assertTrue(validator.isPostalCode('00193', 'MX'))
        self.assertTrue(validator.isPostalCode('43310', 'MX'))
        self.assertTrue(validator.isPostalCode('87945', 'MX'))
    
    def test_isPostalCode_MX_False(self):
        self.assertFalse(validator.isPostalCode('1934', 'MX'))
        self.assertFalse(validator.isPostalCode('193459', 'MX'))
        self.assertFalse(validator.isPostalCode('1934597', 'MX'))
        
    def test_isPostalCode_PL_True(self):
        self.assertTrue(validator.isPostalCode('00-193', 'PL'))
        self.assertTrue(validator.isPostalCode('43-310', 'PL'))
        self.assertTrue(validator.isPostalCode('87-945', 'PL'))
        
    def test_isPotalCode_PL_False(self):
        self.assertFalse(validator.isPostalCode('1934', 'PL'))
        self.assertFalse(validator.isPostalCode('1234', 'PL'))
        self.assertFalse(validator.isPostalCode('123123', 'PL'))            
    
    def test_isPostalCode_PT_True(self):
        #self.assertTrue
        pass

    def test_isPostalCode_PT_False(self):
        pass
    
    def test_isPostalCode_SE_True(self):
        pass
    
    def test_isPostalCode_SE_False(self):
        pass
    
    def test_isPostalCode_TH_True(self):
        pass
    
    def test_isPostalCode_Th_False(self):
        pass
    
    def test_isPostalCode_TR_True(self):
        pass
    
    def test_isPostalCode_TR_False(self):
        pass
    
    def test_isPostalCode_UA_True(self):
        pass
    
    def test_isPostalCode_UA_False(self):
        pass
    
if __name__ == '__main__':
    unittest.main()