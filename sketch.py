import cv2

#Get the image location and the image file name
img_location = "C:/Users/anura/Downloads/OneDrive/Desktop/Python Project"
filename= "Anuradha.jpg"

#Read the image
img = cv2.imread(img_location+filename)

#show the image
cv2.imshow('Original Image',img)
cv2.waitKey(0)