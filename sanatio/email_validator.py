import re
from sanatio.base_class import BaseValidator
from sanatio.utils.utils import regexs_dict


class EmailValidator(BaseValidator):

    def isEmail(self, value: str, checkDNS: bool = False) -> bool:
        """ check if the string is email or not """
        regex = regexs_dict["email_regex"]
        return self.isvalidString(value) and bool(re.search(regex, value))
