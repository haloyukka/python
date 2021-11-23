import numpy as np
b = np.array([2, 4, 6, 8])
# 通常
print(f'array : {b}')

# ndim属性は、階数を返す
print(f'階数 : {b.ndim}')

# 配列内の値の総数は、sizeから得られる
print(f'配列内の値の総数 : {b.size}')

# 各階の値の数は、shapeから得られる
print(f'各階の値の数 : {b.shape}')