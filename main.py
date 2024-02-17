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

################################################################
# Function declarations
################################################################

def validate_input(num_dice, num_faces):
    """
    Validates the input for the number of dice and number of faces per dice.

    Args:
        num_dice (int): The number of dice.
        num_faces (int): The number of faces per dice.

    Raises:
        ValueError: If the input is invalid.

    Returns:
        bool: True if the input is valid.
    """
    if num_dice is str:
        raise ValueError("The number of dice must be an integer not a string.")
    elif num_faces is str:
        raise ValueError("The number of faces per dice must be an integer not a string.")
    elif num_dice != int(num_dice):
        raise ValueError("The number of dice must be an integer.")
    elif num_faces != int(num_faces):
        raise ValueError("The number of faces per dice must be an integer.")
    elif num_dice < 1:
        raise ValueError("The number of dice must be at least 1.")
    elif num_faces < 4:
        raise ValueError("The number of faces per dice must be at least 4.")
    else:
        return True

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
    if validate_input(num_dice, num_faces):
        # Display the result of each roll
        results = []
        for _ in range(num_dice):
            results.append(random.randint(1, num_faces))
        return results


def prompt_user():
    """
    Prompt the user to enter the number of dice to roll and the number of faces per dice.

    Returns:
        tuple: A tuple containing the number of dice to roll and the number of faces per dice.

    Raises:
        ValueError: If the input is invalid.
    """
    num_dice = int(input("Enter the number of dice to roll (min. 1): "))
    num_faces = int(input("Enter the number of faces per dice (min. 4): "))

    if validate_input(num_dice, num_faces):
        return num_dice, num_faces
    else:
        raise ValueError("Invalid prompt input.")

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
