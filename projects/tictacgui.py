from tkinter import *
from tkinter import font
from tkinter.messagebox import *

import pygame as p

w = Tk()
w.geometry("317x340")
p.init()
p.mixer.music.load('C:\\Users\\91810\\Downloads\\click sound.mp3')
w.iconbitmap("C:\\Users\\91810\\Downloads\\tic-tac-toe.ico")
w.title("TIC-TAC-TOE")
r = c = g = 0
a = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

myFont = font.Font(family='Helvetica', size=15, weight='bold')


def check(ch):
    global a, g
    flag1 = False
    if a[0] == ch and a[1] == ch and a[2] == ch:
        flag1 = True
    elif a[3] == ch and a[4] == ch and a[5] == ch:
        flag1 = True
    elif a[6] == ch and a[7] == ch and a[8] == ch:
        flag1 = True
    elif a[0] == ch and a[3] == ch and a[6] == ch:
        flag1 = True
    elif a[1] == ch and a[4] == ch and a[7] == ch:
        flag1 = True
    elif a[2] == ch and a[5] == ch and a[8] == ch:
        flag1 = True
    elif a[0] == ch and a[4] == ch and a[8] == ch:
        flag1 = True
    elif a[2] == ch and a[4] == ch and a[6] == ch:
        flag1 = True
    if flag1:
        if ch == 'X':
            showinfo(title="RESULT", message="Congratulations! Player 1 wins")
        else:
            showinfo(title="RESULT", message="Congratulations! Player 2 wins")
    elif g == 9:
        showinfo(title="RESULT", message="GAME DRAW!")


def insert(l, b):
    global a, g
    p.mixer.music.play()
    s = 'X' if g % 2 == 0 else 'O'
    if a[l] == ' ':
        b.config(text=s)
        a[l] = s
        g += 1
        if s == 'X':
            b.config(fg="red")
        else:
            b.config(fg="blue")
        check(s)


b0 = Button(w, text=' ', font=70, width=8, height=4, fg="green", bg="misty rose", activebackground="floral white",
            activeforeground="orange", command=lambda: insert(0, b0))
myFont = font.Font(family='Helvetica', size=15, weight='bold')
b0['font'] = myFont
b0.grid(row=0, column=0)
b1 = Button(w, text=' ', font=70, width=8, height=4, fg="green", bg="misty rose", activebackground="floral white",
            activeforeground="orange", command=lambda: insert(1, b1))
b1['font'] = myFont
b1.grid(row=0, column=1)

b2 = Button(w, text=' ', font=70, width=8, height=4, fg="green", bg="misty rose", activebackground="floral white",
            activeforeground="orange", command=lambda: insert(2, b2))
b2['font'] = myFont
b2.grid(row=0, column=2)

b3 = Button(w, text=' ', font=70, width=8, height=4, fg="green", bg="misty rose", activebackground="floral white",
            activeforeground="orange", command=lambda: insert(3, b3))
b3['font'] = myFont
b3.grid(row=1, column=0)

b4 = Button(w, text=' ', font=70, width=8, height=4, fg="green", bg="misty rose", activebackground="floral white",
            activeforeground="orange", command=lambda: insert(4, b4))
b4['font'] = myFont
b4.grid(row=1, column=1)

b5 = Button(w, text=' ', font=70, width=8, height=4, fg="green", bg="misty rose", activebackground="floral white",
            activeforeground="orange", command=lambda: insert(5, b5))
b5['font'] = myFont
b5.grid(row=1, column=2)

b6 = Button(w, text=' ', font=70, width=8, height=4, fg="green", bg="misty rose", activebackground="floral white",
            activeforeground="orange", command=lambda: insert(6, b6))
b6['font'] = myFont
b6.grid(row=2, column=0)

b7 = Button(w, text=' ', font=70, width=8, height=4, fg="green", bg="misty rose", activebackground="floral white",
            activeforeground="orange", command=lambda: insert(7, b7))
b7['font'] = myFont
b7.grid(row=2, column=1)

b8 = Button(w, text=' ', font=70, width=8, height=4, fg="green", bg="misty rose", activebackground="floral white",
            activeforeground="orange", command=lambda: insert(8, b8))
b8['font'] = myFont
b8.grid(row=2, column=2)

w.mainloop()
