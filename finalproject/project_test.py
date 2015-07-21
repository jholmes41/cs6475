import numpy as np
import cv2
import unittest

from project import glowingEdges
from project import pencilSketch
from project import watercolor

class FinalProjectTest(unittest.TestCase):
    def setUp(self):
        self.testImage = cv2.imread("IMG_0342.jpg")
        self.testImageGrayScale = cv2.imread("IMG_0342.jpg", cv2.IMREAD_GRAYSCALE)
        self.testImageGray = cv2.imread("IMG_0342.jpg", cv2.COLOR_BGR2GRAY)

        if self.testImage == None:
            raise IOError("Error, test image not found.")

    def test_glowingEdges(self):
        cv2.imwrite("glowing_edges.jpg", glowingEdges(self.testImage, self.testImageGray))
      
    def test_pencilSketch(self):
        cv2.imwrite("sketch_image.jpg", pencilSketch(self.testImageGrayScale))
        
    def test_watercolor(self):
        cv2.imwrite("watercolor_image.jpg", watercolor(self.testImage))

if __name__ == '__main__':
	unittest.main()
