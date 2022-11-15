Number Validation functions
===========================

The following functions are used to validate numbers.

:code:`isDecimal(value)`
    Returns true if the value is a decimal number.

    >>> isDecimal(1)
    True
    >>> isDecimal(1.0)
    True

:code:`isDivisibleBy(value, divisor)`
    Returns true if the value is divisible by the divisor.

    >>> isDivisibleBy(10, 2)
    True
    >>> isDivisibleBy(10, 3)
    False

