【PythonでWebアプリ作成】Flask入門 ！この動画１本でWebアプリが作れちゃう！ 〜 Pythonプログラミング初心者用 〜
https://www.youtube.com/watch?v=EQIAzH0HvzQ



Flaskを使用したWebアプリケーションサンプル
Flask:Webアプリケーションフレームワーク

Django
・Pythonでは一番有名
・備えられている機能が多い
・大きいWebアプリ

Flask
・必要最低限の機能
・小さいWebアプリ



・環境
Flask インストール
pip install flask

jinja2 インストール:HTMLにPythonのデータを埋め込むテンプレートエンジン
pip install jinja2

・フォルダ構成
C:.
│  exec.bat
│  readme.txt
│  tree.txt
│  
└─flaskr					★アプリ名：好きな名前でよい
    │  database.db
    │  db.py
    │  main.py
    │  __init__.py			★エントリー
    │  
    ├─static
    │      style.css
    │      
    └─templates			★HTML格納ディレクトリ。templatesとい名前を変更すると動作しない。
            form.html
            index.html


・FLASKアプリの起動方法
flaskrフォルダ（ソースコード類を格納したディレクトリ）と同じ階層まで移動する。

環境変数の登録（一時的）
・Mac(Bash)
export FLASK_APP=flaskr
export FLASK_ENV=development

・Windows(CMD)
set FLASK_APP=flaskr
set FLASK_ENV=development

・Windows(Powershell)
$env:FLASK_APP="flaskr"
$env:FLASK_ENV="development"

