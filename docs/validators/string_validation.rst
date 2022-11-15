String Validation functions
===========================

The following functions are used to validate strings. 

.. code:: python
    
    from validator import Validator

    val = Validator()

:code:`equals(value1, value2, ignoreCase)` 
    Returns true if the two strings are equal.

    >>> equals("abc", "abc")
    True
    >>> equals("abc", "ABC")
    False
    >>> equals("abc", "ABC", ignoreCase=True)
    True

:code:`isLength(value, min, max)` 
    Returns true if the string is between the specified min and max.

    >>> isLength("abc", 2, 3)
    True
    >>> isLength("abc", 2, 2)
    False

:code:`isEmpty(value)` 
    Returns true if the string is empty.

    >>> isEmpty("")
    True
    >>> isEmpty("abc")
    False

:code:`isAlphanumeric(value)` 
    Returns true if the string is alphanumeric.

    >>> isAlphanumeric("abc123")
    True
    >>> isAlphanumeric("abc123!")
    False

:code:`isAlpha(value)`
    Returns true if the string is alphabetic.

    >>> isAlpha("abc")
    True
    >>> isAlpha("abc123")
    False

:code:`contains(value, substring)`
    Returns true if the string contains the substring.

    >>> contains("abc", "a")
    True
    >>> contains("abc", "d")
    False

