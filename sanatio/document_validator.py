import re

from sanatio.utils.utils import all_country, regexs
from sanatio.utils.checksum import VerhoeffAlgorithm
from sanatio.utils.checksum import LuhnAlgorithm
from sanatio.base_class import BaseValidator


class DocumentValidator(BaseValidator):

    def isAadharCard(self, value) -> bool:
        """ check if the string is Aadhar card or not """
        regex = regexs['aadhar_regex']
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
        country_data = all_country[locale]

        LicensePlate = country_data['LicensePlate']
        Format = LicensePlate['Format']
        Regex = LicensePlate['Regex']
        MinLength = LicensePlate['MinLength']
        MaxLength = LicensePlate['MaxLength']

        if re.match(Format, value) and re.match(Regex, value) \
                and self.isLength(value, MinLength, MaxLength):
            return True

        return False

    def isPassportNumber(self, value, locale: str) -> bool:  # TODO: research more about passport number
        """ check if the string is passport number or not """
        country_data = all_country[locale]

        PassportNumberRegex = country_data['PassportNumberRegex']
        if re.match(PassportNumberRegex, value):
            return True
        return False

    def isCreditCard(self, value: str) -> bool:  # checksum not implemented
        regex = regexs['credit_card_regex']
        if re.match(regex, value):
            if LuhnAlgorithm(value).verify():
                return True
        return False
