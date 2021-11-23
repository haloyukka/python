import numpy as np

a = np.zeros((3,))
print(f'zeros() : {a}')

# ndim属性は、階数を返す
print(f'階数 : {a.ndim}')

# 配列内の値の総数は、sizeから得られる
print(f'配列内の値の総数 : {a.size}')

# 各階の値の数は、shapeから得られる
print(f'各階の値の数 : {a.shape}')

b = np.zeros((2, 4))
print(f'zeros() : {b}')

# ndim属性は、階数を返す
print(f'階数 : {b.ndim}')

# 配列内の値の総数は、sizeから得られる
print(f'配列内の値の総数 : {b.size}')

# 各階の値の数は、shapeから得られる
print(f'各階の値の数 : {b.shape}')

# 同じ値で配列を初期化する特殊関数 ones()
k = np.ones((3, 5))
print(f'ones() : {k}')

# random()は、0.0 から 1.0までの無作為な値を使って配列を作る
m = np.random.random((3, 5))
print(f'random() : {m}')