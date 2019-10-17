"""
Author: Ken Lambert
File: testcraps.py
Project 9

A simple terminal-based test driver for a game of craps.
"""

from crapsgame import CrapsGame

def main():
   """Terminal-based trace of a game of craps."""
   game = CrapsGame()
   (die1, die2, outcome) = game.step()
   print(game)
   while not outcome:
      (die1, die2, outcome) = game.step()
      print(game)
   print(outcome)

if __name__ == "__main__":
   main()
