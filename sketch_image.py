import cv2
import numpy as np

img=cv2.imread(r'C:/Users/anura/Downloads/OneDrive/Desktop/Python Project/Anuradha.jpg',cv2.IMREAD_COLOR)

cv2.imshow('original image',img)
cv2.waitkey(2000)