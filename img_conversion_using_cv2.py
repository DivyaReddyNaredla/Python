import cv2

img = "ibm.png"
img1 = cv2.imread(img)
cv2.imwrite("ibm2.jpg",img1)
