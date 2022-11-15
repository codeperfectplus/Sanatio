Passport Number Validation
=========================

This module provides a validation for passport numbers.

.. code:: python
    
    from validator import Validator

    val = Validator()

:code:`isPassportNumber(value, locale):` - Return True if the string is a valid passport number.
    Args: value, locale

    >>> val.isPassportNumber('A1234567', "IN") 
    True

