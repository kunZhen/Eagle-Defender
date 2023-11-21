import time
from tkinter import *
from musicLogic import musicLogic
from versusGame import versusGame 
from jsonManager import JsonManager
from musicControl import MusicControl
from modificateDataGui import *
import helpSection
import hallOfFameGui
import tkinter as tk
import temporalGui
from User import *


class PrincipalGui:
    def __init__(self, window:tk.Tk, width, height, users):
        self.window = window
        self.width = width
        self.height = height
        self.users = users

        self.players = []
        self.jsonManager = JsonManager()
        self.musicControl:MusicControl = MusicControl()
        self.logo = PhotoImage(file=os.path.abspath("Code/GraphicalUserInterface/GameData/EagleDefender.png"))

        font = "Helvetica"

        #-------------------[Music playlist and timer settings]--------------------#
        self.musicManager = musicLogic()
        self.songNumber = 1
        self.musicTimer = 0

        #-------------------[Music playlist and timer settings]--------------------#

        colorPalette = ["#8B0000", "#630000", "#1C1C1C", "#000000", "#FFFFFF"]
        self.colorPalette=colorPalette
        centerX = width / 2
        self.centerX=centerX
        centerY = height / 2
        self.centerY=centerY

        self.principalFrame = Frame(window, width=width, height=height, bg=colorPalette[0])
        self.principalFrame.pack()

        self.hallOfFameFrameOnTop = Frame(self.principalFrame, width=width - (width / 19.2), height=height - (height / 10.8), bg=self.colorPalette[2])
        self.hallOfFameFrameOnTop.place(x=centerX, y=centerY, anchor="center")

        self.logoCanva = Canvas(self.hallOfFameFrameOnTop, width=400, height=580, bg=self.colorPalette[2])
        self.logoCanva.config(borderwidth=0, highlightthickness=0)
        self.logoCanva.place(x=centerX - (centerX / 18), y=centerY, anchor="center")
        self.logoCanva.create_image(200, 290, anchor="center", image=self.logo)

        self.titleLb = Label(self.principalFrame, text="Eagle Defender", font=(font, 50))
        self.titleLb.config(bg=self.colorPalette[2], fg=self.colorPalette[4])
        self.titleLb.place(x=centerX, y=centerY - (height / 2.8), anchor="center")

        self.user1Btn = Button(self.principalFrame, text=users[0], font=(font, 15), command=self.changeDataUser1)
        self.user1Btn.config(bg=colorPalette[2], fg=colorPalette[4])

        self.user2Btn = Button(self.principalFrame, text=users[1], font=(font, 15), command=self.changeDataUser2)
        self.user2Btn.config(bg=colorPalette[2], fg=colorPalette[4])

        self.user1Btn.place(x=75, y=75, anchor="nw")
        self.user2Btn.place(x=width - 75, y=75, anchor="ne")

        self.playBtn = Button(self.principalFrame, text="Jugar", font=(font, 15), command=self.play)
        self.playBtn.config(bg=colorPalette[2], fg=colorPalette[4])

        self.hallFameBtn = Button(self.principalFrame, text="Salón de la Fama", font=(font, 15), command=self.showHallOfFame)
        self.hallFameBtn.config(bg=colorPalette[2], fg=colorPalette[4])

        self.helpBtn = Button(self.principalFrame, text="Manual de Instrucciones", font=(font, 15), command=self.showHelp)
        self.helpBtn.config(bg=colorPalette[2], fg=colorPalette[4])

        self.playBtn.place(x=centerX, y=centerY + (height / 3), anchor="center")
        self.hallFameBtn.place(x=centerX, y=centerY + (height / 2.6), anchor="center")
        self.helpBtn.place(x=centerX, y=centerY + (height / 2.3), anchor="center")

        self.getPlayers()
        self.__setUpFameLabels()

        #self.startPlaylist()

    def changeDataUser1(self):
        self.principalFrame.pack_forget()
        app = modificateDataGui(self.window, self.width, self.height, self.users[0], self, 0)

    def changeDataUser2(self):
        self.principalFrame.pack_forget()
        app = modificateDataGui(self.window, self.width, self.height, self.users[1], self, 1)

    def updateLb(self):
        self.user1Btn.config(text=self.users[0])
        self.user2Btn.config(text=self.users[1])

    def tempFrame(self):
        self.temporalFrame = temporalGui.temporalFrame(self.window, self.width, self.height,self.principalFrame)
   
        self.window.update_idletasks()  # Forzar la actualización de la interfaz gráfica

    def play(self): 
        self.principalFrame.pack_forget()
        self.tempFrame()

        self.window.after(500, self.afterFrame)
    
    def showHallOfFame(self):
        self.principalFrame.pack_forget()
        frame = hallOfFameGui.HallOfFameGui(self.principalFrame, self.window, self.width, self.height)

    def showHelp(self):
        self.principalFrame.pack_forget()
        self.frame = helpSection.HelpSection(self.window, self.width, self.height, self.principalFrame)
        
    def afterFrame(self):
        user1=User.LoadJson(self.users[0])
        user2=User.LoadJson(self.users[1])
        
        new = versusGame(self.window, self.width, self.height, [user2, user1], self.principalFrame, self.temporalFrame.initialFrame, None)
                
    def prueba(self, temporalFrame):
        self.play()

    def startPlaylist(self):
        songName = f"default{self.songNumber}"
        if(self.musicTimer==0):
            # If the timer is staring or has been reset it sets to a time counter(in seconds)
            self.musicTimer = time.time()
            self.musicManager.setUpMusic(f"Code/GraphicalUserInterface/songs/{songName}.mp3")
        if(self.musicTimer==275):
            # Reset the music timer back to 0
            self.muiscTimer = 0
            # Update the song number once 300 seconds have passed
            self.songNumber+=1
            # If the songnumber has exceeded the 3 maximum; resets it to 1
            if (self.songNumber>3):
                self.songNumber = 1
        self.window.after(100, self.startPlaylist)

    # ----- [Hall of Fame] ----- #
    def __setUpFameLabels(self):
        pX = int((self.width) / 4)
        pY = int((self.height) / 5)
        cont = 0

        if self.players != []:
            for player in self.players:
                cont += 1
                
                hallName = Label(self.hallOfFameFrameOnTop, text=f"{cont}. {player['name']}", font=("Helvetica", 20))
                hallName.config(bg=self.colorPalette[2], fg=self.colorPalette[4])
                hallName.place(x=pX, y=pY, anchor="center")

                hallTime = Label(self.hallOfFameFrameOnTop, text=f"{player['time']}", font=("Helvetica", 20))
                hallTime.config(bg=self.colorPalette[2], fg=self.colorPalette[4])   
                hallTime.place(x= pX + int((self.width) / 2), y=pY, anchor="center")


                pY += int((self.height) / 14 )

    def getPlayers(self):
        self.players = self.jsonManager.readJson('Code/GraphicalUserInterface/GameData/playersFame.json')['results']
    

if __name__ == "__main__":
    root = tk.Tk()
    screenWidth = root.winfo_screenwidth() - 100
    screenheight = root.winfo_screenheight() - 100
    print(screenWidth, screenheight)
    root.geometry(f"{screenWidth}x{screenheight}")
    new = PrincipalGui(root, screenWidth, screenheight, ["kin@gmail.com", "isaac@gmail.com"])
    root.mainloop()

        
