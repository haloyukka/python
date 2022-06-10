import os
import itertools

# 定数
BASE = './'
DELIMITER = '/'

# ユーザー定義
LAYER_00 = ['dir','dir1','dir2']
LAYER_01 = ['000','001','010']
LAYER_02 = ['100','101','110']

# ディレクトリ構成の総当りリストを生成
l_p = list(itertools.product(LAYER_00,LAYER_01,LAYER_02))

for path in l_p:
    os.makedirs(BASE + DELIMITER.join(path))
