"""
Author: Ken Lambert (edited by Sam Bluestone, Evan Phaup, Lily White)
File: crapsgame.py
Project 9

This module represents the game of craps.
"""

from die import Die

class CrapsGame(object):
    """Represents the game of craps."""
    
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()
        self.initalValue = 0
        self.startUp = True
        self.gameState = ""

    def initialRoll(self):
        """Performs the first roll in the game, and
        returns a tuple of the two dice and the
        outcome (a string)."""
        self.die1.roll()
        self.die2.roll()
        dieSum = self.die1.getValue() + self.die2.getValue()
        self.initialValue = dieSum
        outcome = None
        if dieSum == 7 or dieSum == 11:
            outcome = "You win!"
        elif dieSum == 2 or dieSum == 3 or dieSum == 12:
            outcome = "You lose!"
        return (self.die1, self.die2, outcome)
        
    def step(self):
        """Performs the first roll at startup,
        and subsequent rolls thereafter, and returns 
        a tuple of the two dice and the outcome (a string)."""
        # Two cases: the initial roll or any subsequent roll
        if self.startUp:
            self.startUp = False
            return self.initialRoll()
        else:
            self.die1.roll()
            self.die2.roll()
            # Your game logic for any subsequent roll goes here
            dieSum = self.die1.getValue() + self.die2.getValue()
            outcome = None
            if dieSum == self.initialValue:
                outcome = "You win!"
            elif dieSum == 7:
                outcome = "You lose!"
            return (self.die1, self.die2, outcome)

    def __str__(self):
        """Returns the current state of the game."""
        self.gameState = "Die1 = " + str(self.die1.getValue()) + \
                         "  Die2 = " + str(self.die2.getValue()) + \
                         "  Total = " + str(self.die1.getValue() + self.die2.getValue())
        return self.gameState
