""" Luhn Algorithm for checksum calculation. """

class LuhnAlgorithm(object):  # TODO: need to review this variable names
    """Class to validate a number using Luhn algorithm."""
    
    def __init__(self) -> None:
        pass
    
    def __last_digit(self, number: str) -> int:
        """ Returns the last digit of a number """
        return int(number[-1])
    
    def __checksum(self, numbers: str) -> int:
        nums = []
        last_digit = self.__last_digit(numbers)
        for idx, num in enumerate(numbers[:-1]):
            num = int(num)
            idx = idx + 1
            
            if idx % 2 == 0:
                nums.append(num)
            else:
                num = num * 2
                if num > 9:  # if num is 2 digit
                    num = num % 10 + num // 10
                    nums.append(num)
                elif num < 9:
                    nums.append(num)

        total = sum(nums)
        if (total + last_digit) % 10 == 0:
            return True
        return False
    
    def verify(self, numbers: str) -> bool:
        """Verify a number using Luhn algorithm."""
        if isinstance(numbers, int):
            numbers = str(numbers)
            
        return self.__checksum(numbers)
        