from Tkinter import*
import tkMessageBox


class iHartGUI2017():

    def guiApp(self):
        self.root = Tk()
        self.root.title("iHart GUI Demo")
        self.root.geometry('300x270') #specify top-level window size and position
        self.menubar()
        self.create_upper_bar()
        self.slider(10, 15, 20, 30, 40)
        self.root.resizable(0,0)
        self.root.mainloop()


    def create_upper_bar(self):

        flip_frame = Frame(self.root)
        flip_frame.config(height=20)
        flip_frame.grid(row=0, columnspan = 20, sticky=W+E, padx=5, pady=5)
        button = Button(flip_frame, text="Flip Horizontal")
        button.grid(row=5, column=10, padx=50)


    def slider(self, reduceNoise, blurValue, blobSize, motionThread, mergeDistance):

        bottom_frame = Frame(self.root)
        bottom_frame.grid(row=20, column=0, columnspan=3,sticky=W+E+N+S)

        # varibles for further use
        FaceVar = IntVar()
        MotionVar = IntVar()
        ReduceNoiceVar = IntVar()
        BlurValueVar = IntVar()
        BlobSizeVar = IntVar()
        MotionThreadVar = IntVar()
        MergeDistanceVar = IntVar()

        enableFaceCheckBox = Checkbutton(bottom_frame, text = "Enable Face", variable = FaceVar, onvalue = 1, offvalue = 0)
        enableMotionCheckBox = Checkbutton(bottom_frame, text = "Enable Motion", variable = MotionVar, onvalue = 1, offvalue = 0)
        enableFaceCheckBox.pack()
        enableMotionCheckBox.pack()
        enableFaceCheckBox.grid(row = 0, column = 0)
        enableMotionCheckBox.grid(row = 0, column = 2)

        input0 = reduceNoise
        textLabel0 = Label(bottom_frame, text = "Reduce Noise")
        reduceScale = Scale(bottom_frame, from_=0, to=50, variable = ReduceNoiceVar, orient = HORIZONTAL)
        reduceScale.set(input0)
        increaseButton0 = Button(bottom_frame, text = "+", command = self.increase(input0, reduceScale))
        decreaseButton0 = Button(bottom_frame, text = "-", command = self.decrease(input0,reduceScale))
        textLabel0.grid(row = 1, column = 0)
        decreaseButton0.grid(row = 1, column = 1)
        reduceScale.grid(row = 1, column = 2)
        increaseButton0.grid(row = 1, column = 3)

        input1 = blurValue
        textLabel1 = Label(bottom_frame, text = "Blur Value")
        blurScale = Scale(bottom_frame, from_=0, to=50, variable = BlurValueVar, orient = HORIZONTAL)
        blurScale.set(input1)
        increaseButton1 = Button(bottom_frame, text = "+", command = self.increase(input1, blurScale))
        decreaseButton1 = Button(bottom_frame, text = "-", command = self.decrease(input1, blurScale))
        textLabel1.grid(row = 2, column = 0)
        decreaseButton1.grid(row = 2, column = 1)
        blurScale.grid(row = 2, column = 2)
        increaseButton1.grid(row = 2, column = 3)

        input2 = blobSize
        textLabel2 = Label(bottom_frame, text = "Blob Size")
        blobScale = Scale(bottom_frame, from_=0, to=50, variable = BlobSizeVar, orient = HORIZONTAL)
        blobScale.set(input2)
        increaseButton2 = Button(bottom_frame, text = "+", command = self.increase(input2, blobScale))
        decreaseButton2 = Button(bottom_frame, text = "-", command = self.decrease(input2, blobScale))
        textLabel2.grid(row = 3, column = 0)
        decreaseButton2.grid(row = 3, column = 1)
        blobScale.grid(row = 3, column = 2)
        increaseButton2.grid(row = 3, column = 3)

        input3 = motionThread
        textLabel3 = Label(bottom_frame, text = "Motion Thread")
        motionScale = Scale(bottom_frame, from_=0, to=50, variable = MotionThreadVar, orient = HORIZONTAL)
        motionScale.set(input3)
        increaseButton3 = Button(bottom_frame, text = "+", command = self.increase(input3, motionScale))
        decreaseButton3 = Button(bottom_frame, text = "-", command = self.decrease(input3, motionScale))
        textLabel3.grid(row = 4, column = 0)
        decreaseButton3.grid(row = 4, column = 1)
        motionScale.grid(row = 4, column = 2)
        increaseButton3.grid(row = 4, column = 3)

        input4 = mergeDistance
        textLabel4 = Label(bottom_frame, text = "Merge Distance")
        mergeScale = Scale(bottom_frame, from_=0, to=50, variable = MergeDistanceVar, orient = HORIZONTAL)
        mergeScale.set(input4)
        increaseButton4 = Button(bottom_frame, text = "+", command = self.increase(input4, mergeScale))
        decreaseButton4 = Button(bottom_frame, text = "-", command = self.decrease(input4, mergeScale))
        textLabel4.grid(row = 5, column = 0)
        decreaseButton4.grid(row = 5, column = 1)
        mergeScale.grid(row = 5, column = 2)
        increaseButton4.grid(row = 5, column = 3)

    def increase(self, inputIncrease, slideBar):
        result= inputIncrease+1
        slideBar.set(result)

    def decrease(self, inputDecrease, slideBar):
        result= inputDecrease
        slideBar.set(result)


    def menubar(self):

        self.menubar = Menu(self.root)

        # file menu that contains open, save, create presents option
        fileMenu = Menu(self.menubar, tearoff=0 )
        fileMenu.add_command(label="Open Preset", command = self.load_present)
        fileMenu.add_command(label="Save Preset", command = self.save_present)
        fileMenu.add_command(label="Create Preset", command = self.create_present)
        self.menubar.add_cascade(label="File", menu=fileMenu)

        # about menu that contains About option and Info option
        aboutMenu = Menu(self.menubar, tearoff=0)
        aboutMenu.add_command(label="About", command = self.about)
        aboutMenu.add_command(label="Info", command = self.info)
        self.menubar.add_cascade(label="About", menu=aboutMenu)

        # quit menu
        quitMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Quit", menu=quitMenu)
        quitMenu.add_command(label="Quit!", command=self.quit)

        self.root.config(menu=self.menubar)


    def about(self):
        tkMessageBox.showinfo("About","GUI demo for iHart 2017")


    def info(self):
        tkMessageBox.showinfo("Info","GUI demo for iHart 2017")


    def quit(self):
        self.Quitbuttonvar.configure(state="disabled")
        if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()

    def about(self):
        tkMessageBox.showinfo("About","GUI demo for iHart 2017")


    def info(self):
        tkMessageBox.showinfo("Info","GUI demo for iHart 2017")


    def quit(self):
        if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()

    def load_present(self):
        pass

    def save_present(self):
        pass

    def create_present(self):
        pass

