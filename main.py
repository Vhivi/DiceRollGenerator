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
    Validates the input for the number of dice and faces per dice.

    Args:
        num_dice (int): The number of dice to roll.
        num_faces (int): The number of faces per dice.

    Raises:
        ValueError: If the number of dice is less than 1 or the number of faces per dice is less than 4.

    Returns:
        bool: True if the input is valid.
    """
    if num_dice < 1:
        raise ValueError("The number of dice to roll should be at least 1.")
    if num_faces < 4:
        raise ValueError("The number of faces per dice should be at least 4.")

    return True

def roll_dice(num_dice, num_faces):
    if validate_input(num_dice, num_faces):
        # Display the result of each roll
        results = []
        for _ in range(num_dice):
            results.append(random.randint(1, num_faces))
        return results

def main():
    roll_again = "yes"
    while roll_again.lower() == "yes" or roll_again.lower() == "y":
        # Prompt the user to enter the number of dice to roll, minimum 1.
        num_dice = int(input("Enter the number of dice to roll (min. 1): "))
        # Prompt the user to enter the number of faces per dice, minimum 4.
        num_faces = int(input("Enter the number of faces per dice (min. 4): "))

        # Validate the user input
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
