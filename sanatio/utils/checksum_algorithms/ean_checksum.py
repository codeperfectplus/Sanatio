class EANCheckSum:
    def __init__(self, input_value: str) -> None:
        self.input_value = input_value.replace(' ', '')
    
    def __last_digit_and_remaining_numbers(self) -> tuple:
        """ Returns the last digit of a number """
        return int(self.input_value[-1]), self.input_value[:-1]

    def __checksum_ean13(self):
        """Calculate the checksum for the EAN code"""
        last_digit, remaining_numbers = self.__last_digit_and_remaining_numbers()
        total_sum = sum(int(remaining_numbers[i]) * 3 if i % 2 != 0 else \
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
