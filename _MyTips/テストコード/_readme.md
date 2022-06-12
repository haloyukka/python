【Pythonプログラミング入門】テストコードの書き方を解説！(pytest) 〜VTuberと学習〜 【初心者向け】
https://www.youtube.com/watch?v=Hl8UNYrp0Vg


# ◆ 手順
## pytestのインストール
pip install pytest

testsディレクトリに移動
pytest [実行コード]

## テストコードの書き方から実行まで
srcというディレクトリにテストしたいコードがあるとする。<br>
1. srcと同階層に`tests`というディレクトリを作成し、テストコードを記述するファイルを用意する<br>
2. `tests`ディレクトリに`__init__.py`を用意する。
<br>
このコードがないとテストの実施でエラーになる。<br>

3. 記述例<br>
```Python
# テストしたいコードをインポートする
from src import code

def test_sum_numbers():
    result = code.sum_numbers(1, 2)
    assert result == 3 # assertのあとに条件を記述する。Trueになる条件（期待した通りの値）を記述。
```

4. 実行方法<br>
4-1. testsディレクトリに移動<br>
4-2. pytest [実行コード]<br>
例： pytest test_code.py

