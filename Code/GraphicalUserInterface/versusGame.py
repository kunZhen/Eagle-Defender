import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

import math
import os
import time

from musicLogic import *
from User import *

import random
import hallOfFameGui
from temporalGui import temporalFrame

import socket
from threading import Thread


class versusGame:
    def __init__(self, window:tk.Tk, w:int, h:int, users:list, parentFrame, temporalFrame, points:list[int, int] | None):
        #----------------------------PLayer preference setup setup---------------------------#
            #Load players json here:
        self.defenderUser:User=users[0]
        self.attackerUser:User=users[1]

        print(f"Attacker:{self.attackerUser.user} ; Defender:{self.defenderUser.user}")
            #Load players json here:

        # ---> Load the pointers for each player <---
        self.lastround = False
        self.defenderPoints = 0
        self.attackerPoints = 0
        if points is not None:
            self.defenderPoints = points[0]
            self.attackerPoints = points[1]
            self.lastround = True

        print(f"ATK pts: {self.attackerPoints} | DEF pts: {self.defenderPoints}")

        # ---> Retrieving players proffile pictures <---
        self.Profile1 = Image.open("Code/GraphicalUserInterface/Profile/perfil.png")
        self.Profile2 = Image.open("Code/GraphicalUserInterface/Profile/perfil.png")

        # ---> Logic for texture setup <---
        self.textures = self.defenderUser.textures

        # ---> Logic for animation setup <---
        self.animations = self.attackerUser.animation

        self.defenderPalette = self.defenderUser.color
        self.attackerPalette = self.attackerUser.color

        self.font = ("Helvetica", 18)
        colorPalette = ["#8B0000", "#630000", "#1C1C1C", "#000000", "#FFFFFF"]

        
        #----------------------------Screen setup---------------------------#
        self.window = window
        self.window.protocol("WM_DELETE_WINDOW", self.closeControlConnection)
        self.window.title("EagleDefender: Offline Mode")
        self.width = w
        self.height = h
        self.parentFrame=parentFrame
        self.temporalFrame=temporalFrame

        self.mainframe = tk.Frame(self.window, width= self.width, height= self.height)
        

        self.canvas = tk.Canvas(self.mainframe, width= self.width, height=self.height, bg="black")
        self.canvas.pack()

        #Set the defender side screen
        self.canvas.create_rectangle(0, 0, self.width//2, self.height, fill=self.defenderPalette[0])

        #Set the attacker side screen
        self.canvas.create_rectangle(self.width, 0, self.width//2, self.height, fill=self.attackerPalette[0])

        #Set the screen division line
        self.canvas.create_rectangle(self.width//2-10, 0, self.width//2+10, self.height, fill=colorPalette[0])
        self.canvas.create_rectangle(self.width//2-5, 0, self.width//2+5, self.height, fill="black")

        #Set up the profile buttons
        self.buttonDefender = tk.Button( self.canvas, text=f"{self.defenderUser.user}", command=lambda: self.ShowLabels(True, False) )
        self.buttonDefender.place(x=10, y=15)

        self.buttonAttacker = tk.Button( self.canvas, text=f"{self.attackerUser.user}", command=lambda: self.ShowLabels(False, True) )
        self.buttonAttacker.place(x=self.width-120, y=15)
        """"self.pauseBtn=tk.Button(self.canvas, text="▶", command=self.pauseFunction)
        self.pauseBtn.config(bg=colorPalette[2], fg=colorPalette[4])
        self.pauseBtn.place(x= (self.width/2), y=80, anchor="nw")"""


        #----------------------------------Game time-------------------------------------#
        self.musicLogicControler=musicLogic()
        
        randNumber1=random.randint(0,len(self.attackerUser.music)-1)
        attackerSong = self.attackerUser.music[randNumber1][1][0]
        self.attackerTime= self.musicLogicControler.duration(attackerSong)

        randNumber2=random.randint(0,len(self.defenderUser.music)-1)
        defenderSong = self.defenderUser.music[randNumber2][1][0]
        self.defenderTime=self.musicLogicControler.duration(defenderSong)

        print(self.attackerTime, self.defenderTime)

        self.timeLb=tk.Label(self.canvas, text=f"Tiempo restante: {self.defenderTime}s", font=("Helvetica", 35))
        self.timeLb.place(x=self.width/2, y=25,  anchor="center")
        self.timeLb.config(bg=colorPalette[0], fg=colorPalette[3])
        self.inicialGameTime=time.time()
        self.playerGaming="defender"

        # Get the regen times for each user based on their song
        print(self.defenderUser.music[randNumber2][0][1], self.attackerUser.music[randNumber1][0][1])
        self.defenderRegen = self.musicLogicControler.generateTimer(self.defenderUser.music[randNumber2][0][1], self.defenderTime) # In ms
        self.defenderRegen = self.defenderRegen/1000 # Cast to seconds

        self.attackerRegen = self.musicLogicControler.generateTimer(self.attackerUser.music[randNumber1][0][1], self.attackerTime)
        self.attackerRegen = (1/(self.attackerRegen/1000))*100 # Cast to seconds

        print(f"Attacker:{self.attackerRegen} s ", f"Defender:{self.defenderRegen} s")
        
        #---------------------------------------------------------------------------------#

        #----------------------------Defender Settings----------------------#

        self.defenderAngle = 0
        self.defenderPos = [100, self.height//2]
        self.defenderOpenImage = Image.open("Code/GraphicalUserInterface/sprites/defender/cross.png")
        self.defenderPhotoImage = self.DefenderRotate(self.defenderOpenImage)
        self.defender = self.canvas.create_image(self.defenderPos[0], self.defenderPos[1], image=self.defenderPhotoImage)

        self.pickUpState = [True, "Eagle", 0] # This variable holds the currently held block
        self.wallList = list()

        #Placing the Eagle
        self.eagleAlive = True
        self.ondefense = True
        self.placingEagle = True
        self.eagleOpenImage = Image.open("Code/GraphicalUserInterface/sprites/Eagle.png")
        self.eaglePhotoImage = ImageTk.PhotoImage(self.eagleOpenImage)

        self.currentSelection = self.canvas.create_image(self.defenderPos[0], self.defenderPos[1], image= self.eaglePhotoImage)
        self.canvas.tag_raise(self.defender)

        #Blocks
        self.maxBlocks = 10 # Limit of block in-game

        #--------Load wood textures--------#
        self.woodOpenImage = Image.open(f"Code/GraphicalUserInterface/sprites/defender/wood{self.textures}.png")
        self.woodReserve = 10
        """self.woodOnScreen = 0 PROTOTYPE"""
        
        #--------Load stone textures--------#
        self.stoneOpenImage = Image.open(f"Code/GraphicalUserInterface/sprites/defender/stone{self.textures}.png")
        self.stoneReserve = 10
        """self.stoneOnScreen = 0 PROTOTYPE"""

        #--------Load metal textures--------#
        self.metalOpenImage = Image.open(f"Code/GraphicalUserInterface/sprites/defender/metal{self.textures}.png")
        self.metalReserve = 10
        """self.metalReserve = 0 PROTOTYPE"""
        #----------------------------Attacker Settings----------------------#
        self.playerAngle = 180
        self.attackerPos = [self.width//2+100, self.height//2]
        self.attackerOpenImage=Image.open(f"Code/GraphicalUserInterface/sprites/attacker/Goblin{self.attackerUser.avatar}.png").resize((80,80))
        self.attackerPhotoImage = self.AttackerRotate(self.attackerOpenImage)
        self.attacker= self.canvas.create_image(self.attackerPos[0],self.attackerPos[1],image=self.attackerPhotoImage)

        self.animationsList = []
        #Load the fireball png and animation
        self.fireAnimOpen = Image.open(f"Code/GraphicalUserInterface/sprites/attacker/Fire{self.animations}.png")

        self.firepngOpen = Image.open("Code/GraphicalUserInterface/sprites/attacker/Fireball.png")
        self.firepngOpen = self.firepngOpen.resize((85, 85))
            #Setup firebal dmg
        self.fireDMG = 4

        #Load the waterball png
        self.waterAnimOpen = Image.open(f"Code/GraphicalUserInterface/sprites/attacker/Water{self.animations}.png")

        self.waterpngOpen = Image.open("Code/GraphicalUserInterface/sprites/attacker/Waterball.png")
        self.waterpngOpen = self.waterpngOpen.resize((75, 75))
            #Setup firebal dmg
        self.waterDMG = 2
        
        #Load the powderball png
        self.powderAnimOpen = Image.open(f"Code/GraphicalUserInterface/sprites/attacker/Powder{self.animations}.png")

        self.powderpngOpen = Image.open("Code/GraphicalUserInterface/sprites/attacker/Powderball.png")
        self.powderpngOpen = self.powderpngOpen.resize((75, 75))
            #Setup firebal dmg
        self.powderDMG = 10
        
        #Projectiles
        self.fireProjectiles=[]
        self.fireProjectileAmount=0
        self.waterProjectiles=[]
        self.waterProjectileAmount=0
        self.PowderProjectiles=[]
        self.PowderProjectileAmount=0
        #--------------------------Some needed variables----------------------------#
        #____RegenerateAttacks____#
        self.InicialTimeFire = 0
        self.FinalTimeFire = 0
        self.takeInicalTimeFire = True

        self.InicialTimeWater = 0
        self.FinalTimeWater = 0
        self.takeInicalTimeWater = True

        self.InicialTimePowder = 0
        self.FinalTimePowder = 0
        self.takeInicalTimePowder = True

        #____RegenerateBlocks____#
        self.InicialTimeWood = 0
        self.FinalTimeWood = 0
        self.takeInicalTimeWood = True

        self.InicialTimeStone = 0
        self.FinalTimeStone = 0
        self.takeInicalTimeStone = True

        self.InicialTimeMetal = 0
        self.FinalTimeMetal = 0
        self.takeInicalTimeMetal = True

        #_________pause_________#
        self.pause=False
        self.pauseTime=tk.IntVar()
        self.pauseTime.set(0)
        self.pausedTime=0
        

        #_________points_______#
        self.gameOver=False
        self.posiblePoints=0

        #---------------------------------------------------------------------------#

        #---------------------------Tkinter: keybind setup----------------------------------------#
        #            ______________________________________________
        #___________/Defender setup
            #Movement
        self.window.bind("<KeyPress-w>", self.Append_W)
        self.window.bind("<KeyPress-a>", self.Append_A)
        self.window.bind("<KeyPress-s>", self.Append_S)
        self.window.bind("<KeyPress-d>", self.Append_D)
            #Rotation
        self.window.bind("<KeyPress-q>", self.Append_Q)
        self.window.bind("<KeyPress-e>",self.Append_E)
            #Place block
        self.window.bind("<KeyPress-3>", self.Append_3)
        self.window.bind("<KeyPress-4>", self.Append_4)
        self.window.bind("<KeyPress-5>", self.Append_5)

        #            ______________________________________________
        #___________/Attacker setup
            #Movement
        self.window.bind("<KeyPress-i>", self.Append_I)
        self.window.bind("<KeyPress-j>", self.Append_J)
        self.window.bind("<KeyPress-k>", self.Append_K)
        self.window.bind("<KeyPress-l>", self.Append_L)
            #Rotation
        self.window.bind("<KeyPress-o>", self.Append_O)
        self.window.bind("<KeyPress-u>", self.Append_U)
            #Shoot projectiles
        self.window.bind("<KeyPress-8>", self.Append_8)
        self.window.bind("<KeyPress-9>", self.Append_9)
        self.window.bind("<KeyPress-0>", self.Append_0)
        #            ______________________________________________
        #___________/Extra setup
        self.window.bind("<KeyRelease>", self.RemoveKey)
        self.window.bind("<Escape>", self.Append_Esc) # >> For pausing the game
        self.window.bind("<Tab>", self.Append_Tab) # >> For changinng turns
        self.pressedkeys = set()

        #------------------------------UI Creation--------------------------#
        uiCoord = [225, 50] # [X, Y]

        #Common images & resources
        self.keyPng = Image.open("Code/GraphicalUserInterface/sprites/key.png")
        self.keyImage = ImageTk.PhotoImage(self.keyPng.resize((35,35)))
        self.otherKeyImage = ImageTk.PhotoImage(self.keyPng.resize((60,45)))

        # General UI
            # Point labels
        DEFPointsLabel = tk.Label(self.canvas, bg="black", fg="white", text=f"Puntos: {self.defenderPoints}")
        DEFPointsLabel.place(anchor="center", x=80, y=100)
        
        ATKPointsLabel = tk.Label(self.canvas, bg="black", fg="white", text=f"Puntos: {self.attackerPoints}")
        ATKPointsLabel.place(anchor="center", x=self.width-80, y= 100)
            # Change turn keybind
        self.canvas.create_image(35, self.height-200, image=self.otherKeyImage)
        self.canvas.create_text(36.5, self.height-197, text="Tab", fill='white', font= self.font)
        self.canvas.create_text(150, self.height-197, text="Terminar turno", fill='black', font= self.font)
            # Pause keybind
        self.canvas.create_image(35, self.height-135, image=self.otherKeyImage)
        self.canvas.create_text(36.5, self.height-132, text="Esc", fill='white', font= self.font)
        self.canvas.create_text(150, self.height-132, text="Pausar juego", fill='black', font= self.font)
        
        #Defender side
            #Wood
        self.block1pngPhoto = ImageTk.PhotoImage(self.woodOpenImage)

        self.canvas.create_rectangle(uiCoord[0]-40,uiCoord[1]-40, uiCoord[0]+40, uiCoord[1]+40,fill="red", outline="black") # Item box
        self.block1 = self.canvas.create_image(uiCoord[0],uiCoord[1], image=self.block1pngPhoto) # Block type
        self.canvas.create_image(uiCoord[0],uiCoord[1]+35, image=self.keyImage) # Key image
        self.canvas.create_text(uiCoord[0]+1, uiCoord[1]+37, text="3", fill="white", font=(self.font[0], self.font[1]-5)) # Key text
        self.canvas.create_rectangle(uiCoord[0]+15,uiCoord[1]-45, uiCoord[0]+45, uiCoord[1]-15,fill="black", outline="white") # Reserve box
        self.mats1 = self.canvas.create_text(uiCoord[0]+28.5, uiCoord[1]-27.5, text=f"{self.woodReserve}", fill="white", font=self.font) # Reserve text
        uiCoord[0]+= 100

             #Stone
        self.block2pngPhoto = ImageTk.PhotoImage(self.stoneOpenImage)

        self.canvas.create_rectangle(uiCoord[0]-40,uiCoord[1]-40, uiCoord[0]+40, uiCoord[1]+40,fill="red") # Item box
        self.block2 = self.canvas.create_image(uiCoord[0],uiCoord[1], image=self.block2pngPhoto) # Block type
        self.canvas.create_image(uiCoord[0],uiCoord[1]+35, image=self.keyImage) # Key Image
        self.canvas.create_text(uiCoord[0]+1, uiCoord[1]+37, text="4", fill="white", font=(self.font[0], self.font[1]-5)) # Key text
        self.canvas.create_rectangle(uiCoord[0]+15,uiCoord[1]-45, uiCoord[0]+45, uiCoord[1]-15,fill="black", outline="white") # Reserve box
        self.mats2 = self.canvas.create_text(uiCoord[0]+28.5, uiCoord[1]-27.5, text=f"{self.stoneReserve}", fill="white", font=self.font) # Reserve text
        uiCoord[0]+= 100

            #Metal
        self.block3pngPhoto = ImageTk.PhotoImage(self.metalOpenImage)

        self.canvas.create_rectangle(uiCoord[0]-40,uiCoord[1]-40, uiCoord[0]+40, uiCoord[1]+40,fill="red") # Item box
        self.block3 = self.canvas.create_image(uiCoord[0],uiCoord[1], image=self.block3pngPhoto) # Block type
        self.canvas.create_image(uiCoord[0],uiCoord[1]+35, image=self.keyImage) # Key Image
        self.canvas.create_text(uiCoord[0]+1, uiCoord[1]+37, text="5", fill="white", font=(self.font[0], self.font[1]-5)) # Key text
        self.canvas.create_rectangle(uiCoord[0]+15,uiCoord[1]-45, uiCoord[0]+45, uiCoord[1]-15,fill="black", outline="white") # Reserve box
        self.mats3 = self.canvas.create_text(uiCoord[0]+28.5, uiCoord[1]-27.5, text=f"{self.metalReserve}", fill="white", font=self.font) # Reserve text
        uiCoord[0]+= 995

        """   #FinishButton
        self.FinishDefenderTurnbtn=tk.Button(self.canvas, text="Listo",font=("Helvetica,15"))
        self.FinishDefenderTurnbtn.config(bg=colorPalette[2], fg=colorPalette[4], command=self.changeTurn)
        self.FinishDefenderTurnbtn.config(width=int(self.width/21.5))
        self.FinishDefenderTurnbtn.place(x=30, y=self.height-100, anchor="nw")"""
        self.defenderPlaying=True

        #Attacker side
            #Water
        self.bullet1pngOpen = self.waterpngOpen.resize((90,90))
        self.bullet1pngPhoto = ImageTk.PhotoImage(self.bullet1pngOpen)

        self.canvas.create_rectangle(uiCoord[0]-40,uiCoord[1]-40, uiCoord[0]+40, uiCoord[1]+40,fill="red") # Item box
        self.bullet1 = self.canvas.create_image(uiCoord[0], uiCoord[1]+5, image=self.bullet1pngPhoto) # Attack type
        self.canvas.create_image(uiCoord[0],uiCoord[1]+35, image=self.keyImage) # Key Image
        self.canvas.create_text(uiCoord[0]+1, uiCoord[1]+37, text="8", fill="white", font=(self.font[0], self.font[1]-5)) # Key text
        self.canvas.create_rectangle(uiCoord[0]+15,uiCoord[1]-45, uiCoord[0]+45, uiCoord[1]-15,fill="black", outline="white") # Ammo box
        self.ammo1 = self.canvas.create_text(uiCoord[0]+28.5, uiCoord[1]-27.5, text=f"{str(10-self.waterProjectileAmount)}", fill="white", font=self.font) # Ammo text
        uiCoord[0]+= 100

            #Fire
        self.bullet2pngOpen = self.firepngOpen.resize((90,90))
        self.bullet2pngPhoto = ImageTk.PhotoImage(self.bullet2pngOpen)

        self.canvas.create_rectangle(uiCoord[0]-40,uiCoord[1]-40, uiCoord[0]+40, uiCoord[1]+40,fill="red") # Item box
        self.bullet2 = self.canvas.create_image(uiCoord[0]+2, uiCoord[1]+3, image=self.bullet2pngPhoto) # Attack type
        self.canvas.create_image(uiCoord[0],uiCoord[1]+35, image=self.keyImage) # Key Image
        self.canvas.create_text(uiCoord[0]+1, uiCoord[1]+37, text="9", fill="white", font=(self.font[0], self.font[1]-5)) # Key text
        self.canvas.create_rectangle(uiCoord[0]+15,uiCoord[1]-45, uiCoord[0]+45, uiCoord[1]-15,fill="black", outline="white") # Ammo box
        self.ammo2 = self.canvas.create_text(uiCoord[0]+28.5, uiCoord[1]-27.5, text=f"{str(10-self.fireProjectileAmount)}", fill="white", font=self.font) # Ammo text
        uiCoord[0]+= 100

            #Powder
        self.bullet3pngOpen = self.powderpngOpen.resize((90,90))
        self.bullet3pngPhoto = ImageTk.PhotoImage(self.bullet3pngOpen)

        self.canvas.create_rectangle(uiCoord[0]-40,uiCoord[1]-40, uiCoord[0]+40, uiCoord[1]+40,fill="red") # Item box
        self.bullet3 = self.canvas.create_image(uiCoord[0], uiCoord[1]+3, image=self.bullet3pngPhoto) # Attack type
        self.canvas.create_image(uiCoord[0],uiCoord[1]+35, image=self.keyImage) # Key Image
        self.canvas.create_text(uiCoord[0]+1, uiCoord[1]+37, text="0", fill="white", font=(self.font[0], self.font[1]-5)) # Key text
        self.canvas.create_rectangle(uiCoord[0]+15,uiCoord[1]-45, uiCoord[0]+45, uiCoord[1]-15,fill="black", outline="white") # Ammo box
        self.ammo3 = self.canvas.create_text(uiCoord[0]+28.5, uiCoord[1]-27.5, text=f"{str(10-self.PowderProjectileAmount)}", fill="white", font=self.font) # Ammo text
        #-----------------------------------This must to be at the end-----------------------------#
        
        # Defender song 
        self.musicLogicControler.fileName="defender.mp4"

        self.musicLogicControler.downloadYoutubeAudio(defenderSong)
        self.musicLogicControler.setUpVideoMusic("Code/GraphicalUserInterface/songs/defender.mp4")
             
        # Atacker song 
        self.musicLogicControler.fileName="attacker.mp4"

        self.musicLogicControler.downloadYoutubeAudio(attackerSong)
        self.musicLogicControler.setUpVideoMusic("Code/GraphicalUserInterface/songs/attacker.mp4")

        # Setup music for the game
        self.musicLogicControler.setUpMusic("Code/GraphicalUserInterface/songs/defender.mp3")
        self.inicialGameTime=time.time()
        self.showTime(self.defenderTime)
        self.regenerateAttacks()
        self.AnimationsManager()
        self.RegenerateBlocks()

        self.mainframe.place(x=0, y=0)
        #self.temporalFrame.pack_forget()
        #------------------------------------------------------------------------------------------#

        self.ShowLabels(True, True)

        #--------------------#
        #-----Control--------#
        #--------------------#

        self.server_address = ('0.0.0.0', 12345)

        # Configuración del socket para recibir datos de la Raspberry Pi Pico W
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.server_address)

        # Bandera para indicar al hilo que debe salir del bucle
        self.controlConection = True
        #self.controlSignal = tk.StringVar()
        #self.controlSignal.set("Esperando...")

        self.main_loop()





    #----------------------Control--------------------------------------------------#  
    
    
    def receiveControlSignal(self):
        print("ENTRAMOS")
        try:
            while self.controlConection:
                data, address = self.sock.recvfrom(1024)
                #self.controlSignal.set(f' {data.decode()}')
                #--------------Attacker-------------#
                if (data.decode()=="A0"):
                    self.window.event_generate("<KeyPress>", keysym='Escape')
                    self.window.event_generate("<KeyRelease>", keysym='Escape')
                if (data.decode()=="A2"):
                    self.window.event_generate("<KeyPress>", keysym='8')
                    self.window.event_generate("<KeyRelease>", keysym='8')
                if (data.decode()=="A3"):
                    self.window.event_generate("<KeyPress>", keysym='9')
                    self.window.event_generate("<KeyRelease>", keysym='9')
                if (data.decode()=="A4"):
                    self.window.event_generate("<KeyPress>", keysym='0')
                    self.window.event_generate("<KeyRelease>", keysym='0')
                if (data.decode()=="A5"):
                    self.window.event_generate("<KeyPress>", keysym='u')
                    self.window.event_generate("<KeyRelease>", keysym='u')
                if (data.decode()=="A6"):
                    self.window.event_generate("<KeyPress>", keysym='o')
                    self.window.event_generate("<KeyRelease>", keysym='o')
                if (data.decode()=="AU"):
                    self.window.event_generate("<KeyPress>", keysym='i')
                    self.window.event_generate("<KeyRelease>", keysym='i')
                if (data.decode()=="AD"):
                    self.window.event_generate("<KeyPress>", keysym='k')
                    self.window.event_generate("<KeyRelease>", keysym='k')
                if (data.decode()=="AR"):
                    self.window.event_generate("<KeyPress>", keysym='l')
                    self.window.event_generate("<KeyRelease>", keysym='l')
                if (data.decode()=="AL"):
                    self.window.event_generate("<KeyPress>", keysym='j')
                    self.window.event_generate("<KeyRelease>", keysym='j')
                #--------------Defender-------------#
                if (data.decode()=="D5"):
                    self.window.event_generate("<KeyPress>", keysym='q')
                    self.window.event_generate("<KeyRelease>", keysym='q')
                if (data.decode()=="D6"):
                    self.window.event_generate("<KeyPress>", keysym='e')
                    self.window.event_generate("<KeyRelease>", keysym='e')
                if (data.decode()=="D0"):
                    self.window.event_generate("<KeyPress>", keysym='Escape')
                    self.window.event_generate("<KeyRelease>", keysym='Escape')
                if (data.decode()=="D1"):
                    self.window.event_generate("<KeyPress>", keysym='Tab')
                    self.window.event_generate("<KeyRelease>", keysym='Tab')
                if (data.decode()=="D2"):
                    self.window.event_generate("<KeyPress>", keysym='3')
                    self.window.event_generate("<KeyRelease>", keysym='3')
                if (data.decode()=="D3"):
                    self.window.event_generate("<KeyPress>", keysym='4')
                    self.window.event_generate("<KeyRelease>", keysym='4')
                if (data.decode()=="D4"):
                    self.window.event_generate("<KeyPress>", keysym='5')
                    self.window.event_generate("<KeyRelease>", keysym='5')
                if (data.decode()=="DU"):
                    self.window.event_generate("<KeyPress>", keysym='w')
                    self.window.event_generate("<KeyRelease>", keysym='w')
                if (data.decode()=="DD"):
                    self.window.event_generate("<KeyPress>", keysym='s')
                    self.window.event_generate("<KeyRelease>", keysym='s')
                if (data.decode()=="DR"):
                    self.window.event_generate("<KeyPress>", keysym='d')
                    self.window.event_generate("<KeyRelease>", keysym='d')
                if (data.decode()=="DL"):
                    self.window.event_generate("<KeyPress>", keysym='a')
                    self.window.event_generate("<KeyRelease>", keysym='a')

        except socket.error:
            print("ERROR")
    
    def closeControlConnection(self):
        self.controlConection = False
        self.sock.close()

    def start_reception_thread(self):
        thread_recepcion = Thread(target=self.receiveControlSignal)
        thread_recepcion.daemon = True
        thread_recepcion.start()

    def setup_socket_and_thread(self):
        self.server_address = ('0.0.0.0', 12345)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.server_address)
        self.controlConection = True
        #self.controlSignal = tk.StringVar()
        #self.controlSignal.set("Esperando...")
        self.etiqueta_mensaje = tk.Label(self.mainframe) #textvariable=self.controlSignal)
        #self.etiqueta_mensaje.place(x=self.width // 2, y=300)
        self.start_reception_thread()

    def main_loop(self):
        # Llama a este método después de crear el objeto versusGame
        # y comenzar el bucle principal de Tkinter
        self.setup_socket_and_thread()

        
    
    #----------------------Control--------------------------------------------------#  
     
     
        
    

    
    
    #--------------------------------Show Time-------------------------------------#
    def pauseFunction(self): 
        if self.pause:
            self.pause=False
            self.musicLogicControler.unpauseMusic()
        else:
            self.musicLogicControler.pauseMusic()
            self.pauseTime.set(time.time())
            self.pause=True   

    def showTime(self, gameTime): 
        currentTime=time.time()
        if not self.defenderPlaying and not self.playerGaming=="attacker": 
            self.inicialGameTime=time.time()
            gameTime=self.attackerTime
            self.playerGaming="attacker"
        if not self.pause:
            currentTime=time.time()-self.pausedTime
            if currentTime-self.inicialGameTime<=gameTime:
                self.posiblePoints=int(gameTime-(currentTime-self.inicialGameTime))
                self.timeLb.config(text=f"Tiempo restante:  {int(gameTime-(currentTime-self.inicialGameTime))}s")
                self.window.after(50, self.showTime,gameTime)
            else: 
                if self.playerGaming=="defender": 
                    self.playerGaming="attacker"
                    self.inicialGameTime=currentTime
                    self.musicLogicControler.setUpMusic("Code/GraphicalUserInterface/songs/attacker.mp3")
                    self.window.after(50, self.showTime,self.attackerTime)
                else: 
                    self.gameOverByTime()
                    self.timeLb.config(text=f"Fin")
                    self.playerGaming=None
        else: 
            self.pausedTime=currentTime-self.pauseTime.get()
            if not self.gameOver:
                self.window.after(50, self.showTime,gameTime)

    #-----------------------------------Show prompt-----------------------------------#
    def ShowLabels(self, showToDefender:bool, showToAttacker:bool):
        if self.ondefense==True:
            if showToDefender:
                prompt1 = "Rol Defensor:\nColoque el águila con teclas 3,4 or 5\nColoque sus barreras para defenderse!"
            if showToAttacker:
                prompt2 = "Rol Atacante:\nEspere a que el defensor prepare sus defensas"
        else:
            if showToDefender:
                prompt1 = "Rol Defensor:\nContinue poniendo defensas hasta que termine el tiempo"
            if showToAttacker:
                prompt2 = "Rol Atacante:\nDestruye el águila antes de que termine el tiempo"

        if showToDefender:
            #Set the Label
            text1 = tk.Label(self.canvas, text=prompt1, font=self.font, fg=self.attackerPalette[0], bg="black")
            #Get the label coordinates
            labelWidth = text1.winfo_width()
            labelHeight = text1.winfo_height()
            #Place the label
            text1.place(x=(self.width/8)-(labelWidth/2), y=self.height//4-30)
        else:
            text1 = None

        if showToAttacker:
            #Set the label
            text2 = tk.Label(self.canvas, text=prompt2, font= self.font, fg=self.defenderPalette[0], bg="black")
            #Get the label coordinates
            labelWidth = text2.winfo_width()
            labelHeight = text2.winfo_height()
            #Place the label
            text2.place(x=(self.width/2+self.width/8)-(labelWidth/2), y=self.height//4-30)
        else:
            text2 = None

        self.window.after(7000, self.RemoveLabels, text1, text2) # Remove them from screen after 7 s

    def RemoveLabels(self, text1:tk.Label, text2:tk.Label):
        if text1!=None:
            text1.destroy()
        if text2!=None:
            text2.destroy()
    #--------------------------------Common Events-------------------------------#
    def Append_Tab(self, event):
        if self.defenderPlaying:
            self.changeTurn()
        else:
            pass
    def Append_Esc(self, event):
        self.pauseFunction()
    #--------------------------------Attacker Events-------------------------------#
    def Append_W(self, event): 
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()
    def Append_A(self, event): 
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()
    def Append_S(self, event): 
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()
    def Append_D(self, event): 
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()

    def Append_Q(self, event): 
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()
    def Append_E(self, event):
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()

    def Append_3(self, event):
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()
    def Append_4(self, event):
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()
    def Append_5(self, event):
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()
    #--------------------------------Defender Events-------------------------------#
    def Append_I(self, event):
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()
    def Append_K(self, event):
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()
    def Append_L(self, event):
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()
    def Append_J(self, event):
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()

    def Append_U(self, event):
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()
    def Append_O(self, event):
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()

    def Append_8(self, event):
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()
    def Append_9(self, event):
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()
    def Append_0(self, event):
        self.pressedkeys.add(event.keysym)
        self.ComboCheck()
    #--------------------------------KeyRelease event--------------------------------#
    def RemoveKey(self, event):
        if event.keysym in self.pressedkeys:
            self.pressedkeys.remove(event.keysym)
    
    #----------------------------Check pressed keys-----------------------------------#
    def ComboCheck(self):
        if not self.pause:
            if not self.defenderPlaying :
                #-----------Attacker Controls----------#
                #Movement
                if 'l' in self.pressedkeys and self.ondefense==False:
                    if self.attackerPos[0]<self.width:
                        self.attackerPos[0]+=10
                        self.canvas.coords(self.attacker,self.attackerPos[0], self.attackerPos[1])

                if 'k' in self.pressedkeys and self.ondefense==False:
                    if self.attackerPos[1]< self.height:
                        self.attackerPos[1]+=10
                        self.canvas.coords(self.attacker,self.attackerPos[0], self.attackerPos[1])

                if 'j' in self.pressedkeys and self.ondefense==False:
                    if self.attackerPos[0]> self.width//2:
                        self.attackerPos[0]-=10
                        self.canvas.coords(self.attacker,self.attackerPos[0], self.attackerPos[1])

                if 'i' in self.pressedkeys and self.ondefense==False:
                    if self.attackerPos[1]>0:
                        self.attackerPos[1]-=10
                        self.canvas.coords(self.attacker,self.attackerPos[0], self.attackerPos[1])

                #Rotation
                if 'u' in self.pressedkeys:
                    self.playerAngle+=15
                    self.UpdateAttacker()
                if 'o' in self.pressedkeys:
                    self.playerAngle-=15
                    self.UpdateAttacker()

                #Launches
                if '8' in self.pressedkeys and self.ondefense==False:
                    self.Shoot(2)
                    self.canvas.itemconfig(self.ammo1, text=str(10-self.waterProjectileAmount))
                    self.musicLogicControler.playSFX("water")#Plays the sound effect
                if '9' in self.pressedkeys and self.ondefense==False:
                    self.Shoot(3)
                    self.canvas.itemconfig(self.ammo2, text=str(10-self.fireProjectileAmount))
                    self.musicLogicControler.playSFX("fire")#Plays the sound effect
                if '0' in self.pressedkeys and self.ondefense==False:
                    self.Shoot(1)
                    self.canvas.itemconfig(self.ammo3, text=str(10-self.PowderProjectileAmount))
                    self.musicLogicControler.playSFX("powder")#Plays the sound effect

            #----------Defender controls----------#
            #Movement
            if 'w' in self.pressedkeys:
                if self.defenderPos[1]>0:
                    self.defenderPos[1]-=10
                    self.canvas.coords(self.defender, self.defenderPos[0], self.defenderPos[1])
                    self.canvas.coords(self.currentSelection, self.defenderPos[0], self.defenderPos[1])

            
            if 's' in self.pressedkeys:
                if self.defenderPos[1]<self.height:
                    self.defenderPos[1]+=10
                    self.canvas.coords(self.defender, self.defenderPos[0], self.defenderPos[1])
                    self.canvas.coords(self.currentSelection, self.defenderPos[0], self.defenderPos[1])
            
            if 'a' in self.pressedkeys:
                if self.defenderPos[0]>0:
                    self.defenderPos[0]-=10
                    self.canvas.coords(self.defender, self.defenderPos[0], self.defenderPos[1])
                    self.canvas.coords(self.currentSelection, self.defenderPos[0], self.defenderPos[1])
            
            if 'd' in self.pressedkeys:
                if self.defenderPos[0]<self.width//2:
                    self.defenderPos[0]+=10
                    self.canvas.coords(self.defender, self.defenderPos[0], self.defenderPos[1])
                    self.canvas.coords(self.currentSelection, self.defenderPos[0], self.defenderPos[1])

            #Rotation
            if 'q' in self.pressedkeys:
                self.defenderAngle += 15
                self.UpdateDefender()
            if 'e' in self.pressedkeys:
                self.defenderAngle -= 15
                self.UpdateDefender()

            #Placement
            if '3' in self.pressedkeys and self.woodReserve>0:
                if (self.pickUpState[2]!=0 and self.pickUpState[1]=="Wood") and self.placingEagle==False:
                    self.woodReserve-=1
                    self.canvas.itemconfig(self.mats1, text=f"{self.woodReserve}")
                    self.musicLogicControler.playSFX("pop")#Plays the sound effect
                
                self.Place(1, self.defenderAngle, self.defenderPos[0], self.defenderPos[1])

            if '4' in self.pressedkeys and self.stoneReserve>0:
                if (self.pickUpState[2]!=0 and self.pickUpState[1]=="Stone") and self.placingEagle==False:
                    self.stoneReserve-=1
                    self.canvas.itemconfig(self.mats2, text=f"{self.stoneReserve}")
                    self.musicLogicControler.playSFX("pop")#Plays the sound effect

                self.Place(2, self.defenderAngle, self.defenderPos[0], self.defenderPos[1])

            if '5' in self.pressedkeys and self.metalReserve>0:
                if (self.pickUpState[2]!=0 and self.pickUpState[1]=="Metal") and self.placingEagle==False:
                    self.metalReserve-=1
                    self.canvas.itemconfig(self.mats3, text=f"{self.metalReserve}")
                    self.musicLogicControler.playSFX("pop")#Plays the sound effect

                self.Place(3, self.defenderAngle, self.defenderPos[0], self.defenderPos[1])
            #----------Defener controls----------#

    #------------------------------------------Attacker functionalities-------------------------------------------------------#
    def AttackerRotate(self,image):
        rotated = image.rotate(self.playerAngle, expand=True)
        return ImageTk.PhotoImage(rotated)
        
    def UpdateAttacker(self):
        self.attackerPhotoImage = self.AttackerRotate(self.attackerOpenImage)
        self.canvas.itemconfig(self.attacker, image=self.attackerPhotoImage)
    
    def Shoot(self, type:int):
        #Saves projectile info in array: [Label, (x,y), angle]        
        coords=self.canvas.coords(self.attacker)
        projectile=""

        if type==3 and self.fireProjectileAmount<10:
            self.fireProjectiles.append(1)
            self.fireProjectiles[self.fireProjectileAmount]=self.AttackerRotate(self.firepngOpen)

            self.generateAnimation(type, coords[0], coords[1], self.playerAngle*math.pi/180)

            projectile=self.canvas.create_image(coords[0]+10,coords[1]+10,image=self.fireProjectiles[self.fireProjectileAmount])

            self.fireProjectileAmount+=1

            self.ProjectileTravel(projectile, self.fireDMG ,self.playerAngle*math.pi/180)

        elif type==2 and self.waterProjectileAmount<10:
            self.waterProjectiles.append(1)
            self.waterProjectiles[self.waterProjectileAmount] = self.AttackerRotate(self.waterpngOpen)

            self.generateAnimation(type, coords[0], coords[1], self.playerAngle*math.pi/180)

            projectile=self.canvas.create_image(coords[0]+10,coords[1]+10,image=self.waterProjectiles[self.waterProjectileAmount])

            self.waterProjectileAmount+=1

            self.ProjectileTravel(projectile, self.waterDMG ,self.playerAngle*math.pi/180)

        elif type==1 and self.PowderProjectileAmount<10:
            self.PowderProjectiles.append(1)
            self.PowderProjectiles[self.PowderProjectileAmount] = self.AttackerRotate(self.powderpngOpen)

            self.generateAnimation(type, coords[0], coords[1], self.playerAngle*math.pi/180)

            projectile = self.canvas.create_image(coords[0]+10,coords[1]+10,image=self.PowderProjectiles[self.PowderProjectileAmount])

            self.PowderProjectileAmount+=1

            self.ProjectileTravel(projectile, self.powderDMG ,self.playerAngle*math.pi/180)
    
    def ProjectileTravel(self, projectile, dmg:int, angle):
        if not self.gameOver:
            coords=self.canvas.coords(projectile)
            newX=coords[0]+10*math.cos(angle)
            newY=coords[1]+10*math.sin(angle+math.pi)
            if not self.pause:
                self.canvas.coords(projectile, newX, newY)
            if coords[0] > 2 and coords [1]>0:
                if self.checkCollision(newX,newY, dmg) and not self.pause:
                    self.deleteBullet(projectile) 
                    pass
                else:
                    self.window.after(50, self.ProjectileTravel, projectile, dmg ,angle)
            else:
                self.deleteBullet(projectile)
         
    def deleteBullet(self, bullet):
        self.canvas.delete(bullet)

    def checkCollision(self,xPos,yPos, dmg:int): 
        counter=0
        while counter < len(self.wallList):
            wall=self.wallList[counter][0]
            coords= self.canvas.coords(wall)
            flagOne=False
            flagTwo=False
            if (abs(coords[0]-xPos)<=35):
                flagOne=True
            if (abs(coords[1]-yPos)<=30): 
                flagTwo=True
            if flagTwo and flagOne:
                #Change wall health upon impact and/or remove it from screen
                self.wallList[counter][2]-=dmg
                self.musicLogicControler.playSFX("impact")#Plays the sound effect
                if self.wallList[counter][2] <=0:
                    if counter==0: 
                        self.gameOverByattacker()
                    self.deleteWall(self.wallList[counter][0], counter)
                    self.musicLogicControler.playSFX("explosion")#Plays the sound effect
                #Return as collision DID happen
                return True
            counter+=1
        return False         
    
    def regenerateAttacks(self): 
        #Fire attacks regeneration
        if not self.pause:
            if self.fireProjectileAmount!=0: 
                if self.takeInicalTimeFire: 
                    self.InicialTimeFire=time.time()
                    self.takeInicalTimeFire=False
                else: 
                    self.FinalTimeFire=time.time()
                    if self.FinalTimeFire - self.InicialTimeFire >= self.attackerRegen: 
                        self.fireProjectileAmount-=1
                        self.canvas.itemconfig(self.ammo2, text=str(10-self.fireProjectileAmount))
                        self.InicialTimeFire=0
                        self.takeInicalTimeFire=True

            #Water attacks regeneration
            if self.waterProjectileAmount!=0: 
                if self.takeInicalTimeWater: 
                    self.InicialTimeWater=time.time()
                    self.takeInicalTimeWater=False
                else: 
                    self.FinalTimeWater=time.time()
                    if self.FinalTimeWater - self.InicialTimeWater >= self.attackerRegen: 
                        self.waterProjectileAmount-=1
                        self.canvas.itemconfig(self.ammo1, text=str(10-self.waterProjectileAmount))
                        self.InicialTimeWater=0
                        self.takeInicalTimeWater=True

            #Powder attacks regeneration
            if self.PowderProjectileAmount!=0: 
                if self.takeInicalTimePowder: 
                    self.InicialTimePowder=time.time()
                    self.takeInicalTimePowder=False
                else: 
                    self.FinalTimePowder=time.time()
                    if self.FinalTimePowder - self.InicialTimePowder >= self.attackerRegen: 
                        self.PowderProjectileAmount-=1
                        self.canvas.itemconfig(self.ammo3, text=str(10-self.PowderProjectileAmount))
                        self.InicialTimePowder=0
                        self.takeInicalTimePowder=True
        #Timer
        if not self.gameOver:
            self.window.after(50, self.regenerateAttacks)

    def generateAnimation(self, type:int ,x, y, angle):
        if type==1:
            animationPhoto = ImageTk.PhotoImage(self.powderAnimOpen.rotate(self.playerAngle))
        if type==2:
            animationPhoto = ImageTk.PhotoImage(self.waterAnimOpen.rotate(self.playerAngle))
        if type==3:
            animationPhoto = ImageTk.PhotoImage(self.fireAnimOpen.rotate(self.playerAngle))
        newX=x+70*math.cos(angle)
        newY=y+70*math.sin(angle+math.pi)
        animation = self.canvas.create_image(newX, newY, image=animationPhoto)
        self.animationsList.append([animation, animationPhoto])

    def AnimationsManager(self):
        if len(self.animationsList)>0:
            for animationTuple in self.animationsList:
                self.canvas.delete(animationTuple[0])
            self.animationsList.clear()

        self.window.after(1000, self.AnimationsManager)

    def gameOverByattacker(self): 
        self.pauseFunction()
        self.musicLogicControler.stopMusic()
        self.mainframe.destroy()
        self.controlConection = False
        self.gameOver=True
        value = [self.calculatePoints(self.posiblePoints,None,None), self.calculatePoints(self.woodReserve,self.stoneReserve,self.metalReserve)]
        print(f"Generated points by attacker:{value[0]} and defender:{value[1]}")
        if self.lastround == True:
            print(f"Player1 won with {self.defenderPoints+value[0]}")
            app = hallOfFameGui.HallOfFameGui(self.parentFrame,self.window, self.width, self.height, self.attackerUser.user, self.defenderPoints+value[0])
        else:
            self.parentFrame.pack_forget()
            self.temporalFrame = temporalFrame(self.window, self.width, self.height, self.parentFrame)
            self.window.update_idletasks()

            round2 = versusGame(self.window, self.width, self.height, [self.attackerUser, self.defenderUser], self.parentFrame, self.temporalFrame.initialFrame, [self.attackerPoints+value[0], self.defenderPoints+value[1]])
    #--------------------------------------Defender functionalities----------------------------------------------------------------#
    def DefenderRotate(self, image):
        """"""
        rotated = image.rotate(self.defenderAngle, expand=True)
        return ImageTk.PhotoImage(rotated)
    
    def UpdateDefender(self):
        """"""
        self.defenderPhotoImage = self.DefenderRotate(self.defenderOpenImage)
        self.canvas.itemconfig(self.defender, image=self.defenderPhotoImage)
        if self.pickUpState[0] == True:
            images = self.pickUpState[2]
            openImage = images[0]
            openImage = self.DefenderRotate(openImage)
            self.pickUpState[2][1] = openImage
            self.canvas.itemconfig(self.currentSelection, image=openImage)

    def Place(self, type:int, angle, X, Y):
        # >>> Current selection is none and selects the currently held one <<<
        if self.pickUpState[0] == False:
            if type == 1:
                OpenImage = self.woodOpenImage
                self.pickUpState[1] = "Wood"
            if type == 2:
                OpenImage = self.stoneOpenImage
                self.pickUpState[1] = "Stone"
            if type == 3:
                OpenImage = self.metalOpenImage
                self.pickUpState[1] = "Metal"
            OpenImage = OpenImage.resize((55,55))
            Photo_Image = self.DefenderRotate(OpenImage)
            self.pickUpState[0] = True
            self.pickUpState[2] = [OpenImage, Photo_Image]
            self.canvas.itemconfig(self.currentSelection, image=Photo_Image)
            self.canvas.tag_raise(self.defender)
        # >>> Current selection is already a block and must be placed <<<
        elif self.pickUpState[0] == True:
            if self.placingEagle==True:
                #Place the Eagle
                health = 10
                Photo_Image = self.eaglePhotoImage
                eagle_id = self.canvas.create_image(X, Y, image=Photo_Image)
                self.canvas.tag_raise(self.defender)
                self.wallList.append([eagle_id, Photo_Image, health])
                self.placingEagle = False
                self.ondefense = False
                #Modify the properties on the selection and pick up state of the game
                self.pickUpState = [False, ".", 0]
                self.canvas.itemconfig(self.currentSelection, image=self.defenderPhotoImage)
            else:
                #Set the wall-to-place properties
                if type == 1:
                    OpenImage = self.woodOpenImage
                    health = 1
                    confirm = "Wood"
                if type == 2:
                    OpenImage = self.stoneOpenImage
                    health = 6
                    confirm = "Stone"
                if type == 3:
                    OpenImage = self.metalOpenImage
                    health = 4
                    confirm = "Metal"
                #Verify if the block-to-place is the same as the one in the selection
                OpenImage = OpenImage.resize((55,55))
                Photo_Image = self.DefenderRotate(OpenImage)
                if confirm == self.pickUpState[1]:
                    #Place the block
                    wall_id = self.canvas.create_image(X, Y, image=Photo_Image)
                    self.canvas.tag_raise(self.defender)
                    self.wallList.append([wall_id, Photo_Image, health])
                    #Modify the properties on the selection and pick up state of the game
                    self.pickUpState = [False, ".", 0]
                    self.canvas.itemconfig(self.currentSelection, image=self.defenderPhotoImage)
                else:
                    #Modify the properties on the selection and pick up state of the game
                    self.pickUpState = [True, confirm, [OpenImage, Photo_Image]]
                    self.canvas.itemconfig(self.currentSelection, image=Photo_Image)
        
    def deleteWall(self, wall_id, index):
        self.canvas.delete(wall_id)
        self.wallList = self.wallList[0:index]+self.wallList[index+1:]

    def gameOverByTime(self):
        self.pauseFunction()
        self.musicLogicControler.stopMusic()
        self.mainframe.destroy()
        self.controlConection = False
        self.gameOver=True
        value = [self.calculatePoints(self.woodReserve,self.stoneReserve,self.metalReserve), self.calculatePoints(self.posiblePoints,None,None)]
        print(f"Generated points by defender:{value[0]} and attacker:{value[1]}")
        if self.lastround == True:
            print(f"Player2 won with {self.attackerPoints+value[0]}")
            app = hallOfFameGui.HallOfFameGui(self.parentFrame,self.window, self.width, self.height, self.attackerUser.user, self.attackerPoints+value[0])
        else:
            self.parentFrame.pack_forget()
            self.temporalFrame = temporalFrame(self.window, self.width, self.height, self.parentFrame)
            self.window.update_idletasks()
            round2 = versusGame(self.window, self.width, self.height, [self.attackerUser, self.defenderUser], self.parentFrame, self.temporalFrame.initialFrame, [self.attackerPoints+value[1], self.defenderPoints+value[0]])

    def RegenerateBlocks(self):
        if not self.pause and not self.playerGaming=="defender":
        #Wood blocks regeneration
            if not self.defenderPlaying:
                if self.woodReserve < self.maxBlocks: 
                    if self.takeInicalTimeWood: 
                        self.InicialTimeWood = time.time()
                        self.takeInicalTimeWood = False
                    else: 
                        self.FinalTimeWood = time.time()
                        if self.FinalTimeWood- self.InicialTimeWood >= self.defenderRegen: 
                            self.woodReserve += 1
                            self.canvas.itemconfig(self.mats1, text=f"{self.woodReserve}")
                            self.InicialTimeWood = 0
                            self.takeInicalTimeWood = True
                
                #Stone blocks regeneration
                if self.stoneReserve < self.maxBlocks: 
                    if self.takeInicalTimeStone: 
                        self.InicialTimeStone = time.time()
                        self.takeInicalTimeStone = False
                    else: 
                        self.FinalTimeStone = time.time()
                        if self.FinalTimeStone - self.InicialTimeStone >= self.defenderRegen: 
                            self.stoneReserve += 1
                            self.canvas.itemconfig(self.mats2, text=f"{self.stoneReserve}")
                            self.InicialTimeStone = 0
                            self.takeInicalTimeStone = True

                #Metal blocks regeneration
                if self.metalReserve < self.maxBlocks: 
                    if self.takeInicalTimeMetal: 
                        self.InicialTimeMetal = time.time()
                        self.takeInicalTimeMetal = False
                    else: 
                        self.FinalTimeMetal = time.time()
                        if self.FinalTimeMetal - self.InicialTimeWood >= self.defenderRegen: 
                            self.metalReserve += 1
                            self.canvas.itemconfig(self.mats3, text=f"{self.metalReserve}")
                            self.InicialTimeMetal = 0
                            self.takeInicalTimeMetal = True
            
            #Timer
        if not self.gameOver:
            self.window.after(50, self.RegenerateBlocks)

        #---------------------------------------------------General Functionalities-------------------------------------------------#
    def changeTurn(self): 
        if not self.pause:
            if not (self.ondefense):
                self.defenderPlaying=False
                #self.FinishDefenderTurnbtn.destroy()
                self.musicLogicControler.stopMusic()
                self.musicLogicControler.setUpMusic(os.path.abspath("Code/GraphicalUserInterface/songs/attacker.mp3"))
                self.ShowLabels(True, True)
            else: 
                messagebox.showwarning  ("Eagle Defender", "Debes poner el águila")

    @classmethod
    def calculatePoints(cls, param_value1: int , param_value2: int | None, param_value3: int | None):
        """
        Gets the final points of the winner side. The formula changes based on who won, if only the first parameter is specified
        then the winner is the attacker, but if the other two parameters are given then the defender won
        Parameters:
            - param_value1(int): either the currently held points(for attacker) or the remaining wood blocks(for defender)
            - param_value2(int): remaining concrete blocks
            - param_value3(int): remaining steel blocksdef test_CocineroDefender(self):
        self.assertEqual(1,1)
        Returns:
            - Points for the end of the round
        
        """
        formula = 0
        if param_value2 is None and param_value3 is None:
            formula = int((1/(param_value1)*0.5)*100000)
        elif param_value1 != 0 and param_value2 != 0 and param_value3 != 0:
            formula = int(1/(1/(param_value1*1)+1/(param_value2*6)+1/(param_value3*4))*0.5*1000)
        return formula

"""
if __name__ == "__main__":
    root = tk.Tk()
    screenWidth = root.winfo_screenwidth() 
    screenheight = root.winfo_screenheight() 
    print(screenWidth, screenheight)
    root.geometry(f"{screenWidth}x{screenheight}")
    user1=User.LoadJson("Mijo21@estudiantec.cr")
    user2=User.LoadJson("Mijo22@estudiantec.cr")
    new = versusGame(root, screenWidth, screenheight, [user2, user1], None, None, None)
    root.mainloop()
#"""