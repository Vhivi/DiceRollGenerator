import unittest
from unittest.mock import patch
from main import prompt_user

class TestPromptUser(unittest.TestCase):
    @patch('builtins.input', side_effect=['2', '6'])
    def test_valid_input(self, mock_input):
        # Test with valid inputs
        self.assertEqual(prompt_user(), (2, 6))

    @patch('builtins.input', side_effect=['0', '6'])
    def test_invalid_num_dice(self, mock_input):
        # Test with invalid number of dice
        with self.assertRaises(ValueError):
            prompt_user()

    @patch('builtins.input', side_effect=['2', '3'])
    def test_invalid_num_faces(self, mock_input):
        # Test with invalid number of faces
        with self.assertRaises(ValueError):
            prompt_user()

    @patch('builtins.input', side_effect=['-1', '6'])
    def test_invalid_num_dice_negative(self, mock_input):
        # Test with negative number of dice
        with self.assertRaises(ValueError):
            prompt_user()

    @patch('builtins.input', side_effect=['2', '-4'])
    def test_invalid_num_faces_negative(self, mock_input):
        # Test with negative number of faces
        with self.assertRaises(ValueError):
            prompt_user()

    @patch('builtins.input', side_effect=['1.5', '6'])
    def test_invalid_num_dice_float(self, mock_input):
        # Test with float number of dice
        with self.assertRaises(ValueError):
            prompt_user()

    @patch('builtins.input', side_effect=['2', '4.5'])
    def test_invalid_num_faces_float(self, mock_input):
        # Test with float number of faces
        with self.assertRaises(ValueError):
            prompt_user()

    @patch('builtins.input', side_effect=['two', '6'])
    def test_invalid_num_dice_string(self, mock_input):
        # Test with string input for number of dice
        with self.assertRaises(ValueError):
            prompt_user()

    @patch('builtins.input', side_effect=['2', 'six'])
    def test_invalid_num_faces_string(self, mock_input):
        # Test with string input for number of faces
        with self.assertRaises(ValueError):
            prompt_user()

if __name__ == '__main__':
    unittest.main()