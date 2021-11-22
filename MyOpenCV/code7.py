import cv2
import numpy as np

img = cv2.imread('lena.jpg')

edges = cv2.Canny(img, 100, 200) # エッジ抽出

cv2.imshow('edge', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
