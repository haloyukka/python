# python
Pythonドキュメント<br>
https://docs.python.org/ja/3/

Python標準ライブラリ<br>
https://docs.python.org/ja/3/library/index.html

Python入門<br>
https://atmarkit.itmedia.co.jp/ait/articles/1904/02/news024.html

グラフ化サンプルコード<br>
https://www.data-to-viz.com/#bubble

# ライブラリ一覧

|  ライブラリ名称  |  概要  |  URL  |  GitHub  |
| ---- | ---- | ---- | ---- |
|  jupyter  |  ブラウザベースの対話形式エディタ  | https://jupyter.org/ |https://github.com/jupyterlab/jupyterlab|
|  pandas  |  数表および時系列データを操作するためのデータ構造と演算  | https://pandas.pydata.org/docs/# |https://github.com/pandas-dev/pandas|
|  numpy  |  基本的な科学計算  | https://numpy.org/ |https://github.com/numpy/numpy|
|  scipy  |  数学、科学、工学のための数値解析  | https://www.scipy.org/ |https://github.com/scipy/scipy|
|  openpyxl  |  excelファイルの読み書き  | https://openpyxl.readthedocs.io/en/stable/ |https://foss.heptapod.net/openpyxl/openpyxl|
|  matplotlib  |  高品質な図形を生成  | https://matplotlib.org/ |https://github.com/matplotlib/matplotlib|
|  seaborn  |  統計的グラフを作成  | https://seaborn.pydata.org/ |https://github.com/mwaskom/seaborn|
|  scikit-learn  |  様々な機械学習のアルゴリズム  | https://scikit-learn.org/stable/ |https://github.com/scikit-learn/scikit-learn|
|  statsmodels  |  様々な統計解析の手法  | https://www.statsmodels.org/stable/index.html |https://github.com/statsmodels/statsmodels|
|  tensorflow  |  Googleが開発した深層学習フレームワーク  | https://www.tensorflow.org/ |https://github.com/tensorflow/tensorflow|
|  keras  |  TD  | https://keras.io/ja/ |https://github.com/keras-team/keras|
|  gensim  |  自然言語処理  | https://radimrehurek.com/gensim/ |https://github.com/RaRe-Technologies/gensim|
|  pillow  |  画像処理  | https://pillow.readthedocs.io/en/stable/ |https://github.com/python-pillow/Pillow|
|  kivy  |  GUI  | https://kivy.org/#home |https://github.com/kivy/kivy|



# Pythonライブラリ
- Transformers
    - Transformersとは、最先端の自然言語（テキスト）処理を行うためのライブラリ
    - Transformersでできること
        - 分類
        - テキスト生成
        - 質疑応答
        - 要約
        - 翻訳 etc...
    - BERT, GPT-2などの最先端アルゴリズムに対応
    - https://huggingface.co/transformers/
- MediaPipe
    - MediaPipeとは、Google社が提供するストリーミングメディア（動画等）を利用した学習パイプラインを構築するためのフレームワーク
        - 機械学習パイプラインとは、データ収集→データ処理→モデル（再）学習→再学習済モデルによる推論、といった一連の処理を自動化したシステム
    - 顔の形状推定、顔検出、ハンドトラッキング、物体検出等における高精度なモデルを提供。高精度。
    - メディア周りの機械学習を実装した→MediaPipe
    - https://google.github.io/mediapipe/
- PyCaret
    - PyCaretは、たった数行で機械学習を実装できるライブラリであり、機械学習の一連の処理を自動化する「AutoML」をサポートしている
    - データの前処理自動化、モデル（アルゴリズム）の比較自動化、チューニングの自動化などを行ってくれる超便利最強ライブラリ
    - https://pycaret.org/
- FastAPI
    - FastAPIとは、Pythonの標準である型ヒントに基づいてPython3.6以降でAPIを構築するための、モダンで、高速（高パフォーマンス）な、Webフレームワーク
    - コードが直感的でわかりやすい、公式ドキュメンの情報が豊富、自動ドキュメント生成機能、バリデーション（検証）機能の実装が簡単という特徴があります
    - 初学者が、PythonでAPI開発を行うには間違いなくFastAPI一択
    - https://fastapi.tiangolo.com/ja/
- SQLModel
    - SQLModelとは、データベースを操作するためのライブラリであり、型ヒントに基づき、PydanticとSQLAlchemyを利用している
    - 直感的で使いやすく、互換性が高く、堅牢であるように設計されている
    - 比較的新しいライブラリであるが、FastAPI開発者が開発しており、FastAPIの使いやすさ、素晴らしさからも期待
    - https://sqlmodel.tiangolo.com/

# 標準ライブラリ  
数学関数  
https://docs.python.org/ja/3/library/math.html  
## math.floor(x)：切り捨て  
x の「床」 (x 以下の最大の整数) を返します。 x が浮動小数点数でなければ、内部的に x.__floor__() が実行され、 Integral 値が返されます。  
## math.ceil(x)：切り上げ  
x の「天井」 (x 以上の最小の整数) を返します。 x が浮動小数点数でなければ、内部的に x.__ceil__() が実行され、 Integral 値が返されます。  
