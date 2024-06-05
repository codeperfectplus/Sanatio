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
    >>> val.isStrongPassword('123456789@Abc', min_length=10, uppercase=True, 
                                lowercase=True, number=True, special=True)
    True

:code:`isPasswordLength` 
    Returns true if the password length is greater than or equal to the minimum length.

    >>> val.isPasswordLength('123456', 6)
    True
    >>> val.isPasswordLength('123456', 7)
    False

:code:`isPasswordMatch` 
    Returns true if the password matches the confirmation password.

    >>> val.isPasswordMatch('ABC', 'abc')
    True

:code:`isPasswordNotInList`
    Returns true if the password is not in the list of common passwords.
    args: value, list_of_passwords

    >>> val.isPasswordNotInList('password', ['password', '123456'])
    True
    >>> val.isPasswordNotInList('password', ['123456', 'qwerty'])
    True

:code:`isPasswordUppercase`
    Returns true if the password contains at least one uppercase letter.

    >>> val.isPasswordUppercase('abc')
    False
    >>> val.isPasswordUppercase('Abc')
    True

:code:`isPasswordLowercase`
    Returns true if the password contains at least one lowercase letter.

    >>> val.isPasswordLowercase('ABC')
    False
    >>> val.isPasswordLowercase('Abc')
    True

:code:`isPasswordNumber`
    Returns true if the password contains at least one number.

    >>> val.isPasswordNumber('abc')
    False
    >>> val.isPasswordNumber('abc123')
    True

:code:`isPasswordSpecialChar`
    Returns true if the password contains at least one special character.

    >>> val.isPasswordSpecialChar('abc')
    False
    >>> val.isPasswordSpecialChar('abc@')
    True

