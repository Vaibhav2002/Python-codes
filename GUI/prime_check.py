import math as m
from tkinter import *

window = Tk()
window.geometry("500x270")

window.title("Welcome to Vaibhav's app")
lbl1 = Label(window, text="PRIME CHECKER", bg="orange", fg="black", font=10)
lbl1.grid(row=0, column=0, padx=70)
lbl2 = Label(window, text="ENTER THE NUMBER TO CHECK FOR PRIME", font=8)
lbl2.grid(row=1, column=0, padx=30)
t = Text(window, height=1, width=5, font=50)
t.grid(row=5, column=0, pady=20)
t.focus()
lbl3 = Label(window)
lbl3.grid(column=0, row=10, pady=25)


def check():
    n = int(t.get('1.0', END))
    f = True
    for j in range(2, int(m.sqrt(n)) + 1):
        if n % j == 0:
            f = False
            break
    text = " "
    if f:
        text = "PRIME"
    else:
        text = "NOT PRIME"
    lbl3.configure(text=text, font=84)


c = Button(window, text="ENTER", font=64, command=check)
c.grid(row=8, column=0, padx=100, pady=10)

window.mainloop()
