import re
import json
from datetime import datetime
from dateutil.parser import parse
from Levenshtein import distance as levenshtein_distance

from sanatio.utils.utils import all_country, regexs
from sanatio.utils.checksum import checksum_aadhar, checksum_credit_card

class Validator(object):
    """ Validator class for validating the data """
    def __init__(self):
        pass

    def __isvalidString(self, value: str) -> bool:
        """ check if the string is valid or not """
        if value is None or value == '':
            return False

        if isinstance(value, str):
            return True

    def __isvalidNumber(self, value: int)-> bool:
        """ check if the number is valid or not """
        if value is None:
            return False

        if isinstance(value, (int, float)):
            return True

    def __isvalidBoolean(self, value: bool)-> bool:
        """ check if the string is boolean or not """
        if value is None:
            return False

        if isinstance(value, bool):
            return True

    def isAadharCard(self, value)-> bool:
        """ check if the string is Aadhar card or not """
        regex = "^[2-9]{1}[0-9]{3}[0-9]{4}[0-9]{4}$"  # need to improve regex for space and hyphen
        value = value.strip().replace(" ", "")
        if self.isLength(value, 12, 12):
            if isinstance(value, int):
                value = str(value)

            if value[0] != '0' or value[0] != '1':
                if re.match(regex, value):
                    if checksum_aadhar(value):
                        return True

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

    def isPassportNumber(self, value, locale: str)-> bool:  # TODO: research more about passport number
        """ check if the string is passport number or not """
        country_data = all_country[locale]

        PassportNumberRegex = country_data['PassportNumberRegex']
        if re.match(PassportNumberRegex, value):
            return True
        return False

    def isMobilePhone(self, value, locale: str) -> bool:
        """ check if the string is mobile phone or not """
        country_data = all_country[locale]

        MobileNumberRegex = country_data['MobileNumberRegex']

        if re.match(MobileNumberRegex, value):
            return True

        return False

    def isDiscordUsername(self, value: str) -> bool:
        regex = "^.{3,32}#[0-9]{4}$"
        if re.match(regex, value):
            return True
        return False

    def isCreditCard(self, value: str) -> bool:  # checksum not implemented
        regex = regexs['credit_card_regex']
        if re.match(regex, value):
            if checksum_credit_card(value):
                return True
        return False

    def equals(self, value1: str, value2: str, ignoreCase: bool=False)-> bool:
        """ Check if the two string are equal or not """
        if not self.__isvalidString(value1) or not self.__isvalidString(value2):
            return False

        if ignoreCase:
            value1 = value1.lower()
            value2 = value2.lower()

        if value1 == value2:
            return True

        return False

    def isLength(self, value: str, min: int=0, max: int=None) -> bool:
        """ check if the string length is between min and max """
        if min <= len(value) <= max:
            return True

        return False

    def isEmpty(self, value: str) -> bool:
        """ check if the string is empty or not """
        value = value.strip()
        if value == "":
            return True

        return False

    def isAlphanumeric(self, value: str) -> bool:
        if value.isalnum():
            return True

        return False

    def isAlpha(self, value: str) -> bool:
        if value.isalpha():
            return True

        return False

    def isAscii(self, value) -> bool:
        if value.isascii():
            return True

        return False

    def contains(self, value: str, substring: str, ignoreCase: bool=False) -> bool:
        if ignoreCase:
            value = value.lower()
            substring = substring.lower()

        if substring in value:
            return True

        return False

    def isAfter(self, date1, date2=datetime.now()) -> bool:
        """ check if date1 is after date2 default date2 is current date

        Args:
            date1 (str): date in string format
            date2 (str): date in string format default is current date

        """

        if isinstance(date1, str):
            date1 = datetime.strptime(date1, '%Y-%m-%d')
        if isinstance(date2, str):
            date2 = datetime.strptime(date2, '%Y-%m-%d')

        if date1 > date2:
            return True

        return False

    def isBefore(self, date1, date2=datetime.now()) -> bool:
        """
        check if date1 is before date2 default date2 is current date

        Args:
            date1 (str): date in string format
            date2 (str): date in string format default is current date
        """
        if isinstance(date1, str):
            date1 = datetime.strptime(date1, '%Y-%m-%d')
        if isinstance(date2, str):
            date2 = datetime.strptime(date2, '%Y-%m-%d')

        if date1 < date2:
            return True

        return False

    def isDate(self, value) -> bool:
        """ check if the string is date or not """
        if not self.__isvalidString(value):
            return False
        try:
            date_obj = parse(value)
            if date_obj:
                return True
        except Exception:
            return False
        return False

    def isLeapYear(self, year) -> bool:
        """ check if the year is leap year or not """
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


    def isEmail(self, value: str, checkDNS: bool=False) -> bool:
        """ check if the string is email or not """
        if not self.__isvalidString(value):
            return False
        regex = "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
        if re.search(regex, value):
            return True

        return False

    def isDecimal(self, value: float) -> bool:
        """ check if the string is decimal or not """
        if not self.__isvalidNumber(value):
            return False

        if value.isdecimal():
            return True

        return False

    def isDivisibleBy(self, number: int, divisor: int) -> bool:
        """ check if the number is divisible by divisor or not """
        if self.__isvalidNumber(number) and self.__isvalidNumber(divisor) and divisor != 0:
            if number % divisor == 0:
                return True

        return False

    def isEAN(self, value) -> bool:
        """ check if the string is EAN or not """
        pass

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
        regex = '^(?!0{3})(?!6{3})[0-8]\d{2}-(?!0{2})\d{2}-(?!0{4})\d{4}$'
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
        regex = "^[A-Za-z0-9_-]{2,}(?:\.[A-Za-z0-9_-]{2,}){2}$"
        if re.match(regex, value):
            return True

        return False

    def isLatLong(self, value: str) -> bool:
        """ check if the string is lat long or not """
        regex = "^((\-?|\+?)?\d+(\.\d+)?),\s*((\-?|\+?)?\d+(\.\d+)?)$"
        if re.match(regex, value):
            return True
        return False

    def isMACAddress(self, value: str) -> bool:
        """ check if the string is MAC address or not """
        regex = regexs['mac_address_regex']
        if self.__isvalidString(value) and re.search(regex, value, re.IGNORECASE):
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

    def isStrongPassword(self, value: str) -> bool:
        """ check if the string is strong password or not

        requirements:
            1. At least 8 characters long
            2. At least one uppercase letter
            3. At least one lowercase letter
            4. At least one number
            5. At least one special character
        """
        if len(value) < 8:
            return False

        if not re.search("[a-z]", value):
            return False

        if not re.search("[A-Z]", value):
            return False

        if not re.search("[0-9]", value):
            return False

        if not re.search("[_@$]", value):
            return False

        return True

    def isUUID(self, value: str) -> bool:
        """ check if the string is UUID or not """
        pass

    def toDate(self, value):  # need to improve this function
        """ convert string to date """
        format = '%Y-%m-%d'
        if self.isDate(value):
            date = datetime.strptime(value, format)
            return date

        else:
            return None

    def toInt(self, value):
        """ convert string to int """
        if isinstance(value, int):
            return value

        elif isinstance(value, float):
            return int(value)

        try:
            value = int(float(value))
            return value

        except ValueError:
            value = 0

        return value

    def trim(self, value):
        """ trim string """
        if self.__isvalidString(value):
            return value.strip()

    def ltrim(self, value):
        if self.__isvalidString(value):
            return value.lstrip()

    def rtrim(self, value):
        if self.__isvalidString(value):
            return value.rstrip()

    def toUpperCase(self, value):
        """ convert string to upper case """
        if self.__isvalidString(value):
            return value.upper()

    def toLowerCase(self, value):
        """ convert string to lower case """
        if self.__isvalidString(value):
            return value.lower()

    def removeSpaces(self, value):
        """ remove spaces from string """
        if self.__isvalidString(value):
            return value.replace(" ", "")

    def removeSymbols(self, value):
        """ remove symbols from string """
        if self.__isvalidString(value):
            return re.sub(r'[^\w\s]', '', value)

    def levenshtein_distance(self, value1, value2):
        """ calculate distance between two strings """
        distance = levenshtein_distance(value1, value2)
        return distance

    def edit_distance(self, value1, value2):
        """ calculate distance between two strings """
        if len(value1) > len(value2):
            difference = len(value1) - len(value2)

        elif len(value2) > len(value1):
            difference = len(value2) - len(value1)

        else:
            difference = 0

        for val1, val2 in zip(value1, value2):
            if val1 != val2:
                difference += 1

        return difference

    def removeNonASCII(self, value):
        """ remove non ASCII characters from string """
        if self.__isvalidString(value):
            return value.encode("ascii", "ignore").decode()

    def removeNonWord(self, value):
        """ remove non word characters from string """
        if self.__isvalidString(value):
            return re.sub(r'[^\w]', '', value)

    def removeNonNumeric(self, value):
        """ remove non numeric characters from string """
        if self.__isvalidString(value):
            return re.sub(r'[^\d]', '', value)

    def removeTags(self, value):
        """ remove tags from string """
        if self.__isvalidString(value):
            return re.sub(r'<[^>]*>', '', value)

    def removeWhiteSpace(self, value):
        """ remove white space from string """
        if self.__isvalidString(value):
            return value.replace(" ", "")
