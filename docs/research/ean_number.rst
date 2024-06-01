EAN Number
==========

Ever wondered what those black and white stripes on your groceries mean? Those are EAN codes, 
a global system for identifying products. Like a fingerprint, each EAN code is unique, pinpointing a
specific item from a particular manufacturer.  Think of it as a secret product language, understood 
by scanners at checkout and streamlining everything from store shelves to stockrooms. 
Next time you see a barcode, remember, it's not just stripes - it's a tiny passport for your purchase!

The first two numbers is a country code;
The following five numbers, which are the manufacturing code;
Five more numbers which serve as the product code; and
A single check digit at the end of the sequence.

How to Validate an EAN Code
---------------------------

1. EAN numbers are 13 digits long! If the number is less than 13 digits, it's not a valid EAN code.
2. Add the odd-numbered digits together.
3. multiply the even numbers by 3 and add them together.
4. divide the sum by 10. If the remainder is 0, the check digit is 0. Otherwise, subtract the remainder from 10 to get the check digit.
5. If the check digit is the same as the last digit of the EAN number, the EAN number is valid.
