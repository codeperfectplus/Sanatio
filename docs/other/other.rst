Number Validation functions
===========================

The following functions are used to 

.. code:: python
    
    from sanatio import Validator

    val = Validator()

:code:`isEan13` - Check if the value is a valid EAN13 number
    Returns true if the value is a valid EAN13 number

    >>> val.isEan13('0067238891190')
    True
    
