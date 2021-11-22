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
