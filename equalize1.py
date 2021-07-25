'''This is just for for the histograms and doesnt include the physical image'''

import sys
from plotfreqs import *
from cImage import *

def originalValues(sourceImage):
    width = sourceImage.getWidth()
    height = sourceImage.getHeight()
    newImage = EmptyImage(width,height)

     #This creates the original gray scale values by going through each pixel and calculate the average value between the blue, red, and green value.
    for x in range(width):
        originalGrayValues = []
        for y in range(height):
            p = sourceImage.getPixel(x,y)
            blue = int(p.getBlue())
            red = int(p.getRed())
            green = int(p.getGreen())
            gray = (blue + red + green) // 3
            originalGrayValues.append(gray)

    return originalGrayValues

def cumulative(sourceImage):
    width = sourceImage.getWidth()
    height = sourceImage.getHeight()
    newImage = EmptyImage(width,height)

     #This creates the original gray scale values by going through each pixel and calculate the average value between the blue, red, and green value.
    for x in range(width):
        originalGrayValues = []
        for y in range(height):
            p = sourceImage.getPixel(x,y)
            blue = int(p.getBlue())
            red = int(p.getRed())
            green = int(p.getGreen())
            gray = (blue + red + green) // 3
            originalGrayValues.append(gray)

     #This creates the cumulative distribution list
    cdf = [0]*len(originalGrayValues)
    for i in range(len(originalGrayValues)):
        cdf[i] = cdf[i-1] + originalGrayValues[i]

    return cdf

def newValues(sourceImage):
    width = sourceImage.getWidth()
    height = sourceImage.getHeight()
    newImage = EmptyImage(width,height)

     #This creates the original gray scale values by going through each pixel and calculate the average value between the blue, red, and green value.
    for x in range(width):
        originalGrayValues = []
        for y in range(height):
            p = sourceImage.getPixel(x,y)
            blue = int(p.getBlue())
            red = int(p.getRed())
            green = int(p.getGreen())
            gray = (blue + red + green) // 3
            originalGrayValues.append(gray)

     #This creates the cumulative distribution list
    cdf = [0]*len(originalGrayValues)
    for i in range(len(originalGrayValues)):
        cdf[i] = cdf[i-1] + originalGrayValues[i]
    
 #This hopefully creates a list of the new gray scale values after equalization
    newGrayList = []
    
    for i in range(len(cdf)):
        newGrayValue = ((cdf[i]-cdf[0])/(width*height-cdf[0])*255)
        newGrayValue = int(newGrayValue)
        newGrayList.append(newGrayValue)

    return newGrayList



def main():
    fileName = sys.argv[1]
    imageToProcess = FileImage(fileName)

    frequencies1 = originalValues(imageToProcess)
    frequencies2 = cumulative(imageToProcess)
    frequencies3 = newValues(imageToProcess)

    plotFreqs(frequencies1,frequencies2,frequencies3)

main()

