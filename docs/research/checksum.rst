Checksum
========

A checksum is a number. It is a kind of redundancy check. There are
different ways to calculate it. It serves as a check, that no errors
have been made when writing down the number. In its simplest form, the
digits are simply added up. This can however not detect errors of
swapping digits around. One of the uses of checksums is to check that
account numbers have been entered correctly.

Use of checksums in this project
--------------------------------

In Sanatio, Checksum is implemented as a validator. It is used to check
that a number has been entered correctly. It is used in the following
validators with the following algorithms:

=========== =========
Document    Algorithm
=========== =========
Credit Card Luhn
Aadhar card Verhoeff
=========== =========

References
----------

-  `Wikipedia <https://en.wikipedia.org/wiki/Checksum>`__