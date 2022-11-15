Email Validation Functions
==========================

The following functions are used to validate email addresses. 

.. code:: python
    
    from validator import Validator

    val = Validator()

:code:`isEmail()` - Returns true if the email address is valid, false otherwise.
    args: value, checkDNS

    >>> val.isEmail('abc@mail.com')
    True
    
