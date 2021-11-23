from numpy import *
a = arange(4)

print(f'array : {a}')
# NumPyの再定義された演算(*)演算子を使用して、NumPy配列のすべての要素に同じ値を掛ける
a *= 3
print(f'a*=3 : {a}')

# Pythonの標準のリストの各要素に同じ値を掛けようと思ったら、ループか内包表記を使わなければならない。
plain_list = list(range(4))
print(f'plain_list : {plain_list}')

plain_list = [num * 3 for num in plain_list]
print(f'plain_list : {plain_list}')

# この一斉演算の動作は、加算、減算、除算など、NumPyライブラリの他の関数にも当てはまる
# たとえば、zeros()と+を使えば、配列のすべての要素を同じ値で初期化できる
a = zeros((2, 5)) + 17
print(f'array : {a}')