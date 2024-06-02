Number Validation functions
===========================

The following functions are used to 

.. code:: python
    
    from sanatio import Sanatio

    val = Sanatio()

:code:`isEan13` - Check if the value is a valid EAN13 number
    Returns true if the value is a valid EAN13 number

    >>> val.isEan13('0067238891190')
    True
    
:code:`isIMEI` - Check if the value is a valid IMEI number
    Returns true if the value is a valid IMEI number

    >>> val.isIMEI('351755052323794')
    True

:code:`isIPV4` - Check if the value is a valid IPV4 number
    Returns true if the value is a valid IPV4 number

    >>> val.isIPV4('192.168.1.1')
    True

:code:`isIPV6` - Check if the value is a valid IPV6 number
    Returns true if the value is a valid IPV6 number

    >>> val.isIPV6('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
    True

:code:`isSSN` - Check if the value is a valid SSN number
    Returns true if the value is a valid SSN number

    >>> val.isSSN('123-45-6789')
    True

:code:`isJWT` - Check if the value is a valid JWT number
    Returns true if the value is a valid JWT number

    >>> val.isJWT('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c')
    True

:code:`isLatLong` - Check if the value is a valid Latitude and Longitude number
    Returns true if the value is a valid Latitude and Longitude number

    >>> val.isLatLong('37.7749° N, 122.4194° W')
    True

:code:`isMAC` - Check if the value is a valid MAC number
    Returns true if the value is a valid MAC number

    >>> val.isMAC('00:1A:2B:3C:4D:5E')
    True

:code:`isPort` - Check if the value is a valid Port number
    Returns true if the value is a valid Port number

    >>> val.isPort('80')
    True

:code:`isSlug` - Check if the value is a valid Slug number
    Returns true if the value is a valid Slug number

    >>> val.isSlug('this-is-a-slug')
    True

:code:`isPostalCode` - Check if the value is a valid Postal Code number
    Returns true if the value is a valid Postal Code number
    args:
        locale: str - The locale to use for the validation

    >>> val.isPostalCode('110016', locale='IN')
    True

:code:`isMobilePhone` - Check if the value is a valid Mobile Phone number
    Returns true if the value is a valid Mobile Phone number
    args:
        locale: str - The locale to use for the validation

    >>> val.isMobilePhone('9876543210', locale='IN')
    True
