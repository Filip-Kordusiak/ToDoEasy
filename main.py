from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import ttk

root = Tk()
def ukonczone():

    w2.insert(0, w.get(w.curselection()))
    w.delete(w.curselection())

frame = LabelFrame(root)
frame.grid(row=0, column=0)
w = Listbox(frame)
w.grid(row=0, column=0)
b4 = Button(frame, text="ukończone", command=ukonczone)
b4.grid(row=1, column=0)


def dodaj():
    e.get()
    w.insert(0, e.get())
def usun():

    w2.delete(first=0, last=END)




frame2 = LabelFrame(root)
frame2.grid(row=1, column=0)
b2 = Button(frame2, text="dodaj czynność", command=dodaj)
b2.grid(row=1, column=0)
e = Entry(frame2)
e.get()
e.clipboard_clear()
e.grid(row=0, column=0)

frame3 = LabelFrame(root, text="ukończone")
frame3.grid(row=2, column=0)
w2 = Listbox(frame3)
w2.grid(row=0, column=0)
b3 = Button(frame3, text="usuń wszystko", command=usun)
b3.grid(row=1, column=0)

root.mainloop()
