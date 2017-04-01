import tkMessageBox
from Tkinter import *
from tkFont import Font
from collections import defaultdict


class App():
    def __init__(self, root):
        self.root = root  # creates an instance --> what we call the root window
        self.main_panel = MainPanel(self.root)
        self.upper_bar = UpperBar(self.root, self.main_panel)
        self.slider = Slider(self.root, self.main_panel, 10)
        self.menu = MenuBar(self.root, self.main_panel)


class MainPanel():
    def __init__(self, root):
        self.root = root
        self.custom_font = Font(family="courier", size=12)
        self.root.option_add("*Font", self.custom_font)
        self.root.title("iHart GUI Demo")
        self.default_width = 300
        self.default_height = 300
        self.ratio = 1
        frame_width = int(self.default_width * self.ratio)
        frame_height = int(self.default_height * self.ratio)
        self.root.geometry("%dx%d" % (frame_width, frame_height))

        #
        # board = Frame(root, height=frame_height, width=frame_width)
        # self.board = Canvas(board, bd=1, bg="black")
        #
        # board.grid(row=1, column=1)
        # self.board.grid(row=1, column=1)

    def change_font(self):
        new_font = Font(family="Times", size=12)
        self.root.option_add("*Font", new_font)
        self.root.update_idletasks()

    def larger_font(self):
        size = self.custom_font['size']
        self.custom_font.configure(size=size + 2)
        self.root.update_idletasks()

    def smaller_font(self):
        size = self.custom_font['size']
        self.custom_font.configure(size=size - 2)
        self.root.update_idletasks()

    def change_font(self, n):
        courier12 = Font(family="courier", size=12)
        # helv12 = Font(family="Helvetica", size=12)
        # times12 = Font(family="Times", size=12, )
        if n == 1:
            self.root.option_add("*Font", courier12)
            # self.custom_font.config(family="courier")
            self.root.update_idletasks()
            # self.root.option_add("*Font", courier12)
        elif n == 2:
            # self.custom_font.config(family="Helvetica")
            self.root.update_idletasks()
            # self.root.option_add("*Font", helv12)
        elif n == 3:
            self.custom_font.config(family="Times")
            self.root.update_idletasks()


class UpperBar():
    def __init__(self, root, main_panel):
        self.root = root
        self.board = main_panel
        # Style().configure('green/black.TLabel', foreground='green', background='black')
        flip_frame = Frame(self.root)
        flip_frame.pack(side="top", fill="x", expand=False)
        # flip_frame.config(width=self.board.default_width, height=2)
        flip_frame.grid(row=0, columnspan=10, sticky=W + E, padx=5, pady=5)
        button = Button(flip_frame, text="Flip Horizontal")
        button.pack(anchor=CENTER)


