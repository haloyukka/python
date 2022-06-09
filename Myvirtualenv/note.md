# 目的
virtualenvは、pipとともに使われることが多いプログラムで、既存のPythonパッケージとの相互干渉を防ぐために使用する。指定したディレクトリ（フォルダに）にPythonパッケージをインストールする。<br>

# 概要
venv：Python 3.3から標準で組み込まれている<br>
※Python 3.3以降ならインストール不要

URL<br>
公式<br>
https://docs.python.org/ja/3/library/venv.html

# 使用方法
1. インストールされているパッケージを表示
```
pip list
```

2. プロジェクトのディレクトリへ移動
```
cd <<対象プロジェクト>>
```

3. venvで仮想環境の作成
```
python -m venv <<作成する仮想環境の名前>>
```

4. 仮想環境の実行

|プラットフォーム|シェル|仮想環境を有効化するためのコマンド|
|---|---|---|
|POSIX|ash/zsh|$ source <venv>/bin/activate|
|POSIX|fish|$ source <venv>/bin/activate.fish|
|POSIX|csh/tcsh|$ source <venv>/bin/activate.csh|
|POSIX|PowerShell Core|$ <venv>/bin/Activate.ps1|
|Windows|cmd.exe|C:\> <venv>\Scripts\activate.bat|
|Windows|PowerShell|PS C:\> <venv>\Scripts\Activate.ps1|

5. pythonのバージョンを確認する
```
python -V
```

6. インストールされているパッケージを確認する
```
pip list
```

7. 仮想環境の終了
```
deactivate
```

8. 仮想環境の削除<br>
作成した仮想環境のフォルダをゴミ箱に入れて削除