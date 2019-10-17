"""
Author: Ken Lambert (edited by Sam Bluestone, Evan Phaup, Lily White)
File: wargui.py
Project 9

Pops up a window that allows the user to view each card by pressing 
a button.  After the last card is drawn, the backside of the deck 
is displayed.
"""

from breezypythongui import EasyFrame

from tkinter import PhotoImage

from cards import Card

from wargame import WarGame

class WarGUI(EasyFrame):

   def __init__(self):
      """Creates the war game, and sets up the Images and labels
      for the two cards to be displayed, the state label,
      and the command button."""
      EasyFrame.__init__(self, title = "Let's play War!")
      self.setSize(300, 300)
      self.game = WarGame()
      self.game.deal()
      self.playerLabel1 = self.addLabel(row = 0, column = 0,
                                         text = "Player 1")
      self.playerLabel2 = self.addLabel(row = 0, column = 1,
                                         text = "Player 2")
      self.image1 = PhotoImage(file = Card.BACK_NAME)
      self.image2 = PhotoImage(file = Card.BACK_NAME)
      self.cardImageLabel1 = self.addLabel("", row = 1, column = 0)
      self.cardImageLabel1["image"] = self.image1
      self.cardImageLabel2 = self.addLabel("", row = 1, column = 1)
      self.cardImageLabel2["image"] = self.image2
      self.stateLabel = self.addLabel("", row = 2, column = 0,
                                      columnspan = 2)
      self.nextCardButton = self.addButton(row = 3, column = 0,
                                   text = "Next card", 
                                   command = self.nextCard)
      self.newGameButton = self.addButton(row = 4 , column = 0,
                                          text = "New Game",
                                          state = "disabled",
                                          command = self.newGame)

   def newGame(self):
      self.game = WarGame()
      self.game.deal()
      self.newGameButton['state'] = "disabled"
      self.nextCardButton['state'] = "normal"
   
   def nextCard(self):
      """Makes a move in the game and updates the view with
      the results."""
      (card1, card2) = self.game.step()
      self.image1 = PhotoImage(file = card1.fileName)
      self.cardImageLabel1["image"] = self.image1
      self.image2 = PhotoImage(file = card2.fileName)
      self.cardImageLabel2["image"] = self.image2
      self.stateLabel["text"] = str(self.game)
      if self.game.winner():
         self.messageBox("Game Is Over!", self.game.winner())
         self.newGameButton['state'] = "normal"
         self.nextCardButton['state'] = "disabled"
           

def main():
   app = WarGUI()
   app.mainloop()

if __name__ == "__main__":
   main()
