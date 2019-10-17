"""
Author: Ken Lambert
File: testcard.py
Project 9

A simple terminal-based test driver for cards.
"""

from cards import Card

def main():
   for suit in Card.SUITS:
      for rank in Card.RANKS:
         card = Card(rank, suit)
         print(card)

if __name__ == "__main__":
   main()
