Mobile Number Validation
=========================

This is a simple library to validate mobile numbers. It is based on the list of
mobile number ranges published by the ITU-T E.164. The list is updated

.. code:: python
    
    from sanatio import Sanatio

    val = Sanatio()

:code:`isMobilePhone(value, locale)` - checks if the string is a valid mobile phone number.

    >>> val.isMobilePhone('987654321', 'IN')