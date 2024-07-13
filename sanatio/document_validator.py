import re

from sanatio.utils.utils import country_json, regexs_dict
from sanatio.utils.checksum import VerhoeffAlgorithm
from sanatio.utils.checksum import LuhnAlgorithm
from sanatio.base_class import BaseValidator


class DocumentValidator(BaseValidator):
    """ 
    DocumentValidator class is used to validate document numbers like Aadhar card, License plate, Passport number, Credit card number

    Methods
    -------
    isAadharCard(value: str) -> bool:
        check if the string is Aadhar card or not

    isLicensePlate(value: str, locale: str) -> bool:
        check if the string is license plate or not

    isPassportNumber(value: str, locale: str) -> bool:
        check if the string is passport number or not

    isCreditCard(value: str) -> bool:
        check if the string is credit card number or not

    """

    def isAadharCard(self, value) -> bool:
        """ check if the string is Aadhar card or not """
        regex = regexs_dict.get('aadhar_regex')
        value = value.strip().replace(" ", "")
        if isinstance(value, int):
            value = str(value)
        if self.isLength(str(value), 12, 12) \
            and value[0] not in ['0', '1'] and re.match(regex, value) \
                and VerhoeffAlgorithm(value).verify():
            return True
        return False

    def isLicensePlate(self, value, locale: str) -> bool:
        """ check if the string is license plate or not """
        value = value.upper()
        country_data = country_json[locale]

        LicensePlate = country_data['LicensePlate']
        Format = LicensePlate['Format']
        Regex = LicensePlate['Regex']
        MinLength = LicensePlate['MinLength']
        MaxLength = LicensePlate['MaxLength']

        if re.match(Format, value) and re.match(Regex, value) \
                and self.isLength(value, MinLength, MaxLength):
            return True

        return False

    # TODO: research more about passport number
    def isPassportNumber(self, value, locale: str) -> bool:
        """ check if the string is passport number or not """
        country_data = country_json[locale]

        PassportNumberRegex = country_data['PassportNumberRegex']
        if re.match(PassportNumberRegex, value):
            return True
        return False

    def isCreditCard(self, value: str) -> bool:  # checksum not implemented
        regex = regexs_dict.get('credit_card_regex')
        if re.match(regex, value):
            if LuhnAlgorithm(value).verify():
                return True
        return False
