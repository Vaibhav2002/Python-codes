import random as r
from tkinter import *

w = Tk()
w.geometry("560x400")
a = ['STONE', 'PAPER', 'SCISSOR']


def check(s, s1):
    if (s == 'STONE' and s1 == 'SCISSOR') or (s == 'PAPER' and s1 == 'STONE') or (s == 'SCISSOR' and s1 == 'PAPER'):
        return 1
    elif s == s1:
        return 0
    else:
        return -1


def click(i):
    global a
    s = a[i]
    comp = r.randint(0, 2)
    s1 = a[comp]
    b.config(text=s, fg='blueviolet')
    c.config(text=s1, fg='lime green')
    if check(s, s1) == 1:
        l.config(text="YOU WIN")
    elif check(s, s1) == 0:
        l.config(text="DRAW")
    else:
        l.config(text="COM WINS")


f = Frame(w)
f.pack(side='left')
f1 = Frame(w)
f1.pack(side="right")
l = Label(f, font=('times roman', 17), fg="RED")
l.grid(row=2, column=1, padx=30)

b0 = Button(f, text="STONE", width=12, height=6, activebackground='turquoise', command=lambda: click(0))
b1 = Button(f, text="PAPER", width=12, height=6, activebackground='turquoise', command=lambda: click(1))
b2 = Button(f, text="SCISSOR", width=12, height=6, activebackground='turquoise', command=lambda: click(2))
c0 = Button(f1, text="STONE", width=12, height=6, activebackground='pale green')
c1 = Button(f1, text="PAPER", width=12, height=6, activebackground='pale green')
c2 = Button(f1, text="SCISSOR", width=12, height=6, activebackground='pale green')
b = Label(f, width=12, height=6, font=('times roman', 15))
b.grid(row=1, column=1)
c = Label(f1, width=12, height=6, font=('times roman', 15))
c.grid(row=1, column=0)
b0.grid(row=0, column=0, padx=10, pady=10)
b1.grid(row=1, column=0, padx=10, pady=10)
b2.grid(row=2, column=0, padx=10, pady=10)
c0.grid(row=0, column=1, padx=10, pady=10)
c1.grid(row=1, column=1, padx=10, pady=10)
c2.grid(row=2, column=1, padx=10, pady=10)
w.mainloop()
