import unittest
from unittest.mock import patch, call
from main import main

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['2', '6', 'n'])
    @patch('main.roll_dice', return_value=[3, 4])
    @patch('builtins.print')
    def test_main(self, mock_print, mock_roll_dice, mock_input):
        main()
        calls = mock_print.call_args_list
        mock_input.assert_any_call("Enter the number of dice to roll (min. 1): ")
        mock_input.assert_any_call("Enter the number of faces per dice (min. 4): ")
        mock_input.assert_any_call("Do you want to roll again? (y/n): ")
        mock_roll_dice.assert_called_once_with(2, 6)
        self.assertIn(call('Dice', 1, ':', 3), calls)
        self.assertIn(call('Dice', 2, ':', 4), calls)
        self.assertIn(call('Sum of all the rolls:', 7), calls)

if __name__ == '__main__':
    unittest.main()