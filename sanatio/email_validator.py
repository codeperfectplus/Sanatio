import re
from sanatio.base_class import BaseValidator


class EmailValidator(BaseValidator):
    def __init__(self):
        super().__init__()

    def isEmail(self, value: str, checkDNS: bool=False) -> bool:
        """ check if the string is email or not """
        if not self.isvalidString(value):
            return False
        regex = "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
        if re.search(regex, value):
            return True

        return False
