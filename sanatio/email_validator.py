import re
from sanatio.base_class import BaseValidator
from sanatio.utils.utils import regexs_dict


class EmailValidator(BaseValidator):
    """ 
    EmailValidator class is used to validate email address

    Methods
    -------

    isEmail(value: str, checkDNS: bool = False) -> bool:
        check if the string is email or not

    """

    def isEmail(self, value: str, checkDNS: bool = False) -> bool:
        """ check if the string is email or not """
        regex = regexs_dict.get('email_regex')
        return self.isvalidString(value) and bool(re.search(regex, value))
