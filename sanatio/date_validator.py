from datetime import datetime
from dateutil.parser import parse
from dateutil import relativedelta

from sanatio.base_class import BaseValidator


class DateValidator(BaseValidator):

    def isLeapYear(self, year) -> bool:
        """ check if the year is leap year or not """
        if isinstance(year, str):
            year = int(year)
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def isAfter(self, date1, date2=datetime.now(), format='%Y-%m-%d') -> bool:
        """ check if date1 is after date2 default date2 is current date

        Args:
            date1 (str): date in string format
            date2 (str): date in string format default is current date

        """
        if isinstance(date1, str):
            date1 = datetime.strptime(date1, format)
        if isinstance(date2, str):
            date2 = datetime.strptime(date2, format)

        return date1 > date2

    def isBefore(self, date1, date2=datetime.now(), format='%Y-%m-%d') -> bool:
        """
        check if date1 is before date2 default date2 is current date

        Args:
            date1 (str): date in string format
            date2 (str): date in string format default is current date
        """
        if isinstance(date1, str):
            date1 = datetime.strptime(date1, format)
        if isinstance(date2, str):
            date2 = datetime.strptime(date2, format)

        return date1 < date2

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
        return datetime.strptime(value, format) if self.isDate(value) else None

    def getYearDiff(self, date1, date2, increment=False, date_format="%d-%m-%Y"):
        """ get the difference between two dates in years """
        if isinstance(date1, str):
            date1 = datetime.strptime(date1, date_format)

        if isinstance(date2, str):
            date2 = datetime.strptime(date2, date_format)

        diff = relativedelta.relativedelta(date1, date2)
        total_days = abs(diff.years) * 365 + abs(diff.months) * 30 + abs(diff.days) if diff else 0
        total_years = total_days // 364
        if total_days % 364 > 0 and increment:
            total_years += 1

        return total_years
