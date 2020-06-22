import cv2
import numpy as np

img = cv2.imread('book.PNG')

#Theresholding using THRESH_BINARY on the RGB image
_, RGB_binary_threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

#Gray Scaling the RGB Image
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Theresholding using THRESH_BINARY on the Gray Scaled image
_, grayscale_binary_threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)

#Theresholding using ADAPTIVE_THRESH_GAUSSIAN_C on the Gray Scaled image
grayscaale_adaptive_binary_threshold = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

#OUTPUTS:
#Showing the orignal image
cv2.imshow('original',img)

#Showing the RGB_binary_threshold image
cv2.imshow('RGB_binary_threshold', RGB_binary_threshold)

#Showing the grayscale_binary_threshold image
cv2.imshow('grayscale_binary_threshold', grayscale_binary_threshold)

#Showing the grayscaale_adaptive_binary_threshold image
cv2.imshow('grayscaale_adaptive_binary_threshold', grayscaale_adaptive_binary_threshold)

#Setting the wait key to "ESC"
cv2.waitKey(0)
cv2.destroyAllWindows()     #Press escape to exit the program



