import tkinter as tk
import random as r

uranai = ['大吉','吉','凶']

root = tk.Tk()
root.title('windowのタイトル')
root.minsize(400,300)

static1 = tk.Label(text='test')
static1.pack()

entry1 = tk.Entry(width=40)
entry1.pack()

entry2 = tk.Entry(width=40)
entry2.pack()

def get_entry(event):
    kekka = r.choice(uranai)
    entry_value = entry1.get()
    op = f'{entry_value}さんの結果は{kekka}です。'
    # print(entry_value,kekka)
    entry2.delete(0,tk.END) #一行テキストボックスの場合
    # entry2.delete('1.0', 'end') #複数行テキストボックスの場合
    #「開始位置（1行目を小数型で）」,「終了位置（最後まで）」
    entry2.insert(tk.END,op)


button = tk.Button(text='ボタン')
button.bind('<1>',get_entry)
button.pack()

root.mainloop()