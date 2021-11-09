Tkinderのwidget  
基底クラスの(Frame)のイニシャライザを呼ぶ  
```
class Application(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root
            width=420, height=320,
            borderwidth=4, relief='groove')
        self.pack() #位置を設定して配置する
        self.pack_propagate(0)
        self.root=root #別のクラスでも使用するためインスタンス変数に格納する
```

# ここからはフレームにいろんなアイテムを追加する
アイデア次第でいろんな形を作成できる。  

```
class Application(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root,
            width=420, height=320,
            borderwidth=4, relief='groove')
        self.pack() #位置を設定して配置する
        self.pack_propagate(0)
        self.root=root #別のクラスでも使用するためインスタンス変数に格納する
    def create_widgets(self):
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = '閉じる'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side='bottom')
```

# Tkinterのwidget
- Button
- Entry
- Radiobutton
- Message
- Checkbutton
- Text
- Listbox
- Spinbox

# app
| head1 | head2 |
| --- | --- |
| データが保存されないアプリ | データが保存されるアプリ |
| 電卓アプリ | スケジュールアプリ |
| --- | Tkinterならファイルに書き込んで保存 |