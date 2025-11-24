import re
from functools import lru_cache
from typing import Union, Optional
from Levenshtein import distance as levenshtein_distance
from sanatio.base_class import BaseValidator


class StringValidator(BaseValidator):
    """
    StringValidator provides comprehensive string validation and manipulation methods.
    
    Updates:
    - Character type validation (alpha, numeric, alphanumeric, ASCII)
    - Length and content validation
    - String comparison and distance calculation
    - Text cleaning and transformation utilities
    - Performance optimized with caching where applicable
    """
    
    # Compiled regex patterns for better performance
    _compiled_patterns = {
        'symbols': re.compile(r'[^\w\s]'),
        'non_word': re.compile(r'[^\w]'), 
        'non_numeric': re.compile(r'[^\d]'),
        'html_tags': re.compile(r'<[^>]*>'),
        'protocol': re.compile(r'^https?://'),
    }

    def isAlphanumeric(self, value: str) -> bool:
        """
        Check if the string contains only alphanumeric characters.
        
        Args:
            value (str): The string to validate
            
        Returns:
            bool: True if string is alphanumeric and not empty, False otherwise
            
        Example:
            >>> validator.isAlphanumeric("abc123")
            True
            >>> validator.isAlphanumeric("abc-123")
            False
        """
        return bool(value and isinstance(value, str) and value.isalnum())

    def isAlpha(self, value: str) -> bool:
        """
        Check if the string contains only alphabetic characters.
        
        Args:
            value (str): The string to validate
            
        Returns:
            bool: True if string contains only letters and is not empty, False otherwise
            
        Example:
            >>> validator.isAlpha("hello")
            True
            >>> validator.isAlpha("hello123")
            False
        """
        return bool(value and isinstance(value, str) and value.isalpha())

    def isAscii(self, value: Union[str, int, float]) -> bool:
        """
        Check if the string contains only ASCII characters.
        
        Args:
            value (str|int|float): The value to validate
            
        Returns:
            bool: True if all characters are ASCII, False otherwise
            
        Example:
            >>> validator.isAscii("hello")
            True
            >>> validator.isAscii("héllo")
            False
        """
        if not isinstance(value, str):
            value = str(value)
        return value.isascii()

    # isLength method removed from StringValidator - now inherited from BaseValidator

    def isEmpty(self, value: str) -> bool:
        """
        Check if the string is empty or contains only whitespace.
        
        Args:
            value (str): The string to validate
            
        Returns:
            bool: True if string is empty or whitespace only, False otherwise
            
        Example:
            >>> validator.isEmpty("")
            True
            >>> validator.isEmpty("   ")
            True
            >>> validator.isEmpty("hello")
            False
        """
        if not isinstance(value, str):
            return False
        return not value.strip()

    def contains(self, value: str, substring: str, ignoreCase: bool = False) -> bool:
        """
        Check if the string contains a specific substring.
        
        Args:
            value (str): The string to search in
            substring (str): The substring to search for
            ignoreCase (bool): Whether to ignore case differences, default False
            
        Returns:
            bool: True if substring is found, False otherwise
            
        Example:
            >>> validator.contains("Hello World", "world", ignoreCase=True)
            True
            >>> validator.contains("Hello World", "world", ignoreCase=False)
            False
        """
        if not self.isvalidString(value) or not self.isvalidString(substring):
            return False
            
        if ignoreCase:
            return substring.lower() in value.lower()
        return substring in value

    @lru_cache(maxsize=256)
    def levenshtein_distance(self, value1: str, value2: str) -> int:
        """
        Calculate Levenshtein distance between two strings using optimized library.
        
        Args:
            value1 (str): First string
            value2 (str): Second string
            
        Returns:
            int: The minimum number of single-character edits required
            
        Example:
            >>> validator.levenshtein_distance("kitten", "sitting")
            3
        """
        if not isinstance(value1, str) or not isinstance(value2, str):
            return -1
        return levenshtein_distance(value1, value2)

    def edit_distance(self, value1: str, value2: str) -> int:
        """
        Calculate simple edit distance (Hamming-like) between two strings.
        More efficient for strings of similar length.
        
        Args:
            value1 (str): First string
            value2 (str): Second string
            
        Returns:
            int: Number of character differences
            
        Example:
            >>> validator.edit_distance("hello", "hallo")
            1
        """
        if not isinstance(value1, str) or not isinstance(value2, str):
            return -1
            
        # Start with length difference
        difference = abs(len(value1) - len(value2))
        
        # Compare characters up to the shorter length
        min_len = min(len(value1), len(value2))
        for i in range(min_len):
            if value1[i] != value2[i]:
                difference += 1
                
        return difference

    def isEquals(self, value1: str, value2: str, ignoreCase: bool = False) -> bool:
        """
        Check if two strings are equal with optional case sensitivity.
        
        Args:
            value1 (str): First string to compare
            value2 (str): Second string to compare
            ignoreCase (bool): Whether to ignore case differences, default False
            
        Returns:
            bool: True if strings are equal, False otherwise
            
        Example:
            >>> validator.isEquals("Hello", "hello", ignoreCase=True)
            True
            >>> validator.isEquals("Hello", "hello", ignoreCase=False)
            False
        """
        if not self.isvalidString(value1) or not self.isvalidString(value2):
            return False
            
        if ignoreCase:
            return value1.lower() == value2.lower()
        return value1 == value2

    def isVowel(self, value: str) -> bool:
        """
        Check if a single character is a vowel.
        
        Args:
            value (str): Character to check
            
        Returns:
            bool: True if character is a vowel (a,e,i,o,u), False otherwise
            
        Example:
            >>> validator.isVowel("a")
            True
            >>> validator.isVowel("b")
            False
        """
        if not isinstance(value, str) or len(value) != 1:
            return False
        return value.lower() in 'aeiou'

    def isConsonant(self, value: str) -> bool:
        """
        Check if a single character is a consonant.
        
        Args:
            value (str): Character to check
            
        Returns:
            bool: True if character is a letter but not a vowel, False otherwise
            
        Example:
            >>> validator.isConsonant("b")
            True
            >>> validator.isConsonant("a")
            False
        """
        if not isinstance(value, str) or len(value) != 1:
            return False
        return value.isalpha() and value.lower() not in 'aeiou'

    def isPalindrome(self, value: str, ignore_case: bool = True, ignore_spaces: bool = True) -> bool:
        """
        Check if a string is a palindrome (reads the same forwards and backwards).
        
        Args:
            value (str): String to check
            ignore_case (bool): Whether to ignore case differences, default True
            ignore_spaces (bool): Whether to ignore spaces and punctuation, default True
            
        Returns:
            bool: True if string is a palindrome, False otherwise
            
        Example:
            >>> validator.isPalindrome("A man a plan a canal Panama")
            True
            >>> validator.isPalindrome("racecar")
            True
        """
        if not isinstance(value, str):
            return False
            
        processed = value
        if ignore_spaces:
            processed = re.sub(r'[^a-zA-Z0-9]', '', processed)
        if ignore_case:
            processed = processed.lower()
            
        return processed == processed[::-1]

    def trim(self, value: str, chars: Optional[str] = None) -> Optional[str]:
        """
        Remove whitespace or specified characters from both ends of string.
        
        Args:
            value (str): String to trim
            chars (str|None): Characters to remove, None means whitespace
            
        Returns:
            str|None: Trimmed string or None if invalid input
            
        Example:
            >>> validator.trim("  hello  ")
            "hello"
            >>> validator.trim("...hello...", ".")
            "hello"
        """
        if not self.isvalidString(value):
            return None
        return value.strip(chars)

    def ltrim(self, value: str, chars: Optional[str] = None) -> Optional[str]:
        """Remove whitespace or specified characters from left end of string."""
        if not self.isvalidString(value):
            return None
        return value.lstrip(chars)

    def rtrim(self, value: str, chars: Optional[str] = None) -> Optional[str]:
        """Remove whitespace or specified characters from right end of string."""
        if not self.isvalidString(value):
            return None
        return value.rstrip(chars)

    def toUpperCase(self, value: str) -> Optional[str]:
        """Convert string to uppercase."""
        if not self.isvalidString(value):
            return None
        return value.upper()

    def toLowerCase(self, value: str) -> Optional[str]:
        """Convert string to lowercase."""
        if not self.isvalidString(value):
            return None
        return value.lower()

    def removeSymbols(self, value: str) -> Optional[str]:
        """Remove symbols and punctuation, keeping only alphanumeric characters and spaces."""
        if not self.isvalidString(value):
            return None
        return self._compiled_patterns['symbols'].sub('', value)

    def removeNonASCII(self, value: str) -> Optional[str]:
        """Remove non-ASCII characters from string."""
        if not self.isvalidString(value):
            return None
        return value.encode("ascii", "ignore").decode()

    def removeNonWord(self, value: str) -> Optional[str]:
        """Remove non-word characters (anything except letters, digits, underscore)."""
        if not self.isvalidString(value):
            return None
        return self._compiled_patterns['non_word'].sub('', value)

    def removeNonNumeric(self, value: str) -> Optional[str]:
        """Remove all non-numeric characters."""
        if not self.isvalidString(value):
            return None
        return self._compiled_patterns['non_numeric'].sub('', value)

    def removeTags(self, value: str) -> Optional[str]:
        """Remove HTML/XML tags from string."""
        if not self.isvalidString(value):
            return None
        return self._compiled_patterns['html_tags'].sub('', value)

    def removeWhiteSpace(self, value: str) -> Optional[str]:
        """Remove all whitespace characters."""
        if not self.isvalidString(value):
            return None
        return value.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")

    def removeProtocol(self, value: str) -> Optional[str]:
        """Remove HTTP/HTTPS protocol from URL."""
        if not self.isvalidString(value):
            return None
        return self._compiled_patterns['protocol'].sub('', value)

    def removeProfanity(self, value: str, word_list: Optional[list] = None) -> Optional[str]:
        """
        Remove or replace profanity words from string.
        
        Args:
            value (str): String to clean
            word_list (list|None): List of words to remove/replace
            
        Returns:
            str|None: Cleaned string with profanity removed
            
        Note:
            This is a basic implementation. For production use, consider using
            dedicated profanity filtering libraries like 'better-profanity'.
        """
        if not self.isvalidString(value):
            return None
            
        if word_list is None:
            # Basic list - in production, use a comprehensive profanity database
            word_list = ['damn', 'hell', 'crap']
            
        cleaned = value
        for word in word_list:
            # Case-insensitive replacement
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            cleaned = pattern.sub('*' * len(word), cleaned)
            
        return cleaned

    # New utility methods
    def isNumeric(self, value: str) -> bool:
        """Check if string represents a number (int or float)."""
        if not self.isvalidString(value):
            return False
        try:
            float(value)
            return True
        except ValueError:
            return False

    def capitalize_words(self, value: str) -> Optional[str]:
        """Capitalize first letter of each word."""
        if not self.isvalidString(value):
            return None
        return value.title()

    def reverse(self, value: str) -> Optional[str]:
        """Reverse the string."""
        if not self.isvalidString(value):
            return None
        return value[::-1]

    def count_words(self, value: str) -> int:
        """Count number of words in string."""
        if not self.isvalidString(value):
            return 0
        return len(value.split())

    def truncate(self, value: str, max_length: int, suffix: str = "...") -> Optional[str]:
        """
        Truncate string to specified length with optional suffix.
        
        Args:
            value (str): String to truncate
            max_length (int): Maximum length
            suffix (str): Suffix to add when truncated, default "..."
            
        Returns:
            str|None: Truncated string or None if invalid input
        """
        if not self.isvalidString(value) or max_length < 0:
            return None
            
        if len(value) <= max_length:
            return value
            
        if max_length <= len(suffix):
            return suffix[:max_length]
            
        return value[:max_length - len(suffix)] + suffix
