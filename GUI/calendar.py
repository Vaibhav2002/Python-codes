from tkinter import *
from calendar import *
window=Tk()
window.title("Welcome to my calendar");
window.configure(background="gray")
window.geometry("600x500")
l=Label(window,text=calendar(year=2020).split())
l.grid(row=0,column=0)


window.mainloop()