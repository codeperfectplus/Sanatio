import re

from sanatio.base_class import BaseValidator
from sanatio.utils.utils import regexs_dict


class NumberValidator(BaseValidator):

    def isDecimal(self, value: float) -> bool:
        """ check if the string is decimal or not """
        return self.isvalidNumber(value)

    def isDivisibleBy(self, number: int, divisor: int) -> bool:
        """ check if the number is divisible by divisor or not """
        return (self.isvalidNumber(number) and
                self.isvalidNumber(divisor) and
                divisor != 0 and
                number % divisor == 0)

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
        return (self.isvalidNumber(value) and
                self.isvalidNumber(other) and
                value > other)

    def isGreaterThanOrEqual(self, value, other):
        """ check if the value is greater than or equal to other or not """
        return (self.isvalidNumber(value) and
                self.isvalidNumber(other) and
                value >= other)

    def isLessThan(self, value, other):
        """ check if the value is less than other or not """
        return (self.isvalidNumber(value) and
                self.isvalidNumber(other) and
                value < other)

    def isLessThanOrEqual(self, value, other):
        """ check if the value is less than or equal to other or not """
        return (self.isvalidNumber(value) and
                self.isvalidNumber(other) and
                value <= other)

    def isBetween(self, value, min_value, max_value):
        """ check if the value is between min_value and max_value or not """
        return (self.isvalidNumber(value) and
                self.isvalidNumber(min_value) and
                self.isvalidNumber(max_value) and
                min_value <= value <= max_value)

    def isPrime(self, value) -> bool:
        """ check if the value is a prime number or not """
        if not self.isvalidNumber(value) or value < 2:
            return False
        for i in range(2, int(value ** 0.5) + 1):
            if value % i == 0:
                return False
        return True

    def isEven(self, value) -> bool:
        """ check if the value is even or not """
        return self.isvalidNumber(value) and value % 2 == 0

    def isOdd(self, value) -> bool:
        """ check if the value is odd or not """
        return self.isvalidNumber(value) and value % 2 != 0

    def isMultipleOf(self, value, multiple) -> bool:
        """ check if the value is a multiple of another number """
        if (not self.isvalidNumber(value) or
                not self.isvalidNumber(multiple) or
                multiple == 0):
            return False
        return value % multiple == 0

    def isSquare(self, value) -> bool:
        """ Check if the value is a perfect square or not """
        if not self.isvalidNumber(value):
            return False
        if value < 0:
            return False
        square_root = round(value ** 0.5)
        return square_root ** 2 == value

    def isCube(self, value) -> bool:
        """ Check if the value is a perfect cube or not """
        if not self.isvalidNumber(value):
            return False
        if value < 0:
            cube_root = round((-value) ** (1/3))
            return -cube_root ** 3 == value
        else:
            cube_root = round(value ** (1/3))
            return cube_root ** 3 == value
