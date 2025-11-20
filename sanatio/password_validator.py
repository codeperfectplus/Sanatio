import re
from typing import List, Optional

from sanatio.base_class import BaseValidator


class PasswordValidator(BaseValidator):

    def is_strong_password(self, value: str,
                           min_length: int = 8,
                           special_chars: bool = True,
                           numbers: bool = True,
                           uppercase: bool = True,
                           lowercase: bool = True) -> bool:
        """Check if the string is a strong password.

        Requirements:
            1. At least `min_length` characters
            2. At least one uppercase letter (optional)
            3. At least one lowercase letter (optional)
            4. At least one number (optional)
            5. At least one special character (optional)
        """
        if not self.is_password_length(value, min_length):
            return False
        if special_chars and not self.is_password_special_char(value):
            return False
        if numbers and not self.is_password_number(value):
            return False
        if uppercase and not self.is_password_uppercase(value):
            return False
        if lowercase and not self.is_password_lowercase(value):
            return False

        return True

    def is_password_uppercase(self, value: str, min_length: int = 1) -> bool:
        """Check if the string has at least `min_length` uppercase letters."""
        return len(re.findall(r'[A-Z]', value)) >= min_length

    def is_password_lowercase(self, value: str, min_length: int = 1) -> bool:
        """Check if the string has at least `min_length` lowercase letters."""
        return len(re.findall(r'[a-z]', value)) >= min_length

    def is_password_number(self, value: str, min_length: int = 1) -> bool:
        """Check if the string has at least `min_length` digits."""
        return len(re.findall(r'\d', value)) >= min_length

    def is_password_length(self, value: str, min_length: int = 8) -> bool:
        """Check if the string is at least `min_length` characters long."""
        return len(value) >= min_length

    def is_password_special_char(self, value: str, min_length: int = 1) -> bool:
        """Check if the string has at least `min_length` special characters."""
        # Common special characters set: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        return len(re.findall(r'[^a-zA-Z0-9]', value)) >= min_length

    def is_password_match(self, value: str, match_value: str, ignore_case: bool = False) -> bool:
        """Check if the password matches `match_value`."""
        if ignore_case:
            return value.lower() == match_value.lower()
        return value == match_value

    def is_password_not_match(self, value: str, match_value: str, ignore_case: bool = False) -> bool:
        """Check if the password does not match `match_value`."""
        if ignore_case:
            return value.lower() != match_value.lower()
        return value != match_value

    def is_password_not_in_list(self, value: str, list_values: Optional[List[str]] = None,
                                ignore_case: bool = False) -> bool:
        """Check if the password is not in a list of disallowed passwords."""
        if list_values is None:
            list_values = []

        if ignore_case:
            return value.lower() not in [x.lower() for x in list_values]
        return value not in list_values

    def is_password_not_in_file(self, value: str, file_path: str, ignore_case: bool = False) -> bool:
        """Check if the password is not in a file of disallowed passwords."""
        if not hasattr(self, "read_file"):
            raise NotImplementedError("read_file() method not implemented in BaseValidator or subclass.")

        data = self.read_file(file_path, split_lines=True)

        if ignore_case:
            return value.lower() not in [x.lower() for x in data]
        return value not in data

    # Alias method for backward compatibility with tests
    def isStrongPassword(self, value: str, min_length: int = 8, special_chars: bool = True, 
                        numbers: bool = True, uppercase: bool = True, lowercase: bool = True) -> bool:
        """Alias for is_strong_password method."""
        return self.is_strong_password(value, min_length, special_chars, numbers, uppercase, lowercase)
