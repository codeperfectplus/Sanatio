class BaseValidator:
    """ Base validator class for validating the data """
    def __init__(self):
        pass

    def isvalidString(self, value: str) -> bool:
        """ check if the string is valid or not """
        if value is None or value == '':
            return False

        if isinstance(value, str):
            return True
        
    def isvalidNumber(self, value: int)-> bool:
        """ check if the number is valid or not """
        if value is None:
            return False

        if isinstance(value, (int, float)):
            return True
        
    def isvalidBoolean(self, value)-> bool:
        """ check if the string is boolean or not """
        if value is None:
            return False

        if isinstance(value, bool):
            return True
