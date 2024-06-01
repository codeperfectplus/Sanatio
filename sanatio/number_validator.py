from sanatio.base_class import BaseValidator


class NumberValidator(BaseValidator):
    def __init__(self) -> None:
        pass

    def isDecimal(self, value: float) -> bool:
        """ check if the string is decimal or not """
        if not self.isvalidNumber(value):
            return False

        if value.isdecimal():
            return True

        return False

    def isDivisibleBy(self, number: int, divisor: int) -> bool:
        """ check if the number is divisible by divisor or not """
        if self.isvalidNumber(number) and self.isvalidNumber(divisor) and divisor != 0:
            if number % divisor == 0:
                return True

        return False

    def toInt(self, value):
        """ convert string to int """
        if isinstance(value, int):
            return value

        elif isinstance(value, float):
            return int(value)

        try:
            value = int(float(value))
            return value

        except ValueError:
            value = 0

        return value

