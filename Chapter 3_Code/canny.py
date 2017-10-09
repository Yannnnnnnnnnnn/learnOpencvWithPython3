import cv2
import numpy as np

img = cv2.imread("lena.bmp", 0)
cv2.imwrite("canny.jpg", cv2.Canny(img, 512, 512))
cv2.imshow("canny", cv2.imread("canny.jpg"))
cv2.waitKey()
cv2.destroyAllWindows()
