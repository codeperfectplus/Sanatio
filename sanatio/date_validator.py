import re
import json
from datetime import datetime
from dateutil.parser import parse
from Levenshtein import distance as levenshtein_distance

from sanatio.utils.utils import all_country, regexs
from sanatio.utils.checksum import checksum_aadhar, checksum_credit_card
from sanatio.base_class import BaseValidator


class DateValidator:
    def __init__(self) -> None:
        pass

    def isLeapYear(self, year) -> bool:
        """ check if the year is leap year or not """
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def isAfter(self, date1, date2=datetime.now()) -> bool:
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

    def isBefore(self, date1, date2=datetime.now()) -> bool:
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

    def isDate(self, value) -> bool:
        """ check if the string is date or not """
        if not self.isvalidString(value):
            return False
        try:
            date_obj = parse(value)
            if date_obj:
                return True
        except Exception:
            return False
        return False

    def toDate(self, value, format='%Y-%m-%d'):  # need to improve this function
        """ convert string to date """
        if self.isDate(value):
            date = datetime.strptime(value, format)
            return date
        else:
            return None

