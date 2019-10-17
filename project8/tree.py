"""
Tree.py

Evan Phaup, Lily White, Sam Bluestone

Recursive Program that draws a pretty tree.
"""
from turtle import Turtle

def main():
    turt = Turtle()
    length = int(input("Enter the length for the starting branch: "))
    level = int(input("Enter the number of levels for the tree: "))
    turt.down()
    turt.setheading(90)
    turt.forward(length)
    makeTree(turt, length, level)


def makeTree(turt, length, level):
    
    
    if level > 0:
        turt.right(60)
        turt.forward(length)
        makeTree(turt, length/2, level - 1)
        turt.backward(length)
        
        turt.left(60)
        turt.forward(length)
        makeTree(turt, length/2, level - 1)
        turt.backward(length)
        
        turt.left(60)
        turt.forward(length)
        makeTree(turt, length/2, level - 1)
        turt.backward(length)

        turt.right(60)
        
    

if __name__ == "__main__":
    main()
