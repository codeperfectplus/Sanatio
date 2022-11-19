Number Validation functions
===========================

The following functions are used to validate numbers.

.. code:: python
    
    from sanatio import Validator

    val = Validator()

:code:`isDecimal(value)`
    Returns true if the value is a decimal number.

    >>> val.isDecimal(1)
    True
    >>> val.isDecimal(1.0)
    True

:code:`isDivisibleBy(value, divisor)`
    Returns true if the value is divisible by the divisor.

    >>> val.isDivisibleBy(10, 2)
    True
    >>> val.isDivisibleBy(10, 3)
    False

