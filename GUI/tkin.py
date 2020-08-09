from tkinter import *

from tkinter import ttk

window = Tk()

window.geometry()

window.title("Welcome to Vaibhav's App")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='noob')

tab_control.add(tab2, text='nigga')

tab_control.add(tab3, text='nibba')

lbl1 = Label(tab1, text='label1',bg="orange",fg="blue")

lbl1.grid(column=0, row=0)

lbl2 = Label(tab2, text='label2',bg="green",fg="yellow")

lbl2.grid(column=0,row=0)

lbl3 = Label(tab3, text='label3')

lbl3.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

window.mainloop()
