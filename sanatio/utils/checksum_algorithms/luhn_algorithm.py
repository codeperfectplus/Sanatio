""" Luhn Algorithm for checksum calculation. """

class LuhnAlgorithm(object):  # TODO: need to review this variable names
    """Class to validate a number using Luhn algorithm."""
    
    def __init__(self, input_value: str) -> None:
        self.input_value = input_value.replace(' ', '')
    
    def __last_digit_and_remaining_numbers(self) -> tuple:
        """ Returns the last digit of a number """
        return int(self.input_value[-1]), self.input_value[:-1]
    
    def __checksum(self) -> int:
        last_digit, remaining_numbers = self.__last_digit_and_remaining_numbers()
        for idx, num in enumerate(remaining_numbers):
            nums = [int(num) if idx % 2 != 0 else int(num) * 2 if int(num) * 2 <= 9 \
                    else int(num) * 2 % 10 + int(num) * 2 // 10 \
                        for idx, num in enumerate(remaining_numbers)]

        return (sum(nums) + last_digit) % 10 == 0
    
    def verify(self) -> bool:
        """Verify a number using Luhn algorithm."""            
        return self.__checksum()
        