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
        check if date1 is before date2 default date2 is current date

    >>> val.is_before(date1='2012-12-12', date2='2012-12-13')
    True

:code:`isAfter()` Returns true if the value is after the date.
    args: date1, date2
        check if date1 is after date2 default date2 is current date

    >>> val.is_after(date1='2012-12-12', date2='2012-12-11')
    True

