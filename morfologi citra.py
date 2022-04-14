import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('330px-F55120049-(test_image).png')

karnel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,karnel,iterations=1)
dilation = cv2.dilate(img,karnel,iterations=1)

karnel1=np.ones((3,3),np.uint8)
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,karnel1)
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,karnel1)
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,karnel1)

cv2.imshow("citra asli",img)

cv2.imshow("erosion",erosion)

cv2.imshow("dilasi",dilation)

cv2.imshow("opening",opening)

cv2.imshow("clossing",closing)

cv2.imshow("gradient",gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()