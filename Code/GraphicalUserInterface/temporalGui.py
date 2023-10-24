import os
import tkinter
from tkinter import *

class temporalFrame: 
    def __init__(self, window, width, height, parent ):
        self.window = window
        self.width = width
        self.height = height

        centerX = width / 2
        centerY = height / 2
        self.parent=parent
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


        self.titleLb = Label(self.initialFrame, text="Cargando datos...", font=(font, 50))
        self.titleLb.config(bg=colorPalette[1], fg=colorPalette[3])
        self.titleLb.place(x=centerX, y=2*centerY-200, anchor="center")
