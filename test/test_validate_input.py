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

    def test_invalid_num_dice_negative(self):
        # Test with negative number of dice
        with self.assertRaises(ValueError):
            validate_input(-1, 6)

    def test_invalid_num_faces_negative(self):
        # Test with negative number of faces
        with self.assertRaises(ValueError):
            validate_input(2, -4)

    def test_invalid_num_dice_float(self):
        # Test with float number of dice
        with self.assertRaises(ValueError):
            validate_input(1.5, 6)

    def test_invalid_num_faces_float(self):
        # Test with float number of faces
        with self.assertRaises(ValueError):
            validate_input(2, 4.5)

    def test_invalid_num_dice_string(self):
        # Test with string input for number of dice
        with self.assertRaises(ValueError):
            validate_input("2", 6)

    def test_invalid_num_faces_string(self):
        # Test with string input for number of faces
        with self.assertRaises(ValueError):
            validate_input(2, "6")

if __name__ == '__main__':
    unittest.main()