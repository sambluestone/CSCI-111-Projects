"""
Author: Evan Phaup
File: rainbow.py
Project 9

Makes an image rainbow-like
"""

from images import Image

def main():
    colors = [(255, 0, 0),
              (255, 255, 0),
              (0, 255, 0),
                 (0, 255, 255),
                 (0, 0, 255),
                 (255, 0, 255)]
    
    img = Image(500, 200)
    rainbow(img, colors)
    img.draw()
    #img.save(filename = "rainbow.gif")
    

def colorFade(startColor, endColor, percent):
    #Linearly interpolates a color between startColor and endColor
    #based on percent
    r1, g1, b1 = startColor
    r2, g2, b2 = endColor
    r = int((r2 - r1)*percent)+ r1
    g = int((g2- g1)*percent) + g1
    b = int((b2 - b1)*percent)+ b1
    return (r, g, b)

def rainbow (img, colors):
    #Given an image and a list of color-triples,
    #evenly fades between each color horizontally
    pixel = (0, 0, 0)
    percent = 100
    i = 1
    for x in range(img.getWidth()):
        if x % 100 == 0 and x != 0:
            i += 1
        if i == 1:
            percent = x / (100 * i)
        else:
            percent = (x - (100 * (i - 1))) / ((100 * i) - (100 * (i - 1)))
        #print(x)  
        #for testing
        pixel = colorFade(colors[i-1], colors[i], percent)
        for y in range(img.getHeight()):
            img.setPixel(x, y, pixel)
        

if __name__ == "__main__":
    main()
