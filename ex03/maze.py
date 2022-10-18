#git add ex03/maze.py
#git commit -m "ooooo"

import tkinter as tk
import tkinter.messagebox as tkm


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    #練習２
    canv = tk.Canvas(root, width= 1500, height=900, bg= "black")
    canv.pack()

    tori =tk.PhotoImage(file = "fig/5.png")

    cx, cy = 300,400
    canv.create_image(cx.cy,image = tori,tag = "tori")

    key = ""

    root.mainloop()


