import tkMessageBox
from Tkinter import *
from tkFont import Font



class iHartGUI2017():

    def guiApp(self):
        self.root = Tk()
        self.root.title("iHart GUI Demo")
        self.customFont = Font(family="courier", size=12)
        self.root.option_add("*Font", self.customFont)
        self.defaultW=300
        self.defaultH=270
        self.ratio = 1
        self.frameW  = int(self.defaultW* self.ratio)
        self.frameH  = int(self.defaultH * self.ratio)
        self.root.geometry("%dx%d"%(self.frameW,self.frameH))
        self.menubar()
        self.create_upper_bar()
        self.slider(10, 10, 10, 10, 10)
        self.root.resizable(0,0)
        self.root.mainloop()

    def create_upper_bar(self):

        flip_frame = Frame(self.root)
        flip_frame.config(height=20)
        flip_frame.grid(row=0, columnspan = 20, sticky=W+E, padx=5, pady=5)
        button = Button(flip_frame, text="Flip Horizontal")
        button.pack(anchor = CENTER)


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
        enableFaceCheckBox.grid(row=0, column = 0)
        enableMotionCheckBox.grid(row = 0, column = 2)

        self.input0 = reduceNoise
        textLabel0 = Label(bottom_frame, text = "Reduce Noise")
        self.reduceScale = Scale(bottom_frame, from_=0, to=20, variable = ReduceNoiceVar, orient = HORIZONTAL)
        self.reduceScale.set(self.input0)
        increaseButton0 = Button(bottom_frame, text = "+", command = self.increase0)
        decreaseButton0 = Button(bottom_frame, text = "-", command = self.decrease0)
        textLabel0.grid(row = 1, column = 0)
        decreaseButton0.grid(row = 1, column = 1)
        self.reduceScale.grid(row = 1, column = 2)
        increaseButton0.grid(row = 1, column = 3)

        self.input1 = blurValue
        textLabel1 = Label(bottom_frame, text = "Blur Value")
        self.blurScale = Scale(bottom_frame, from_=0, to=20, variable = BlurValueVar, orient = HORIZONTAL)
        self.blurScale.set(self.input1)
        increaseButton1 = Button(bottom_frame, text = "+", command = self.increase1)
        decreaseButton1 = Button(bottom_frame, text = "-", command = self.decrease1)
        textLabel1.grid(row = 2, column = 0)
        decreaseButton1.grid(row = 2, column = 1)
        self.blurScale.grid(row = 2, column = 2)
        increaseButton1.grid(row = 2, column = 3)

        self.input2 = blobSize
        textLabel2 = Label(bottom_frame, text = "Blob Size")
        self.blobScale = Scale(bottom_frame, from_=0, to=20, variable = BlobSizeVar, orient = HORIZONTAL)
        self.blobScale.set(self.input2)
        increaseButton2 = Button(bottom_frame, text = "+", command = self.increase2)
        decreaseButton2 = Button(bottom_frame, text = "-", command = self.decrease2)
        textLabel2.grid(row = 3, column = 0)
        decreaseButton2.grid(row = 3, column = 1)
        self.blobScale.grid(row = 3, column = 2)
        increaseButton2.grid(row = 3, column = 3)

        self.input3 = motionThread
        textLabel3 = Label(bottom_frame, text = "Motion Thread")
        self.motionScale = Scale(bottom_frame, from_=0, to=50, variable = MotionThreadVar, orient = HORIZONTAL)
        self.motionScale.set(self.input3)
        increaseButton3 = Button(bottom_frame, text = "+", command = self.increase3)
        decreaseButton3 = Button(bottom_frame, text = "-", command = self.decrease3)
        textLabel3.grid(row = 4, column = 0)
        decreaseButton3.grid(row = 4, column = 1)
        self.motionScale.grid(row = 4, column = 2)
        increaseButton3.grid(row = 4, column = 3)

        self.input4 = mergeDistance
        textLabel4 = Label(bottom_frame, text = "Merge Distance")
        self.mergeScale = Scale(bottom_frame, from_=0, to=10, variable = MergeDistanceVar, orient = HORIZONTAL)
        self.mergeScale.set(self.input4)
        increaseButton4 = Button(bottom_frame, text = "+", command = self.increase4)
        decreaseButton4 = Button(bottom_frame, text = "-", command = self.decrease4)
        textLabel4.grid(row = 5, column = 0)
        decreaseButton4.grid(row = 5, column = 1)
        self.mergeScale.grid(row = 5, column = 2)
        increaseButton4.grid(row = 5, column = 3)

    def increase0(self):
        self.input0= self.input0+1
        self.reduceScale.set(self.input0)

    def decrease0(self):
        self.input0= self.input0-1
        self.reduceScale.set(self.input0)

    def increase1(self):
        self.input1= self.input1+1
        self.blurScale.set(self.input1)

    def decrease1(self):
        self.input1= self.input1-1
        self.blurScale.set(self.input1)

    def increase2(self):
        self.input2= self.input2+1
        self.blobScale.set(self.input2)

    def decrease2(self):
        self.input2= self.input2-1
        self.blobScale.set(self.input2)

    def increase3(self):
        self.input3= self.input3+1
        self.motionScale.set(self.input3)

    def decrease3(self):
        self.input3= self.input3-1
        self.motionScale.set(self.input3)

    def increase4(self):
        self.input4= self.input4+1
        self.mergeScale.set(self.input4)

    def decrease4(self):
        self.input4= self.input4-1
        self.mergeScale.set(self.input4)


    def menubar(self):

        self.menubar = Menu(self.root)

        # file menu that contains open, save, create presents option
        fileMenu = Menu(self.menubar, tearoff=0 )
        # fileMenu.add_command(label="Open Preset", command = self.load_present)
        # fileMenu.add_command(label="Save Preset", command = self.save_present)
        # fileMenu.add_command(label="Create Preset", command = self.create_present)
        self.menubar.add_cascade(label="File", menu=fileMenu)

        # about menu that contains About option and Info option
        aboutMenu = Menu(self.menubar, tearoff=0)
        aboutMenu.add_command(label="About", command = self.about)
        aboutMenu.add_command(label="Info", command = self.info)
        self.menubar.add_cascade(label="About", menu=aboutMenu)

        # #preference menu
        prefMenu = Menu(self.menubar, tearoff=0)
        prefMenu.add_command(label="Larger Font", command = self.largerFont)
        prefMenu.add_command(label="Smaller Font", command = self.smallerFont)
        self.menubar.add_cascade(label="Preference", menu=prefMenu)

        # quit menu
        quitMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Quit", menu=quitMenu)
        quitMenu.add_command(label="Quit!", command=self.quit)

        self.root.config(menu=self.menubar)

    def largerFont(self):
        # self.ratio = self.ratio * 1.2
        size = self.customFont['size']
        self.customFont.configure(size=size+2)
        self.root.update_idletasks()


    def smallerFont(self):
        size = self.customFont['size']
        self.customFont.configure(size=size-2)
        # self.ratio = self.ratio* 0.8
        self.root.update_idletasks()

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

