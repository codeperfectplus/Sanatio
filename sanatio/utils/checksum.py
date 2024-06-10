# Verhoeff's algorithm implementation for checksum digit calculation
verhoeff_table_d = (
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    (1, 2, 3, 4, 0, 6, 7, 8, 9, 5),
    (2, 3, 4, 0, 1, 7, 8, 9, 5, 6),
    (3, 4, 0, 1, 2, 8, 9, 5, 6, 7),
    (4, 0, 1, 2, 3, 9, 5, 6, 7, 8),
    (5, 9, 8, 7, 6, 0, 4, 3, 2, 1),
    (6, 5, 9, 8, 7, 1, 0, 4, 3, 2),
    (7, 6, 5, 9, 8, 2, 1, 0, 4, 3),
    (8, 7, 6, 5, 9, 3, 2, 1, 0, 4),
    (9, 8, 7, 6, 5, 4, 3, 2, 1, 0))

verhoeff_table_p = (
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    (1, 5, 7, 6, 2, 8, 3, 0, 9, 4),
    (5, 8, 0, 3, 7, 9, 6, 1, 4, 2),
    (8, 9, 1, 6, 0, 4, 3, 5, 2, 7),
    (9, 4, 5, 3, 1, 2, 6, 8, 7, 0),
    (4, 2, 8, 6, 5, 7, 3, 9, 0, 1),
    (2, 7, 9, 3, 8, 0, 6, 4, 1, 5),
    (7, 0, 4, 6, 9, 1, 3, 2, 5, 8))

verhoeff_table_inv = (0, 4, 3, 2, 1, 5, 6, 7, 8, 9)


class BaseChecksumAlgorithm:
    def __init__(self, input_value: str) -> None:
        self.input_value = input_value.replace(' ', '')

    def last_digit_and_remaining_numbers(self) -> tuple:
        """ Returns the last digit and the remaining numbers """
        return int(self.input_value[-1]), self.input_value[:-1]


class VerhoeffAlgorithm(BaseChecksumAlgorithm):

    def __checksum(self):
        """ For a given number returns a Verhoeff checksum digit """
        c = 0
        last_digit, remaining_numbers = self.last_digit_and_remaining_numbers()
        for i, item in enumerate(reversed(remaining_numbers)):
            c = verhoeff_table_d[c][verhoeff_table_p[(i + 1) % 8][int(item)]]

        if c == last_digit:
            return True

        return False

    def verify(self):
        """ Verify a given number including its checksum digit """
        return self.__checksum()


class EANCheckSum(BaseChecksumAlgorithm):

    def __checksum_ean13(self):
        """Calculate the checksum for the EAN code"""
        last_digit, remaining_numbers = self.last_digit_and_remaining_numbers()
        total_sum = sum(int(remaining_numbers[i]) * 3 if i % 2 != 0 else
                        int(remaining_numbers[i]) for i in range(len(remaining_numbers)))
        unit_digit = 0 if total_sum % 10 == 0 else 10 - (total_sum % 10)
        if unit_digit == last_digit:
            return True

    def __checksum_ean8(self) -> bool:
        """Calculate the checksum for the EAN code"""
        pass

    def verify(self) -> bool:
        """Check if the EAN code is valid"""
        return self.__checksum_ean13() if len(self.input_value) == 13 else self.__checksum_ean8()


class LuhnAlgorithm(BaseChecksumAlgorithm):
    """Class to validate a number using Luhn algorithm.

    Args:
        input_value (str): The input value to validate.

    returns:
        bool: True if the number is valid, False otherwise.
    """

    def __checksum(self) -> int:
        last_digit, remaining_numbers = self.last_digit_and_remaining_numbers()
        nums = [int(num) if idx % 2 != 0 else int(num) * 2 if int(num) * 2 <= 9
                else int(num) * 2 % 10 + int(num) * 2 // 10
                for idx, num in enumerate(reversed(remaining_numbers))]

        return (sum(nums) + last_digit) % 10 == 0

    def verify(self) -> bool:
        """Verify a number using Luhn algorithm."""
        return self.__checksum()


class Mod10Algorithm(LuhnAlgorithm):
    # luhn algorithm and mod10 algorithm are same
    pass
