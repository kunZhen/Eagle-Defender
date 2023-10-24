import datetime
import os
from tkinter import *
from apiX_Twitter import ApiX_Twitter
from musicControl import *
from jsonManager import JsonManager

class HallOfFameGui:
    def __init__(self,parentFrame, window, width, height, username=None, time=None):
        self.window = window
        self.width = width
        self.height = height
        self.name = username
        self.time = time  
        self.parentFrame:Frame=parentFrame
        self.publishPlayers = " --------------------- SALÓN DE LA FAMA --------------------- \n"
        self.players = []
        self.apiX_Twitter = ApiX_Twitter()
        self.jsonManager = JsonManager()
        self.musicControl:MusicControl = MusicControl()
        self.date = datetime.datetime.now()

        font = "Helvetica"

        centerX = width / 2
        centerY = height / 2

        self.colorPalette = ["#8B0000", "#630000", "#1C1C1C", "#000000", "#FFFFFF"]

        self.logo = PhotoImage(file=os.path.abspath("Code/GraphicalUserInterface/GameData/EagleDefender.png"))


        self.hallOfFameFrame = Frame(window, width=width, height=height, bg=self.colorPalette[0])
        self.hallOfFameFrame.pack()

        self.hallOfFameFrameOnTop = Frame(self.hallOfFameFrame, width=width - (width / 19.2), height=height - (height / 10.8), bg=self.colorPalette[2])
        self.hallOfFameFrameOnTop.place(x=centerX, y=centerY, anchor="center")
    
        self.logoCanva = Canvas(self.hallOfFameFrameOnTop, width=400, height=580, bg=self.colorPalette[2])
        self.logoCanva.config(borderwidth=0, highlightthickness=0)
        self.logoCanva.place(x=centerX - (centerX / 18), y=centerY, anchor="center")
        self.logoCanva.create_image(200, 290, anchor="center", image=self.logo)

        self.title = Label(self.hallOfFameFrame, text="Salón de la Fama", font=(font, 50))
        self.title.config(bg=self.colorPalette[2], fg=self.colorPalette[4])
        self.title.place(x=centerX, y=centerY - (height / 2.8), anchor="center")

        self.comeBackToMainBtn = Button(self.hallOfFameFrame, text="Regresar al menú principal", font=(font, 20), command=self.comeBackToMain)
        self.comeBackToMainBtn.place(x=centerX, y=centerY + (height / 2.8), anchor="center")
    
        self.getPlayers()
        self.updateJson()
        self.__setUpFameLabels()
        self.publishTweet()
        self.musicControl.setUpMusic("Code/GraphicalUserInterface/songs/victoryMusic.mp3")
        #self.musicControl.setUpVideoMusic("data/rosas.mp4")
        
    def __setUpFameLabels(self):
        pX = int((self.width) / 4)
        pY = int((self.height) / 5)
        cont = 0

        if self.players != []:
            self.publishPlayers = self.publishPlayers + f"Fecha y Hora: {self.date.strftime('%d/%m/%Y %H:%M:%S')} \n"
            for player in self.players:
                cont += 1
                
                hallName = Label(self.hallOfFameFrame, text=f"{cont}. {player['name']}", font=("Helvetica", 20))
                hallName.config(bg=self.colorPalette[2], fg=self.colorPalette[4])
                hallName.place(x=pX, y=pY, anchor="center")

                hallTime = Label(self.hallOfFameFrame, text=f"{player['time']}", font=("Helvetica", 20))
                hallTime.config(bg=self.colorPalette[2], fg=self.colorPalette[4])   
                hallTime.place(x= pX + int((self.width) / 2), y=pY, anchor="center")

                self.publishPlayers = self.publishPlayers + "\n" + f"{cont}. {player['name']} - {player['time']}"

                pY += int((self.height) / 14 )
            
    def getPlayers(self):
        self.players = self.jsonManager.readJson('Code/GraphicalUserInterface/GameData/playersFame.json')['results']
    
    def updateJson(self):
        if self.name is not None or self.time is not None:
            value = {"name": self.name, "time": self.time}
            print(f"self.players: {self.players}")
            self.players.append(value)
            print(f"self.players: {self.players}")
            print(f"value: {value}")
            sortedPlayers = sorted(self.players, key=lambda k: k['time'])
            
            if len (sortedPlayers) > 10:
                bestPlayers = sortedPlayers[:10]
            else: 
                bestPlayers = sortedPlayers
            
            print(f"bestPlayers: {bestPlayers}")
            self.jsonManager.writeJson({"results":bestPlayers}, 'Code/GraphicalUserInterface/GameData/playersFame.json')
            self.getPlayers()
    
    def publishTweet(self):
        self.apiX_Twitter.publishTweet(self.publishPlayers)

    def comeBackToMain(self):
        self.hallOfFameFrame.destroy()
        self.musicControl.stopMusic()
        self.parentFrame.pack()
        
