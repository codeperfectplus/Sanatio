import re

class PasswordValidator:
    def __init__(self):
        super().__init__()

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
    
    def isPasswordLength(self, value: str, min_length: int, max_length: int) -> bool:
        """ check if the string length is between min and max """
        if min_length <= len(value) <= max_length:
            return True

        return False
    
    def isPasswordMatch(self, value: str, match_value: str) -> bool:
        """ check if the string matches the match_value """
        if value == match_value:
            return True

        return False
    
    def isPasswordNotMatch(self, value: str, match_value: str) -> bool:
        """ check if the string does not match the match_value """
        if value != match_value:
            return True

        return False
    
    def isPasswordNotInList(self, value: str, list_values: list) -> bool:
        """ check if the string is not in the list """
        if value not in list_values:
            return True

        return False
    
    def isPasswordNotInFile(self, value: str, file_path: str) -> bool:
        """ check if the string is not in the file """
        with open(file_path, 'r') as f:
            data = f.read().splitlines()
        
        if value not in data:
            return True

        return False
    
    def isPasswordNotInDict(self, value: str, dict_values: dict) -> bool:
        """ check if the string is not in the dictionary """
        if value not in dict_values:
            return True

        return False
    