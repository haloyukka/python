import numpy as np
a = np.arange(10)

# 通常
print(f'array : {a}')

# ndim属性は、階数を返す
print(f'階数 : {a.ndim}')

# 配列内の値の総数は、sizeから得られる
print(f'配列内の値の総数 : {a.size}')

# 各階の値の数は、shapeから得られる
print(f'各階の値の数 : {a.shape}')

# ２つの値を渡すと、最初の値から第２の値マイナス１までの配列が作られる
a = np.arange(7, 11)
print(f'引数7と11 : {a}')

# 第３引数として１以外のステップ数を指定できる
a = np.arange(7, 11, 2)
print(f'引数7と11 ステップ数2 : {a}')

# floatでも動作する
f = np.arange(2.0, 9.8, 0.3)
print(f'float(2.0-9.8 step:0.3) : {f}')

# dtype引数を指定すると、どの型の値を生成するかをarangeに指示できる
g = np.arange(10, 4, -1.5, dtype=np.float)
print(f'dtype=np.float : {g}')