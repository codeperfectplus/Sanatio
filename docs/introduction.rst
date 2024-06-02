Introduction
============

This project is inspired from Validator.js which is a library for string validation. 
So people who are familiar with Validator.js can easily switch to this library.
 
This library is written in pure python and is very easy to use. 
It is a simple library that can be used to validate strings, documents, emails, dates, urls, domain names, etc.

Installation
------------

To install the library, you can use pip: 

:code:` pip install sanatio`

Usage-Examples
--------------

.. code:: python

from sanatio import Sanatio
val = Sanatio()


# Check if the string is equal to the given value

.. code:: python

val.equals("abc", "abc") # True







