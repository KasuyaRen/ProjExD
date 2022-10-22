#git add ex03/maze.py
#git commit -m "ooooo"

import tkinter as tk
import maze_maker as mm #練習8


#練習5
def key_down(event):
    global key
    key = event.keysym

#練習6
def key_up(event):
    global key
    key = ""

#練習7
def main_proc():
    global mx, my
    global cx, cy
    if key == "w" or key == "Up":
        my -= 1
    if key == "s" or key == "Down":
        my += 1
    if key == "a" or key == "Left":
        mx -= 1
    if key == "d" or key == "Right":
        mx += 1
    if key == "r":
        mx, my = 1, 1

    if maze_lst[my][mx] == 0:
        cx, cy = mx*100+50, my*100+50
    else:
        if key == "w" or key == "Up":
            my += 1
        if key == "s" or key == "Down":
            my -= 1
        if key == "a" or key == "Left":
            mx += 1
        if key == "d" or key =="Right":
            mx -= 1        

    canv.coords("tori", cx, cy) 
    root.after(100, main_proc)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#練習1
    


    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()#練習2

    maze_lst = mm.make_maze(15,9)#練習9
    maze_up = mm.show_maze(canv, maze_lst)#練習10

    tori = tk.PhotoImage(file="fig/9.png")
    mx, my = 1, 1
    cx, cy = 300, 400
    canv.create_image(cx, cy, image = tori, tag="tori")#練習3

    key = "" #現在押されているキーを表す#練習4

    root.bind("<KeyPress>", key_down)#練習5

    root.bind("<KeyRelease>", key_up)#練習6
    
    main_proc()#練習7

    root.mainloop()