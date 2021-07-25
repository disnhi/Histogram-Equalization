
import sys
from plotf import *
from cImage import *

def originalValues(sourceImage):
    width = sourceImage.getWidth()
    height = sourceImage.getHeight()
    newImage = EmptyImage(width,height)

    for x in range(width):
        originalGrayValues = [0]*256
        for y in range(height):
            p = sourceImage.getPixel(x,y)
        
