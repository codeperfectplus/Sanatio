String Validation functions
===========================

The following functions are used to validate strings. 

.. code:: python
    
    from sanatio import Validator

    val = Validator()

:code:`equals(value1, value2, ignoreCase)` 
    Returns true if the two strings are equal.

    >>> val.equals("abc", "abc")
    True
    >>> val.equals("abc", "ABC")
    False
    >>> val.equals("abc", "ABC", ignoreCase=True)
    True

:code:`isLength(value, min, max)` 
    Returns true if the string is between the specified min and max.

    >>> val.isLength("abc", 2, 3)
    True
    >>> val.isLength("abc", 2, 2)
    False

:code:`isEmpty(value)` 
    Returns true if the string is empty.

    >>> val.isEmpty("")
    True
    >>> val.isEmpty("abc")
    False

:code:`isAlphanumeric(value)` 
    Returns true if the string is alphanumeric.

    >>> val.isAlphanumeric("abc123")
    True
    >>> val.isAlphanumeric("abc123!")
    False

:code:`isAlpha(value)`
    Returns true if the string is alphabetic.

    >>> val.isAlpha("abc")
    True
    >>> val.isAlpha("abc123")
    False

:code:`contains(value, substring)`
    Returns true if the string contains the substring.

    >>> val.contains("abc", "a")
    True
    >>> val.contains("abc", "d")
    False

