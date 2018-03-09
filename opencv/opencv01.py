import cv2 as cv

img = cv.imread('IMG_0497.png')

cv.imshow('Image', img)
cv.waitKey(2000)
