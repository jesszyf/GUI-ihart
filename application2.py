from Tkinter import *
import tkMessageBox


class iHartGUI2017():

    def guiApp(self):
        self.root = Tk()
        self.root.title("iHart GUI Demo")
        self.root.geometry('300x250') #specify top-level window size and position
        self.menubar()
        self.create_upper_bar()
        self.buttons(10, 15, 20, 30, 40)
        self.root.mainloop()


    def create_upper_bar(self):
        flip_frame = Frame(self.root)
        flip_frame.config(height=20)
        flip_frame.grid(row=0, columnspan = 20, sticky=W+E, padx=5, pady=5)
        button = Button(flip_frame, text="Flip Horizontal")
        button.grid(row=5, column=10, padx=50)

    def buttons(self, reduceNoise, blurValue, blobSize, motionThread, mergeDistance):
        bottom_frame = Frame(self.root)
        bottom_frame.grid(row=20, column=0, columnspan=3,sticky=W+E+N+S)

        self.enableFaceButton = Button(bottom_frame, text = "Enable Face", command = self.enableFace)
        self.enableMotionButton = Button(bottom_frame, text = "Enable Motion", command = self.enableMotion)
        self.enableFaceButton.grid(row = 0, column = 0)
        self.enableMotionButton.grid(row = 0, column = 2)

        self.input0 = reduceNoise
        self.numText0 = str(self.input0)

        self.textLabel0 = Label(bottom_frame, text = "Reduce Noise", bg="grey")
        self.num0 = Label(bottom_frame, text = self.numText0)
        self.increaseButton0 = Button(bottom_frame, text = "+", command = self.increase0)
        self.decreaseButton0 = Button(bottom_frame, text = "-", command = self.decrease0)

        self.textLabel0.grid(row=1, column=0)
        self.increaseButton0.grid(row=1,column=1)
        self.num0.grid(row=1,column=2)
        self.decreaseButton0.grid(row=1,column=3)

        self.input1 = blurValue
        self.numText1 = str(self.input1)

        self.textLabel1 = Label(bottom_frame, text = "Blur Value", bg="grey")
        self.num1 = Label(bottom_frame, text = self.numText1)
        self.increaseButton1 = Button(bottom_frame, text = "+", command = self.increase1)
        self.decreaseButton1 = Button(bottom_frame, text = "-", command = self.decrease1)

        self.textLabel1.grid(row=2, column=0)
        self.increaseButton1.grid(row=2,column=1)
        self.num1.grid(row=2,column=2)
        self.decreaseButton1.grid(row=2,column=3)

        self.input2 = blobSize
        self.numText2 = str(self.input2)

        self.textLabel2 = Label(bottom_frame, text = "Blob Size", bg="grey")
        self.num2 = Label(bottom_frame, text = self.numText2)
        self.increaseButton2 = Button(bottom_frame, text = "+", command = self.increase2)
        self.decreaseButton2 = Button(bottom_frame, text = "-", command = self.decrease2)

        self.textLabel2.grid(row=3, column=0)
        self.increaseButton2.grid(row=3,column=1)
        self.num2.grid(row=3,column=2)
        self.decreaseButton2.grid(row=3,column=3)

        self.input3 = motionThread
        self.numText3 = str(self.input3)

        self.textLabel3 = Label(bottom_frame, text = "Motion Thread", bg="grey")
        self.num3 = Label(bottom_frame, text = self.numText3)
        self.increaseButton3 = Button(bottom_frame, text = "+", command = self.increase3)
        self.decreaseButton3 = Button(bottom_frame, text = "-", command = self.decrease3)

        self.textLabel3.grid(row=4, column=0)
        self.increaseButton3.grid(row=4,column=1)
        self.num3.grid(row=4,column=2)
        self.decreaseButton3.grid(row=4,column=3)

        self.input4 = mergeDistance
        self.numText4 = str(self.input4)

        self.textLabel4 = Label(bottom_frame, text = "Merge Distance", bg="grey")
        self.num4 = Label(bottom_frame, text = self.numText4)
        self.increaseButton4 = Button(bottom_frame, text = "+", command = self.increase4)
        self.decreaseButton4 = Button(bottom_frame, text = "-", command = self.decrease4)

        self.textLabel4.grid(row=5, column=0)
        self.increaseButton4.grid(row=5,column=1)
        self.num4.grid(row=5,column=2)
        self.decreaseButton4.grid(row=5,column=3)


    def increase0(self):
        self.input0 = self.input0+1
        self.numText0 = str(self.input0)
        self.num0.config(text=self.numText0)

    def decrease0(self):
        self.input0 = self.input0-1
        self.numText0 = str(self.input0)
        self.num0.config(text=self.numText0)

    def increase1(self):
        self.input1 = self.input1+1
        self.numText1 = str(self.input1)
        self.num1.config(text=self.numText1)

    def decrease1(self):
        self.input1 = self.input1-1
        self.numText1 = str(self.input1)
        self.num1.config(text=self.numText1)

    def increase2(self):
        self.input2 = self.input2+1
        self.numText2 = str(self.input2)
        self.num2.config(text=self.numText2)

    def decrease2(self):
        self.input2 = self.input2-1
        self.numText2 = str(self.input2)
        self.num2.config(text=self.numText2)

    def increase3(self):
        self.input3 = self.input3+1
        self.numText3 = str(self.input3)
        self.num3.config(text=self.numText3)

    def decrease3(self):
        self.input3 = self.input3-1
        self.numText3 = str(self.input3)
        self.num3.config(text=self.numText3)

    def increase4(self):
        self.input4 = self.input4+1
        self.numText4 = str(self.input4)
        self.num4.config(text=self.numText4)

    def decrease4(self):
        self.input4 = self.input4-1
        self.numText4 = str(self.input4)
        self.num4.config(text=self.numText4)



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

    def enableFace(self):
        pass

    def enableMotion(self):
        pass

    def load_present(self):
        pass

    def save_present(self):
        pass

    def create_present(self):
        pass

