import re
import json
from datetime import datetime
from dateutil.parser import parse
from Levenshtein import distance as levenshtein_distance

from sanatio.utils.utils import all_country, regexs
from sanatio.utils.checksum import checksum_aadhar, checksum_credit_card
from sanatio.base_class import BaseValidator


class OtherValidator(BaseValidator):
    def __init__(self):
        super().__init__()

    def isEAN13(self, value) -> bool:
        """ check if the string is EAN or not """
        if isinstance(value, int):
            value = str(value)
        if not self.isLength(value, 13, 13):
            return False

        last_digit = int(value[-1])
        remaining_numbers = value[:-1]
        total_sum = sum(int(remaining_numbers[i]) * 3 if i % 2 != 0 else \
            int(remaining_numbers[i]) for i in range(len(remaining_numbers)))
        unit_digit = 0 if total_sum % 10 == 0 else 10 - (total_sum % 10)
        if unit_digit == last_digit:
            return True

    def isHash(self, value) -> bool:
        """ check if the string is hash or not """
        pass

    def isIMEI(self, value) -> bool:
        """ check if the string is IMEI or not """
        if len(value) == 15 or len(value) == 17:
            return True
        return False

    def isIPV4(self, value: str) -> bool:
        """ check if the string is IP or not """
        regex = regexs['ipv4_regex']
        if re.search(regex, value):
            return True
        return False

    def isIPV6(self, value: str) -> bool:
        regex = regexs['ipv6_regex']
        if re.match(regex, value):
            return True
        return False

    def isSSN(self, value) -> bool:
        """ check if the string is SSN or not """
        regex = r'^(?!0{3})(?!6{3})[0-8]\d{2}-(?!0{2})\d{2}-(?!0{4})\d{4}$'
        if re.match(regex, value):
            return True
        return False

    def isJSON(self, value) -> bool:
        """ check if the string is JSON or not """
        try:
            json.loads(value)
            return True
        except ValueError:
            return False

    def isJWT(self, value) -> bool:
        """ check if the string is JWT or not """
        regex = r"^[A-Za-z0-9_-]{2,}(?:\.[A-Za-z0-9_-]{2,}){2}$"
        if re.match(regex, value):
            return True

        return False

    def isLatLong(self, value: str) -> bool:
        """ check if the string is lat long or not """
        regex = r"^((\-?|\+?)?\d+(\.\d+)?),\s*((\-?|\+?)?\d+(\.\d+)?)$"
        if re.match(regex, value):
            return True
        return False

    def isMACAddress(self, value: str) -> bool:
        """ check if the string is MAC address or not """
        regex = regexs['mac_address_regex']
        if self.isvalidString(value) and re.search(regex, value, re.IGNORECASE):
            return True
        return False

    def isMD5(self, value) -> bool:
        """ check if the string is MD5 or not """
        pass

    def isPort(self, value: int) -> bool:
        """ check if the string is port or not
        A port number is a 16-bit unsigned integer,
        so it has a minimum value of 0 and a maximum value of 65535.
        """
        if value.isdigit() and 0 <= int(value) <= 65535:
            return True
        return False

    def isSlug(self, value: str) -> bool:
        """ check if the string is slug or not """
        regex = "^[a-z0-9-]+$"
        if re.match(regex, value):
            return True
        return False

    def isUUID(self, value: str) -> bool:
        """ check if the string is UUID or not """
        pass

    def isPostalCode(self, value, locale: str)-> bool:
        """ check if the string is postal code or not """
        country_data = all_country[locale]

        PostalCode = country_data['PostalCode']

        PostalCodeFormat = PostalCode['Format']
        PostalCodeRegex = PostalCode['Regex']
        MinPostalCodeLength = PostalCode['MinLength']
        MaxPostalCodeLength = PostalCode['MaxLength']

        if re.match(PostalCodeRegex, value) and re.match(PostalCodeFormat, value) \
            and self.isLength(str(value), MinPostalCodeLength, MaxPostalCodeLength):
                return True

        return False

    def isMobilePhone(self, value, locale: str) -> bool:
        """ check if the string is mobile phone or not """
        country_data = all_country[locale]

        MobileNumberRegex = country_data['MobileNumberRegex']

        if re.match(MobileNumberRegex, value):
            return True

        return False
