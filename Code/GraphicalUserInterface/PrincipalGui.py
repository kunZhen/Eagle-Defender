from tkinter import *

class PrincipalGui:
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height

        font = "Helvetica"

        centerX = width / 2
        centerY = height / 2

        self.principalFrame = Frame(window, width=width, height=height, bg="purple")
        self.principalFrame.pack()

        self.titleLb = Label(self.principalFrame, text="Eagle Defender", font=(font, 50))
        self.titleLb.place(x=centerX, y=75, anchor="center")

        self.user1Btn = Button(self.principalFrame, text="Usuraio", font=(font, 15))
        self.user2Btn = Button(self.principalFrame, text="Usuraio", font=(font, 15))
        self.user1Btn.place(x=75, y=75, anchor="nw")
        self.user2Btn.place(x=width - 75, y=75, anchor="ne")

        self.playBtn = Button(self.principalFrame, text="Jugar", font=(font, 15))
        self.hallFameBtn = Button(self.principalFrame, text="Salón de la Fama", font=(font, 15))
        self.helpBtn = Button(self.principalFrame, text="Sección de ayuda", font=(font, 15))
        self.playBtn.place(x=centerX, y=centerY + 150, anchor="center")
        self.hallFameBtn.place(x=centerX, y=centerY + 200, anchor="center")
        self.helpBtn.place(x=centerX, y=centerY + 250, anchor="center")
