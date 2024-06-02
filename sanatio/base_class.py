class BaseValidator:
    """ Base validator class for validating the data """
    def __init__(self):
        pass

    def isvalidString(self, value: str) -> bool:
        """ check if the string is valid or not """
        return isinstance(value, str) and value != ''
        
    def isvalidNumber(self, value: int)-> bool:
        """ check if the number is valid or not """
        return isinstance(value, int)
        
    def isvalidBoolean(self, value)-> bool:
        """ check if the string is boolean or not """
        return isinstance(value, bool)

    def removeSpaces(self, value):
        """ remove spaces from string """
        return value.replace(" ", "") if self.isvalidString(value) else None
