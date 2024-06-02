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
    (7, 0, 4, 6, 9, 1, 3, 2, 5 ,8))

verhoeff_table_inv = (0, 4, 3, 2, 1, 5, 6, 7, 8, 9)

class VerhoeffAlgorithm(object):  # TODO: need to review this variable names
    def __init__(self, input_value: str) -> None:
        self.input_value = input_value.replace(' ', '')
    
    def __last_digit_and_remaining_numbers(self) -> tuple:
        """ Returns the last digit of a number """
        return int(self.input_value[-1]), self.input_value[:-1]

    def __checksum(self):
        """ For a given number returns a Verhoeff checksum digit """
        c = 0
        last_digit, remaining_numbers = self.__last_digit_and_remaining_numbers()
        for i, item in enumerate(reversed(remaining_numbers)):
            c = verhoeff_table_d[c][verhoeff_table_p[(i+1)%8][int(item)]]
    
        if c == last_digit:
            return True
        
        return False

    def verify(self):
        """ Verify a given number including its checksum digit """
        # if isinstance(input_value, int):
        #     number = str(input_value)
        return self.__checksum()
