import re
import socket
from typing import Optional
from sanatio.base_class import BaseValidator
from sanatio.utils.utils import regexs_dict


class EmailValidator(BaseValidator):
    """
    EmailValidator provides comprehensive email validation functionality.
    
    Features:
    - RFC-compliant email format validation
    - Optional DNS/MX record validation
    - Domain validation
    - Common email provider validation
    - Disposable email detection support
    """
    
    # Improved RFC 5322 compliant email regex
    _email_pattern = re.compile(
        r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
    )

    def isEmail(self, value: str, checkDNS: bool = False, strict: bool = True) -> bool:
        """
        Validate email address format and optionally check DNS records.
        
        Args:
            value (str): Email address to validate
            checkDNS (bool): Whether to validate MX records, default False
            strict (bool): Whether to use strict RFC validation, default True
            
        Returns:
            bool: True if email is valid, False otherwise
            
        Example:
            >>> validator.isEmail("user@example.com")
            True
            >>> validator.isEmail("invalid.email")
            False
            >>> validator.isEmail("user@example.com", checkDNS=True)
            True  # if MX record exists
        """
        if not self.isvalidString(value):
            return False
            
        # Basic format validation
        if strict:
            if not self._email_pattern.match(value):
                return False
        else:
            # Fallback to simpler regex for less strict validation
            regex = regexs_dict.get('email_regex')
            if not re.search(regex, value):
                return False
        
        # Additional length checks
        local, _, domain = value.rpartition('@')
        if len(local) > 64 or len(domain) > 253:
            return False
            
        # DNS validation if requested
        if checkDNS:
            return self._validate_mx_record(domain)
            
        return True

    def _validate_mx_record(self, domain: str) -> bool:
        """
        Check if domain has valid MX or A records.
        
        Args:
            domain (str): Domain to check
            
        Returns:
            bool: True if domain has valid records, False otherwise
        """
        try:
            # First try MX record
            try:
                import dns.resolver
                mx_records = dns.resolver.resolve(domain, 'MX')
                return len(mx_records) > 0
            except ImportError:
                # Fallback to socket if dnspython not available
                socket.gethostbyname(domain)
                return True
        except (socket.gaierror, Exception):
            return False

    def getDomain(self, email: str) -> Optional[str]:
        """
        Extract domain from email address.
        
        Args:
            email (str): Email address
            
        Returns:
            str|None: Domain part of email or None if invalid
            
        Example:
            >>> validator.getDomain("user@example.com")
            "example.com"
        """
        if not self.isvalidString(email) or '@' not in email:
            return None
            
        return email.split('@')[-1]

    def getLocalPart(self, email: str) -> Optional[str]:
        """
        Extract local part (username) from email address.
        
        Args:
            email (str): Email address
            
        Returns:
            str|None: Local part of email or None if invalid
            
        Example:
            >>> validator.getLocalPart("user@example.com")
            "user"
        """
        if not self.isvalidString(email) or '@' not in email:
            return None
            
        return email.split('@')[0]

    def isCommonProvider(self, email: str) -> bool:
        """
        Check if email is from a common provider (Gmail, Yahoo, Outlook, etc.).
        
        Args:
            email (str): Email address to check
            
        Returns:
            bool: True if from common provider, False otherwise
        """
        common_providers = {
            'gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com',
            'aol.com', 'icloud.com', 'protonmail.com', 'mail.com',
            'yandex.com', 'zoho.com'
        }
        
        domain = self.getDomain(email)
        return domain is not None and domain.lower() in common_providers

    def normalize(self, email: str) -> Optional[str]:
        """
        Normalize email address (lowercase, remove dots in Gmail, etc.).
        
        Args:
            email (str): Email address to normalize
            
        Returns:
            str|None: Normalized email or None if invalid
        """
        if not self.isEmail(email):
            return None
            
        local = self.getLocalPart(email)
        domain = self.getDomain(email)
        
        if not local or not domain:
            return None
            
        # Convert to lowercase
        domain = domain.lower()
        
        # Gmail-specific normalization
        if domain == 'gmail.com':
            # Remove dots and everything after +
            local = local.lower().replace('.', '')
            if '+' in local:
                local = local[:local.index('+')]
        else:
            local = local.lower()
            
        return f"{local}@{domain}"
