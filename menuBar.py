from Tkinter import *


root = Tk()

menubar = Menu(root)

# file menu that contains open, save, create presents option
fileMenu = Menu(menubar, tearoff=0 )
fileMenu.add_command(label="Open Present")
fileMenu.add_command(label="Save Present")
fileMenu.add_command(label="Create Present")
menubar.add_cascade(label="File", menu=fileMenu)

# about menu that contains About option and Info option
aboutMenu = Menu(menubar, tearoff=0)
aboutMenu.add_command(label="About")
aboutMenu.add_command(label="Info")
menubar.add_cascade(label="About", menu=aboutMenu)

# quit menu
quitMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Quit", menu=quitMenu)


root.config(menu=menubar)   # Displaying menu on top of root.

root.mainloop()             # main loop of top-level
