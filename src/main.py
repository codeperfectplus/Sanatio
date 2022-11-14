import re
import string
from datetime import datetime

class Validator(object):
    
    def __init__(self):
        pass

    def equals(self, string1, string2, ignoreCase=False):
        """ Check if the two string are equal or not """
        if string1 == string2:
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

    def contains(self, string1, string2):
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
    
    def isDate(self, date1):
        """ check if the string is date or not """
        try:
            datetime.strptime(date1, '%Y-%m-%d')
            return True
        except ValueError:
            return False
        
    def isEmail(self, email):
        """ check if the string is email or not """
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
        if number % divisor == 0:
            return True
        
        return False
    
    def isEAN(self, string1):
        """ check if the string is EAN or not """
        pass
    
    def isEmpty(self, string1):
        """ check if the string is empty or not """
        if string1 == "":
            return True
        
        return False
    
    def isHash(self, string1):
        """ check if the string is hash or not """
        pass
    
    def isIMEI(self, string1):
        """ check if the string is IMEI or not """
        if len(string1) == 15:
            return True
        
    def isIP(self, string1):
        """ check if the string is IP or not """
        regex = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        if re.search(regex, string1):
            return True
        return False
    
    def isJSON(self, string1):
        """ check if the string is JSON or not """
        pass
    
    def isJWT(self, string1):
        """ check if the string is JWT or not """
        pass
    
    def isLatLong(self, string1):
        """ check if the string is lat long or not """
        pass
    
    def isLength(self, string, min=0, max=None):
        """ check if the string length is between min and max """
        if min <= len(string) <= max:
            return True
        
        return False
    
    def isLicensePlate(self, string1):
        """ check if the string is license plate or not """
        pass
    
    def isMACAddress(self, string1):
        """ check if the string is MAC address or not """
        pass
    
    def isMD5(self, string1):
        """ check if the string is MD5 or not """
        pass
    
    def isPassportNumber(self, string1):
        """ check if the string is passport number or not """
        if len(string1) == 9 and string1.isalnum():
            return True
        return False

    def isPort(self, string1):
        """ check if the string is port or not 
        A port number is a 16-bit unsigned integer, 
        so it has a minimum value of 0 and a maximum value of 65535.
        """
        if string1.isdigit() and 0 <= int(string1) <= 65535:
            return True
        return False
    
    def isPostalCode(self, string1):
        """ check if the string is postal code or not """
        pass
    
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
    
    def toBoolean(self, string1):
        """ convert string to boolean """
        pass
    
    def toFloat(self, string1):
        """ convert string to float """
        pass
    
    def toInt(self, string1):
        """ convert string to int """
        pass
    
    def trim(self, string1):
        """ trim string """
        pass
    
    
        
    
    