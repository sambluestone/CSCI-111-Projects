"""
Framework for a mini zombie game
Author: Elizabeth Matthews
For use in CS 111 at Washington and Lee University
"""

from modules.charInput import getch
from modules.clearScreen import clear
from modules.timer import Timer
from modules.gameObjects import *
from modules.room import Room
from modules.coordinates import *

from os import path, listdir


class GameEngine(object):   

   SCORE = 0
   
   def __init__(self, roomsLocation=None):
      """
      Initializes the game engine to the starting
      state of the game.
      """
      
      self.turns = 0
      self.score = 0
      # Initialize timers with a minimum and maximum number of turns before spawning something
      self.timers = {
         "zombie" : Timer(Timer.TIMER_ZOMBIE_MIN, Timer.TIMER_ZOMBIE_MAX),
         "item" : Timer(Timer.TIMER_ITEM_MIN, Timer.TIMER_ITEM_MAX),
         "sword": Timer(Timer.TIMER_SWORD_MIN, Timer.TIMER_SWORD_MAX)
      }
      
      # Set up rooms
      if roomsLocation == None:
         self.rooms = [Room()]
      else:
         # Get files from the directory
        
         self.rooms = [Room(roomsLocation + "/room_01.txt"), Room(roomsLocation + "/room_02.txt"), Room(roomsLocation + "/room_03.txt")]
         
      # Select current room
      self.currentRoom = 0
      
      # Place hero in the center of the room
      self.hero = Hero(*self.rooms[self.currentRoom].heroStart)
      
  
   # Displays all active items in the game
   def display(self):
      """
      Displays the game in its current state.
      """
      
      # Draw the room
      self.rooms[self.currentRoom].drawRoom()
      
      # Draw hero in the room
      self.hero.draw(self.rooms[self.currentRoom].board)      
      
      # Clear terminal screen
      ### Disable this if you need to add print statements elsewhere ###
      clear()
      
      # Display game board to screen      
      print("\n".join(["".join(x) for x in self.rooms[self.currentRoom].board]))
      
      # Display HUD
      print("\nTurn:", self.turns)
      print("Health:", self.hero.hp)
      print("Points:", GameEngine.SCORE)
      print("Current Room #" + str(self.currentRoom + 1))
      
      ### Print stuff here if you need to check a value ###
      
   
   def update(self, command):
      """
      Allows all active objects in the game to
      think and update their states.
      """
      
      # Set up and iterate over each sequence of things that can be updated
      for sequence in [[self.hero], self.rooms[self.currentRoom].entities]:
         # Iterate over each entity in the sequenec
         for entity in sequence:
            # Update based on type of entity
            if isinstance(entity, Hero):                  
               entity.update(command)
               """if entity.useLaser:
                  while True"""
            elif isinstance(entity, Mega):
               if entity.isDead():
                  GameEngine.SCORE += 5
               entity.update(self.hero)
            elif isinstance(entity, Boss):
               #charge attack
               if entity.position.x == self.hero.position.x \
               or entity.position.y == self.hero.position.y:
                  entity.update(self.hero)
               #Boss moves every other turn if not in line with hero
               elif self.turns % 2 == 1:
                  entity.update(self.hero)
               #spawn zombies around
               elif self.turns % 5 == 0:
                  if self.rooms[self.currentRoom].positionCheck(self.hero, Coordinates(entity.position.x + 1, entity.position.y)) == None:
                     self.rooms[self.currentRoom].addZombie(Coordinates(entity.position.x + 1, entity.position.y))
                  if self.rooms[self.currentRoom].positionCheck(self.hero, Coordinates(entity.position.x - 1, entity.position.y)) == None:
                     self.rooms[self.currentRoom].addZombie(Coordinates(entity.position.x - 1, entity.position.y))
                  if self.rooms[self.currentRoom].positionCheck(self.hero, Coordinates(entity.position.x, entity.position.y + 1)) == None:
                     self.rooms[self.currentRoom].addZombie(Coordinates(entity.position.x, entity.position.y + 1))
                  if self.rooms[self.currentRoom].positionCheck(self.hero, Coordinates(entity.position.x, entity.position.y - 1)) == None:
                     self.rooms[self.currentRoom].addZombie(Coordinates(entity.position.x, entity.position.y - 1))

                
                  
            else:
               if entity.isDead():
                  GameEngine.SCORE += 1
               entity.update()               
         
            # If the entity wants to move somewhere, handle collision
            if entity.targetPosition:
               collider = self.rooms[self.currentRoom].positionCheck(self.hero, entity.targetPosition)
               
               # No collider lets the entity move to their target position
               if collider == None:
                  entity.position = entity.targetPosition
               
               # Allow health packs to be used only by the hero
               elif isinstance(collider, HealthPack) and isinstance(entity, Hero):
                  entity.increaseHP(collider.amount)
                  collider.used = True
               
               # Have entities attack each other only if the hero is attacking a zombie or vice versa
               elif (isinstance(collider, Zombie) and isinstance(entity, Hero)) or \
                    (isinstance(collider, Hero) and isinstance(entity, Zombie)):
                  collider.decreaseHP(entity.attack())

               elif (isinstance(collider, Stairs) and isinstance(entity, Hero)):
                  if collider.direction == "up":
                     self.currentRoom += 1
                  else:
                     self.currentRoom -= 1

               elif (isinstance(collider, Pitfall) and isinstance(entity, Hero)):
                  self.currentRoom-=1
               elif isinstance(collider, Egg) and isinstance(entity, Hero):
                  #spawns baby zombies if egg is picked up
                  collider.used = True
                  if self.rooms[self.currentRoom].positionCheck(self.hero, Coordinates(collider.position.x + 1, collider.position.y)) == None:
                     self.rooms[self.currentRoom].addBabyZombie(Coordinates(collider.position.x + 1, collider.position.y))
                  if self.rooms[self.currentRoom].positionCheck(self.hero, Coordinates(entity.position.x - 1, entity.position.y)) == None:
                     self.rooms[self.currentRoom].addBabyZombie(Coordinates(collider.position.x - 1, collider.position.y))
                  if self.rooms[self.currentRoom].positionCheck(self.hero, Coordinates(entity.position.x, entity.position.y + 1)) == None:
                     self.rooms[self.currentRoom].addBabyZombie(Coordinates(collider.position.x, collider.position.y + 1))
                  if self.rooms[self.currentRoom].positionCheck(self.hero, Coordinates(collider.position.x, entity.position.y - 1)) == None:
                     self.rooms[self.currentRoom].addBabyZombie(Coordinates(collider.position.x, collider.position.y - 1))  

               elif isinstance(collider, Sword) and isinstance(entity, Hero):
                  #doubles hero's AP if sword is picked up
                  collider.used = True
                  self.hero.AP = 4
      # Update timers by one
      for t in self.timers.keys():
         self.timers[t].tick()
         
         # Add items if need be
         if self.timers[t].isDone():
            if self.currentRoom != len(self.rooms) - 1:
               self.rooms[self.currentRoom].addEntity(self.hero, t)
               
            else:
               self.rooms[self.currentRoom].addEntity(self.hero, t)
 
            self.timers[t].reset()
  
   
   
   def run(self):
      """
      Runs the game until either the game is quit
      or the end condition is met.
      """
      
      RUNNING = True
      WIN = False
      
      while(RUNNING):
      
         # Display things
         self.display()
         
         # Get action
         command = getch()
         
         # Check for quit command
         if (command in ["q", "Q"]):
            RUNNING = False
         else:
            # Update things
            self.update(command)
         if self.currentRoom == len(self.rooms) - 1:
            for s in self.rooms[self.currentRoom].entities:
               if type(s) == Boss:
                  if s.isDead():
                     RUNNING = False
                     WIN = True
                     
         
         # Remove things that are dead or used
         self.rooms[self.currentRoom].cleanUp()         

       
         # Check for game over
         if self.hero.isDead():
            RUNNING = False
         
                   
         # Increase number of turns
         self.turns += 1
      
      # Game over!
      self.display()
      if not WIN:
         print("\n\nGame Over!")
      else:
         print("\nYou Win!")

      



if __name__ == '__main__':
   game = GameEngine("rooms")
   
   game.run()
