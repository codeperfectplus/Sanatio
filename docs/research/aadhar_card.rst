Aadhar Card
===========

What is Aadhar Card?
--------------------

Aadhar Card is a 12 digit unique identification number issued by the
Unique Identification Authority of India (UIDAI) to all Indian residents
based on their biometric and demographic data. The Aadhar card is issued
by the UIDAI, a statutory authority established by the Government of
India under the provisions of the Aadhar (Targeted Delivery of Financial
and Other Subsidies, Benefits and Services) Act, 2016.

What is the purpose of Aadhar Card?
-----------------------------------

Aadhar Card Number Format
-------------------------

-  Addhar card number is 12 digit number.
-  Last digit is checksum digit.
-  Checksum digit is calculated using verhoeff algorithm.

Verhoeff Algorithm
------------------

-  The Verhoeff algorithm is a checksum formula for error detection
   developed by the Dutch mathematician Jacobus Verhoeff and was first
   published in 1969.

The Verhoeff algorithm can be implemented using three tables: a
multiplication table d, an inverse table inv, and a permutation table p.

For each index i of the array n, starting at zero, replace c with

::

   d(c, p[i mod 8])

where d is the multiplication table, p is the permutation table, and mod
is the modulo operator.

References
----------

-  `Verhoeff
   Algorithm <https://en.wikipedia.org/wiki/Verhoeff_algorithm>`__