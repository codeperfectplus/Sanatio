import re

from sanatio.base_class import BaseValidator
from sanatio.utils.utils import regexs_dict


class NumberValidator(BaseValidator):

    def isDecimal(self, value: float) -> bool:
        """ check if the string is decimal or not """
        return self.isvalidNumber(value)

    def isDivisibleBy(self, number: int, divisor: int) -> bool:
        """ check if the number is divisible by divisor or not """
        return self.isvalidNumber(number) and self.isvalidNumber(divisor) and divisor != 0 and number % divisor == 0

    def truncate(self, value: float, digits: int) -> float:
        """ truncate the float value """
        regex = regexs_dict.get('truncate_regex')
        return float(re.findall(f'{regex}{{{digits}}}', str(value))[0])

    def toInt(self, value):
        """ convert string to int """
        try:
            return int(float(value))
        except ValueError:
            return None

    def toFloat(self, value):
        """ convert string to float """
        try:
            return float(value)
        except ValueError:
            return None

    def isPositive(self, value):
        """ check if the value is positive or not """
        return self.isvalidNumber(value) and value > 0

    def isNegative(self, value):
        """ check if the value is negative or not """
        return self.isvalidNumber(value) and value < 0

    def isInteger(self, value):
        """ check if the value is integer or not """
        return self.isvalidNumber(value) and isinstance(value, int)

    def isFloat(self, value):
        """ check if the value is float or not """
        return self.isvalidNumber(value) and isinstance(value, float)

    def isZero(self, value):
        """ check if the value is zero or not """
        return self.isvalidNumber(value) and value == 0

    def isNonZero(self, value):
        """ check if the value is non-zero or not """
        return self.isvalidNumber(value) and value != 0

    def isGreaterThan(self, value, other):
        """ check if the value is greater than other or not """
        return self.isvalidNumber(value) and self.isvalidNumber(other) and value > other

    def isGreaterThanOrEqual(self, value, other):
        """ check if the value is greater than or equal to other or not """
        return self.isvalidNumber(value) and self.isvalidNumber(other) and value >= other

    def isLessThan(self, value, other):
        """ check if the value is less than other or not """
        return self.isvalidNumber(value) and self.isvalidNumber(other) and value < other

    def isLessThanOrEqual(self, value, other):
        """ check if the value is less than or equal to other or not """
        return self.isvalidNumber(value) and self.isvalidNumber(other) and value <= other

    def isBetween(self, value, min_value, max_value):
        """ check if the value is between min_value and max_value or not """
        return self.isvalidNumber(value) and self.isvalidNumber(min_value) and \
            self.isvalidNumber(max_value) and min_value <= value <= max_value
