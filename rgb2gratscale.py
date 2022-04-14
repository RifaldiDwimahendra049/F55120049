import cv2

img = cv2.imread("330px-F55120049-(test_image).png")
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)


cv2.imshow("Citra Rifaldi RGB",img)
cv2.imshow("Citra Rifaldi Grayscale",gray)

cv2.waitKey(0)
cv2.destroyAllWindows()