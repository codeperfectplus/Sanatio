import re
import json
from datetime import datetime
from dateutil.parser import parse
from Levenshtein import distance as levenshtein_distance

from sanatio.utils.utils import all_country, regexs
from sanatio.utils.checksum import checksum_aadhar, checksum_credit_card
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
