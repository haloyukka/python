import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg') # 入力画像を読み込む
color = ('b', 'g', 'r')
for i, col in enumerate (color):
    histr = cv2.calcHist([img], [i], None, [256], [0,256]) # ヒストグラムの算出
    plt.plot(histr, color = col) # ヒストグラムの表示
plt.xlim([0, 256])
plt.show()
