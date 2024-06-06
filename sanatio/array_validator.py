from sanatio.base_class import BaseValidator


class ArrayValidator(BaseValidator):

    def isArray(self, value) -> bool:
        """ check if the string is array or not """
        return isinstance(value, list)

    def isArrayLength(self, value, min: int = 0, max: int = None) -> bool:
        """ check if the array length is between min and max """
        return min <= len(value) <= max

    def isContains(self, value, contains) -> bool:
        """ check if the array contains the element or not """
        return contains in value

    def isUnique(self, value) -> bool:
        """ check if the array contains unique elements or not """
        return len(value) == len(set(value))

    def isMultidimensional(self, value) -> bool:
        """ check if the array is multidimensional or not """
        return any(isinstance(i, list) for i in value)

    def isMinlength(self, value, min: int) -> bool:
        """ check if the array length is greater than min """
        return len(value) > min

    def isMaxlength(self, value, max: int) -> bool:
        """ check if the array length is less than max """
        return len(value) < max
