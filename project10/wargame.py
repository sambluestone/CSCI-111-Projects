"""
Author: Ken Lambert (edited by Sam Bluestone, Lily White, Evan Phaup)
File: wargame.py
Project 9

Module for playing the game of War
"""

from cards import Deck

class WarGame(object):
    """Plays the game of War."""

    def __init__(self):
        """Sets up the two players, the war pile, the deck, and the
        game state."""
        self.player1 = Player()
        self.player2 = Player()
        self.warPile = []
        self.gameState = ""
        self.deck = Deck()
        self.deck.shuffle()

    def __str__(self):
        """Returns the game state."""
        return self.gameState

    def deal(self):
        """Deals 26 cards to each player."""
        while not self.deck.isEmpty():
            self.player1.addToUnplayedPile(self.deck.deal())
            self.player2.addToUnplayedPile(self.deck.deal())

    def step(self):
        """Makes one move in the game, and returns the two cards
        played."""
        card1 = self.player1.getCard()
        card2 = self.player2.getCard()
        self.warPile.append(card1)
        self.warPile.append(card2)
        self.gameState = "Player 1: " + str(card1) + "\n" +\
                         "Player 2: " + str(card2)
        if card1.rank == card2.rank:
            self.gameState += "\nCards added to War pile\n"
        elif card1.rank > card2.rank:
            self.transferCards(self.player1)
            self.gameState += "\nCards go to Player 1"
        else:
            self.transferCards(self.player2)
            self.gameState += "\nCards go to Player 2"
        return (card1, card2)

    def transferCards(self, player):
        """Transfers cards from the war pile to the player's
        winnings pile."""
        while len(self.warPile) > 0:
            player.addToWinningsPile(self.warPile.pop())

    def winner(self):
        """Returns None if there is no winner yet.  Otherwise,
        returns a string indicating the player who won with each
        player's number of cards, or a tie."""
        if self.player1.isDone() or self.player2.isDone():
            count1 = self.player1.winningsCount()
            count2 = self.player2.winningsCount()
            if count1 > count2:
                return "Player 1 wins, " + str(count1) + " to " +\
                       str(count2) +"!"
            elif count2 > count1:
                return "Player 2 wins, " + str(count2) + " to " +\
                       str(count1) +"!"
            else:
                return "The game ends in a tie!\n"
        else:
            return None

class Player(object):
    """Represents a War game player."""

    def __init__(self):
        """Sets up the player's unplayed and winnings piles."""
        self.unplayed = []
        self.winnings = []
        

    def __str__(self):
        """Returns a description of the player's winnings pile."""
        return str(self.winnings)

    def addToUnplayedPile(self, card):
        """Adds card to the player's unplayed pile."""
        self.unplayed.append(card)

    def addToWinningsPile(self, card):
        """Adds card to the player's winnings pile."""
        self.winnings.append(card)

    def getCard(self):
        """Removes and returns a card from the player's unplayed pile."""
        if self.unplayed != []:
            return self.unplayed.pop(0)
        return None

    def isDone(self):
        """Returns True if the player's unplayed pile is empty,
        or False otherwise."""
        if self.unplayed == []:
            return True
        return False

    def winningsCount(self):
        """Returns the number of cards in the player's winnings pile."""
        return len(self.winnings)
        

        
