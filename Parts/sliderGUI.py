from Tkinter import*

class buttonGUI:

  def __init__(self, reduceNoise, blurValue, blobSize, motionThread, mergeDistance):
    self.__mainWindow = Tk()

    # varibles for further use
    FaceVar = IntVar()
    MotionVar = IntVar()
    ReduceNoiceVar = IntVar()
    BlurValueVar = IntVar()
    BlobSizeVar = IntVar()
    MotionThreadVar = IntVar()
    MergeDistanceVar = IntVar()

    self.enableFaceCheckBox = Checkbutton(self.__mainWindow, text = "Enable Face", variable = FaceVar, onvalue = 1, offvalue = 0, height=3, width = 15)
    self.enableMotionCheckBox = Checkbutton(self.__mainWindow, text = "Enable Motion", variable = MotionVar, onvalue = 1, offvalue = 0, height=3, width = 15)
    self.enableFaceCheckBox.pack()
    self.enableMotionCheckBox.pack()

    self.enableFaceCheckBox.grid(row = 0, column = 0)
    self.enableMotionCheckBox.grid(row = 0, column = 1)

    self.input0 = reduceNoise
    self.textLabel0 = Label(self.__mainWindow, text = "Reduce Noise")
    self.reduceScale = Scale(self.__mainWindow, from_=0, to=50, variable = ReduceNoiceVar, orient = HORIZONTAL)
    self.reduceScale.set(self.input0)
    self.textLabel0.grid(row = 1, column = 0)
    self.reduceScale.grid(row = 1, column = 1)

    self.input1 = blurValue
    self.textLabel1 = Label(self.__mainWindow, text = "Blur Value")
    self.blurScale = Scale(self.__mainWindow, from_=0, to=50, variable = BlurValueVar, orient = HORIZONTAL)
    self.blurScale.set(self.input1)
    self.textLabel1.grid(row = 2, column = 0)
    self.blurScale.grid(row = 2, column = 1)

    self.input2 = blobSize
    self.textLabel2 = Label(self.__mainWindow, text = "Blob Size")
    self.blobScale = Scale(self.__mainWindow, from_=0, to=50, variable = BlobSizeVar, orient = HORIZONTAL)
    self.blobScale.set(self.input2)
    self.textLabel2.grid(row = 3, column = 0)
    self.blobScale.grid(row = 3, column = 1)

    self.input3 = motionThread
    self.textLabel3 = Label(self.__mainWindow, text = "Motion Thread")
    self.motionScale = Scale(self.__mainWindow, from_=0, to=50, variable = MotionThreadVar, orient = HORIZONTAL)
    self.motionScale.set(self.input3)
    self.textLabel3.grid(row = 4, column = 0)
    self.motionScale.grid(row = 4, column = 1)

    self.input4 = mergeDistance
    self.textLabel4 = Label(self.__mainWindow, text = "Merge Distance")
    self.mergeScale = Scale(self.__mainWindow, from_=0, to=50, variable = MergeDistanceVar, orient = HORIZONTAL)
    self.mergeScale.set(self.input4)
    self.textLabel4.grid(row = 5, column = 0)
    self.mergeScale.grid(row = 5, column = 1)

    mainloop()


myGUI = buttonGUI(10, 15,20, 30, 40)
