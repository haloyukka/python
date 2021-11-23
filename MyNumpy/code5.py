import numpy as np

a = np.arange(10)
print(f'array : {a}')
print(f'a[7] : {a[7]}')
print(f'a[-1] : {a[-1]}')

# 配列の形状が異なる場合には、カンマ区切りの添字を使う
a.shape = (2, 5)
print(f'array : {a}')
print(f'a[1,2] : {a[1,2]}')

# これはPythonの2次元リストとは異なる
l = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
print(f'Python 2D list : {l}')
# l[1,2]
# # Traceback (most recent call last):
# #   File "c:\dev\python\MyNumPy\code5.py", line 16, in <module>
# #     l[1,2]
# # TypeError: list indices must be integers or slices, not tuple

print(f'Python 2D list : {l[1][2]}')

# もうひとつ重要なポイント。スライスは使える。
# しかし、１セットしかない各かっこのなかで使わなければならない。
a = np.arange(10)
a = a.reshape(2, 5)
print(f'array : {a}')
# スライスを使って先頭行のオフセット2から末尾までの要素を取り出す
print(f'a[0, 2:] : {a[0, 2:]}')
# 最後の行の先頭からオフセット3-1=2までの要素を取り出す
print(f'a[-1, :3] : {a[-1, :3]}')
# スライスを使って複数の要素に値をまとめて代入することもできる。
# すべての行のオフセット2と3の列に1000という値を代入する
a[:, 2:4] = 1000
print(f'a[:, 2:4] = 1000 : {a}')