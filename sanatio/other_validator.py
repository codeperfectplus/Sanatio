import re
import json

from sanatio.utils.utils import regexs_dict, country_json
from sanatio.base_class import BaseValidator
from sanatio.utils.checksum import EANCheckSum


class OtherValidator(BaseValidator):

    def isEAN13(self, value) -> bool:
        """ check if the string is EAN or not """
        value = str(value) if isinstance(value, int) else value
        return self.isLength(value, 13, 13) and EANCheckSum(value).verify()

    def isIMEI(self, value) -> bool:
        """ check if the string is IMEI or not """
        return len(value) == 15 or len(value) == 17

    def isIPV4(self, value: str) -> bool:
        """ check if the string is IP or not """
        regex = regexs_dict.get('ipv4_regex')
        return True if re.match(regex, value) else False

    def isIPV6(self, value: str) -> bool:
        regex = regexs_dict.get('ipv6_regex')
        return True if re.match(regex, value) else False

    def isSSN(self, value) -> bool:
        """ check if the string is SSN or not """
        regex = regexs_dict.get('ssn_regex')
        return True if re.match(regex, value) else False

    def isJSON(self, value) -> bool:
        """ check if the string is JSON or not """
        try:
            json.loads(value)
            return True
        except ValueError:
            return False

    def isJWT(self, value) -> bool:
        """ check if the string is JWT or not """
        regex = regexs_dict.get('jwt_regex')
        return True if re.match(regex, value) else False

    def isLatLong(self, value: str) -> bool:
        """ check if the string is lat long or not """
        regex = regexs_dict.get('lat_long_regex')
        return True if re.match(regex, value) else False

    def isMACAddress(self, value: str) -> bool:
        """ check if the string is MAC address or not """
        regex = regexs_dict.get('mac_address_regex')
        if self.isvalidString(value) and re.search(regex, value, re.IGNORECASE):
            return True
        return False

    def isPort(self, value: int) -> bool:
        """ check if the string is port or not
        A port number is a 16-bit unsigned integer,
        so it has a minimum value of 0 and a maximum value of 65535.
        """
        return value.isdigit() and 0 <= int(value) <= 65535

    def isSlug(self, value: str) -> bool:
        """ check if the string is slug or not """
        regex = regexs_dict.get('slug_regex')
        return True if re.match(regex, value) else False

    def isPostalCode(self, value, locale: str) -> bool:
        """ check if the string is postal code or not """
        country_data = country_json[locale]

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
        country_data = country_json[locale]
        MobileNumberRegex = country_data['MobileNumberRegex']
        if re.match(MobileNumberRegex, value):
            return True

    def isUUID(self, value: str) -> bool:
        """ check if the string is UUID or not """
        regex = regexs_dict.get('uuid_regex')
        return True if re.match(regex, value) else False
