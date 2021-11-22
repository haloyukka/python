import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')

# 高さ
height = img.shape[0]
# 幅
width = img.shape[1]
# 高さ・幅を150pxずつ取り除く
trim_img = img[150: height, 150:width]

# matplotlibで表示する場合はRGBからBGRに変換
trim_img = cv2.cvtColor(trim_img, cv2.COLOR_RGB2BGR)
plt.imshow(trim_img)
plt.show()

