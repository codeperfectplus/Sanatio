Card Validation function
========================

This function is used to validate the card number and the card type. 
`Luhn algorithm` is used to validate the card number. The function returns 
boolean value.

.. code:: python
    
    from sanatio import Validator

    val = Validator()

:code:`isCreditCard(value)` - Checks if the value is a valid credit card number.

    >>> val.isCreditCard('5191914942157165')
    True
    >>> val.isCreditCard('5191914942157166')
    True