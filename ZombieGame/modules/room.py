from .gameObjects import *
from os import path

class Room(object):
   """
   Room object contains the walls and dimensions of the area.
   """
   
   # Maximum Numbers
   MAX_ITEMS = 5
   MAX_ENTITIES = 20
   
   # Chances for spawning types
   MEGAZ_CHANCE = 25    # out of 100   
   
   # Room defaults   
   WIDTH_DEFAULT = 30
   HEIGHT_DEFAULT = 16
   HERO_START_DEFAULT = (15,8)
   
   def __init__(self, fileName=None):
      
      self.structures = []
      self.entities = []
      self.items = []
      self.board = []
      
      if fileName == None or not path.exists(fileName):      
         # Make a default room instead
         self.heroStart = Room.HERO_START_DEFAULT
         self.board = [["." for x in range(Room.WIDTH_DEFAULT)] for y in range(Room.HEIGHT_DEFAULT)]
         print(len(self.board), len(self.board[0]))
         
         # Create outer walls
         for x in range(Room.WIDTH_DEFAULT):
            self.structures.append(Wall(x, 0))
            self.structures.append(Wall(x, Room.HEIGHT_DEFAULT - 1))
            
         for y in range(Room.HEIGHT_DEFAULT):
            self.structures.append(Wall(0, y))
            self.structures.append(Wall(Room.WIDTH_DEFAULT - 1, y))

      else:
         #if a file is provided, read in the board from a file
         self.heroStart = (0, 0)
         newFile = open(fileName, "r")
         readFile = newFile.read()
         splitList = readFile.split("\n")   
         
         self.board = []
         for i in range(len(splitList)):
            new = []
            for j in range(len(splitList[i])):
               new.append(".")

            self.board.append(new)
         
         
         for x in range(len(self.board)):
            for y in range(len(self.board[x])):
               self.board[x][y] = splitList[x][y]
               if self.board[x][y] == "#":
                  self.structures.append(Wall(x, y))
               elif self.board[x][y] == " ":
                  self.structures.append(Void(x, y))
               elif self.board[x][y] == "@":
                  self.heroStart = (x, y)
               elif self.board[x][y] == "^":
                  self.structures.append(Stairs("up", x, y))
               elif self.board[x][y] == "v":
                  self.structures.append(Stairs("down", x, y))
               elif self.board[x][y] == "O":
                  self.structures.append(Pitfall(x, y))
               elif self.board[x][y] == "B":
                  self.entities.append(Boss(x, y))
               elif self.board[x][y] == "e":
                  self.items.append(Egg(x, y))

         
   # Clear the drawing board, draw everything
   def drawRoom(self):
      # Redraw the room
      for col in range(len(self.board)):
         for row in range(len(self.board[col])):
            if self.board[col][row] != " " and self.board[col][row] != "#":
               self.board[col][row] = "."
      
      # Let each entity and structure draw itself
      for sequence in [self.structures, self.entities, self.items]:         
         for s in sequence:
            s.draw(self.board)
   
   def positionCheck(self, hero, position):
      """
      Searches through all active objects in the game to detect
      if position would collide with the object.
      """
      # Check to see if it is a valid location
      if self.board[position.x][position.y] == " ":
         return "void"
      
      # Search room objects, zombies, hps, and hero
      for sequence in [self.structures,
                       self.entities,
                       self.items,
                       [hero]]:
         for s in sequence:
            if s.position == position:
               return s
      
      return None
   
   def addEntity(self, hero, entity):
      """
      Adds a new active object to the world.
      Entity parameter is a string indicating the
      type of new entity to add.
      
      Will fail if the randomly selected position is
      already occupied.
      """
      
      positionX = randint(1, len(self.board) - 1)
      positionY = randint(1, len(self.board[positionX]) - 1)
      
      position = Coordinates(positionX, positionY)
      
      if self.positionCheck(hero, position) == None:
         if entity == "zombie":
            self.addZombie(position)
            
         elif entity == "item":
            self.addItem(position)

         else:
            self.addSword(position)
            
      
   
   def addZombie(self, position):
      """
      Will attempt to add a zombie if we haven't hit the max
      number. Randomly selects between a normal Zombie or
      Mega Zombie based on MEGAZ_CHANCE.
      
      This is invoked by addEntity.
      """
      
      if len(self.entities) < Room.MAX_ENTITIES:
            choice = randint(1, 100)
            if choice < Room.MEGAZ_CHANCE:
               self.entities.append(Mega(*position))
            else:
               self.entities.append(Zombie(*position))
      else:
            self.entities.append(Zombie(*position))


   def addBabyZombie(self, position):
      self.entities.append(BabyZombie(*position))
   
   def addSword(self, position):
      """Adds a sword """

      self.items.append(Sword(*position))
      
   
   def addItem(self, position):
      """
      Will attempt to add a health pack if we haven't hit the max
      number.
      
      This is invoked by addEntity.
      """
      if len(self.items) < Room.MAX_ITEMS:
         self.items.append(HealthPack(*position))
         
   
      
   def cleanUp(self):
      
      # Clean up dead things
      self.entities = [x for x in self.entities if not x.isDead()]
      
      # Clean up used items         
      self.items = [x for x in self.items if not x.used]
   

      
   
