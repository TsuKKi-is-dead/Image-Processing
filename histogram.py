import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

img = cv.imread('NewYork.jpg')
cv.imshow('Original', img)  

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Create a histogram of the grayscale image
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()  

cv.waitKey(0)
cv.destroyAllWindows()