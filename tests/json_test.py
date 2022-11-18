import sys
import unittest
sys.path.append('.')
from sanatio.main import Validator

validator = Validator()

class JsonTest(unittest.TestCase):
    def test_json_true(self):
        self.assertTrue(validator.isJSON('{"name":"John", "age":30, "city":"New York"}'))
        
    def test_json_false(self):
        self.assertFalse(validator.isJSON('"name":"John", "age":30, "city":"New York"}'))
        
    def test_isJWT_true(self):
        self.assertTrue(validator.isJWT("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"))

    def test_isJWT_false(self):
        self.assertFalse(validator.isJWT("eyJ"))
        

if __name__ == '__main__':
    unittest.main()