class Slider():

    def __init__(self, root, main_panel, init_val):

        self.root = root
        self.board = main_panel

        FaceVar = IntVar()
        FaceVar.set(1)
        MotionVar = BooleanVar()

        checkbox_frame = Frame(self.root)
        checkbox_frame.grid(row=2, column=0, columnspan=3, sticky=W + E + N + S)

        enableface_checkbox = Checkbutton(checkbox_frame, text="Enable Face", variable=FaceVar, onvalue=1, offvalue=0)
        enablemotion_checkbox = Checkbutton(checkbox_frame, text="Enable Motion", variable=MotionVar, onvalue=True, offvalue=False)
        enableface_checkbox.pack()
        enablemotion_checkbox.pack()
        enableface_checkbox.grid(row=0, column=0)
        enablemotion_checkbox.grid(row=0, column=2)

        bottom_frame = Frame(self.root)
        bottom_frame.grid(row=3, column=0, columnspan=3, sticky=W + E + N + S)

        self.create_buttons(bottom_frame)

    def create_buttons(self, frame):

        label_text = ["Reduce Noise", "Blur Value", "Blob Size", "Motion Thread", "Merge Distance"]
        to_value = [20, 20, 20, 50, 10]

        self.inputs = {}
        self.labels = {}
        self.scales = {}
        self.increases = {}
        self.decreases = {}
        self.vars = {}
        for i in range (0,5):
            self.vars[i] = IntVar()

        for r in range(0, 5):
            self.labels[r] = Label(frame, text=label_text[r])
            self.inputs[r] = 10
            self.scales[r] = Scale(frame, from_=0, to=to_value[r], variable=self.vars[r], orient=HORIZONTAL)
            self.scales[r].set(self.inputs[r])
            self.increases[r] = Button(frame, text="+", command=self.increase_val(r))
            self.decreases[r] = Button(frame, text="-", command=self.decrease_val(r))
            self.labels[r].grid(row=r+3, column=0)
            self.decreases[r].grid(row=r+3, column=1)
            self.scales[r].grid(row=r+3, column=2)
            self.increases[r].grid(row=r+3, column=3)

    def increase_val(self,r):
        self.inputs[r] = self.inputs[r]+1
        self.scales[r].set(self.inputs[r])

    def decrease_val(self, r):
        self.inputs[r] = self.inputs[r] - 1
        self.scales[r].set(self.inputs[r])

        # def increase0(self):
        #     self.input0= self.input0+1
        #     self.reduceScale.set(self.input0)
        #
        # def decrease0(self):
        #     self.input0= self.input0-1
        #     self.reduceScale.set(self.input0)
        #
        # def increase1(self):
        #     self.input1= self.input1+1
        #     self.blurScale.set(self.input1)
        #
        # def decrease1(self):
        #     self.input1= self.input1-1
        #     self.blurScale.set(self.input1)
        #
        # def increase2(self):
        #     self.input2= self.input2+1
        #     self.blobScale.set(self.input2)
        #
        # def decrease2(self):
        #     self.input2= self.input2-1
        #     self.blobScale.set(self.input2)
        #
        # def increase3(self):
        #     self.input3= self.input3+1
        #     self.motionScale.set(self.input3)
        #
        # def decrease3(self):
        #     self.input3= self.input3-1
        #     self.motionScale.set(self.input3)
        #
        # def increase4(self):
        #     self.input4= self.input4+1
        #     self.mergeScale.set(self.input4)
        #
        # def decrease4(self):
        #     self.input4= self.input4-1
        #     self.mergeScale.set(self.input4)


class MenuBar():
    def __init__(self, root, main_panel):
        self.root = root
        self.board = main_panel
        self.menubar = Menu(self.root)

        # file menu that contains open, save, create presents option
        fileMenu = Menu(self.menubar, tearoff=0)
        # fileMenu.add_command(label="Open Preset", command = self.load_present)
        # fileMenu.add_command(label="Save Preset", command = self.save_present)
        # fileMenu.add_command(label="Create Preset", command = self.create_present)
        self.menubar.add_cascade(label="File", menu=fileMenu)

        # about menu that contains About option and Info option
        aboutMenu = Menu(self.menubar, tearoff=0)
        aboutMenu.add_command(label="About", command=self.about)
        aboutMenu.add_command(label="Info", command=self.info)
        self.menubar.add_cascade(label="About", menu=aboutMenu)

        # #preference menu
        prefMenu = Menu(self.menubar, tearoff=0)
        prefMenu.add_command(label="Larger Font", command=self.board.larger_font)
        prefMenu.add_command(label="Smaller Font", command=self.board.smaller_font)
        prefMenu.add_command(label="Helvetica Font", command=self.board.change_font(2))
        self.menubar.add_cascade(label="Preference", menu=prefMenu)

        # quit menu
        quitMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Quit", menu=quitMenu)
        quitMenu.add_command(label="Quit!", command=self.quit)

        self.root.config(menu=self.menubar)

    def about(self):
        tkMessageBox.showinfo("About", "GUI demo for iHart 2017")

    def info(self):
        tkMessageBox.showinfo("Info", "GUI demo for iHart 2017")

    def quit(self):
        self.Quitbuttonvar.configure(state="disabled")
        if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()

    def about(self):
        tkMessageBox.showinfo("About", "GUI demo for iHart 2017")

    def info(self):
        tkMessageBox.showinfo("Info", "GUI demo for iHart 2017")

    def quit(self):
        if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()

    def load_present(self):
        pass

    def save_present(self):
        pass

    def create_present(self):
        pass


"""This is the code that is executed by python when we run this .py file"""
if __name__ == '__main__':
    root = Tk()  # creates an instance --> what we call the root window
    App(root)
    root.mainloop()
