"""
File name: polygonFlower.py
Project 8
Authors: Sam Bluestone, Evan Phaup, Lily White
Description: Draws a flower with a given length, number of petals, and number
of sides from the user
"""
from turtle import Turtle
from turtleexamples import drawSquare
def main():
    t = Turtle()
    length = int(input("Enter the length: "))
    numPetals = int(input("Enter the number of polygons to draw: "))
    numSides = int(input("Enter the number of sides: "))
    drawFlower(t, length, numPetals, lambda t , length: drawPolygon(t, length, numSides))

def drawPolygon(t , length , numSides):

    t.down()
    totalAngles = 180*(numSides - 2)

    for count in range(numSides):
        t.forward(length)
        t.left(180 - (totalAngles/numSides))

    t.up()
    
def drawFlower(t, length, numPetals = 4, function = drawSquare):
    """Draws a flower with a given length, number of petals, and function
       for drawing the shape. The number of petals is set at a default
       value of 4, and function is set to the default function of drawSquare
    """
    t.down()
    for petals in range(numPetals):
        function(t , length)
        t.left(360/numPetals)




if __name__ == "__main__":
    main()
