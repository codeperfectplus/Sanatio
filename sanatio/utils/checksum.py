from sanatio.utils.verhoeff_algorithm import Verhoeff

var = Verhoeff()

def checksum_aadhar(aadhar_number):
    """ validates aadhar number """
    if int(aadhar_number[-1]) == var.calcsum(str(aadhar_number)[:-1]):
        return True
    return False

def checksum_pan(pan_number):
    """ pancard checksum """
    pass

def checksum_credit_card(credit_card_number):
    """ credit card checksum """
    pass
    