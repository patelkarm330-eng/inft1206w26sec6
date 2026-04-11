# test_age_validator.py
# Karm Patel 
# ICE 3
# Description: Importing the unittest and trying to run the test case

import unittest
from age_validator import AgeValidator

class TestAgeValidator(unittest.TestCase):

    def setUp(self):
        self.validator = AgeValidator()

    # Valid boundary tests
    def test_age_min_boundary(self):
        self.assertTrue(self.validator.validate_age(18))

    def test_age_max_boundary(self):
        self.assertTrue(self.validator.validate_age(65))

    # Invalid boundary tests
    def test_age_below_min(self):
        self.assertFalse(self.validator.validate_age(17))

    def test_age_above_max(self):
        self.assertFalse(self.validator.validate_age(66))

    # Valid interior value
    def test_age_valid_middle(self):
        self.assertTrue(self.validator.validate_age(30))

    # Invalid type tests
    def test_age_string_input(self):
        with self.assertRaises(TypeError):
            self.validator.validate_age("25")

    def test_age_float_input(self):
        with self.assertRaises(TypeError):
            self.validator.validate_age(18.5)

    def test_age_none_input(self):
        with self.assertRaises(TypeError):
            self.validator.validate_age(None)

if __name__ == "__main__":
    unittest.main()