"""
Author: Ken Lambert
File: crapsgui.py
Project 9

Pops up a window that allows the user to view each card by pressing 
a button.  After the last card is drawn, the backside of the deck 
is displayed.
"""

from breezypythongui import EasyFrame

from tkinter import PhotoImage

from crapsgame import CrapsGame

class CrapsGUI(EasyFrame):

   def __init__(self):
      """Creates the craps game, and sets up the Images and labels
      for the two dice to be displayed, the state label,
      and the two command buttons."""
      EasyFrame.__init__(self, title = "Let's play Craps!")
      self.setSize(220, 200)
      self.game = CrapsGame()
      self.dieImageLabel1 = self.addLabel("", row = 0, column = 0)
      self.dieImageLabel2 = self.addLabel("", row = 0, column = 1)
      self.stateLabel = self.addLabel("", row = 1, column = 0,
                                      columnspan = 2)
      self.nextRollButton = self.addButton(row = 2, column = 0,
                                           text = "Roll",
                                   command = self.nextRoll)
      self.newGameButton = self.addButton(row = 2, column = 1,
                                          text = "New game",
                                          command = self.newGame,
                                          state = "disabled")

   def nextRoll(self):
      """Makes a move in the game and updates the view with
      the results."""
      (die1, die2, outcome) = self.game.step()
      self.image1 = PhotoImage(file = die1.fileName)
      self.dieImageLabel1["image"] = self.image1
      self.image2 = PhotoImage(file = die2.fileName)
      self.dieImageLabel2["image"] = self.image2
      self.stateLabel["text"] = str(self.game)
      if outcome:
         self.messageBox("Game Is Over!", outcome)
         self.nextRollButton["state"] = "disabled"
         self.newGameButton["state"] = "normal"

   def newGame(self):
      """Create a new craps game and updates the view."""
      self.game = CrapsGame()
      self.image1 = None
      self.image2 = None
      self.stateLabel["text"] = ""
      self.newGameButton["state"] = "disabled"
      self.nextRollButton["state"] = "normal"

def main():
   app = CrapsGUI()
   app.mainloop()

if __name__ == "__main__":
   main()
