import string


class Validator(object):
    
    def __init__(self):
        pass

    def equals(self, string1, string2, ignoreCase=False):
        """ Check if the two string are equal or not """
        if string1 == string2:
            return True
        
        return False

    def isAlphanumeric(self, string1):
        if string1.isalnum():
            return True
        
        return False

    def isAlpha(self, string1):
        if string1.isalpha():
            return True

        return False
    
    def isAscii(self, string1):
        pass

    





