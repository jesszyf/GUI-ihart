from Tkinter import*

class buttonGUI:
  def __init__(self, reduceNoise, blurValue, blobSize, motionThread, mergeDistance):
    self.__mainWindow = Tk()

    self.enableFaceButton = Button(self.__mainWindow, text = "Eable Face")
    self.enableMotionButton = Button(self.__mainWindow, text = "Enable Motion")
    self.enableFaceButton.grid(row = 0, column = 0)
    self.enableMotionButton.grid(row = 0, column = 2)

    self.input0 = reduceNoise
    self.numText0 = str(self.input0)

    self.textLabel0 = Label(self.__mainWindow, text = "Reduce Noise")
    self.num0 = Label(self.__mainWindow, text = self.numText0)
    self.increaseButton0 = Button(self.__mainWindow, text = "+", command = self.increase0)
    self.decreaseButton0 = Button(self.__mainWindow, text = "-", command = self.decrease0)

    self.textLabel0.grid(row=1, column=0)
    self.increaseButton0.grid(row=1,column=1)
    self.num0.grid(row=1,column=2)
    self.decreaseButton0.grid(row=1,column=3)

    self.input1 = blurValue
    self.numText1 = str(self.input1)

    self.textLabel1 = Label(self.__mainWindow, text = "Blur Value")
    self.num1 = Label(self.__mainWindow, text = self.numText1)
    self.increaseButton1 = Button(self.__mainWindow, text = "+", command = self.increase1)
    self.decreaseButton1 = Button(self.__mainWindow, text = "-", command = self.decrease1)

    self.textLabel1.grid(row=2, column=0)
    self.increaseButton1.grid(row=2,column=1)
    self.num1.grid(row=2,column=2)
    self.decreaseButton1.grid(row=2,column=3)

    self.input2 = blobSize
    self.numText2 = str(self.input2)

    self.textLabel2 = Label(self.__mainWindow, text = "Blob Size")
    self.num2 = Label(self.__mainWindow, text = self.numText2)
    self.increaseButton2 = Button(self.__mainWindow, text = "+", command = self.increase2)
    self.decreaseButton2 = Button(self.__mainWindow, text = "-", command = self.decrease2)

    self.textLabel2.grid(row=3, column=0)
    self.increaseButton2.grid(row=3,column=1)
    self.num2.grid(row=3,column=2)
    self.decreaseButton2.grid(row=3,column=3)

    self.input3 = motionThread
    self.numText3 = str(self.input3)

    self.textLabel3 = Label(self.__mainWindow, text = "Motion Thread")
    self.num3 = Label(self.__mainWindow, text = self.numText3)
    self.increaseButton3 = Button(self.__mainWindow, text = "+", command = self.increase3)
    self.decreaseButton3 = Button(self.__mainWindow, text = "-", command = self.decrease3)

    self.textLabel3.grid(row=4, column=0)
    self.increaseButton3.grid(row=4,column=1)
    self.num3.grid(row=4,column=2)
    self.decreaseButton3.grid(row=4,column=3)

    self.input4 = mergeDistance
    self.numText4 = str(self.input4)

    self.textLabel4 = Label(self.__mainWindow, text = "Merge Distance")
    self.num4 = Label(self.__mainWindow, text = self.numText4)
    self.increaseButton4 = Button(self.__mainWindow, text = "+", command = self.increase4)
    self.decreaseButton4 = Button(self.__mainWindow, text = "-", command = self.decrease4)

    self.textLabel4.grid(row=5, column=0)
    self.increaseButton4.grid(row=5,column=1)
    self.num4.grid(row=5,column=2)
    self.decreaseButton4.grid(row=5,column=3)

    mainloop()

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


myGUI = buttonGUI(10, 20, 30, 40,50)
