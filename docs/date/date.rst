Date Validation Functions
=========================

The following functions are used to validate dates.  They return a boolean value.

.. code:: python
    
    from sanatio import Sanatio

    val = Sanatio()

:code:`IsDate()` Returns true if the value is a valid date.
    args: value

    >>> val.is_date('2012-12-12')
    True

:code:`isBefore()` Returns true if the value is before the date.
    args: date1, date2
        date2 is optional, if not provided, the current date is used.

    >>> val.is_before('2012-12-12', '2012-12-13')
    True

:code:`isAfter()` Returns true if the value is after the date.
    args: date1, date2
        date2 is optional, if not provided, the current date is used.

    >>> val.is_after('2012-12-12', '2012-12-11')
    True

