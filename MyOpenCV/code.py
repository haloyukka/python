import cv2

# 画像の読み込み
img = cv2.imread('lena.jpg', 1)
print(img)

cv2.imshow('windows-name', img)
cv2.imwrite('output.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()