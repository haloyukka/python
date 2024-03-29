import numpy as np
import cv2
im = cv2.imread('lena.jpg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 107, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(im, contours, -1, (0, 0, 255), 3) # 全輪郭を描画
cv2.imshow('im', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
