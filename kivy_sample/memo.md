# 環境構築
```
pip install kivy  
```


windowを表示する  

```Python
import kivy.app from App

App().run()

```

コードのレイアウトを記述するとごちゃごちゃしてしまう。  
Kivyではレイアウトに関する情報などはKvファイル（拡張子.kv）にKivy Languageで書くことで設定することができます。  

kvファイルの作成  
ファイル名について  
TestApp(App)とtest.kv→赤文字のように一致させる必要がある。


