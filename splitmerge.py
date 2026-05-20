import cv2 as cv
import numpy as np  

img = cv.imread('NewYork.jpg')
cv.imshow('Original Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)
# Split the image into its color channels
b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
cv.imshow('Blue Channel', blue)
green = cv.merge([blank, g, blank])
cv.imshow('Green Channel', green)
red = cv.merge([blank, blank, r])
cv.imshow('Red Channel', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)
cv.destroyAllWindows()


#merge the channels back into a single image
merged_img = cv.merge((b,g,r))
cv.imshow('Merged image',merged_img)
cv.waitKey(0)
cv.destroyAllWindows()
