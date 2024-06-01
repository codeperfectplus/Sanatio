import sys
import unittest
sys.path.append('.')
from sanatio import Validator

validator = Validator()


class StringConversionTest(unittest.TestCase):
    def test_trim(self):
        self.assertEqual(validator.trim('  foo  '), 'foo')
        self.assertEqual(validator.trim('  bar  '), 'bar')
        
    def test_ltrim(self):
        self.assertEqual(validator.ltrim('  foo  '), 'foo  ')
        self.assertEqual(validator.ltrim('  bar  '), 'bar  ')
        
    def test_rtrim(self):
        self.assertEqual(validator.rtrim('  foo  '), '  foo')
        self.assertEqual(validator.rtrim('  bar  '), '  bar')
        
    def test_toLowerCase(self):
        self.assertEqual(validator.toLowerCase('FOO'), 'foo')
        self.assertEqual(validator.toLowerCase('BAR'), 'bar')
        
    def test_toUpperCase(self):
        self.assertEqual(validator.toUpperCase('foo'), 'FOO')
        self.assertEqual(validator.toUpperCase('bar'), 'BAR')
        
    def test_removeSpaces(self):
        self.assertEqual(validator.removeSpaces('foo bar'), 'foobar')
        self.assertEqual(validator.removeSpaces('foo  bar'), 'foobar')
        self.assertEqual(validator.removeSpaces('foo   bar'), 'foobar')
        self.assertEqual(validator.removeSpaces('foo    bar'), 'foobar')
        
    def test_removeSymbols(self):
        self.assertEqual(validator.removeSymbols('foo!@#$%^&*()+'), 'foo')
        self.assertEqual(validator.removeSymbols('bar!@#$%^&*()+'), 'bar')
        
    def test_removeTags(self):
        self.assertEqual(validator.removeTags('<p>foo</p>'), 'foo')
        self.assertEqual(validator.removeTags('<p>bar</p>'), 'bar')
        
    def test_removeWhiteSpace(self):
        self.assertEqual(validator.removeWhiteSpace('foo bar'), 'foobar')
        self.assertEqual(validator.removeWhiteSpace('foo  bar'), 'foobar')
        self.assertEqual(validator.removeWhiteSpace('foo   bar'), 'foobar')
        self.assertEqual(validator.removeWhiteSpace('foo    bar'), 'foobar')
        
    def test_removeNonWord(self):
        self.assertEqual(validator.removeNonWord('foobar@'), 'foobar')
        self.assertEqual(validator.removeNonWord('@#$%^&*()foobar'), 'foobar')
        self.assertEqual(validator.removeNonWord('foo@#$%^&*()bar'), 'foobar')
        self.assertEqual(validator.removeNonWord('foo@#$%^&*()bar@#$'), 'foobar')
        self.assertEqual(validator.removeNonWord('@#@$@$@$@$@$@$@$'), '')
        

if __name__ == '__main__':
    unittest.main()