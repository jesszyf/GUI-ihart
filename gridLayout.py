from Tkinter import *

root = Tk()
root.geometry("300x200+30+30")

textPart = ['reduce noice','blur value','blob size','motion thread','merge distance']

Button(root, text="Flip Horizontal").grid(row=0, column=0, sticky=N)
r = 2
for i in range(5):
    Label(root,text=textPart[i]).grid(row=r,column=0, sticky=E)
    Entry(root).grid(row=r, column=1, sticky=E)

    r = r + 1


root.mainloop()
