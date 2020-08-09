from tkinter import *

w=Tk()
w.title("Calculator")
w.geometry("400x500")

f=Frame(w).pack(side="bottom")
b1=Button(f,text="Click",font=40).pack()
w.mainloop()