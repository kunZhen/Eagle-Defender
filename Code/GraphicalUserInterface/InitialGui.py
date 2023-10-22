import os.path
from tkinter import *
from mailGui import *
import sys

sys.path.append("Code")


# GUI -> Graphical User Interface
class InitialGui:
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height

        centerX = width / 2
        centerY = height / 2

        font = "Helvetica"

        colorPalette = ["#8B0000", "#630000", "#1C1C1C", "#000000", "#FFFFFF"]

        self.logo = PhotoImage(file=os.path.abspath("Code/GraphicalUserInterface/GameData/EagleDefender.png"))

        # frames are used to facilitate the creation and deletion of screens
        self.initialFrame = Frame(window, width=width, height=height, bg=colorPalette[1])
        self.initialFrame.pack()

        # is replaced by the logo
        # Lb: Label. Specify the type of element
        self.titleLb = Label(self.initialFrame, text="Eagle Defender", font=(font, 50))
        self.titleLb.config(bg=colorPalette[1], fg=colorPalette[3])
        self.titleLb.place(x=centerX, y=100, anchor="center")

        self.titleCanvas = Canvas(self.initialFrame, width=400, height=580, bg=colorPalette[1])
        self.titleCanvas.place(x=centerX, y=150, anchor="n")
        self.titleCanvas.config(borderwidth=0, highlightthickness=0)
        self.titleCanvas.create_image(200, 300, anchor="center", image=self.logo)

        # Btn: Button
        self.loginBtn = Button(self.initialFrame, text="Ingresar", command=self.Login, font=(font, 15))
        self.loginBtn.config(bg=colorPalette[2], fg=colorPalette[4])
        self.loginBtn.place(x=centerX, y=height - 300, anchor="center")

        self.closeBtn = Button(self.initialFrame, text="Cerrar", command=self.CloseGame, font=(font, 15))
        self.closeBtn.config(bg=colorPalette[2], fg=colorPalette[4])
        self.closeBtn.place(x=centerX, y=height - 250, anchor="center")

    def Login(self):
        self.initialFrame.destroy()
        mail = mailGui(self.window, self.width, self.height, 1)

    def CloseGame(self):
        self.window.destroy()
