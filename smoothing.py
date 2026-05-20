import cv2 as cv
import numpy as np
img= cv.imread('NewYork.jpg')
cv.imshow('NewYork', img)

#Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

#Gaussian blurring
gaussian = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian', gaussian)

#Median Blurring
median = cv.medianBlur(img, 3)
cv.imshow('Median', median) 

#Bilateral Blurring
bilateral = cv.bilateralFilter(img, 9, 75, 75)  
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)
cv.destroyAllWindows()