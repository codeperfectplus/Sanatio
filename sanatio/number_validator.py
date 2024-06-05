from sanatio.base_class import BaseValidator


class NumberValidator(BaseValidator):

    def isDecimal(self, value: float) -> bool:
        """ check if the string is decimal or not """
        if not self.isvalidNumber(value):
            return False

        if value.isdecimal():
            return True

        return False

    def isDivisibleBy(self, number: int, divisor: int) -> bool:
        """ check if the number is divisible by divisor or not """
        return self.isvalidNumber(number) and self.isvalidNumber(divisor) and divisor != 0 and number % divisor == 0

    def toInt(self, value):
        """ convert string to int """
        try:
            return int(float(value))
        except ValueError:
            return None
