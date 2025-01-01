import sys
import unittest
from sanatio import Sanatio
sys.path.append('.')

validator = Sanatio()


class NumberTest(unittest.TestCase):
    def test_isDivisibleBy_true_positive(self):
        self.assertTrue(validator.isDivisibleBy(10, 2))
        self.assertTrue(validator.isDivisibleBy(10, 5))
        self.assertTrue(validator.isDivisibleBy(10, 10))
        self.assertTrue(validator.isDivisibleBy(10, 1))
    
    def test_isDivisibleBy_true_negative(self):
        self.assertTrue(validator.isDivisibleBy(10, -1))
        self.assertTrue(validator.isDivisibleBy(10, -5))
        self.assertTrue(validator.isDivisibleBy(10, -10))
        self.assertTrue(validator.isDivisibleBy(-10, 2))
            
    def test_isDivisibleBy_false(self):
        self.assertFalse(validator.isDivisibleBy(10, 3))
        self.assertFalse(validator.isDivisibleBy(10, 7))
        self.assertFalse(validator.isDivisibleBy(10, 0))
        self.assertFalse(validator.isDivisibleBy("foo", "bar"))
        self.assertFalse(validator.isDivisibleBy("foo", 1))
        
    def test_toInt_true(self):
        self.assertEqual(validator.toInt("10"), 10)
        self.assertEqual(validator.toInt("10.0"), 10)
        self.assertEqual(validator.toInt("10.1"), 10)
        self.assertEqual(validator.toInt(10.9), 10)
    
    def test_toInt_false(self):
        self.assertEqual(validator.toInt("foo"), None)
        self.assertEqual(validator.toInt("foo.0"), None)
        self.assertEqual(validator.toInt("foo.1"), None)
        self.assertEqual(validator.toInt("foo.9"), None)
        
    def test_toFloat_true(self):
        self.assertEqual(validator.toFloat("10"), 10.0)
        self.assertEqual(validator.toFloat("10.0"), 10.0)
        self.assertEqual(validator.toFloat("10.1"), 10.1)
        self.assertEqual(validator.toFloat(10), 10.0)

    def test_toFloat_false(self):
        self.assertEqual(validator.toFloat("foo"), None)
        self.assertEqual(validator.toFloat("foo.0"), None)
        self.assertEqual(validator.toFloat("foo.1"), None)
        self.assertEqual(validator.toFloat("foo.9"), None)

    def test_isvalidNumber_true(self):
        self.assertTrue(validator.isvalidNumber(10))
        self.assertTrue(validator.isvalidNumber(10.0))
        self.assertTrue(validator.isvalidNumber(-10))
        self.assertTrue(validator.isvalidNumber(-10.0))
        self.assertTrue(validator.isvalidNumber(0))
        self.assertTrue(validator.isvalidNumber(0.0))

    def test_isvalidNumber_false(self):
        self.assertFalse(validator.isvalidNumber("foo"))
        self.assertFalse(validator.isvalidNumber("foo.0"))
        self.assertFalse(validator.isvalidNumber("foo.1"))
        self.assertFalse(validator.isvalidNumber("foo.9"))

    def test_isPositive_true(self):
        self.assertTrue(validator.isPositive(10))
        self.assertTrue(validator.isPositive(10.0))
        self.assertTrue(validator.isPositive(0.1))

    def test_isPositive_false(self):
        self.assertFalse(validator.isPositive(-10))
        self.assertFalse(validator.isPositive(-10.0))
        self.assertFalse(validator.isPositive(0))
        self.assertFalse(validator.isPositive(0.0))

    def test_isNegative_true(self):
        self.assertTrue(validator.isNegative(-10))
        self.assertTrue(validator.isNegative(-10.0))
    
    def test_isNegative_false(self):
        self.assertFalse(validator.isNegative(10))
        self.assertFalse(validator.isNegative(10.0))
        self.assertFalse(validator.isNegative(0))
        self.assertFalse(validator.isNegative(0.0))

    def test_isInteger_true(self):
        self.assertTrue(validator.isInteger(10))
        self.assertTrue(validator.isInteger(-10))
        self.assertTrue(validator.isInteger(0))

    def test_isInteger_false(self):
        self.assertFalse(validator.isInteger(10.0))
        self.assertFalse(validator.isInteger(-10.0))
        self.assertFalse(validator.isInteger(0.0))
        self.assertFalse(validator.isInteger("foo"))

    def test_isFloat_true(self):
        self.assertTrue(validator.isFloat(10.0))
        self.assertTrue(validator.isFloat(-10.0))
        self.assertTrue(validator.isFloat(0.0))

    def test_isFloat_false(self):
        self.assertFalse(validator.isFloat(10))
        self.assertFalse(validator.isFloat(-10))
        self.assertFalse(validator.isFloat(0))
        self.assertFalse(validator.isFloat("foo"))

    def test_isZero_true(self):
        self.assertTrue(validator.isZero(0))
        self.assertTrue(validator.isZero(0.0))

    def test_isZero_false(self):
        self.assertFalse(validator.isZero(10))
        self.assertFalse(validator.isZero(10.0))
        self.assertFalse(validator.isZero(-10))
        self.assertFalse(validator.isZero(-10.0))

    def test_isNonZero_true(self):
        self.assertTrue(validator.isNonZero(10))
        self.assertTrue(validator.isNonZero(10.0))
        self.assertTrue(validator.isNonZero(-10))
        self.assertTrue(validator.isNonZero(-10.0))

    def test_isNonZero_false(self):
        self.assertFalse(validator.isNonZero(0))
        self.assertFalse(validator.isNonZero(0.0))

    def test_isGreaterThan_true(self):
        self.assertTrue(validator.isGreaterThan(10, 5))
        self.assertTrue(validator.isGreaterThan(10.0, 5))
        self.assertTrue(validator.isGreaterThan(10, 5.0))
        self.assertTrue(validator.isGreaterThan(10.0, 5.0))

    def test_isGreaterThan_false(self):
        self.assertFalse(validator.isGreaterThan(5, 10))
        self.assertFalse(validator.isGreaterThan(5.0, 10))
        self.assertFalse(validator.isGreaterThan(5, 10.0))
        self.assertFalse(validator.isGreaterThan(5.0, 10.0))

    def test_isGreaterThanOrEqual_true(self):
        self.assertTrue(validator.isGreaterThanOrEqual(10, 5))
        self.assertTrue(validator.isGreaterThanOrEqual(10.0, 5))
        self.assertTrue(validator.isGreaterThanOrEqual(10, 5.0))
        self.assertTrue(validator.isGreaterThanOrEqual(10.0, 5.0))
        self.assertTrue(validator.isGreaterThanOrEqual(10, 10))
        self.assertTrue(validator.isGreaterThanOrEqual(10.0, 10))
        self.assertTrue(validator.isGreaterThanOrEqual(10, 10.0))
        self.assertTrue(validator.isGreaterThanOrEqual(10.0, 10.0))

    def test_isGreaterThanOrEqual_false(self):
        self.assertFalse(validator.isGreaterThanOrEqual(5, 10))
        self.assertFalse(validator.isGreaterThanOrEqual(5.0, 10))
        self.assertFalse(validator.isGreaterThanOrEqual(5, 10.0))
        self.assertFalse(validator.isGreaterThanOrEqual(5.0, 10.0))

    def test_truncate(self):
        self.assertEqual(validator.truncate(10.123456, 2), 10.12)
        self.assertEqual(validator.truncate(-10.123456, 4), -10.1234)
        self.assertEqual(validator.truncate(-10.123456, 6), -10.123456)
        self.assertEqual(validator.truncate(10.123456, 0), 10.0)

    def test_isBetween_true(self):
        self.assertTrue(validator.isBetween(10, 5, 15))
        self.assertTrue(validator.isBetween(10.0, 5, 15))
        self.assertTrue(validator.isBetween(10, 5.0, 15))
        self.assertTrue(validator.isBetween(10.0, 5.0, 15))
        self.assertTrue(validator.isBetween(10, 5, 10))
        self.assertTrue(validator.isBetween(10.0, 5, 10))
        self.assertTrue(validator.isBetween(10, 5.0, 10))
        self.assertTrue(validator.isBetween(10.0, 5.0, 10))

    def test_isBetween_false(self):
        self.assertFalse(validator.isBetween(5, 10, 15))
        self.assertFalse(validator.isBetween(5.0, 10, 15))
        self.assertFalse(validator.isBetween(5, 10.0, 15))
        self.assertFalse(validator.isBetween(5.0, 10.0, 15))
        self.assertFalse(validator.isBetween(5, 10, 5))
        self.assertFalse(validator.isBetween(5.0, 10, 5))
        self.assertFalse(validator.isBetween(5, 10.0, 5))
        self.assertFalse(validator.isBetween(5.0, 10.0, 5))

    def test_isPrime_true(self):
        self.assertTrue(validator.isPrime(2))
        self.assertTrue(validator.isPrime(3))
        self.assertTrue(validator.isPrime(5))
        self.assertTrue(validator.isPrime(7))
        self.assertTrue(validator.isPrime(7919))
        self.assertTrue(validator.isPrime(97))

    def test_isPrime_false(self):
        self.assertFalse(validator.isPrime(1))
        self.assertFalse(validator.isPrime(4))
        self.assertFalse(validator.isPrime(6))
        self.assertFalse(validator.isPrime(8))
        self.assertFalse(validator.isPrime(-1))
        self.assertFalse(validator.isPrime(0))
        self.assertFalse(validator.isPrime(1))
        self.assertFalse(validator.isPrime(1001))
        self.assertFalse(validator.isPrime(-17))

    def test_isEven_true(self):
        self.assertTrue(validator.isEven(2))
        self.assertTrue(validator.isEven(4))
        self.assertTrue(validator.isEven(6))
        self.assertTrue(validator.isEven(8))
        self.assertTrue(validator.isEven(0))
        self.assertTrue(validator.isEven(-2))

    def test_isEven_false(self):
        self.assertFalse(validator.isEven(1))
        self.assertFalse(validator.isEven(3))
        self.assertFalse(validator.isEven(5))
        self.assertFalse(validator.isEven(7))
        self.assertFalse(validator.isEven(-3))

    def test_isOdd_true(self):
        self.assertTrue(validator.isOdd(1))
        self.assertTrue(validator.isOdd(3))
        self.assertTrue(validator.isOdd(5))
        self.assertTrue(validator.isOdd(7))
        self.assertTrue(validator.isOdd(-3))

    def test_isOdd_false(self):
        self.assertFalse(validator.isOdd(2))
        self.assertFalse(validator.isOdd(4))
        self.assertFalse(validator.isOdd(6))
        self.assertFalse(validator.isOdd(8))
        self.assertFalse(validator.isOdd(0))
        self.assertFalse(validator.isOdd(-2))

    def test_isMultipleOf_true(self):
        self.assertTrue(validator.isMultipleOf(10, 2))
        self.assertTrue(validator.isMultipleOf(15, 3))
        self.assertTrue(validator.isMultipleOf(20, 5))
        self.assertTrue(validator.isMultipleOf(25, 5))
        self.assertTrue(validator.isMultipleOf(0, 1))
        self.assertTrue(validator.isMultipleOf(-10, 2))
        self.assertTrue(validator.isMultipleOf(-10, -2))
        self.assertTrue(validator.isMultipleOf(0, -3))

    def test_isMultipleOf_false(self):
        self.assertFalse(validator.isMultipleOf(10, 3))
        self.assertFalse(validator.isMultipleOf(15, 4))
        self.assertFalse(validator.isMultipleOf(20, 6))
        self.assertFalse(validator.isMultipleOf(25, 4))
        self.assertFalse(validator.isMultipleOf(1, 0))
        self.assertFalse(validator.isMultipleOf(10, -3))
        self.assertFalse(validator.isMultipleOf(10, 0))

    def test_isSquare_true(self):
        self.assertTrue(validator.isSquare(4))
        self.assertTrue(validator.isSquare(9))
        self.assertTrue(validator.isSquare(16))
        self.assertTrue(validator.isSquare(25))
        self.assertTrue(validator.isSquare(0))
        self.assertTrue(validator.isSquare(1000000))

    def test_isSquare_false(self):
        self.assertFalse(validator.isSquare(3))
        self.assertFalse(validator.isSquare(8))
        self.assertFalse(validator.isSquare(10))
        self.assertFalse(validator.isSquare(15))
        self.assertFalse(validator.isSquare(-15))
        self.assertFalse(validator.isSquare(-1))
        self.assertFalse(validator.isSquare(18))

    def test_isCube_true(self):
        self.assertTrue(validator.isCube(8))
        self.assertTrue(validator.isCube(-8))
        self.assertTrue(validator.isCube(27))
        self.assertTrue(validator.isCube(64))
        self.assertTrue(validator.isCube(125))
        self.assertTrue(validator.isCube(0))
        self.assertTrue(validator.isCube(1000000000))
        self.assertTrue(validator.isCube(-125))

    def test_isCube_false(self):
        self.assertFalse(validator.isCube(9))
        self.assertFalse(validator.isCube(16))
        self.assertFalse(validator.isCube(20))
        self.assertFalse(validator.isCube(30))
        self.assertFalse(validator.isCube(-23))
        self.assertFalse(validator.isCube(-100))


if __name__ == '__main__':
    unittest.main()
