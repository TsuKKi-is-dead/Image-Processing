import cv2 as cv
import numpy as np

blank = np.zeros((400, 400, 3), dtype='uint8')
cv.imshow("Blank", blank)

# 1. Paint the image a certain color
blank[:] = 0, 255, 0
cv.imshow("Green", blank)