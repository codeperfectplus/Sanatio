import sys
import unittest
sys.path.append('.')
from sanatio import Sanatio

validator = Sanatio()


class UsernameTest(unittest.TestCase):
    def test_discordusername_true(self):
        self.assertTrue(validator.isDiscordUsername('Disコルド#0001'))
        self.assertTrue(validator.isDiscordUsername('KiBender#1234'))
        self.assertTrue(validator.isDiscordUsername('SkankHunt42#2134'))
        
    def test_discordusername_false(self):
        self.assertFalse(validator.isDiscordUsername('Disコルド#0001#'))
        self.assertFalse(validator.isDiscordUsername('KiBender#1234#'))
        self.assertFalse(validator.isDiscordUsername('SkankHunt42#2134#'))
        self.assertFalse(validator.isDiscordUsername('123456789'))
        

if __name__ == '__main__':
    unittest.main()