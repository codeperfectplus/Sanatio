Number Validation functions
===========================

The following functions are used to validate numbers.

.. code:: python
    
    from sanatio import Sanatio

    val = Sanatio()

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

:code:`isPrime(value)`
    Returns true if the value is a prime number.

    >>> val.isPrime(5)
    True
    >>> val.isPrime(4)
    False

:code:`isEven(value)`
    Returns true if the value is even.

    >>> val.isEven(4)
    True
    >>> val.isEven(5)
    False

:code:`isOdd(value)`
    Returns true if the value is odd.

    >>> val.isOdd(5)
    True
    >>> val.isOdd(4)
    False

:code:`isMultipleOf(value, multiple)`
    Returns true if the value is a multiple of another number.

    >>> val.isMultipleOf(10, 2)
    True
    >>> val.isMultipleOf(10, 3)
    False

:code:`isSquare(value)`
    Returns true if the value is a perfect square.

    >>> val.isSquare(4)
    True
    >>> val.isSquare(5)
    False

:code:`isCube(value)`
    Returns true if the value is a perfect cube.

    >>> val.isCube(8)
    True
    >>> val.isCube(9)
    False