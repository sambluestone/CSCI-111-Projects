"""
Author: Ken Lambert (edited by Sam Bluestone, Evan Phaup, and Lily White)
File: testimages.py
Project 8

Script for testing image processing functions.
"""

from images import Image
from random import randint

# Functions that transform images
def posterize(image, postPixel = (0, 0, 0)):
    """Posterizes Image"""
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, postPixel)
            else:
                image.setPixel(x, y, whitePixel)

def blackAndWhite(image):
    """Converts image to black and white."""
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, blackPixel)
            else:
                image.setPixel(x, y, whitePixel)

def colorscale(image , postColor):
    """Instead of scaling from black to white,
        scales from black to a random color"""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            red =   (int(.299* r))
            green =  (int(.587* g))
            blue =  (int(.114 * b) )
            gray =  red  + green + blue
            scalar = gray/255
            image.setPixel(x , y , ( int(scalar * postColor[0]) ,
                                     int(scalar * postColor[1]) ,
                                     int(scalar * postColor[2])))
            

def sepia(image):
    """Converts image to sepia."""
    grayscale(image)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            if r < 63:
                r = int(r * 1.1)
                b = int(b * .9)
            elif r < 192:
                r = int(r * 1.15)
                b = int(b * .85)
            else:
                r = min(int(r * 1.08) , 255)
                b = int(b * .93)

            image.setPixel(x , y , (r , g , b))

def sharpen(image , degree , threshold):
    """Sharpens the image."""
    newImage = image.clone()
    image = detectEdges(image , degree)
    blackPixel = (0, 0, 0)

    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            
            (r , g , b) = image.getPixel(x , y)
            (r1 , g1 , b1) = newImage.getPixel(x , y)
            
            if (r , b , g) == blackPixel:
                newImage.setPixel(x , y ,
                                  (max(0 , r1 - threshold) ,
                                   max(0 , g1 - threshold) ,
                                   max(0 , b1 - threshold)))
            else:
                newImage.setPixel(x , y ,
                                  (min(255 , r1 + threshold) ,
                                   min(255 , g1 + threshold) ,
                                   min(255 , b1 + threshold)))

    return newImage


def rotateRight(image):
    """Rotates the image 90 degrees """
    newImage = Image(image.getHeight() , image.getWidth())
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            newImage.setPixel(image.getHeight() - y - 1 ,x , (r , g , b))

    return newImage           
    

def grayscale(image):
    """Converts image to grayscale """
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r , g , b) = image.getPixel(x , y)
            r = int(r * .299)
            g = int(g * .587)
            b = int(b * .114)
            gray = r + g + b
            image.setPixel(x , y , (gray , gray , gray))
    
    
def detectEdges(image, amount):
    """Builds and returns a new image in which the 
    edges of the argument image are highlighted and
    the colors are reduced to black and white."""

    def average(triple):
        (r, g, b) = triple
        return (r + g + b) // 3

    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    new = image.clone()
    y = 0
    for y in range(image.getHeight() - 1):
        for x in range(1, image.getWidth()):
            oldPixel = image.getPixel(x, y)
            leftPixel = image.getPixel(x - 1, y)
            bottomPixel = image.getPixel(x, y + 1)
            oldLum = average(oldPixel)
            leftLum = average(leftPixel)
            bottomLum = average(bottomPixel)
            if abs(oldLum - leftLum) > amount or \
               abs(oldLum - bottomLum) > amount:
                new.setPixel(x, y, blackPixel)
            else:
                new.setPixel(x, y, whitePixel)
    return new

# Tester functions
def testPosterize(name = "smokey.gif"):
    """Loads and draws an image, then
    converts it to black and white and redraws it."""
    image = Image(name)
    print("Close the image window to see the transformation")
    image.draw()
    posterize(image, (0, 0, 255))
    image.draw()
    image.save(filename = "posterize_" + name)
    

def testBlackAndWhite(name = "smokey.gif"):
    """Loads and draws an image, then
    converts it to black and white and redraws it."""
    image = Image(name)
    print("Close the image window to see the transformation")
    image.draw()
    blackAndWhite(image)
    image.draw()

def testDetect(name = "smokey.gif", amount = 20):
    """Loads and draws an image, then
    detects edges and redraws it."""
    image = Image(name)
    print("Close the image window to see the transformation")
    image.draw()
    image2 = detectEdges(image, amount)
    image2.draw()

def testColorScale(name = "smokey.gif"):
    """Loads and draws an image, then applies colorscale
    to the image and redraws it."""
    image = Image(name)
    print("Close the image window to see the transformation")
    image.draw()
    colorscale(image, (randint(0 , 255), randint(0 , 255), randint(0 , 255)))
    image.draw()
    image.save(filename = "colorscale_" + name)

def testSharpen(name = "smokey.gif"):
    """Loads and draws an image, then sharpens
    the image and redraws it."""
    image = Image(name)
    print("Close the image window to see the transformation")
    image.draw()
    image2 = sharpen(image, 20 , 50)
    image2.draw()
    image2.save(filename = "sharpen_" + name)


def testSepia(name = "smokey.gif"):
    """Loads and draws an image, then
    converts it to sepia and redraws it."""
    image = Image(name)
    print("Close the image window to see the transformation")
    image.draw()
    sepia(image)
    image.draw()
    image.save(filename = "sepia_" + name)

def testRotateRight(name = "smokey.gif"):
    """Loads and draws an image, then
    rotates it 90 degrees to the right and redraws it."""
    image = Image(name)
    print("Close the image window to see the transformation")
    image.draw()
    image2 = rotateRight(image)
    image2.draw()
    image2.save(filename = "rotateRight_" + name)


# Code to run a tester function

def main(name = "halloween.gif"):
    name = input("Enter the name of a gif that you wish to test: ")

    testBlackAndWhite(name)
    testDetect(name)
    testPosterize(name)
    testColorScale(name)
    testSepia(name)
    testSharpen(name)
    testRotateRight(name)
if __name__ == "__main__":
    main()
        
