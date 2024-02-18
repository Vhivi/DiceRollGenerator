#!/usr/bin/python
# -*- coding: utf-8 -*-

# Project Description: The objective of this program is to simulate a dice roll.
# The program should prompt the user to enter the number of dice to roll and the
# number of faces per dice. The program should then display the result of each roll.
# Author :
# Creation Date (dd/mm/yyyy): 16/02/2024
# Version :
# Python 3.10.11

################################################################
# Importing modules
################################################################

import random

################################################################
# Declaration of global variables
################################################################

ERROR_MSG_1 = "The number of dice must be an integer."
ERROR_MSG_2 = "The number of faces per dice must be an integer."
ERROR_MSG_3 = "The number of dice must be at least 1."
ERROR_MSG_4 = "The number of faces per dice must be at least 4."
ERROR_MSG_5 = "You have exceeded the maximum number of attempts."
ERROR_MSG_6 = "Try again."

################################################################
# Function declarations
################################################################

def validate_input(num_dice, num_faces):
    """
    Validate the input for the number of dice and number of faces.

    Args:
        num_dice (int): The number of dice.
        num_faces (int): The number of faces on each dice.

    Returns:
        tuple: A tuple containing a boolean value indicating whether the input is valid and an error code if the input is invalid.
               If the input is valid, the error code is None.

    """
    if type(num_dice) is not int:
        return False, 1 # ERROR_MSG_1
    elif type(num_faces) is not int:
        return False, 2 # ERROR_MSG_2
    elif num_dice != int(num_dice):
        return False, 1 # ERROR_MSG_1
    elif num_faces != int(num_faces):
        return False, 2 # ERROR_MSG_2
    elif num_dice < 1:
        return False, 3 # ERROR_MSG_3
    elif num_faces < 4:
        return False, 4 # ERROR_MSG_4
    else:
        return True, None

def roll_dice(num_dice, num_faces):
    """
    Rolls a specified number of dice with a specified number of faces.

    Args:
        num_dice (int): The number of dice to roll.
        num_faces (int): The number of faces on each die.

    Returns:
        list: A list containing the result of each roll.
    """
    # Validate the input and return the results if true or prompt the user to
    # enter the input again
    state, _ = validate_input(num_dice, num_faces)
    
    if state:
        # Display the result of each roll
        results = []
        for _ in range(num_dice):
            results.append(random.randint(1, num_faces))
        return results


def prompt_user():
    """
    Prompts the user to enter the number of dice to roll and the number of faces per dice.
    
    Returns:
        tuple: A tuple containing the number of dice to roll and the number of faces per dice.

    Raises:
        ValueError: If too many attempts are invalid.
    """
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        if attempts != 0:
            print("You have", max_attempts - attempts, "attempts left.")

        num_dice = int(input("Enter the number of dice to roll (min. 1): "))
        num_faces = int(input("Enter the number of faces per dice (min. 4): "))
        
        state, error = validate_input(num_dice, num_faces)

        if state:
            return num_dice, num_faces
        else:
            if error == 1:
                print(ERROR_MSG_1)
                print(ERROR_MSG_6)
                attempts += 1
            elif error == 2:
                print(ERROR_MSG_2)
                print(ERROR_MSG_6)
                attempts += 1
            elif error == 3:
                print(ERROR_MSG_3)
                print(ERROR_MSG_6)
                attempts += 1
            elif error == 4:
                print(ERROR_MSG_4)
                print(ERROR_MSG_6)
                attempts += 1
    
    print(ERROR_MSG_5)
    raise ValueError(ERROR_MSG_5)

def main():
    """
    Function to simulate rolling dice.

    This function prompts the user to enter the number of dice to roll and the number of faces per dice.
    It then rolls the dice, displays the result of each roll, and calculates the sum of all the rolls.
    The user is asked if they want to roll again.

    Parameters:
    None

    Returns:
    None
    """
    # Initialize the roll_again variable
    roll_again = "y"

    # Loop to allow the user to roll the dice multiple times
    while roll_again.lower() == "y":
        # Prompt the user to enter the number of dice to roll and the number of faces per dice
        num_dice, num_faces = prompt_user()

        # Roll the dice
        results = roll_dice(num_dice, num_faces)

        # Display the result of each roll
        for i in range(len(results)):
            print("Dice", i+1, ":", results[i])

        # Display the sum of all the rolls
        print("Sum of all the rolls:", sum(results))

        # Ask the user if they want to roll again
        roll_again = input("Do you want to roll again? (y/n): ")

if __name__ == "__main__":
    main()
