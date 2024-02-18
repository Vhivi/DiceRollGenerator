import unittest
from unittest.mock import patch
from main import validate_input, roll_dice, prompt_user

class TestDiceRoller(unittest.TestCase):

    @patch('builtins.input', side_effect=['2', '6'])
    def test_valid_input(self, mock_input):
        result = prompt_user()
        self.assertEqual(result, (2, 6))

    @patch('builtins.input', side_effect=['a', '2', '6'])
    def test_invalid_input_string(self, mock_input):
        with self.assertRaises(ValueError):
            prompt_user()

    @patch('builtins.input', side_effect=['2', 'b', '6'])
    def test_invalid_input_string_faces(self, mock_input):
        with self.assertRaises(ValueError):
            prompt_user()

    @patch('builtins.input', side_effect=['2', '6', ''])
    def test_invalid_input_empty(self, mock_input):
        with self.assertRaises(ValueError):
            prompt_user()

    @patch('builtins.input', side_effect=['0', '6', '3', '6', '2', '6'])
    def test_multiple_attempts_invalid_input(self, mock_input):
        with self.assertRaises(ValueError):
            prompt_user()

    def test_valid_input_validation(self):
        result = validate_input(2, 6)
        self.assertTrue(result[0])
        self.assertIsNone(result[1])

    def test_invalid_input_validation_dice_type(self):
        result = validate_input('a', 6)
        self.assertFalse(result[0])
        self.assertEqual(result[1], 1)

    def test_invalid_input_validation_faces_type(self):
        result = validate_input(2, 'b')
        self.assertFalse(result[0])
        self.assertEqual(result[1], 2)

    def test_invalid_input_validation_dice_negative(self):
        result = validate_input(-2, 6)
        self.assertFalse(result[0])
        self.assertEqual(result[1], 3)

    def test_invalid_input_validation_faces_negative(self):
        result = validate_input(2, -6)
        self.assertFalse(result[0])
        self.assertEqual(result[1], 4)

    def test_invalid_input_validation_dice_float(self):
        result = validate_input(2.5, 6)
        self.assertFalse(result[0])
        self.assertEqual(result[1], 1)

    def test_invalid_input_validation_faces_float(self):
        result = validate_input(2, 6.5)
        self.assertFalse(result[0])
        self.assertEqual(result[1], 2)

    def test_roll_dice(self):
        result = roll_dice(3, 6)
        self.assertEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()
