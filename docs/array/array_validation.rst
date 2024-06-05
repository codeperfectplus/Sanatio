Array Validation functions
===========================

The following functions are used to validate Array

.. code:: python
    
    from sanatio import Sanatio

    val = Sanatio()

- `isArray` - Check if the value is an array

:code:`isArray()` Returns True if the value is an array
    args: value

    >>> val.is_array([1, 2, 3])
    True

    >>> val.is_array(1)
    False

- `isArrayLength` - Check if the value is an array and has a specific length
    args: value, min, max

    >>> val.is_array_length([1, 2, 3], min=2, max=3)
    True

    >>> val.is_array_length([1, 2, 3], min=4, max=5)
    False

- `isContains` - Check if the value is an array and contains a specific value
    args: value, contains

    >>> val.is_contains([1, 2, 3], element=2)
    True

    >>> val.is_contains([1, 2, 3], element=4)
    False

- `isUnique` - Check if the value is an array and contains unique values

    >>> val.is_unique([1, 2, 3])
    True

    >>> val.is_unique([1, 2, 3, 1])
    False

- `isMultidimensional` - Check if the value is a multidimensional array

    >>> val.is_multidimensional([[1, 2, 3], [4, 5, 6]])
    True

    >>> val.is_multidimensional([1, 2, 3])
    False

- `isMinlength` - Check if the value is an array and has a minimum length
    args: value, min

    >>> val.is_minlength([1, 2, 3], min=2)
    True

    >>> val.is_minlength([1, 2, 3], min=4)
    False

- `isMaxlength` - Check if the value is an array and has a maximum length
    args: value, max

    >>> val.is_maxlength([1, 2, 3], max=4)
    True

    >>> val.is_maxlength([1, 2, 3], max=2)
    False


