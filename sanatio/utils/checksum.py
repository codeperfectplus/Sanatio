import sys
sys.path.append('.')
from sanatio.utils.checksum_algorithms.verhoeff_algorithm import VerhoeffAlgorithm
from sanatio.utils.checksum_algorithms.luhn_algorithm import LuhnAlgorithm

verhoeff = VerhoeffAlgorithm()
luhn = LuhnAlgorithm()


def checksum_aadhar(aadhar_number):
    """ validates aadhar number """
    return verhoeff.verify(aadhar_number)

def checksum_pan(pan_number):
    """ pancard checksum """
    pass

def checksum_credit_card(credit_card_number):
    """ credit card checksum """
    return luhn.verify(credit_card_number)
    
    
    
# res = checksum_credit_card('4578423013769219')
# print(res)
