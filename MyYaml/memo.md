# YAMLについて
構造化データやオブジェクトを文字列にシリアライズ（直列化）するためのデータ形式の一種  
語源  
YAML : YAML Ain't a Markup Language(→YAMLはマークアップ言語じゃない)

# 使うシーン
|JSON|YAML|
|---|---|
|システム間のデータの受け渡し(WebAPI)|設定ファイル、定義ファイル|
|JSONは書くのが面倒|JSONより簡単に記述可能|
|WebAPI|DBの接続先<br>ストレージのURL<br>APIの接続先|

# 環境構築
```Python
pip install pyyaml
```

yamlファイルの読み込み
```Python
import yaml

with open ('yamlファイルパス', 'r') as f:
    x = yaml.safe_load(f)

print(x)
```

# 扱えるデータ型
- シーケンス
- マップ（マッピング）
- スカラー

# シーケンス型
シーケンスは連続した数字の添字を持つ配列のことを指します。  
YAML
```YAML
- abc
- def
- 123
```
JSON
```JSON
["abc", "def", 123]
```

# マップ型
マップは添字を指定できる配列（連想配列）を指します。  
キーと値が対になっていて、値はスカラー、シーケンス、マップをとることができるため、構造が複雑になりやすい側面がある。  
YAML
```YAML
aaa: test1
bbb: test2
ccc: test3
ddd:
  eee: test4
  fff: test5
```
JSON
```JSON
{"abc": "test1", "bbb": "test2", "ccc": "test3", "ddd": {"eee": "test4", "fff": "test5"}}
```

# スカラー型
スカラーは数値や文字列、ブール値など、単一の値を指す。  
マップ、シーケンス以外のデータ型すべてがスカラー型とされている。  

YAML
```YAML
- 100                                       # number (10進数)
- 016                                       # number (8進数）
- 0xAC                                      # number (16進数)
- 3.14                                      # number (float)
- 12.3e+4                                   # number (指数)
- .inf                                      # number (+方向の無限大)
- -.inf                                     # number (-方向の無限大)
- true                                      # bool
- false                                     # bool
- on                                        # bool
- off                                       # bool
- yes                                       # bool
- no                                        # bool
- null                                      # null
- ~                                         # null
- test                                      # string
- 1980/09/02                                # string (注意)
- 1980-09-02 00:00:00.000-09:00             # datetime (ISO-8601 format)
- 1980-09-02                                # date (year, month, day)
- 1980                                      # date (year)
```

文字列が改行を含めた複数行のデータを持ち得るため、複数行のテキストデータを表現するための記述方法がいくつか用意されている。  
```YAML
# シンプルな改行を含めたテキスト
test1: |
  改行を含めたテキストが書けます。
  改行を含めたテキストが書けます。
```
```YAML
# 改行を半角スペースに置換する (データを取り出した時点では改行コードは存在しないことになる)
test2: >
  改行を含めたテキストが書けます。
  改行を含めたテキストが書けます。
```
```YAML
# 最終行の行末に改行コードを付ける
test3: |+
  改行を含めたテキストが書けます。
  改行を含めたテキストが書けます。
```
```YAML
# 最終行の行末に改行コードを付けない
test4: |-
  改行を含めたテキストが書けます。
  改行を含めたテキストが書けます。
```
```YAML
# 最終行の行末に改行コードを付ける (ただし、文中の改行については除去する)
test3: >+
  改行を含めたテキストが書けます。
  改行を含めたテキストが書けます。
```
```YAML
# 最終行の行末に改行コードを付けない
test4: >-
  改行を含めたテキストが書けます。
  改行を含めたテキストが書けます。
```
```YAML
# 各行頭に2つのスペースを入れる
test1: |2
  改行を含めたテキストが書けます。
  改行を含めたテキストが書けます。
```
```YAML
# 各行頭に4つのスペースを入れる
test1: |4
    改行を含めたテキストが書けます。
    改行を含めたテキストが書けます。
```
## ネストについて
```YAML
# シーケンス同士のネスト
- aaa
- bbb
- ccc
  - ddd
  - eee
  - fff
```
```YAML
# マップ同士のネスト
aaa: test1
bbb: test2
ccc:
  ddd: test3
  eee: test4
  fff: test5
```
```YAML
# シーケンスとマップのネスト
- aaa
- bbb
- ccc
  ddd: test1
  eee: test2
  fff: test3
```
```YAML
# マップとシーケンスのネスト
aaa: test1
bbb: test2
ccc:
  - ddd
  - eee
  - fff
```
```YAML
# 順序ありマップのネスト (インデントの数に注意)
- aaa: test1
- ccc: test2
- bbb:
    - ddd
    - eee
    - fff
```