import cv2
import numpy as np


# 定数定義
FILE_ORG = "img.png"
FILE_GRAY = "gray.png"
FILE_GRADIENT = "gradient.png"
FILE_HIGH_PASS = "highpass.png"
FILE_LAPLACIAN_3x3 = "laplacian3x3.png"
FILE_LAPLACIAN_5x5 = "laplacian5x5.png"
FILE_GAUSSIAN = "gaussian.png"
FILE_GRADIENT_3x3 = "gradient3x3.png"
FILE_GRADIENT_5x5 = "gradient5x5.png"

FILE_SOBEL_3x3 = "sobel3x3.png"
FILE_SOBEL_Y5x5 = "sobelY5x5.png"
FILE_SOBEL_X5x5 = "sobelX5x5.png"

# 元の画像を読み込む
img_org = cv2.imread(FILE_ORG, cv2.IMREAD_COLOR)

# グレースケール変換
# グレスケ別関数用：
img_gray = cv2.cvtColor(img_org, cv2.COLOR_BGR2GRAY)
cv2.imwrite(FILE_GRAY, img_gray)

# グラディエント フィルタ（３ｘ３）
kernel_gradient_3x3 = np.array([
                            [ 1,  1,  1],
                            [ 0,  0,  0],
                            [-1, -1, -1]
                            ], np.float32)
img_gradient_3x3 = cv2.filter2D(img_gray, -1, kernel_gradient_3x3)
cv2.imwrite(FILE_GRADIENT_3x3, img_gradient_3x3)

# グラディエント フィルタ（５ｘ５）
kernel_gradient_5x5 = np.array([
                            [ 5,  5,  5,  5,  5],
                            [ 3,  3,  3,  3,  3],
                            [ 0,  0,  0,  0,  0],
                            [-3, -3, -3, -3, -3],
                            [-5, -5, -5, -5, -5]
                            ], np.float32)
img_gradient_5x5 = cv2.filter2D(img_gray, -1, kernel_gradient_5x5)
cv2.imwrite(FILE_GRADIENT_5x5, img_gradient_5x5)

# ハイパス フィルタ
kernel_high_pass = np.array([
                            [-1, -1, -1],
                            [-1,  8, -1],
                            [-1, -1, -1]
                            ], np.float32)
img_high_pass = cv2.filter2D(img_gray, -1, kernel_high_pass)
cv2.imwrite(FILE_HIGH_PASS, img_high_pass)

# ラプラシアン フィルタ（３×３）
kernel_laplacian_3x3 = np.array([
                            [1,  1, 1],
                            [1, -8, 1],
                            [1,  1, 1]
                            ], np.float32)
img_laplacian_3x3 = cv2.filter2D(img_gray, -1, kernel_laplacian_3x3)
cv2.imwrite(FILE_LAPLACIAN_3x3, img_laplacian_3x3)

# ラプラシアン フィルタ（５ｘ５）
kernel_laplacian_5x5 = np.array([
                            [-1, -3, -4, -3, -1],
                            [-3,  0,  6,  0, -3],
                            [-4,  6, 20,  6, -4],
                            [-3,  0,  6,  0, -3],
                            [-1, -3, -4, -3, -1]
                            ], np.float32)
img_laplacian_5x5 = cv2.filter2D(img_gray, -1, kernel_laplacian_5x5)
cv2.imwrite(FILE_LAPLACIAN_5x5, img_laplacian_5x5)

# ガウシアン フィルタ
kernel_gaussian = np.array([
                            [1,  2, 1],
                            [2,  4, 2],
                            [1,  2, 1]
                            ], np.float32) / 16
img_gaussian = cv2.filter2D(img_gray, -1, kernel_gaussian)
cv2.imwrite(FILE_GAUSSIAN, img_gaussian)

# ソーベル フィルタ（３ｘ３）
kernel_sobel_3x3 = np.array([
                            [ 1,  2,  1],
                            [ 0,  0,  0],
                            [-1, -2, -1]
                            ], np.float32)
img_sobel = cv2.filter2D(img_gray, -1, kernel_sobel_3x3)
cv2.imwrite(FILE_SOBEL_3x3, img_sobel)

# ソーベル フィルタY方向（5x5） frComp 垂直に偏微分
# 前準備のグレースケールの変換方法がボードと違う。グレースケール用の別関数を用意する。
# というかそもそもフィルタの適用方法が違う？
# X方向、Y方向のsobelフィルタをsrcに対して個別にかける -> で？
kernel_sobel_Y5x5 = np.array([
                            [ 1,  4,   6,  4,  1],
                            [ 2,  8,  12,  8,  2],
                            [ 0,  0,   0,  0,  0],
                            [-2, -8, -12, -8, -2],
                            [-1, -4,  -6, -4, -1]
                            ], np.float32)
img_sobelY = cv2.filter2D(img_gray, -1, kernel_sobel_Y5x5)
cv2.imwrite(FILE_SOBEL_Y5x5, img_sobelY)

# ソーベル フィルタX方向（5x5） frComp 水平に偏微分
# Intensity = absolute(垂直に偏微分^2 + 水平に偏便分 ^ 2)
# 上記で輝度計算
kernel_sobel_X5x5 = np.array([
                            [ 1,  2,  0,  -2, -1],
                            [ 4,  8,  0,  -8, -4],
                            [ 6, 12,  0, -12, -6],
                            [ 4,  8,  0,  -8, -4],
                            [ 1,  2,  0,  -2, -1]
                            ], np.float32)
img_sobelX = cv2.filter2D(img_gray, -1,kernel_sobel_X5x5)
cv2.imwrite(FILE_SOBEL_X5x5, img_sobelX)

# 上記処理をpythonでクラス化、関数化する。