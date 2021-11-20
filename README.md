# python

# ライブラリ一覧

|  ライブラリ名称  |  概要  |  URL  |
| ---- | ---- | ---- |
|  jupyter  |  ブラウザベースの対話形式エディタ  | https://jupyter.org/ |
|  pandas  |  数表および時系列データを操作するためのデータ構造と演算  | https://pandas.pydata.org/docs/# |
|  numpy  |  基本的な科学計算  | https://numpy.org/ |
|  scipy  |  数学、科学、工学のための数値解析  | https://www.scipy.org/ |
|  openpyxl  |  excelファイルの読み書き  | https://openpyxl.readthedocs.io/en/stable/ |
|  matplotlib  |  高品質な図形を生成  | https://matplotlib.org/ |
|  seaborn  |  統計的グラフを作成  | https://seaborn.pydata.org/ |
|  scikit-learn  |  様々な機械学習のアルゴリズム  | https://scikit-learn.org/stable/ |
|  statsmodels  |  様々な統計解析の手法  | https://www.statsmodels.org/stable/index.html |
|  tensorflow  |  Googleが開発した深層学習フレームワーク  | https://www.tensorflow.org/ |
|  keras  |  TD  | https://keras.io/ja/ |
|  gensim  |  自然言語処理  | https://radimrehurek.com/gensim/ |
|  pillow  |  画像処理  | https://pillow.readthedocs.io/en/stable/ |


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

