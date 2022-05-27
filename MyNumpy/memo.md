NumPy
https://numpy.org/

# NumPy
NumPy( https://numpy.org/ )は、科学者の間でPythonが人気を集めている大きな理由の一つだ。Pythonなどの動的言語は、Cのようなコンパイル言語、さらにはJavaのようなインタープリタ言語と比べても遅いと言われている。NumPyは、FORTRANのような科学言語と同じように高速な多次元数値配列を提供するために作られた。CのスピードとPythonのデベロッパーにとっての使いやすさが結合しているのだ。  

Scientific Pythonディストリビューションのどれかをダウンロードしていれば、すでにNumPyは含まれている。そうでなければ、NumPyのダウンロードページ(https://www.scipy.org/download/)の指示にしたがってダウンロードしよう。  
NumPyを使うためには、ndarray(N-dimentional array=N次元配列という意味)、あるいは略してただarrayと呼ばれる基本データ構造を理解する必要がある。Pythonのリスト、タプルとは異なり、`個々の要素は同じ型でなければならない`。NumPyは、配列の次元数を`階数(rank)`と呼ぶ。１次元配列は値の行のようになり、２次元配列は値の行列のようになる。３次元配列はルービックキューブのようになる。各次元での長さは同じでなくてかまわない。

NumPyのarrayと標準Pythonのarrayは別のものだ。

しかし、なぜ配列が必要なのだろうか？  
- 科学的データは、大規模なデータシーケンスから構成されることが多い

- このようなデータに対する科学計算は、行列演算、回帰、シミュレーション、その他一度に多数のデータポイントを処理するテクニックを使うことが多い
- NumPyはPython標準リスト、タプルよりも非常に高速に配列を処理する

NumPy配列にはさまざまな作り方がある。

# array()による配列の作成
```Python
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
```

# arange()による配列の作成
```Python
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
```

# zeros(), ones(), random()による配列の作成
zeros()メソッドは、全ての値がゼロになっている配列を返す。引数として配列の形を指定するタプルを渡せる。
```Python
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
```

# reshape()による配列形状の変更
今までは、配列にリストやタプルの違いは感じられなかった。  
しかし、reshape()を使った形状の変更のようなトリックがあるところは、リストやタプルとは異なる。
```Python
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

```

# []による要素の取得
１次元配列は、リストと同じように動作する。
```Python
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
```

# 配列の数学演算
```Python
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
```

# 線形代数
NumPyには、線形代数のための関数が多数含まれている。  
次の連立１次方程式について考える  
4x + 5y = 20  
 x + 2y = 13  
```Python
import numpy as np
coefficients = np.array([[4, 5], [1, 2]])
dependents = np.array([20, 13])

# linalgモジュールのsolve()関数を使う
answers = np.linalg.solve(coefficients, dependents)
print(f'answer : {answers}')

# 結果を見ると、xはおおよそ-8.3、yはおよそ10.6 となっている。  
# これらの値で方程式は解決するだろうか
print(f'4 * answers[0] + 5 * answers[1] = {4 * answers[0] + 5 * answers[1]}')
print(f'1 * answers[0] + 2 * answers[1] = {1 * answers[0] + 2 * answers[1]}')


# NumPy配列のドット積を計算させれば、この大量の入力は避けられる
product = np.dot(coefficients, answers)
print(f'product : {product}')

# この解が正しければ、product配列の値は、dependentsのなかの値と非常に近くなっているはずだ。
# allclose()関数を使えば、ふたつの配列がほぼ等しいかどうかをチェックできる
# 浮動小数点数の丸め誤差のために、両者ぴったりと一致しない場合がある
print(f'np.allclose(product, dependents) = {np.allclose(product, dependents)}')
```
NumPyには、多項式、フーリエ変換、統計、確率分布のためのモジュールもある。
