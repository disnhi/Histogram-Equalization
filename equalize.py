

import sys
'''This module was imported to use the command line operand to import a picture file'''

from plotfreqs import *
'''This module was imported to use for the plotting of the 3 different histograms'''

from cImage import *
'''This module was imported to edit the image file and generate the equalized image'''

def originalValues(sourceImage):

    #This assigns the image's width and height to a variable, making it easier to utilize
    width = sourceImage.getWidth()
    height = sourceImage.getHeight()

    #This creates the original gray scale values by going through each pixel and calculate the average value between the blue, red, and green value.

    #This initializes a list of 255 zeros.
    originalGrayValues = [0]*256

    #This nested loop will go through every pixel in the image to find the gray scale value of each and then add one to the originalGrayValues list everytime that value occurs.
    for x in range(width):
        for y in range(height):
            p = sourceImage.getPixel(x,y)
            gray = p.getBlue() #The gray-scale image Red = Blue = Green
            originalGrayValues[gray] = originalGrayValues[gray] + 1
        
    return originalGrayValues


def cumulative(sourceImage):

    #This assigns the list determined from the originalValues function to "grayValues"
    grayValues = originalValues(sourceImage)
    
    #This initializes a list of 255 zeros.
    cdf = [0]*256

    #This for loop goes through the grayValues list and creates a cumulative distribution list.
    for i in range(len(grayValues)):
        cdf[i] = cdf[i-1] + grayValues[i]

    return cdf


def newValues(sourceImage):

    #This assigns the list determined from the originalValues function to "grayValues"
    grayValues = originalValues(sourceImage)

    #This assigns the list determined from the cumulative function to "cdf"
    cdf = cumulative(sourceImage)

    #This assigns the image's width and height to a variable, making it easier to utilize
    width = sourceImage.getWidth()
    height = sourceImage.getHeight()

    #This creates an empty image
    newImage = EmptyImage(width,height)
    

    #This for loop will go through the cdf list to find the smallest value.
    currentMin = 1000000000000
    for i in range(len(cdf)):
        if (cdf[i] < currentMin and cdf[i] != 0):
            currentMin = cdf[i]

    #This nested for loop will go through each pixel and calculate the new gray value based on the given equation. It will then assign the newly calculated gray value to the new image and return that image.
    for x in range(width):
        for y in range(height):
            p = sourceImage.getPixel(x,y)
            gray  = p.getBlue()
            newGrayValue = ((cdf[gray]-currentMin)/(width*height-currentMin)*255)
            newGrayValue = int(newGrayValue)
            newImage.setPixel(x,y,Pixel(newGrayValue,newGrayValue,newGrayValue))
            
    return newImage


def main():

    #This will take in the image file as a command line argument and process the file.
    fileName = sys.argv[1]
    imageToProcess = FileImage(fileName)

    #This creates two seperate windows with a size that is  slightly large than the image to give the image a white boarder.
    win1 = ImageWin('Original Image',imageToProcess.getWidth()+10,imageToProcess.getHeight()+10)
    win2 = ImageWin('Original Image',imageToProcess.getWidth()+10,imageToProcess.getHeight()+10)

    #This draws the original image into the first window and the second equalized image gathered from the newValues function into the second window.
    imageToProcess.draw(win1)
    newValues(imageToProcess).draw(win2)

    #This allows the user to exit the image window upon clicking it.
    win1.exitonclick()
    win2.exitonclick()

    #This assigns the original gray scale value distribution, the cumulative distribution value, and the equalized gray scale value distribution data gathered using their associated functions to the three different parameteres that will be used in the plotFreqs module. 
    frequencies1 = originalValues(imageToProcess)
    frequencies2 = cumulative(imageToProcess)
    frequencies3 = originalValues(newValues(imageToProcess))

    #This will graph a histogram for the gray scale value distribution, the cumulative distribution value, and the equalized gray scale value distribution. 
    plotFreqs(frequencies1,frequencies2,frequencies3)
 
main()

