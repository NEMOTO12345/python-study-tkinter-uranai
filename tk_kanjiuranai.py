import tkinter as tk
import random as r

uranai = ['大吉','吉','凶']
# uranai = {'羊':'ひつじ','天秤':'てんびん','蟹':'かに'}
katakana = ['ダイキチ','キチ','キョウ']
root = tk.Tk()
root.title('windowのタイトル')
root.minsize(400,300)

static1 = tk.Label(text='test')
static1.pack()

static2 = tk.Label(text='名前を入力してね↓')
static2.pack()
entry1 = tk.Entry(width=40)
entry1.pack()

static3 = tk.Label(text='今日の運勢')
static3.pack()
entry2 = tk.Entry(width=40)
entry2.pack()


static4 = tk.Label(text='読み')
static4.pack()
entry3 = tk.Entry(width=40)
entry3.pack()
num = 0

#問題表示
def get_entry(event):
    num = r.randint(0,2)
    q = uranai[num]
    entry_value = entry1.get()
    op = f'{entry_value}さんの運勢はは「{q}」です。'
    entry2.delete(0,tk.END)
    entry2.insert(tk.END,op)
    a = katakana[num]
    qa = entry_value + "," + q + "," + a + "\n"
    with open("data/user.csv", "w") as f:
        f.write(qa)


        


def get_yomi(event):
    user_file = open("data/user.csv","r")
    #何で作ったデータかわからないからencodingをつける
    entry_value = entry1.get()
    for line in user_file:
        a = line.strip().split(",")
        if a[0] == entry_value:
            entry3.delete(0,tk.END)
            entry3.insert(tk.END,f"「{a[1]}」は「{a[2]}」と読みます。") 

button1 = tk.Button(text='占う')
button1.bind('<1>',get_entry)
button1.pack()

button2 = tk.Button(text='読み（カタカナ）')
button2.bind('<1>',get_yomi)
button2.pack()


root.mainloop()