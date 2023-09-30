from tkinter import *
from mailGui import *


# GUI -> Graphical User Interface
class InitialGui:
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height

        centerX = width / 2
        centerY = height / 2

        font = "Helvetica"

        # frames are used to facilitate the creation and deletion of screens
        self.initialFrame = Frame(window, width=width, height=height, bg="red")
        self.initialFrame.pack()

        # is replaced by the logo
        # Lb: Label. Specify the type of element
        self.titleLb = Label(self.initialFrame, text="Eagle Defender", font=(font, 50))
        self.titleLb.place(x=centerX, y=centerY, anchor="center")

        # is replaced by mouse event
        # Btn: Button
        self.loginBtn = Button(self.initialFrame, text="Ingresar", command=self.Login, font=(font, 15))
        self.loginBtn.place(x=centerX, y=height - 350, anchor="center")

        self.closeBtn = Button(self.initialFrame, text="Cerrar", command=self.CloseGame, font=(font, 15))
        self.closeBtn.place(x=centerX, y=height - 250, anchor="center")

    def Login(self):
        self.initialFrame.destroy()
        login = mailGui(self.window, self.width, self.height)
        login.pack()

    def CloseGame(self):
        self.window.destroy()
