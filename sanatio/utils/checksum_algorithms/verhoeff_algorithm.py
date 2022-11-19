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

class VerhoeffAlgorithm(object):
    def __init__(self):
        pass

    def __checksum(self, number):
        """ For a given number returns a Verhoeff checksum digit """
        c = 0
        last_digit = int(number[-1])
        for i, item in enumerate(reversed(number[:-1])):
            c = verhoeff_table_d[c][verhoeff_table_p[(i+1)%8][int(item)]]
        
        print('c', c, type(c))
        print('last_digit', last_digit, type(last_digit))
        
        if c == last_digit:
            return True
        
        return False

    def verify(self, number):
        """ Verify a given number including its checksum digit """
        if isinstance(number, int):
            number = str(number)

        number = number.replace(' ', '')
        return self.__checksum(number)