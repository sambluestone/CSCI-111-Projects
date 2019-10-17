"""
Author: Ken Lambert
File: die.py
Project 9

This module defines the Die class.
"""

from random import randint

class Die:
    """This class represents a six-sided die."""

    def __init__(self):
        self.roll()

    def roll(self):
        """Resets the die's value to a random number between 1 and 6
        and resets the file name of the image."""
        self.value = randint(1, 6)
        self.fileName = "DICE/" + str(self) + ".gif"

    def getValue(self):
        """Returns the value of the die's top face."""
        return self.value

    def __str__(self):
        """Returns the string rep of the die."""
        return str(self.getValue())
