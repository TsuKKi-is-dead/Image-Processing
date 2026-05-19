import cv2 as cv
import numpy as np


img = cv.imread('NewYork.jpg')
cv.imshow('NewYork', img)

blank= np.zeros(img.shape[:3], dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur=cv.GaussianBlur(gray, (5, 5), 0)
cv.imshow('blur', blur)

cv.imshow('gray', gray)
canny = cv.Canny(gray, 150, 200)
cv.imshow('canny', canny)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found!')
#RETR_LIST: It retrieves all of the contours without establishing any hierarchical relationships.
#RETR_EXTERNAL: It retrieves only the extreme outer contours. It sets hierarchy[i][2]=hierarchy[i][3]=-1 for all the contours.
#RETR_CCOMP: It retrieves all of the contours and organizes them into a two-level hierarchy. At the top level, there are external boundaries of the components. At the second level, there are boundaries of the holes. If there is another contour inside a hole of a connected component, it is still put at the top level.
cv.drawContours(blank, contours, -1, (0, 255, 0), 1)
cv.imshow('contours', blank)

cv.waitKey(0)
cv.destroyAllWindows()

