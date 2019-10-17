"""
File name: snowflake.py
Project 8
Authors: Sam Bluestone , Evan Phaup , Lily White
Description: Contructs a full Koch snowflake taking in the level
and size of the snowflake from the user
"""
from turtle import Turtle
from turtle import tracer
from turtle import update
def main():
    
    t = Turtle()
    level = int(input("Enter the level: "))
    size = int(input("Enter the size: "))
    t.down()
    t.speed(0)
    
    if level > 6:
        tracer(False)
        
    drawFractalLine(t , size , -120 , level)
    drawFractalLine(t , size , 0 , level)
    drawFractalLine(t , size , 120 , level)
    
    if level > 6:
        update()
  
def drawFractalLine(t , distance , angle , level):
    """
    Constructs a Koch snowflake of at a given level 
    """
    
    if level == 0:
        t.setheading(angle)
        t.forward(distance)
    
    else:
        drawFractalLine(t , distance/3 , angle , level - 1)
        drawFractalLine(t , distance/3 ,  angle - 60 , level - 1)
        drawFractalLine(t , distance/3 , angle + 60 , level - 1)
        drawFractalLine(t , distance/3 ,angle , level - 1)

        



if __name__ == "__main__":
    main()
