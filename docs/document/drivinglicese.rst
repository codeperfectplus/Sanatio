Driving License Validation
==========================

This is a simple script to validate driving license numbers. 

.. code:: python
    
    from sanatio import Validator

    val = Validator()

:code:`isDriverLicense(value, locale):` - returns true if the value is a valid driving license number for the specified locale.

    >>> isDriverLicense('123456789', 'IN')
    True

    >>> isDriverLicense('123456789', 'US')
    False
