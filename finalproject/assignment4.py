# ASSIGNMENT 4
# Jennifer Holmes
# jholmes41 / 901491580

import cv2
import numpy as np
import scipy as sp

""" Assignment 4 - Detecting Gradients / Edges

This file has a number of functions that you need to fill out in order to
complete the assignment. Please write the appropriate code, following the
instructions on which functions you may or may not use.

GENERAL RULES:
    1. DO NOT INCLUDE code that saves, shows, displays, writes the image that
    you are being passed in. Do that on your own if you need to save the images
    but the functions should NOT save the image to file. (This is a problem
    for us when grading because running 200 files results a lot of images being
    saved to file and opened in dialogs, which is not ideal). Thanks.

    2. DO NOT import any other libraries aside from the three libraries that we
    provide. You may not import anything else, you should be able to complete
    the assignment with the given libraries (and in most cases without them).

    3. DO NOT change the format of this file. Do not put functions into classes,
    or your own infrastructure. This makes grading very difficult for us. Please
    only write code in the allotted region.
"""

def imageGradientX(image):
    """ This function differentiates an image in the X direction.

    Note: See lectures 02-06 (Differentiating an image in X and Y) for a good
    explanation of how to perform this operation.

    The X direction means that you are subtracting columns:
    der. F(x, y) = F(x+1, y) - F(x, y)
    This corresponds to image[r,c] = image[r,c+1] - image[r,c]

    You should compute the absolute value of the differences in order to avoid
    setting a pixel to a negative value which would not make sense.

    We want you to iterate the image to complete this function. You may NOT use
    any functions that automatically do this for you.

    Args:
        image (numpy.ndarray): A grayscale image represented in a numpy array.

    Returns:
        output (numpy.ndarray): The image gradient in the X direction. The shape
                                of the output array should have a width that is
                                one less than the original since no calculation
                                can be done once the last column is reached. 
    """
    # WRITE YOUR CODE HERE.

    numRows = image.shape[0]
    numCols = image.shape[1]
    
    finalImage = np.empty([numRows, numCols-1])
    
    for i in range(0, numRows - 1):
        for j in range(0, numCols - 1):
            finalImage[i, j] = abs(int(image[i, j+1]) - int(image[i, j]))
    
    return finalImage

    # END OF FUNCTION.

def imageGradientY(image):
    """ This function differentiates an image in the Y direction.

    Note: See lectures 02-06 (Differentiating an image in X and Y) for a good
    explanation of how to perform this operation.

    The Y direction means that you are subtracting rows:
    der. F(x, y) = F(x, y+1) - F(x, y)
    This corresponds to image[r,c] = image[r+1,c] - image[r,c]

    You should compute the absolute value of the differences in order to avoid
    setting a pixel to a negative value which would not make sense.

    We want you to iterate the image to complete this function. You may NOT use
    any functions that automatically do this for you.

    Args:
        image (numpy.ndarray): A grayscale image represented in a numpy array.

    Returns:
        output (numpy.ndarray): The image gradient in the Y direction. The shape
                                of the output array should have a height that is
                                one less than the original since no calculation
                                can be done once the last row is reached.
    """
    # WRITE YOUR CODE HERE.

    numRows = image.shape[0]
    numCols = image.shape[1]
    
    finalImage = np.empty([numRows-1, numCols])
    
    for i in range(0, numRows - 1):
        for j in range(0, numCols - 1):
            finalImage[i, j] = abs(int(image[i+1, j]) - int(image[i, j]))
    
    return finalImage

    # END OF FUNCTION.

def computeGradient(image, kernel):
    """ This function applies an input 3x3 kernel to the image, and outputs the
    result. This is the first step in edge detection which we discussed in
    lecture.

    You may assume the kernel is a 3 x 3 matrix.
    View lectures 2-05, 2-06 and 2-07 to review this concept.

    The process is this: At each pixel, perform cross-correlation using the
    given kernel. Do this for every pixel, and return the output image.

    The most common question we get for this assignment is what do you do at
    image[i, j] when the kernel goes outside the bounds of the image. You are
    allowed to start iterating the image at image[1, 1] (instead of 0, 0) and
    end iterating at the width - 1, and column - 1.
    
    Note: The output is a gradient depending on what kernel is used.

    Args:
        image (numpy.ndarray): A grayscale image represented in a numpy array.
        kernel (numpy.ndarray): A 3x3 kernel represented in a numpy array.

    Returns:
        output (numpy.ndarray): The computed gradient for the input image. The
                                size of the output array should be two rows and
                                two columns smaller than the original image
                                size.
    """                            
    # WRITE YOUR CODE HERE.

    numRows = image.shape[0]
    numCols = image.shape[1]
    
    finalImage = np.empty([numRows-2, numCols-2])
    
    for i in range(1, numRows - 2):
        for j in range(1, numCols - 2):
            finalImage[i, j] = int(((kernel[0, 0] * image[i-1, j-1]) + (kernel[1, 0] * image[i, j-1]) + (kernel[2, 0] * image[i+1, j-1]) + (kernel[0, 1] * image[i-1, j]) + (kernel[1, 1] * image[i, j]) + (kernel[2, 1] * image[i+1, j]) + (kernel[0, 2] * image[i-1, j+1]) + (kernel[2, 1] * image[i, j+1]) + (kernel[2, 2] * image[i+1, j+1])) / 9)
    
    return finalImage

    # END OF FUNCTION.
    
def convertToBlackAndWhite(image):
    """ This function converts a grayscale image to black and white.

    Assignment Instructions: Iterate through every pixel in the image. If the
    pixel is strictly greater than 128, set the pixel to 255. Otherwise, set the
    pixel to 0. You are essentially converting the input into a 1-bit image, as 
    we discussed in lecture, it is a 2-color image.

    You may NOT use any thresholding functions provided by OpenCV to do this.
    All other functions are fair game.

    Args:
        image (numpy.ndarray): A grayscale image represented in a numpy array.

    Returns:
        numpy.ndarray: The black and white image.
    """
    # WRITE YOUR CODE HERE.

    for position,value in np.ndenumerate( image ):
        if value > 23:
            image[position] = 255
        else:
            image[position] = 0
            
    return image

    # END OF FUNCTION.
    