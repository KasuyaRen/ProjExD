import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event): # 練習3
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END, num) # 練習5


def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res) # 練習7

def click_sakujo(event):
    entry.delete(0, tk.END)
    
def click_modoru(event):
    a = len(entry.get())-1
    entry.delete(a,tk.END)



root = tk.Tk() # 練習1
root.geometry("280x605")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right") # 練習4
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0 # r: 行を表す変数／c：列を表す変数
numbers = list(range(9, -1, -1)) # 数字だけのリスト
operators = ["+"] # 演算子だけのリスト
operators2 = ["-"]
operators3 = ["/"]
operators4 = ["*"]
for i, num in enumerate(numbers+operators+operators2+operators3+operators4, 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2,bg='pink2')
    btn.bind("<1>", click_number)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

btn = tk.Button(root, text=f"=", font=("", 30), width=4, height=2)
btn.bind("<1>", click_equal)
btn.bind("<3>",click_sakujo)
btn.bind("<2>",click_modoru)
btn.bind("<Double-1>",click_modoru)
btn.grid(row=r, column=c)

root.mainloop()