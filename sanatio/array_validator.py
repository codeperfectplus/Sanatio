class ArrayValidator:
    def __init__(self) -> None:
        pass
    
    def isArray(self, value) -> bool:
        """ check if the string is array or not """
        return isinstance(value, list)
    
    def isLength(self, value, min: int=0, max: int=None) -> bool:
        """ check if the array length is between min and max """
        return min <= len(value) <= max
    
    def isContains(self, value, element) -> bool:
        """ check if the array contains the element or not """
        return element in value
    
    def isUnique(self, value) -> bool:
        """ check if the array contains unique elements or not """
        return len(value) == len(set(value))
