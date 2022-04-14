import  cv2

img = cv2.imread("330px-F55120049-(test_image).png",0)

img_1= 255 - img

cv2.imshow("citra asli",img)
cv2.imshow("citra negatif",img_1)

cv2.waitKey(0)
cv2.destroyAllWindows()