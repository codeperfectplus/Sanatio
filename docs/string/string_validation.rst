String Validation functions
===========================

The following functions are used to validate strings. 

.. code:: python
    
    from sanatio import Sanatio

    val = Sanatio()

:code:`isEquals(value1, value2, ignoreCase)` 
    Returns true if the two strings are equal.

    >>> val.equals("abc", "abc")
    True
    >>> val.equals("abc", "ABC")
    False
    >>> val.equals("abc", "ABC", ignoreCase=True)
    True

:code:`isLength(value, min, max)` 
    Returns true if the string is between the specified min and max.

    >>> val.isLength("abc", 2, 3)
    True
    >>> val.isLength("abc", 2, 2)
    False

:code:`isEmpty(value)` 
    Returns true if the string is empty.

    >>> val.isEmpty("")
    True
    >>> val.isEmpty("abc")
    False

:code:`isAlphanumeric(value)` 
    Returns true if the string is alphanumeric.

    >>> val.isAlphanumeric("abc123")
    True
    >>> val.isAlphanumeric("abc123!")
    False

:code:`isAlpha(value)`
    Returns true if the string is alphabetic.

    >>> val.isAlpha("abc")
    True
    >>> val.isAlpha("abc123")
    False

:code:`contains(value, substring)`
    Returns true if the string contains the substring.

    >>> val.contains("abc", "a")
    True
    >>> val.contains("abc", "d")
    False

:code:`isSlug(input_string)`
    Returns true if the string contains the substring.

    >>> val.contains("foo-bar")
    True
    >>> val.contains("foo bar)
    False

:code:`isAlphanumeric(value)`
    Returns true if the string is an email.

    >>> val.isAlphanumeric("abc123")
    True
    
:code:`isLength(value)`
    Returns if the string has the valid length. 

    >>> val.isLength("abc", 2, 3)
    True
    >>> val.isLength("abc", 2, 2)
    False

:code:`isEmpty(value)`
    Returns if the string is empty. 

    >>> val.isEmpty("")
    True
    >>> val.isEmpty("abc")
    False

:code:`isVowel(value)`
    Returns if the string is a vowel. 

    >>> val.isVowel("abc")
    True
    >>> val.isVowel("bcd")
    False

:code:`isConsonant(value)`
    Returns if the string is a consonant. 

    >>> val.isConsonant("abc")
    True
    >>> val.isConsonant("aaa")
    False

:code:`trim(value)`
    Returns the string without leading or trailing spaces. 

    >>> val.trim(" abc ")
    "abc"

:code:`ltrim(value)`
    Returns the string without leading spaces. 

    >>> val.ltrim(" abc ")
    "abc "

:code:`rtrim(value)`
    Returns the string without trailing spaces. 

    >>> val.rtrim(" abc ")
    " abc"

:code:`toUpperCase(value)`
    Returns the string in uppercase. 

    >>> val.toUpperCase("abc")
    "ABC"

:code:`toLowerCase(value)`
    Returns the string in lowercase. 

    >>> val.toLowerCase("ABC")
    "abc"

:code:`removeSpaces(value)`
    Returns the string without spaces. 

    >>> val.removeSpaces("a b c")
    "abc"

:code:`removeSymbols(value)`
    Returns the string without symbols. 

    >>> val.removeSymbols("a!b@c")
    "abc"

:code:`removeNonASCII(value)`
    Returns the string without non-ASCII characters. 

    >>> val.removeNonASCII("a!b@c")
    "abc"

:code:`removeNonWord(value)`
    Returns the string without non-word characters.
    
    >>> val.removeNonWord("a!b@c")
    "abc"

:code:`removeTags(value)`
    Returns the string without HTML tags. 

    >>> val.removeTags("<p>abc</p>")
    "abc"

:code:`removeProtocol(value)`
    Returns the string without the protocol. 

    >>> val.removeProtocol("http://www.google.com")
    "www.google.com"

