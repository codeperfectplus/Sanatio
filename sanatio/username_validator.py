import re
from sanatio.utils.utils import regexs

class UsernameValidator:
    def __init__(self):
        pass

    def isDiscordUsername(self, value: str) -> bool:
        regex = regexs["discord_username_regex"]
        if re.match(regex, value):
            return True
        return False