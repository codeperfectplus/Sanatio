Postal Code Validation Functions
================================

The following functions are used to validate postal codes. 

.. code:: python
    
    from validator import Validator

    val = Validator()

:code:`isPostalCode` - return true if the postal code is valid for the country
    args: value, locale

    >>> val.isPostalCode(value='110016', locale='IN')  
    True

    >>> val.isPostalCode(value='10133-1234', locale='US')
    True

