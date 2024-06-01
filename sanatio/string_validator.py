import re
from Levenshtein import distance as levenshtein_distance
from sanatio.base_class import BaseValidator


class StringValidator(BaseValidator):
    def __init__(self) -> None:
        super().__init__()

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

    def contains(self, value: str, substring: str, ignoreCase: bool=False) -> bool:
        if ignoreCase:
            value = value.lower()
            substring = substring.lower()

        if substring in value:
            return True

        return False

    def trim(self, value):
        """ trim string """
        if self.isvalidString(value):
            return value.strip()

    def ltrim(self, value):
        if self.isvalidString(value):
            return value.lstrip()

    def rtrim(self, value):
        if self.isvalidString(value):
            return value.rstrip()

    def toUpperCase(self, value):
        """ convert string to upper case """
        if self.isvalidString(value):
            return value.upper()

    def toLowerCase(self, value):
        """ convert string to lower case """
        if self.isvalidString(value):
            return value.lower()

    def removeSpaces(self, value):
        """ remove spaces from string """
        if self.isvalidString(value):
            return value.replace(" ", "")

    def removeSymbols(self, value):
        """ remove symbols from string """
        if self.isvalidString(value):
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

    def equals(self, value1: str, value2: str, ignoreCase: bool=False)-> bool:
        """ Check if the two string are equal or not """
        if not self.isvalidString(value1) or not self.isvalidString(value2):
            return False

        if ignoreCase:
            value1 = value1.lower()
            value2 = value2.lower()

        if value1 == value2:
            return True

        return False

    def removeNonASCII(self, value):
        """ remove non ASCII characters from string """
        if self.isvalidString(value):
            return value.encode("ascii", "ignore").decode()

    def removeNonWord(self, value):
        """ remove non word characters from string """
        if self.isvalidString(value):
            return re.sub(r'[^\w]', '', value)

    def removeNonNumeric(self, value):
        """ remove non numeric characters from string """
        if self.isvalidString(value):
            return re.sub(r'[^\d]', '', value)

    def removeTags(self, value):
        """ remove tags from string """
        if self.isvalidString(value):
            return re.sub(r'<[^>]*>', '', value)

    def removeWhiteSpace(self, value):
        """ remove white space from string """
        if self.isvalidString(value):
            return value.replace(" ", "")

