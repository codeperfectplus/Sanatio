import re


from sanatio.utils.utils import regexs
from sanatio.base_class import BaseValidator


class UsernameValidator(BaseValidator):

    def isDiscordUsername(self, value: str) -> bool:
        regex = regexs["discord_username_regex"]
        if re.match(regex, value):
            return True
        return False
