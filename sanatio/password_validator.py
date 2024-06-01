import re
import json
from datetime import datetime
from dateutil.parser import parse
from Levenshtein import distance as levenshtein_distance

from sanatio.utils.utils import all_country, regexs
from sanatio.utils.checksum import checksum_aadhar, checksum_credit_card
from sanatio.base_class import BaseValidator


class PasswordValidator(BaseValidator):
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


