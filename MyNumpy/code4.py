import numpy as np

a = np.arange(10)
print(f'array : {a}')

a = a.reshape(2, 5)
print(f'reshape(2, 5) : {a}')

# ndim属性は、階数を返す
print(f'階数 : {a.ndim}')

# 配列内の値の総数は、sizeから得られる
print(f'配列内の値の総数 : {a.size}')

# 各階の値の数は、shapeから得られる
print(f'各階の値の数 : {a.shape}')


# 同じ配列を様々な形状に変更できる
a = a.reshape(5, 2)
print(f'array : {a}')

# ndim属性は、階数を返す
print(f'階数 : {a.ndim}')

# 配列内の値の総数は、sizeから得られる
print(f'配列内の値の総数 : {a.size}')

# 各階の値の数は、shapeから得られる
print(f'各階の値の数 : {a.shape}')

# shape に形状を指定するタプルを代入する方法でも、同じ結果が得られる。
a.shape = (2, 5)
print(f'a.shape = (2, 5 : {a}')

# 形状に関する制限は、各階のサイズの積が値の総数と同じでなければならないということだけだ（ここでは10）
# a = a.reshape(3, 4)
# # Traceback (most recent call last):
# #   File "c:\dev\python\MyNumPy\code4.py", line 37, in <module>
# #     a = a.reshape(3, 4)
# # ValueError: cannot reshape array of size 10 into shape (3,4)
