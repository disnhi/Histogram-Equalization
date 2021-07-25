# Histogram-Equalization
Histogram equalization for gray-scale images

Equalize.py contains 4 functions, originalValues, cumulative, newValues, and main. The originalValues function will take in the source image as a parameter and use a nested loop to go through each pixel to determine its gray scale value. The gray scale value is found by finding the blue color component of the pixel because since the image is gray scale, the red, green, and blue component are the same values. With this determined gray scale value, the function will find that number within the initialized list and add one to the current value in that position to generate a list of the overall distribution of the gray scale values in the image.

The cumulative function will use the list generated from the originalValue and use a simple for loop to create a cumulative distribution list by adding up all the numbers leading up to that position.

The newValues function will go through the cumulative list to determine the minimum number within the loop, which will then be used in the equation given. The function will then go through each pixel and calculate the new gray value based on the given equation using the gray scale value of the pixel, the minimum cumulative distribution frequency value, and the area of the image. The function then uses that new gray scale value to set the Pixel for a new image.