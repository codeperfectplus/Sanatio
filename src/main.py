import re
import json
from datetime import datetime

from src.utils import all_country

class Validator(object):
    """ Validator class for validating the data """
    def __init__(self):
        pass

    def __isvalidString(self, value):
        """ check if the string is valid or not """
        if value is None or value == '':
            return False

        if isinstance(value, str):
            return True

        return False

    def __isvalidNumber(self, value):
        """ check if the number is valid or not """
        if value is None:
            return False

        if isinstance(value, (int, float)):
            return True

        return False

    def __isvalidBoolean(self, value):
        """ check if the string is boolean or not """
        if value is None:
            return False
        if isinstance(value, bool):
            return True

        return False
    
    def isPostalCode(self, string1, locale):
        """ check if the string is postal code or not """
        country_data = all_country[locale]

        PostalCodeFormat = country_data['PostalCodeFormat']
        PostalCodeRegex = country_data['PostalCodeRegex']

        if re.match(PostalCodeRegex, string1):
            if re.match(PostalCodeFormat, string1):
                return True

        return False

    def isLicensePlate(self, string1, locale):
        """ check if the string is license plate or not """
        string1 = string1.upper()
        country_data = all_country[locale]

        LicensePlateFormat = country_data['LicensePlateFormat']

        if re.match(LicensePlateFormat, string1):
            return True

        return False
    
    def isPassportNumber(self, string1, locale):  # TODO: research more about passport number
        """ check if the string is passport number or not """
        country_data = all_country[locale]
        
        PassportNumberRegex = country_data['PassportNumberRegex']
        if re.match(PassportNumberRegex, string1):
            return True
        return False

    def isMobilePhone(self, string1, locale):
        """ check if the string is mobile phone or not """
        country_data = all_country[locale]

        MobileNumberRegex = country_data['MobileNumberRegex']

        if re.match(MobileNumberRegex, string1):
            return True

        return False
    
    def isDriverLicense(self, string1, locale):
        """ check if the string is driver license or not """
        country_data = all_country[locale]

        DrivingLicenseNumberRegex = country_data['DrivingLicenseNumberRegex']

        if re.match(DrivingLicenseNumberRegex, string1):
            return True

        return False
    
    def isDiscordUsername(self, string1):
        regex = "^.{3,32}#[0-9]{4}$"
        if re.match(regex, string1):
            return True
        return False
    
    def isCreditCard(self, string1):
        regex = "(^4[0-9]{12}(?:[0-9]{3})?$)|(^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$)|(3[47][0-9]{13})|(^3(?:0[0-5]|[68][0-9])[0-9]{11}$)|(^6(?:011|5[0-9]{2})[0-9]{12}$)|(^(?:2131|1800|35\d{3})\d{11}$)"
        if re.match(regex, string1):
            return True
        return False

    def equals(self, string1, string2, ignoreCase=False)-> bool:
        """ Check if the two string are equal or not """
        if not isinstance(string1, str) or not isinstance(string2, str):
            return False
        if ignoreCase:
            string1 = string1.lower()
            string2 = string2.lower()

        if string1 == string2:
            return True

        return False

    def isLength(self, string, min=0, max=None):
        """ check if the string length is between min and max """
        if min <= len(string) <= max:
            return True

        return False

    def isEmpty(self, string1):
        """ check if the string is empty or not """
        string1 = string1.strip()
        if string1 == "":
            return True

        return False

    def isAlphanumeric(self, string1):
        if string1.isalnum():
            return True

        return False

    def isAlpha(self, string1):
        if string1.isalpha():
            return True

        return False

    def isAscii(self, string1):
        if string1.isascii():
            return True

        return False

    def contains(self, string1, string2, ignoreCase=False):
        if ignoreCase:
            string1 = string1.lower()
            string2 = string2.lower()

        if string2 in string1:
            return True

        return False

    def isAfter(self, date1, date2=datetime.now()):
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

    def isBefore(self, date1, date2=datetime.now()):
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

    def isDate(self, date1):  # TODO: add more date format, currently only support YYYY-MM-DD
        """ check if the string is date or not """
        try:
            datetime.strptime(date1, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def isEmail(self, email):
        """ check if the string is email or not """
        if not self.__isvalidString(email):
            return False
        regex = "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
        if re.search(regex, email):
            return True

        return False

    def isDecimal(self, string1):
        """ check if the string is decimal or not """
        if string1.isdecimal():
            return True

        return False

    def isDivisibleBy(self, number, divisor):
        """ check if the number is divisible by divisor or not """
        if self.__isvalidNumber(number) and self.__isvalidNumber(divisor) and divisor != 0:
            if number % divisor == 0:
                return True

        return False

    def isEAN(self, string1):
        """ check if the string is EAN or not """
        pass

    def isHash(self, string1):
        """ check if the string is hash or not """
        pass

    def isIMEI(self, string1):
        """ check if the string is IMEI or not """
        if len(string1) == 15 or len(string1) == 17:
            return True
        return False

    def isIPV4(self, string1):
        """ check if the string is IP or not """
        regex = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        if re.search(regex, string1):
            return True
        return False

    def isIPV6(self, string1):
        regex = '(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'
        if re.match(regex, string1):
            return True
        return False

    def isSSN(self, string1):
        """ check if the string is SSN or not """
        regex = '^(?!0{3})(?!6{3})[0-8]\d{2}-(?!0{2})\d{2}-(?!0{4})\d{4}$'
        if re.match(regex, string1):
            return True
        return False
    
    def isJSON(self, string1):
        """ check if the string is JSON or not """
        try:
            json.loads(string1)
            return True
        except ValueError:
            return False

    def isJWT(self, string1):
        """ check if the string is JWT or not """
        pass

    def isLatLong(self, string1):
        """ check if the string is lat long or not """
        regex = '^((\-?|\+?)?\d+(\.\d+)?),\s*((\-?|\+?)?\d+(\.\d+)?)$'
        if re.match(regex, string1):
            return True
        return False

    def isMACAddress(self, string1):
        """ check if the string is MAC address or not """
        regex = '(([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})|([0-9a-fA-F]{2}[-]){5}([0-9a-fA-F]{2})|[0-9a-fA-F]{12})'
        if self.__isvalidString(string1) and re.search(regex, string1, re.IGNORECASE):
            return True
        return False

    def isMD5(self, string1):
        """ check if the string is MD5 or not """
        pass

   
    def isPort(self, string1):
        """ check if the string is port or not
        A port number is a 16-bit unsigned integer,
        so it has a minimum value of 0 and a maximum value of 65535.
        """
        if string1.isdigit() and 0 <= int(string1) <= 65535:
            return True
        return False

    def isSlug(self, string1):
        """ check if the string is slug or not """
        pass

    def isStrongPassword(self, string1):
        """ check if the string is strong password or not

        requirements:
            1. At least 8 characters long
            2. At least one uppercase letter
            3. At least one lowercase letter
            4. At least one number
            5. At least one special character
        """
        if len(string1) < 8:
            return False

        if not re.search("[a-z]", string1):
            return False

        if not re.search("[A-Z]", string1):
            return False

        if not re.search("[0-9]", string1):
            return False

        if not re.search("[_@$]", string1):
            return False

        return True

    def isUUID(self, string1):
        """ check if the string is UUID or not """
        pass

    # Sanitizers functions
    def toDate(self, string1):
        """ convert string to date """
        pass


    def toInt(self, string1):
        """ convert string to int """
        pass

    def trim(self, string1):
        """ trim string """
        if self.__isvalidString(string1):
            return string1.strip()
        
    def ltrim(self, string1):
        if self.__isvalidString(string1):
            return string1.lstrip()
        
    def rtrim(self, string1):
        if self.__isvalidString(string1):
            return string1.rstrip()
        
    def toUpperCase(self, string1):
        """ convert string to upper case """
        if self.__isvalidString(string1):
            return string1.upper()

    def toLowerCase(self, string1):
        """ convert string to lower case """
        if self.__isvalidString(string1):
            return string1.lower()

    def removeSpaces(self, string1):
        """ remove spaces from string """
        if self.__isvalidString(string1):
            return string1.replace(" ", "")
        
    def removeSymbols(self, string1):
        """ remove symbols from string """
        if self.__isvalidString(string1):
            return re.sub(r'[^\w\s]', '', string1)
    
    def distance(self, string1, string2):
        """ calculate distance between two strings """
        pass

    def distanceByIndex(self, string1, string2):
        """ calculate distance between two strings by index """
        pass

    def removeNonASCII(self, string1):
        """ remove non ASCII characters from string """
        if self.__isvalidString(string1):
            return string1.encode("ascii", "ignore").decode()

    def removeNonWord(self, string1):
        """ remove non word characters from string """
        pass

    def removeTags(self, string1):
        """ remove tags from string """
        if self.__isvalidString(string1):
            return re.sub(r'<[^>]*>', '', string1)

    def removeWhiteSpace(self, string1):
        """ remove white space from string """
        if self.__isvalidString(string1):
            return string1.replace(" ", "")
