Password Validation
===================

The password validation is done by the function isStrongPassword().

.. code:: python
    
    from sanatio import Sanatio

    val = Sanatio()

:code:`isStrongPassword(value)`
    Returns true if the password is strong enough, false otherwise.

    >>> val.isStrongPassword('123456')
    False
    >>> val.isStrongPassword('123456789@Abc')
    True