import os
import cv2
import numpy as np

directory = 'input'
outputdirectory = 'output'
kernel3by3 = np.ones((3,3),np.uint8)
kernel5by5 = np.ones((5,5),np.uint8)

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    img = cv2.imread(f)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    thresh,blackAndWhiteImage = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    blackAndWhiteImage = cv2.bitwise_not(blackAndWhiteImage)
    eroded = cv2.erode(blackAndWhiteImage, kernel3by3)
    dilated = cv2.dilate(eroded, kernel5by5)
    if (not os.path.exists(outputdirectory)):
        os.mkdir(outputdirectory)
    cv2.imwrite(os.path.join(outputdirectory , filename), dilated)
