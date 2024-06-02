import re


class UsernameValidator:
    def __init__(self):
        pass

    def isDiscordUsername(self, value: str) -> bool:
        regex = "^.{3,32}#[0-9]{4}$"
        if re.match(regex, value):
            return True
        return False
