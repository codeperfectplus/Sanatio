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
that a number has been entered correctly or to identify any malicious
activity. The checksum validator is used to validate the following.
Checksum Algorithm are helpful to identify if the number is valid or not.

=========== =========
Document    Algorithm
=========== =========
Credit Card Luhn
Aadhar card Verhoeff
Ean13       Ean13 checksum
=========== =========

References
----------

-  `Wikipedia <https://en.wikipedia.org/wiki/Checksum>`__