"""
Author: Ken Lambert
File: testwar.py
Project 9

A simple terminal-based test driver for a game of War.
"""

from wargame import WarGame

def main():
   """Terminal-based trace of a game of War."""
   game = WarGame()
   game.deal()
   while not game.winner():
      game.step()
      print(game)
   print(game.winner())

if __name__ == "__main__":
   main()
