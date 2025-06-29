from typing import Any, List, Optional
from sanatio.base_class import BaseValidator


class ArrayValidator(BaseValidator):
    def is_array(self, value: Any) -> bool:
        """Check if the value is a list (array)."""
        return isinstance(value, list)

    def is_array_length(self, value: List[Any], min_length: int = 0, max_length: Optional[int] = None) -> bool:
        """Check if the array length is between min_length and max_length (inclusive)."""
        if not self.is_array(value):
            return False
        if max_length is not None:
            return min_length <= len(value) <= max_length
        return len(value) >= min_length

    def is_contains(self, value: List[Any], item: Any) -> bool:
        """Check if the array contains a given element."""
        if not self.is_array(value):
            return False
        return item in value

    def is_unique(self, value: List[Any]) -> bool:
        """Check if all elements in the array are unique."""
        if not self.is_array(value):
            return False
        try:
            return len(value) == len(set(value))
        except TypeError:
            # Handles case where elements are unhashable (e.g., lists)
            seen = []
            for i in value:
                if i in seen:
                    return False
                seen.append(i)
            return True

    def is_multidimensional(self, value: List[Any]) -> bool:
        """Check if the array is multidimensional (contains at least one list)."""
        if not self.is_array(value):
            return False
        return any(isinstance(i, list) for i in value)

    def is_min_length(self, value: List[Any], min_length: int) -> bool:
        """Check if the array length is greater than or equal to min_length."""
        if not self.is_array(value):
            return False
        return len(value) >= min_length

    def is_max_length(self, value: List[Any], max_length: int) -> bool:
        """Check if the array length is less than or equal to max_length."""
        if not self.is_array(value):
            return False
        return len(value) <= max_length
