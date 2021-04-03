try:
    from tkinter import * 
except ImportError:
    from Tkinter import *

root = Tk()

def maketable(data):
    height = 8
    width = 8
    for i in range(height): #Rows
        for j in range(width): #Columns
            b = Entry(root, text=data[i][j]["solved"])
            b.grid(row=i, column=j)

    mainloop()