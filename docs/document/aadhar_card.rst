Aadhar Card Validation
======================  

aadhar card is 12 digit number.
`Vorhoef Algorithm` is use to validate aadhar card number.


.. code:: python
    
    from sanatio import Validator

    val = Validator()

:code:`isAadharCard(value)` - check if the value is a valid aadhar card number.
    >>> val.isAadharCard('9284 9436 2499')
    True

