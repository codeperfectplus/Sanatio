Username Validation
====================

The following validation rules are applied to the username: 

.. code:: python
    
    from sanatio import Sanatio

    val = Sanatio()

:code:`isDiscordUsername(value)` - Checks if the username is a valid Discord username. 
    >>> val.isDiscordUsername('test#1234')
    True

