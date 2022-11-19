""" Luhn Algorithm for checksum calculation. """

class LuhnAlgorithm(object):
    """Class to validate a number using Luhn algorithm."""
    
    def __init__(self) -> None:
        pass
    
    def __checksum(self, number: str) -> int:
        nums = []
        
        last_digit = int(number[-1])
        
        for idx, num in enumerate(number[:-1]):
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
    
    def verify(self, number: str) -> bool:
        """Verify a number using Luhn algorithm."""
        if isinstance(number, int):
            number = str(number)
            
        return self.__checksum(number)
        
        
        