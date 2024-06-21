import sys
import unittest
sys.path.append('.')
from sanatio import Sanatio

validator = Sanatio()


class UUIDTest(unittest.TestCase):
    def test_uuid_true(self):
        self.assertTrue(validator.isUUID('8d2d5fc2-62fa-4ed1-bf82-bbc8e8cd8532'))
        self.assertTrue(validator.isUUID('908cd63e-38a0-4044-b05c-c24f9fb4fbcc'))
        self.assertTrue(validator.isUUID('88dd8db0-3195-4a60-9949-88c4aa0fb2f9'))
        self.assertTrue(validator.isUUID('f1eff7e9-28e8-4acc-94c8-115af1a2b28d'))
        self.assertTrue(validator.isUUID('5f6b542f-a89f-4309-a88f-deb6ce89c71c'))
        self.assertTrue(validator.isUUID('9c35514f-baa7-4567-8eb7-6cbb49f3956e'))
        self.assertTrue(validator.isUUID('f9473805-6368-4a76-bc0d-f6ab7b0754e2'))

    def test_uuid_false(self):
        self.assertFalse(validator.isUUID('8d2d5fc2-62fa-4ed1-bf82-bbc8e8cd853'))
        self.assertFalse(validator.isUUID('908cd63e-38a0-4044-b05c-c24f9fb4fbc'))
        self.assertFalse(validator.isUUID('88dd8db0-3195-4a60-9949-88c4aa0fb2f'))
        self.assertFalse(validator.isUUID('f1eff7e9-28e8-4acc-94c8-115af1a2b28'))
        self.assertFalse(validator.isUUID('5f6b542f-a89f-4309-a88f-deb6ce89c71'))
        self.assertFalse(validator.isUUID('9c35514f-baa7-4567-8eb7-6cbb49f3956'))
        self.assertFalse(validator.isUUID('f9473805-6368-4a76-bc0d-f6ab7b0754e'))


if __name__ == '__main__':
    unittest.main()
