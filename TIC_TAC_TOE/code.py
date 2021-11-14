import sys
import tkinter as tk
from tkinter import messagebox
import random

field = [
    ["0", "1", "2"],
    ["3", "4", "6"],
    ["7", "8", "9"]
]

turn = 0

def print_field(filed):
    for i in field:
        print(i)

# print_field(field)

'''
縦横ナナメ判定
同じ文字が並んでいたら、その文字を返す
並んでいなかったら、0を返す
'''
def judge(field):
    for x in field:
        if x[0] == x[1] and x[1] == x[2]:
            return x[0]
        for y in range(3):
            if field[0][y] == field[1][y] and field[1][y] == field[2][y]:
                return field[0][y]
        if field[0][0] == field[1][1] and field[1][1] == field[2][2]:
            return field[0][0]
        if field[0][2] == field[1][1] and field[1][1] == field[2][0]:
            return field[0][2]
        return 0

def click_btn(btn):
#     pass
    global turn, field
    
    select_place = list(btn.widget._name)
    
    #varsでどんなメンバがあるか参照できる。
#     print(vars(btn.widget))
    if field[int(select_place[0])][int(select_place[1])] not in ["○", "✕"]:
        field[int(select_place[0])][int(select_place[1])] = "○"
    else:
        tk.messagebox.showinfo("ゲームマスター","そこには置けません")
    
    btn.widget["text"] = "○"
    btn.widget["fg"] = "#ffffff"
    turn += 1
    
    if judge(field):
        tk.messagebox.showinfo("ゲームマスター","あなたの勝ちです！")
        root.destroy()
        sys.exit()
    if turn == 5:
        tk.messagebox.showinfo("ゲームマスター","引き分けです")
        root.destroy()
        sys.exit()

    tk.messagebox.showinfo("ゲームマスター","相手の番です。")
    while True:
        x = random.randint(0,2)
        y = random.randint(0,2)
        if field[x][y] != "○" and field[x][y] != "✕":
            field[x][y] = "x"
            select_place = str(x+1)+"/"+str(y+1)
            btn_idx = x+y*3
            btns[btn_idx]["text"] = "✕"
            break
        tk.messagebox("ゲームマスタ","相手が["+ select_place+"]に置きました")
        if judge(field):
            tk.messagebox.showinfo("ゲームマスター","あなたの負けです...")
            root.destroy()
            sys.exit()
        tk.messagebox.showinfo("ゲームマスター","あなたの番です")
            
    
root = tk.Tk()
root.title("○✕")
root.configure(bg="gray30")

# btn = tk.Button(root, text="aaaaa")
# btn.place(x=10, y=10)
btns = []
for y in range(3):
    for x in range(3):
        btn_place = str(x)+str(y)
#         print(btn_place)
        btns.append(tk.Button(root, text="", name=btn_place))
        btns[x+y*3].place(x=x*50+20, y=y*50+135,width=50, height=50)
        btns[x+y*3].configure(bg="gray50")
# print(btns)

meu_img = tk.PhotoImage(file="meu01.png",master=root) #ここtk.PhotoImageの引数としてmasterを指定する必要があって、その画像を表示するwidgetが格納される、rootなりframeなりを master=root のように明示すると解決した。
board_img = meu_img.subsample(2)
meu = tk.Label(root, image=board_img)
meu.place(x=0, y=15, height=110)

#bind <1>は左クリックのこと
root.bind("<1>", click_btn)

root.geometry("200x300")
root.mainloop()