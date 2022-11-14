import sys
import unittest
sys.path.append('.')
from src.main import Validator

validator = Validator()

class JsonTest(unittest.TestCase):
    def test_json_true(self):
        self.assertTrue(validator.isJSON('{"name":"John", "age":30, "city":"New York"}'))
        
    def test_json_false(self):
        self.assertFalse(validator.isJSON('"name":"John", "age":30, "city":"New York"}'))
        

if __name__ == '__main__':
    unittest.main()