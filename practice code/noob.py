from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Welcome to vaibhav's app")
lbl = Label(window, text="NOOB CHECKER", bg="Yellow", fg="Red", font=30)
lbl.grid(column=5, row=0)
lbl2 = Label(window, text="Enter your name", font=25)
lbl2.grid(column=4, row=10)
box = Entry(window, width=20)
box.grid(column=5, row=10)


def clicked():
    res = box.get()
    if res == "akshat":
        lbl3 = Label(window, text="NOOB", font=20)
        lbl3.grid(column=4, row=15)
        g = Label(window, text="NOOB", font=20)
        g.grid(column=4, row=17)
        lbl5 = Label(window, text="NOOB", font=20)
        lbl5.grid(column=4, row=19)
        lbl6 = Label(window, text="NOOB", font=20)
        lbl6.grid(column=4, row=21)
        lbl7 = Label(window, text="NOOB", font=20)
        lbl7.grid(column=4, row=23)

    elif res == "vaibhav":
        lbl3 = Label(window, text="PRO", font=50)
        lbl3.grid(column=4, row=15)
        g = Label(window, text="PRO", font=50)
        g.grid(column=4, row=17)
        lbl5 = Label(window, text="PRO", font=50)
        lbl5.grid(column=4, row=19)
        lbl6 = Label(window, text="PRO", font=50)
        lbl6.grid(column=4, row=21)
        lbl7 = Label(window, text="PRO", font=50)
        lbl7.grid(column=4, row=23)


bn = Button(window, text="Click Me", command=clicked)
bn.grid(column=7, row=10)

window.mainloop()
