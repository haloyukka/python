#

アプリケーションを本番環境にデプロイする際に
`pip install fastapi

サーバーとして動作するように`uvicorn`をインストールする
`pip install uvicorn[standard]

`main.py`
```Python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

ライブサーバーを実行
```
uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
`uvicorn main:app`は以下の通り  
- `main`:`main.py`ファイル（Python "module")
- `app`:`main.py`内部で作られるobject(app = FastAPI()のように記述される)
- `--reload`:コードの変更時にサーバーを再起動させる。開発用。

出力に以下のように行がある
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```
ブラウザで`http://127.0.0.1:8000`を開く