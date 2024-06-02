class EANCheckSum:
    def __init__(self):
        pass

    def checksum_ean13(self, value: str) -> bool:
        """Calculate the checksum for the EAN code"""
        last_digit = int(value[-1])
        remaining_numbers = value[:-1]
        total_sum = sum(int(remaining_numbers[i]) * 3 if i % 2 != 0 else \
            int(remaining_numbers[i]) for i in range(len(remaining_numbers)))
        unit_digit = 0 if total_sum % 10 == 0 else 10 - (total_sum % 10)
        if unit_digit == last_digit:
            return True
        
    def checksum_ean8(self, value: str) -> bool:
        """Calculate the checksum for the EAN code"""
        pass

    def is_valid(self, value: str) -> bool:
        """Check if the EAN code is valid"""
        return self.checksum_ean13(value) if len(value) == 13 else self.checksum_ean8(value)
