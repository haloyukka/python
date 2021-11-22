# OpenCVのレポジトリで公開されているサンプル画像
https://github.com/opencv/opencv/tree/master/samples/data 

# OpenCVについて
「Open CV」とは、Open Source Computer Vision Libraryの略で、`画像や動画を処理するための機能がまとめて実装されているオープンソースのライブラリ`です。

元々はC/C++で動作するライブラリでしたがPythonでも使用できるようになっています。

PythonでOpenCVを使用するメリットとしては、

- コードが短くてよみやすい
- コードの可読性が良く本格的な画像処理が可能
- 周辺ライブラリパッケージが充実しており、scipyやnumpyなどの他のライブラリと組み合わせやすい
- エラーの原因を特定しやすい

といったことがあげられます

# OpenCVのインストール方法
Windows  
```
pip install opencv – python
```

# OpenCVの機能
1. 画像の読み込み・表示
2. 画像の作成・保存
3. 画像のトリミング・リサイズ・重ね合わせ
4. 画像の回転・上下反転・左右反転
5. グレースケール変換・色チャンネル分析・減色処理
6. モザイク処理・マスク処理・2枚の画像を合成
7. 図形の描画・文字の描画
8. ノイズ除去・平滑化・ぼかしフィルタ・メディアンフィルタ・ガウシアンフィルタ
9. 物体検出
10. テンプレートマッチング

## 画像の読み込み
画像を読み込むには「cv2.imread()」を使用します。  

第2引数は画像の読み込み方法を指定するためのフラグで次用な意味があります。
- cv2.IMREAD_COLOR : カラー画像として読み込み、画像の透過度は無視される
- cv2.IMREAD_GRAYSCALE : グレースケール画像として読み込む
- cv2.IMREAD_UNCHANGED : アルファチャンネルも含めた画像として読み込む

これらのフラグを使用する代わりに、上から1, 0, -1の整数値を与えて指定することもできる。
```Python
import cv2

# 画像の読み込み
img = cv2.imread('ファイル名', 1)
```
画像ファイルのパスが間違っていてもエラーにはならないが、print(img)時の実行結果が「None」となる。

## 画像の表示
画像を`ウィンドウ上に表示するためには「cv2.imshow()」を使用`します。ウィンドウサイズは自動的に画像サイズに合わせられる。

```Python
cv2.imshow('window-name', img)
cv2.waitKey(0)
cv2.destroyAllwindows()
```
複数個のウィンドウを表示することは可能ですが、`各ウィンドウには異なる名前を付ける必要があります。`

## 画像の保存
`画像を保存するには「cv2.imwrite()」を使用`します。
```Python
# 第1引数は画像のファイル名、第2引数は保存したい画像
cv2.imwrite('ファイル名', img)
```

# 画像のトリミング・リサイズ
画像のトリミング方法は以下のようになっています。
```Python
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
```

# 画像のサイズ変更
`画像のサイズ変更を行うには「cv2.resize()」を使用`します
```Python
import cv2
import numpy as np

img = cv2.imread('lena.jpg')

res = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

height ,width = img.shape[:2]
res = cv2.resize(img, (2*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.imwrite('code3.jpg',res)
```
- cv2.INTER_AREA : 縮小
- cv2.INTER_CUBIC : 拡大
- cv2.INTER_LINEAR : 拡大

# 顔を検出
```Python
import numpy as np
import cv2

# Haar - like特徴分類機の読み込み
face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

# イメージファイルの読み込み
img = cv2.imread('lena.jpg')
# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # 検知した顔を囲む
    roi_gray = gray[y:y+h, x:x+w] # 顔画像/グレースケール
    roi_color = img[y:y+h, x:x+w] # 顔画像/カラースケール
    eyes = eye_cascade.detectMultiScale(roi_gray) # 顔の中から目を検知
    
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2) # 検知した目を囲む
        
# 画像を表示
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
# 円の検出
`円の検出には「cv2.HoughCircles()」を使用`します
```Python
import cv2
import numpy as np

img = cv2.imread('img/detect_blob.png', 0)
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=500, param2=30, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg, (i[0], i[1]), i[2], (0,255,0), 2)
    # draw the center of the circle
    cv2.circle(cimg, (i[0], i[1]), 2, (0,0,255),3)

cv2.imshow('detected circles', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows
```
cv2.HoughCircles()で指定している`引数「param1」の値を小さくすると、より多くの円が検出`されるようになる。

# 輪郭の検出
```Python
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
```
「cv2.RETR_EXTERNAL」を指定すると輪郭を圧縮して冗長な点の情報を取り除き、メモリの使用を抑えることが可能。

# Canny法によるエッジの検出
```Python
import cv2
import numpy as np

img = cv2.imread('lena.jpg')

edges = cv2.Canny(img, 100, 200) # エッジ抽出

cv2.imshow('edge', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

# 画像のヒストグラムを求める
```Python
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
```
`画像のヒストグラムを求めるには「cv.calcHist()」を使用`します。  
画像のヒストグラムでは横軸に明るさの階調、縦軸にピクセル数をR・G・Bのチャンネルごとに表示します。

# まとめ
- OpenCVとは画像・動画を処理するためのオープンソースのライブラリ
- 画像の読み込みにはcv2 . imread( )を使用
- 画像の表示にはcv2 . imshow( )
- 画像の保存にはcv2 . imwrite( )を使用
- 顔の検出にはcv2 . CascadeClassifier( )を使用
- 円の検出にはcv2 . HoughCircles( )を使用
- 輪郭の検出にはcv2 . findContours( )を使用
- Canny法でエッジを検出するにはcv2 . Canny( )を使用
- 画像のヒストグラムを求めるにはcv . calcHist( )を使用
- しっかり押さえておきましょう。