import re

from sanatio.base_class import BaseValidator


class PasswordValidator(BaseValidator):

    def isStrongPassword(self, value: str,
                         min_length: int = 8,
                         special_chars: bool = True,
                         numbers: bool = True,
                         uppercase: bool = True,
                         lowercase: bool = True) -> bool:
        """ check if the string is strong password or not

        requirements:
            1. At least 8 characters long
            2. At least one uppercase letter
            3. At least one lowercase letter
            4. At least one number
            5. At least one special character
        """
        if not self.isPasswordLength(value, min_length) or \
           (special_chars and not self.isPasswordSpecialChar(value)) or \
           (numbers and not self.isPasswordNumber(value)) or \
           (uppercase and not self.isPasswordUppercase(value)) or \
           (lowercase and not self.isPasswordLowercase(value)):
            return False

        return True

    def isPasswordUppercase(self, value: str, min_length: int = 1) -> bool:
        """ check if the string has uppercase letters """
        if len(re.findall(r'[A-Z]', value)) >= min_length:
            return True

    def isPasswordLowercase(self, value: str, min_length: int = 1) -> bool:
        """ check if the string has lowercase letters """
        if len(re.findall(r'[a-z]', value)) >= min_length:
            return True

    def isPasswordNumber(self, value: str, min_length: int = 1) -> bool:
        """ check if the string has numbers """
        if len(re.findall(r'[0-9]', value)) >= min_length:
            return True

    def isPasswordLength(self, value: str, min_length: int = 8) -> bool:
        """ check if the string length is between min and max """
        if len(value) >= min_length:
            return True

    def isPasswordSpecialChar(self, value: str, min_length: int = 1) -> bool:
        """ check if the string has special characters """
        if len(re.findall(r'[_@$]', value)) >= min_length:
            return True

    def isPasswordMatch(self, value: str, match_value: str, ignore_case: bool = False) -> bool:
        """ check if the string matches the match_value """
        if ignore_case and value.lower() == match_value.lower():
            return True
        elif value == match_value:
            return True

    def isPasswordNotMatch(self, value: str, match_value: str, ignore_case: bool = False) -> bool:
        """ check if the string does not match the match_value """
        if ignore_case and value.lower() != match_value.lower():
            return True
        elif value != match_value:
            return True

    def isPasswordNotInList(self, value: str, list_values: list, ignore_case: bool = False) -> bool:
        """ check if the string is not in the list """
        if ignore_case and value.lower() not in [x.lower() for x in list_values]:
            return True
        elif value not in list_values:
            return True

    def isPasswordNotInFile(self, value: str, file_path: str, ignore_case: bool = False) -> bool:
        """ check if the string is not in the file """
        data = self.read_file(file_path, split_lines=True)

        if ignore_case and value.lower() not in [x.lower() for x in data]:
            return True
        elif value not in data:
            return True
