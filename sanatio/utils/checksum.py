import sys
sys.path.append('.')
from sanatio.utils.checksum_algorithms.verhoeff_algorithm import VerhoeffAlgorithm
from sanatio.utils.checksum_algorithms.luhn_algorithm import LuhnAlgorithm
from sanatio.utils.checksum_algorithms.ean_checksum import EANCheckSum


def checksum_aadhar(aadhar_number):
    """ validates aadhar number """
    return VerhoeffAlgorithm().verify(aadhar_number)

def checksum_pan(pan_number):
    """ pancard checksum """
    pass

def checksum_credit_card(credit_card_number):
    """ credit card checksum """
    return LuhnAlgorithm().verify(credit_card_number)
    
def checksum_ean(ean_number):
    """ ean checksum """
    return EANCheckSum().is_valid(ean_number)
