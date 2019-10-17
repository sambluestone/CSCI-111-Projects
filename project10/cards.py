"""
Author: Ken Lambert (edited by Sam Bluestone, Evan Phaup, Lily White)
File: cards.py
Project 9

Module for playing cards, with classes Card and Deck
""" 
import random

class Card(object):
    """ A card object with a suit, rank, and file name.
    The file name refers to the card's image on disk."""

    RANKS = tuple(range(1, 14))

    SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')

    BACK_NAME = 'DECK/b.gif'

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        if not (rank in Card.RANKS):
            raise RuntimeError('Rank must be in ' + str(Card.RANKS))
        if not (suit in Card.SUITS):
            raise RuntimeError('Suit must be in ' + str(Card.SUITS))
        self.rank = rank
        self.suit = suit
        self.fileName = 'DECK/' + str(rank) + suit[0].lower() + '.gif'
        
    def __str__(self):
        """Returns the string representation of a card."""
        if self.rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = self.rank
        return str(rank) + ' of ' + self.suit

## The definition of class Deck goes here
class Deck(object):

    def __init__(self):
        """Creates a deck object with 52 cards """
            self.cards = []
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    self.cards.append(Card(rank, suit))
    def __len__(self):
        """Returns the number of cards in the deck """
        return(len(self.cards))

    def isEmpty(self):
        """Returns true if the deck is empty, false if it isn't """
        if self.cards == []:
            return True
        return False

    def deal(self):
        """Deals the top card of the deck by returning and removing it """
        return self.cards.pop(0)

    def shuffle(self):
        """Shuffles the deck """
        return random.shuffle(self.cards)
    def __str__(self):
        """Returns a sttring representation of the deck """
        retString = ""
        for card in self.cards:
            retString += str(card) + "\n"
        return retString
            
        
        

    
        
