from .coordinates import Coordinates
from random import randint


class Drawable(object):
   """
   The base class for all drawable objects.
   """
   
   def __init__(self, icon, x, y):
      self.icon = icon
      self.position = Coordinates(x, y)
   
   def draw(self, board):
      board[self.position.x][self.position.y] = self.icon

class Wall(Drawable):
   """
   Wall object for collision only.
   """
   def __init__(self, x, y):
      super().__init__("#", x, y)

class Void(Drawable):
   """
   Void object for collision/void only.
   """
   def __init__(self, x, y):
      super().__init__(" ", x, y)
         

class HealthPack(Drawable):
   """
   Health Packs that the hero can pick up.
   """
   
   MIN = 5
   MAX = 10
   
   def __init__(self, x, y):
      self.amount = randint(HealthPack.MIN, HealthPack.MAX)
      self.used = False
      super().__init__("H", x, y)

class Alive(Drawable):
   """
   Alive base class for anything that moves and can die.
   Slightly ironic name since zombies inherit from it....
   """
   def __init__(self, icon, hp, ap, x, y):
      self.hp = hp
      self.ap = ap
      super().__init__(icon, x, y)
      
      self.targetPosition = self.position
      
   def isDead(self):
      return self.hp <= 0

   def increaseHP(self, amount):
      self.hp += amount
   
   def decreaseHP(self, amount):
      self.hp -= amount
   
   def attack(self):
      return self.ap

class Zombie(Alive):
   """
   Basic zombie, not very smart
   Will randomly stumble around the room
   """
   
   HP = 4
   AP = 1
   STUMBLE = 2
   
   def __init__(self, x, y):
      super().__init__("Z", Zombie.HP, Zombie.AP, x, y)
   
   def update(self):
      
      self.targetPosition = Coordinates(*self.position)
      
      # randomly move
      choice = randint(0,4 + Zombie.STUMBLE)
      
      if choice == 0:
         # move up
         self.targetPosition.y -= 1
      elif choice == 1:
         # move down
         self.targetPosition.y += 1
      elif choice == 2:
         # move left
         self.targetPosition.x -= 1
      elif choice == 3:
         # move right
         self.targetPosition.x += 1
      else:
         # don't move otherwise
         self.targetPosition = None

     

class Mega(Zombie):
   """
   Mega Zombie class that will sometimes head for the hero.
   Other times it behaves like a normal zombie.
   """
   
   HP = 8
   AP = 2
   INTELLIGENCE = 90 # out of 100
   
   def __init__(self, x, y):
      super().__init__(x, y)
      self.icon = "M"
      self.hp = Mega.HP
      self.ap = Mega.AP
   
   # Based on the intelligence value, will move towards the hero
   def update(self, hero):      
      
      choice = randint(1, 100)
      
      # If we are smart
      if choice < Mega.INTELLIGENCE:
         
         self.targetPosition = Coordinates(*self.position)
         
         # Find where the hero is and move one step closer
         # Priority is given to the x axis
         if hero.position.x < self.targetPosition.x:
            self.targetPosition.x -= 1
         elif hero.position.x > self.targetPosition.x:
            self.targetPosition.x += 1
         elif hero.position.y < self.targetPosition.y:
            self.targetPosition.y -= 1
         else:
            self.targetPosition.y += 1
         
      # If we are not smart 
      else:
         super().update()
      

class Hero(Alive):
   """
   The hero class.
   Makes moves based on a command from the keyboard.
   """
   
   HP = 100
   AP = 2
   
   def __init__(self, x, y):
      super().__init__("@", Hero.HP, Hero.AP, x, y)
      self.targetPosition = None
      self.hasLaser = False
      self.useLaser = False
   
   def update(self, command):
      # Do something based on the command character
      
      self.targetPosition = Coordinates(*self.position)
         
      if command == "w":
         # Move up
         self.targetPosition.x -= 1 
      elif command == "s":
         # Move down
         self.targetPosition.x += 1
      elif command == "a":
         # Move left
         self.targetPosition.y -= 1
      elif command == "d":
         # Move right
         self.targetPosition.y += 1
      
         
      else:
         self.targetPosition = None

class Stairs(Drawable):

   def __init__(self, direction, x , y):
      self.direction = direction
      if self.direction == "up":
         super().__init__("^" , x, y)
      elif self.direction == "down":
         super().__init__("v", x, y)

      

class Boss(Zombie):
   """Boss class
      Given greater HP and AP and updates based on position of the hero"""
   HP = 20
   AP = 10

   def __init__(self, x, y):
      super().__init__(x, y)
      self.icon = "B"
      self.hp = Boss.HP
      self.ap = Boss.AP
      

   def update(self, hero):
      
      self.targetPosition = Coordinates(*self.position)
         
      # Find where the hero is and move one step closer
      # Priority is given to the x axis
      if hero.position.x < self.targetPosition.x:
         self.targetPosition.x -= 1
      elif hero.position.x > self.targetPosition.x:
         self.targetPosition.x += 1
      elif hero.position.y < self.targetPosition.y:
         self.targetPosition.y -= 1
      else:
         self.targetPosition.y += 1



class Egg(Drawable):
   """Egg class, disappears when consumed"""
   def __init__(self, x, y):
      super().__init__("e", x, y)
      self.used = False
   

class BabyZombie(Zombie):
   """Baby Zombie class
      Given lower HP and greater stumble value, updates position randomly"""
   HP = 2
   AP = 1
   STUMBLE = 4
   def __init__(self, x, y):
      super().__init__(x, y)
      self.icon = "z"
      self.hp = BabyZombie.HP
      self.ap = BabyZombie.AP

   def update(self):
      
      self.targetPosition = Coordinates(*self.position)
      
      # randomly move
      choice = randint(0,4 + BabyZombie.STUMBLE)
      
      if choice == 0:
         # move up
         self.targetPosition.y -= 1
      elif choice == 1:
         # move down
         self.targetPosition.y += 1
      elif choice == 2:
         # move left
         self.targetPosition.x -= 1
      elif choice == 3:
         # move right
         self.targetPosition.x += 1
      else:
         # don't move otherwise
         self.targetPosition = None
   

class Sword(Drawable):
   """Sword class
      Disappears when used"""
   def __init__(self, x, y):
      self.used = False
      super().__init__("S", x, y)
   

class Pitfall(Drawable):
   """Pitfall class
      Moves the hero down one floor if collided"""

   def __init__(self, x, y):
      super().__init__("O", x, y)
   

 
      
      

   
