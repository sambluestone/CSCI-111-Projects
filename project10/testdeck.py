"""
Author: Ken Lambert
File: testdeck.py
Project 9

A simple terminal-based test driver for a deck of cards.
"""

from cards import Card, Deck

def main():
   """Creates a deck, deals and prints the cards,
   then creates a second deck, shuffles, deals and prints."""
   deck = Deck()
   print("NUMBER OF CARDS:", len(deck))
   print("THE CARDS IN A NEW DECK:")
   while not deck.isEmpty():
      print(deck.deal())

   deck = Deck()
   deck.shuffle()
   print("\nTHE CARDS IN A SHUFFLED DECK:")   
   while not deck.isEmpty():
      print(deck.deal())

if __name__ == "__main__":
   main()
