import unittest
from main import validate_input

class TestValidateInput(unittest.TestCase):
    def test_valid_input(self):
        # Test with valid inputs
        self.assertTrue(validate_input(2, 6))

    def test_invalid_num_dice(self):
        # Test with invalid number of dice
        with self.assertRaises(ValueError):
            validate_input(0, 6)

    def test_invalid_num_faces(self):
        # Test with invalid number of faces
        with self.assertRaises(ValueError):
            validate_input(2, 3)

if __name__ == '__main__':
    unittest.main()