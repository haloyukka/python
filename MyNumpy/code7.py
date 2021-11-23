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