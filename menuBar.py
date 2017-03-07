from Tkinter import *


root = Tk()

menubar = Menu(root) # frame that holds the menu buttons

# open saved presents
fileMenu = Menu(menubar, tearoff=0 )
fileMenu.add_command(label="Open Present")
fileMenu.add_command(label="Save Present")
fileMenu.add_command(label="Create Present")
menubar.add_cascade(label="File", menu=fileMenu)

aboutMenu = Menu(menubar, tearoff=0)
aboutMenu.add_command(label="About")
aboutMenu.add_command(label="Info")
menubar.add_cascade(label="About", menu=aboutMenu)

quitMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Quit", menu=quitMenu)

# Displaying menu on top of root.
root.config(menu=menubar)

root.mainloop() # main loop of top-level
