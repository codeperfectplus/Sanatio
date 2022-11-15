Card Validation function
========================

.. code:: python
    
    from validator import Validator

    val = Validator()

:code:`isCreditCard(value)` - Checks if the value is a valid credit card number.

    >>> val.isCreditCard('5191914942157165')
    True
    >>> val.isCreditCard('5191914942157166')
    True