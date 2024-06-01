import re
import json
from datetime import datetime
from dateutil.parser import parse
from Levenshtein import distance as levenshtein_distance

from sanatio.utils.utils import all_country, regexs
from sanatio.utils.checksum import checksum_aadhar, checksum_credit_card
from sanatio.base_class import BaseValidator


class UsernameValidator:
    def __init__(self):
        pass

    def isDiscordUsername(self, value: str) -> bool:
        regex = "^.{3,32}#[0-9]{4}$"
        if re.match(regex, value):
            return True
        return False
