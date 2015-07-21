# FINAL PROJECT
# Jennifer Holmes
# jholmes41 / 901491580

import cv2
import numpy as np
import scipy as sp
    
def glowingEdges(image, imageGray):

    imageBlur = cv2.GaussianBlur(imageGray,(3,3),0)
    sobelX = cv2.convertScaleAbs(cv2.Sobel(imageBlur, cv2.CV_16S, 1, 0, ksize = 3, scale = 1, delta = 0, borderType = cv2.BORDER_DEFAULT))
    sobelY = cv2.convertScaleAbs(cv2.Sobel(imageBlur, cv2.CV_16S, 0, 1, ksize = 3, scale = 1, delta = 0, borderType = cv2.BORDER_DEFAULT))
    tempImage = cv2.addWeighted(sobelX, 0.5, sobelY, 0.5, 0)
    
    for position,value in np.ndenumerate(tempImage):
        tempImage[position] = abs(255 - value)
        
    finalImage = np.zeros_like(image)
    
    for position, value in np.ndenumerate(tempImage):
      if value != 255:
        finalImage[position] = value
      else:
        finalImage[position] = image[position]
            
    return finalImage
  
  
  
def pencilSketch(image):
  
    imageBlur = cv2.GaussianBlur(image,(3,3),0)
    sobelX = cv2.convertScaleAbs(cv2.Sobel(imageBlur, cv2.CV_16S, 1, 0, ksize = 3, scale = 1, delta = 0, borderType = cv2.BORDER_DEFAULT))
    sobelY = cv2.convertScaleAbs(cv2.Sobel(imageBlur, cv2.CV_16S, 0, 1, ksize = 3, scale = 1, delta = 0, borderType = cv2.BORDER_DEFAULT))
    tempImage = cv2.addWeighted(sobelX, 0.5, sobelY, 0.5, 0)
    
    finalImage = np.zeros_like(image)
    for position,value in np.ndenumerate(tempImage):
        finalImage[position] = abs(255 - value)
            
    finalImage = cv2.blur(finalImage,(3,5))
    
    return finalImage
  
  
    

def watercolor(image):
    
    finalImage = np.zeros_like(image)
    
    imageBlur = cv2.GaussianBlur(image,(3,3),0)
    imageBlur = cv2.cvtColor(imageBlur, cv2.COLOR_BGR2GRAY)
    sobelX = cv2.convertScaleAbs(cv2.Sobel(imageBlur, cv2.CV_16S, 1, 0, ksize = 3, scale = 1, delta = 0, borderType = cv2.BORDER_DEFAULT))
    sobelY = cv2.convertScaleAbs(cv2.Sobel(imageBlur, cv2.CV_16S, 0, 1, ksize = 3, scale = 1, delta = 0, borderType = cv2.BORDER_DEFAULT))
    tempImage = cv2.addWeighted(sobelX, 0.5, sobelY, 0.5, 0)
    tempImage = cv2.cvtColor(tempImage, cv2.COLOR_GRAY2BGR)
    
    for position,value in np.ndenumerate(tempImage):
        if value <= 128:
            tempImage[position] = 255
        else:
            tempImage[position] = 0
    
    tempColorImage = cv2.pyrMeanShiftFiltering(image, 30, 30)

    finalImage = cv2.addWeighted(tempColorImage, 0.5, tempImage, 0.5, 0)
    finalImage = cv2.addWeighted(tempColorImage, 0.3, finalImage, 0.7, 0)
            
    return finalImage
  
  
    

  
  
  