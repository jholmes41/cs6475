import numpy as np
import cv2
import unittest

from project import glowingEdges
from project import pencilSketch
from project import watercolor

class Assignment4Test(unittest.TestCase):
    def setUp(self):
        self.testImage = cv2.imread("IMG_0342.jpg")
        self.testImageGrayScale = cv2.imread("IMG_0342.jpg", cv2.IMREAD_GRAYSCALE)
        self.testImageGray = cv2.imread("IMG_0342.jpg", cv2.COLOR_BGR2GRAY)
        self.kernelImage = cv2.imread("kernel_gradient.jpg", cv2.IMREAD_GRAYSCALE)

        if self.testImage == None:
            raise IOError("Error, image test_image.jpg not found.")
#    
#    def test_imageGradientX(self):
#        test_output = imageGradientX(self.testImage)
#        self.assertEqual(type(test_output),
#                         type(self.testImage))
#
#        self.assertEqual(test_output.shape[0], self.testImage.shape[0])
#        self.assertEqual(test_output.shape[1], self.testImage.shape[1] - 1)
#
#        print "\n\nSUCCESS: imageGradientX returns the correct output type.\n"
#        
#        cv2.imwrite("x_gradient.jpg", imageGradientX(self.testImage))
#                    
#    def test_imageGradientY(self):
#        test_output = imageGradientY(self.testImage)
#        self.assertEqual(type(test_output),
#                         type(self.testImage))
#        self.assertEqual(test_output.shape[0], self.testImage.shape[0] - 1)
#        self.assertEqual(test_output.shape[1], self.testImage.shape[1])
#        print "\n\nSUCCESS: imageGradientY returns the correct output type.\n"
#        
#        cv2.imwrite("y_gradient.jpg", imageGradientY(self.testImage))
#
#    def test_computeGradient(self):
#        avg_kernel = np.ones((3, 3)) / 9
#
#        gradient = computeGradient(self.testImage, avg_kernel)
#        # Test the output.
#        self.assertEqual(type(gradient), type(self.testImage))
#        # Test the column / rows are two less than input.
#        self.assertEqual(gradient.shape[:2], (self.testImage.shape[0] - 2,
#                                              self.testImage.shape[1] - 2))
#
#        print "\n\nSUCCESS: computeGradient returns the correct output type.\n"
#        
#        cv2.imwrite("kernel_gradient.jpg", computeGradient(self.testImage, avg_kernel))
#        cv2.imwrite("edge_detection.jpg", convertToBlackAndWhite(self.kernelImage))
    def test_glowingEdges(self):
        cv2.imwrite("glowing_edges.jpg", glowingEdges(self.testImage, self.testImageGray))
      
    def test_pencilSketch(self):
        cv2.imwrite("sketch_image.jpg", pencilSketch(self.testImageGrayScale))
        
    def test_watercolor(self):
        cv2.imwrite("watercolor_image.jpg", watercolor(self.testImage, self.testImageGrayScale))

if __name__ == '__main__':
	unittest.main()
