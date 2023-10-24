from tkinter import *
from versusGame import versusGame 
from modificateDataGui import *
import tkinter as tk



class PrincipalGui:
    def __init__(self, window, width, height, users):
        self.window = window
        self.width = width
        self.height = height
        self.users = users

        font = "Helvetica"

        colorPalette = ["#8B0000", "#630000", "#1C1C1C", "#000000", "#FFFFFF"]

        centerX = width / 2
        centerY = height / 2

        self.principalFrame = Frame(window, width=width, height=height, bg=colorPalette[0])
        self.principalFrame.pack()

        self.titleLb = Label(self.principalFrame, text="Eagle Defender", font=(font, 50))
        self.titleLb.config(bg=colorPalette[0], fg=colorPalette[3])
        self.titleLb.place(x=centerX, y=75, anchor="center")

        self.user1Btn = Button(self.principalFrame, text=users[0], font=(font, 15), command=self.changeDataUser1)
        self.user1Btn.config(bg=colorPalette[2], fg=colorPalette[4])

        self.user2Btn = Button(self.principalFrame, text=users[1], font=(font, 15), command=self.changeDataUser2)
        self.user2Btn.config(bg=colorPalette[2], fg=colorPalette[4])

        self.user1Btn.place(x=75, y=75, anchor="nw")
        self.user2Btn.place(x=width - 75, y=75, anchor="ne")

        self.playBtn = Button(self.principalFrame, text="Jugar", font=(font, 15), command=self.play)
        self.playBtn.config(bg=colorPalette[2], fg=colorPalette[4])

        self.hallFameBtn = Button(self.principalFrame, text="Salón de la Fama", font=(font, 15))
        self.hallFameBtn.config(bg=colorPalette[2], fg=colorPalette[4])

        self.helpBtn = Button(self.principalFrame, text="Sección de ayuda", font=(font, 15))
        self.helpBtn.config(bg=colorPalette[2], fg=colorPalette[4])

        self.playBtn.place(x=centerX, y=centerY + 150, anchor="center")
        self.hallFameBtn.place(x=centerX, y=centerY + 200, anchor="center")
        self.helpBtn.place(x=centerX, y=centerY + 250, anchor="center")

    def changeDataUser1(self):
        self.principalFrame.pack_forget()
        app = modificateDataGui(self.window, self.width, self.height, self.users[0], self, 0)

    def changeDataUser2(self):
        self.principalFrame.pack_forget()
        app = modificateDataGui(self.window, self.width, self.height, self.users[1], self, 1)

    def updateLb(self):
        self.user1Btn.config(text=self.users[0])
        self.user2Btn.config(text=self.users[1])
    def play(self): 
        user1=User.LoadJson(self.users[0])
        user2=User.LoadJson(self.users[1])
        self.principalFrame.forget()
        new = versusGame(root, screenWidth, screenheight, [user2, user1], self.principalFrame)

if __name__ == "__main__":
    root = tk.Tk()
    screenWidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    print(screenWidth, screenheight)
    root.geometry(f"{screenWidth}x{screenheight}")
    new = PrincipalGui(root, screenWidth, screenheight, ["Frederick24", "Isaac90@gmail.com"])
    root.mainloop()

        
