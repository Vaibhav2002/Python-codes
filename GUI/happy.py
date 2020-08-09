import math as m
from tkinter import *

window = Tk()
window.geometry("500x300")

window.title("Welcome to Vaibhav's app")
lbl1 = Label(window, text="HAPPY NUMBER CHECKER", bg="orange", fg="black", font=10)
lbl1.grid(row=0, column=0, padx=70)
lbl2 = Label(window, text="ENTER THE NUMBER TO CHECK IF HAPPY NUMBER", font=8)
lbl2.grid(row=1, column=0, padx=4)
t = Text(window, height=1, width=5, font=50)
t.grid(row=5, column=0, pady=20)
t.focus()


def check():
    n = int(t.get('1.0', END))
    s = 0
    while n > 9:
        while n > 0:
            s += int(m.pow(n % 10, 2))
            n = n // 10
        n = s
        s = 0
    if n == 1:
        text = "HAPPY NUMBER"
    else:
        text = "NOT HAPPY NUMBER"
    lbl3 = Label(window, text=text, font=84)
    lbl3.grid(column=0, row=10, pady=25)


c = Button(window, text="ENTER", font=64, command=check)
c.grid(row=8, column=0, padx=100, pady=10)

window.mainloop()
