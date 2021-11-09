import tkinter
class Application(tkinter.Frame):
    def __init__(self, root=None):
        super().__init__(root,
            width=380, height=280,
            borderwidth=1, relief='groove')

        self.root = root        # 別のクラスでも使用するためインスタンス変数に格納する
        self.pack()             # 位置を設定して配置する
        self.pack_propagate(0)  # サイズを調整
        self.create_widgets()   # このクラスのメソッドをコール

    # このメソッドに部品を追加する
    def create_widgets(self):
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = '閉じる'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side='bottom')

        # テキストボックス
        self.text_box = tkinter.Entry(self)
        self.text_box['width'] = 10
        self.text_box.pack()

        # 実行ボタン
        submit_btn = tkinter.Button(self)
        submit_btn['text'] = '実行'
        submit_btn['command'] = self.input_handler
        submit_btn.pack()

        # メッセージの出力
        self.message = tkinter.Message(self)
        self.message.pack()

    def input_handler(self):
        text = self.text_box.get()
        self.message['text'] = text + '!!'


root = tkinter.Tk()
root.title('サプーアプリ')
root.geometry('400x300')
app = Application(root=root)
root.mainloop()
