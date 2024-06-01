class ArrayValidator:
    def __init__(self) -> None:
        pass
    
    def isArray(self, value) -> bool:  # TODO: test cases is pending
        """ check if the string is array or not """
        if isinstance(value, list):
            return True
        return False
    
    def isLength(self, value, min: int=0, max: int=None) -> bool:  # TODO: test cases is pending
        """ check if the array length is between min and max """
        if min <= len(value) <= max:
            return True
        return False
    
    def isContains(self, value, element) -> bool:  # TODO: test cases is pending
        """ check if the array contains the element or not """
        if element in value:
            return True
        return False
