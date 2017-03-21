from Tkinter import*
import tkMessageBox


class iHartGUI2017():

    def guiApp(self):
        self.root = Tk()
        self.root.title("iHart GUI Demo")
        self.root.geometry('250x300') #specify top-level window size and position
        self.menubar()
        self.create_upper_bar()
        self.slider(0, 0, 0, 0, 0)
        self.root.mainloop()


    def create_upper_bar(self):

        flip_frame = Frame(self.root)
        flip_frame.config(height=20)
        flip_frame.grid(row=0, columnspan = 20, sticky=W+E, padx=5, pady=5)
        button = Button(flip_frame, text="Flip Horizontal")
        button.grid(row=5, column=10, padx=1)


    def slider(self, reduceNoise, blurValue, blobSize, motionThread, mergeDistance):

        bottom_frame = Frame(self.root)
        bottom_frame.grid(row=20, column=0, columnspan=3,sticky=W+E+N+S)

        enableFaceButton = Button(bottom_frame, text = "Enable Face")
        enableMotionButton = Button(bottom_frame, text = "Enable Motion")
        enableFaceButton.grid(row = 0, column = 0, sticky = W)
        enableMotionButton.grid(row = 0, column = 1, sticky = E)

        input0 = reduceNoise
        textLabel0 = Label(bottom_frame, text = "Reduce Noise")
        reduceScale = Scale(bottom_frame, from_=0, to=50, orient = HORIZONTAL)
        reduceScale.set(input0)
        textLabel0.grid(row = 1, column = 0, sticky = E)
        reduceScale.grid(row = 1, column = 1, sticky = E)

        input1 = blurValue
        textLabel1 = Label(bottom_frame, text = "Blur Value")
        blurScale = Scale(bottom_frame, from_=0, to=50, orient = HORIZONTAL)
        blurScale.set(input1)
        textLabel1.grid(row = 2, column = 0, sticky = E)
        blurScale.grid(row = 2, column = 1, sticky = E)

        input2 = blobSize
        textLabel2 = Label(bottom_frame, text = "Blob Size")
        blobScale = Scale(bottom_frame, from_=0, to=50, orient = HORIZONTAL)
        blobScale.set(input2)
        textLabel2.grid(row = 3, column = 0, sticky = E)
        blobScale.grid(row = 3, column = 1, sticky = E)

        input3 = motionThread
        textLabel3 = Label(bottom_frame, text = "Motion Thread")
        motionScale = Scale(bottom_frame, from_=0, to=50, orient = HORIZONTAL)
        motionScale.set(input3)
        textLabel3.grid(row = 4, column = 0, sticky = E)
        motionScale.grid(row = 4, column = 1, sticky = E)

        input4 = mergeDistance
        textLabel4 = Label(bottom_frame, text = "Merge Distance")
        mergeScale = Scale(bottom_frame, from_=0, to=50, orient = HORIZONTAL)
        mergeScale.set(input4)
        textLabel4.grid(row = 5, column = 0, sticky = E)
        mergeScale.grid(row = 5, column = 1, sticky = E)


    def menubar(self):

        self.menubar = Menu(self.root)

        # file menu that contains open, save, create presents option
        fileMenu = Menu(self.menubar, tearoff=0 )
        fileMenu.add_command(label="Open Present", command = self.load_present)
        fileMenu.add_command(label="Save Present", command = self.save_present)
        fileMenu.add_command(label="Create Present", command = self.create_present)
        self.menubar.add_cascade(label="File", menu=fileMenu)

        # about menu that contains About option and Info option
        aboutMenu = Menu(self.menubar, tearoff=0)
        aboutMenu.add_command(label="About", command = self.about)
        aboutMenu.add_command(label="Info", command = self.info)
        self.menubar.add_cascade(label="About", menu=aboutMenu)

        # quit menu
        quitMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Quit", menu=quitMenu, command = self.quit)

        self.root.config(menu=self.menubar)


    def about(self):
        tkMessageBox.showinfo("About","GUI demo for iHart 2017")


    def info(self):
        tkMessageBox.showinfo("Info","GUI demo for iHart 2017")


    def quit(self):
        self.Quitbuttonvar.configure(state="disabled")
        if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()


    def load_present(self):
        pass

    def save_present(self):
        pass

    def create_present(self):
        pass

