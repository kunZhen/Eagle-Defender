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


class versusGame:
    def __init__(self, window:tk.Tk, w:int, h:int, users:list, parentFrame, temporalFrame):
        #----------------------------PLayer preference setup setup---------------------------#
            #Load players json here:
        self.defenderUser:User=users[0]
        self.attackerUser:User=users[1]
            #Load players json here:

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

        self.pauseBtn=tk.Button(self.canvas, text="▶", command=self.pauseFunction)
        self.pauseBtn.config(bg=colorPalette[2], fg=colorPalette[4])
        self.pauseBtn.place(x= (self.width/2), y=80, anchor="nw")


        #----------------------------------Game time-------------------------------------#
        randNumber=random.randint(0,len(self.attackerUser.music)-1)
        self.musicLogicControler=musicLogic()
        self.attackerTime= self.musicLogicControler.duration(self.attackerUser.music[randNumber][1][0])
        randNumber=random.randint(0,len(self.defenderUser.music)-1)

        self.defenderTime=self.musicLogicControler.duration(self.defenderUser.music[randNumber][1][0])
        print(self.attackerTime, self.defenderTime)

        self.timeLb=tk.Label(self.canvas, text=f"Tiempo restante: {self.defenderTime}s", font=("Helvetica", 35))
        self.timeLb.place(x=self.width/2, y=25,  anchor="center")
        self.timeLb.config(bg=colorPalette[0], fg=colorPalette[3])
        self.inicialGameTime=time.time()
        self.playerGaming="defender"

        
        #---------------------------------------------------------------------------------#

        #----------------------------Defender Settings----------------------#

        self.defenderAngle = 0
        self.defenderPos = [100, self.height//2]
        self.defenderOpenImage = Image.open("Code/GraphicalUserInterface/sprites/defender/cross.png")
        self.defenderPhotoImage = self.DefenderRotate(self.defenderOpenImage)
        self.defender = self.canvas.create_image(self.defenderPos[0], self.defenderPos[1], image=self.defenderPhotoImage)

        self.wallList = list()
        #Placing the Eagle
        self.eagleAlive = True
        self.ondefense = True
        self.placingEagle = True
        self.eagleOpenImage = Image.open("Code/GraphicalUserInterface/sprites/Eagle.png")
        self.eaglePhotoImage = ImageTk.PhotoImage(self.eagleOpenImage)

        #Blocks
        self.maxBlocks = 10
        self.woodBlocksAmount = 10
        self.stoneBlocksAmount = 10
        self.metalBlocksAmount = 10
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
        #___________/Attacker setup
            #Movement
        self.window.bind("<KeyPress-w>", self.Append_W)
        self.window.bind("<KeyPress-a>", self.Append_A)
        self.window.bind("<KeyPress-s>", self.Append_S)
        self.window.bind("<KeyPress-d>", self.Append_D)
            #Rotation
        self.window.bind("<KeyPress-q>", self.Append_Q)
        self.window.bind("<KeyPress-e>",self.Append_E)
            #Shoot projectile
        self.window.bind("<KeyPress-3>", self.Append_3)
        self.window.bind("<KeyPress-4>", self.Append_4)
        self.window.bind("<KeyPress-5>", self.Append_5)

        #            ______________________________________________
        #___________/Defender setup
            #Movement
        self.window.bind("<KeyPress-i>", self.Append_I)
        self.window.bind("<KeyPress-j>", self.Append_J)
        self.window.bind("<KeyPress-k>", self.Append_K)
        self.window.bind("<KeyPress-l>", self.Append_L)
            #Rotation
        self.window.bind("<KeyPress-o>", self.Append_O)
        self.window.bind("<KeyPress-u>", self.Append_U)
            #Place block
        self.window.bind("<KeyPress-8>", self.Append_8)
        self.window.bind("<KeyPress-9>", self.Append_9)
        self.window.bind("<KeyPress-0>", self.Append_0)
        #            ______________________________________________
        #___________/Extra setup
        self.window.bind("<KeyRelease>", self.RemoveKey)
        self.pressedkeys = set()

        #------------------------------UI Creation--------------------------#
        uiCoord = [225, 50] # [X, Y]
        
        #Defender side
            #Wood
        self.block1pngOpen = Image.open(f"Code/GraphicalUserInterface/sprites/defender/wood{self.textures}.png")
        self.block1pngPhoto = ImageTk.PhotoImage(self.block1pngOpen)
        self.canvas.create_rectangle(uiCoord[0]-40,uiCoord[1]-40, uiCoord[0]+40, uiCoord[1]+40,fill="red")
        self.block1 = self.canvas.create_image(uiCoord[0],uiCoord[1], image=self.block1pngPhoto)
        self.mats1 = self.canvas.create_text(uiCoord[0]-30, uiCoord[1]+32, text=f"{self.woodBlocksAmount}", fill="yellow", font=self.font)
        uiCoord[0]+= 100

             #Stone
        self.block2pngOpen = Image.open(f"Code/GraphicalUserInterface/sprites/defender/stone{self.textures}.png")
        self.block2pngPhoto = ImageTk.PhotoImage(self.block2pngOpen)
        self.canvas.create_rectangle(uiCoord[0]-40,uiCoord[1]-40, uiCoord[0]+40, uiCoord[1]+40,fill="red")
        self.block2 = self.canvas.create_image(uiCoord[0],uiCoord[1], image=self.block2pngPhoto)
        self.mats2 = self.canvas.create_text(uiCoord[0]-30, uiCoord[1]+32, text=f"{self.stoneBlocksAmount}", fill="yellow", font=self.font)
        uiCoord[0]+= 100

            #Metal
        self.block3pngOpen = Image.open(f"Code/GraphicalUserInterface/sprites/defender/metal{self.textures}.png")
        self.block3pngPhoto = ImageTk.PhotoImage(self.block3pngOpen)
        self.canvas.create_rectangle(uiCoord[0]-40,uiCoord[1]-40, uiCoord[0]+40, uiCoord[1]+40,fill="red")
        self.block3 = self.canvas.create_image(uiCoord[0],uiCoord[1], image=self.block3pngPhoto)
        self.mats3 = self.canvas.create_text(uiCoord[0]-30, uiCoord[1]+32, text=f"{self.metalBlocksAmount}", fill="yellow", font=self.font)
        uiCoord[0]+= 1075
            #FinishButton
        self.FinishDefenderTurnbtn=tk.Button(self.canvas, text="Listo",font=("Helvetica,15"))
        self.FinishDefenderTurnbtn.config(bg=colorPalette[2], fg=colorPalette[4], command=self.changeTurn)
        self.FinishDefenderTurnbtn.config(width=int(self.width/21.5))
        self.FinishDefenderTurnbtn.place(x=30, y=self.height-100, anchor="nw")
        self.defenderPlaying=True

        #Attacker side
            #Water
        self.bullet1pngOpen = self.waterpngOpen.resize((90,90))
        self.bullet1pngPhoto = ImageTk.PhotoImage(self.bullet1pngOpen)
        self.canvas.create_rectangle(uiCoord[0]-40,uiCoord[1]-40, uiCoord[0]+40, uiCoord[1]+40,fill="red")
        self.bullet1 = self.canvas.create_image(uiCoord[0], uiCoord[1]+5, image=self.bullet1pngPhoto)
        self.ammo1 = self.canvas.create_text(uiCoord[0]-30, uiCoord[1]+32, text=f"{str(10-self.waterProjectileAmount)}", fill="yellow", font=self.font)
        uiCoord[0]+= 100

            #Fire
        self.bullet2pngOpen = self.firepngOpen.resize((90,90))
        self.bullet2pngPhoto = ImageTk.PhotoImage(self.bullet2pngOpen)
        self.canvas.create_rectangle(uiCoord[0]-40,uiCoord[1]-40, uiCoord[0]+40, uiCoord[1]+40,fill="red")
        self.bullet2 = self.canvas.create_image(uiCoord[0]+2, uiCoord[1]+5, image=self.bullet2pngPhoto)
        self.ammo2 = self.canvas.create_text(uiCoord[0]-30, uiCoord[1]+32, text=f"{str(10-self.fireProjectileAmount)}", fill="yellow", font=self.font)
        uiCoord[0]+= 100

            #Powder
        self.bullet3pngOpen = self.powderpngOpen.resize((90,90))
        self.bullet3pngPhoto = ImageTk.PhotoImage(self.bullet3pngOpen)
        self.canvas.create_rectangle(uiCoord[0]-40,uiCoord[1]-40, uiCoord[0]+40, uiCoord[1]+40,fill="red")
        self.bullet3 = self.canvas.create_image(uiCoord[0], uiCoord[1]+5, image=self.bullet3pngPhoto)
        self.ammo3 = self.canvas.create_text(uiCoord[0]-30, uiCoord[1]+32, text=f"{str(10-self.PowderProjectileAmount)}", fill="yellow", font=self.font)
        #-----------------------------------This must to be at the end-----------------------------#
        
        #defender song#
        self.musicLogicControler.fileName="defender.mp4"
        self.musicLogicControler.downloadYoutubeAudio(self.defenderUser.music[randNumber][1][0])
             

        #atacker song#
        self.musicLogicControler.fileName="attacker.mp4"

        self.musicLogicControler.downloadYoutubeAudio(self.attackerUser.music[randNumber][1][0])
        self.musicLogicControler.setUpVideoMusic("Code/GraphicalUserInterface/songs/attacker.mp4")
        self.musicLogicControler.setUpVideoMusic("Code/GraphicalUserInterface/songs/defender.mp4")

        self.musicLogicControler.setUpMusic("Code/GraphicalUserInterface/songs/defender.mp3")
        self.inicialGameTime=time.time()
        self.showTime(self.defenderTime)
        self.regenerateAttacks()
        self.AnimationsManager()
        self.RegenerateBlocks()

        self.mainframe.place(x=0, y=0)
        self.temporalFrame.pack_forget()
        #------------------------------------------------------------------------------------------#
        
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
                    self.musicLogicControler.setUpMusic("canciones/attacker.mp3")
                    self.window.after(50, self.showTime,self.attackerTime)
                else: 
                    self.gameOverByTime()
                    self.timeLb.config(text=f"Fin")
                    self.playerGaming=None
        else: 
            self.pausedTime=currentTime-self.pauseTime.get()
            if not self.gameOver:
                self.window.after(50, self.showTime,gameTime)
    #------------------------------------------------------------------------------#
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
        #-----------Attacker Controls----------#
        #Movement
        if not self.pause:
            if not self.defenderPlaying :
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
                    self.Shoot(3)
                    self.canvas.itemconfig(self.ammo2, text=str(10-self.fireProjectileAmount))
                    self.musicLogicControler.playSFX("fire")#Plays the sound effect
                if '9' in self.pressedkeys and self.ondefense==False:
                    self.Shoot(2)
                    self.canvas.itemconfig(self.ammo1, text=str(10-self.waterProjectileAmount))
                    self.musicLogicControler.playSFX("water")#Plays the sound effect
                if '0' in self.pressedkeys and self.ondefense==False:
                    self.Shoot(1)
                    self.canvas.itemconfig(self.ammo3, text=str(10-self.PowderProjectileAmount))
                    self.musicLogicControler.playSFX("powder")#Plays the sound effect

            #----------Defener controls----------#
            #Movement
            if 'w' in self.pressedkeys:
                if self.defenderPos[1]>0:
                    self.defenderPos[1]-=10
                    self.canvas.coords(self.defender, self.defenderPos[0], self.defenderPos[1])

            
            if 's' in self.pressedkeys:
                if self.defenderPos[1]<self.height:
                    self.defenderPos[1]+=10
                    self.canvas.coords(self.defender, self.defenderPos[0], self.defenderPos[1])
            
            if 'a' in self.pressedkeys:
                if self.defenderPos[0]>0:
                    self.defenderPos[0]-=10
                    self.canvas.coords(self.defender, self.defenderPos[0], self.defenderPos[1])
            
            if 'd' in self.pressedkeys:
                if self.defenderPos[0]<self.width//2:
                    self.defenderPos[0]+=10
                    self.canvas.coords(self.defender, self.defenderPos[0], self.defenderPos[1])

            #Rotation
            if 'q' in self.pressedkeys:
                self.defenderAngle += 15
                self.UpdateDefender()
            if 'e' in self.pressedkeys:
                self.defenderAngle -= 15
                self.UpdateDefender()

            #Placement
            if '3' in self.pressedkeys and self.woodBlocksAmount>0:
                self.Place(1, self.defenderAngle, self.defenderPos[0], self.defenderPos[1])
                self.woodBlocksAmount-=1
                self.canvas.itemconfig(self.mats1, text=f"{self.woodBlocksAmount}")
                self.musicLogicControler.playSFX("pop")#Plays the sound effect

            if '4' in self.pressedkeys and self.stoneBlocksAmount>0:
                self.Place(2, self.defenderAngle, self.defenderPos[0], self.defenderPos[1])
                self.stoneBlocksAmount-=1
                self.canvas.itemconfig(self.mats2, text=f"{self.stoneBlocksAmount}")
                self.musicLogicControler.playSFX("pop")#Plays the sound effect

            if '5' in self.pressedkeys and self.metalBlocksAmount>0:
                self.Place(3, self.defenderAngle, self.defenderPos[0], self.defenderPos[1])
                self.metalBlocksAmount-=1
                self.canvas.itemconfig(self.mats3, text=f"{self.metalBlocksAmount}")
                self.musicLogicControler.playSFX("pop")#Plays the sound effect
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
        """inicialTime = time.time()  
        finalTime = inicialTime + 3  
        self.bulletTransition= ImageTk.PhotoImage(file="Code/GraphicalUserInterface/sprites/attacker/sprite.png")
        self.canvas.itemconfig(bullet, image=self.bulletTransition)
        while time.time() < finalTime:
            pass  """
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
                    if self.FinalTimeFire - self.InicialTimeFire >=15: 
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
                    if self.FinalTimeWater - self.InicialTimeWater >=15: 
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
                    if self.FinalTimePowder - self.InicialTimePowder >=15: 
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
        self.gameOver=True
        print(self.attackerTime-self.posiblePoints)
        app= hallOfFameGui.HallOfFameGui(self.parentFrame,self.window, self.width, self.height, self.attackerUser.user, self.posiblePoints)
    #--------------------------------------Defender functionalities----------------------------------------------------------------#
    def DefenderRotate(self, image):
        """"""
        rotated = image.rotate(self.defenderAngle, expand=True)
        return ImageTk.PhotoImage(rotated)
    
    def UpdateDefender(self):
        """"""
        self.defenderPhotoImage = self.DefenderRotate(self.defenderOpenImage)
        self.canvas.itemconfig(self.defender, image=self.defenderPhotoImage)
    
    def Place(self, type:int, angle, X, Y):
        if self.placingEagle==True:
            health = 30
            Photo_Image = self.eaglePhotoImage
            eagle_id = self.canvas.create_image(X, Y, image=Photo_Image)
            self.canvas.tag_raise(self.defender)
            self.wallList.append([eagle_id, Photo_Image, health])
            self.placingEagle = False
            self.ondefense = False
        else:
            if type == 1:
                OpenImage = Image.open(f"Code/GraphicalUserInterface/sprites/defender/wood{self.textures}.png")
                health = 1
            if type == 2:
                OpenImage = Image.open(f"Code/GraphicalUserInterface/sprites/defender/stone{self.textures}.png")
                health = 6
            if type == 3:
                OpenImage = Image.open(f"Code/GraphicalUserInterface/sprites/defender/metal{self.textures}.png")
                health = 4
            OpenImage = OpenImage.resize((55,55))
            Photo_Image = self.DefenderRotate(OpenImage)
            wall_id = self.canvas.create_image(X, Y, image=Photo_Image)
            self.canvas.tag_raise(self.defender)
            self.wallList.append([wall_id, Photo_Image, health])
        
    def deleteWall(self, wall_id, index):
        self.canvas.delete(wall_id)
        self.wallList = self.wallList[0:index]+self.wallList[index+1:]
    def gameOverByTime(self):
        self.pauseFunction()
        self.musicLogicControler.stopMusic()
        self.mainframe.destroy()
        self.gameOver=True
        app= hallOfFameGui.HallOfFameGui(self.parentFrame, self.window, self.width, self.height, self.attackerUser.user, self.attackerTime-self.posiblePoints)
    def RegenerateBlocks(self):
        if not self.pause and not self.playerGaming=="defender":
        #Wood blocks regeneration
            if not self.defenderPlaying:
                if self.woodBlocksAmount < self.maxBlocks: 
                    if self.takeInicalTimeWood: 
                        self.InicialTimeWood = time.time()
                        self.takeInicalTimeWood = False
                    else: 
                        self.FinalTimeWood = time.time()
                        if self.FinalTimeWood- self.InicialTimeWood >= 12: 
                            self.woodBlocksAmount += 1
                            self.canvas.itemconfig(self.mats1, text=f"{self.woodBlocksAmount}")
                            self.InicialTimeWood = 0
                            self.takeInicalTimeWood = True
                
                #Stone blocks regeneration
                if self.stoneBlocksAmount < self.maxBlocks: 
                    if self.takeInicalTimeStone: 
                        self.InicialTimeStone = time.time()
                        self.takeInicalTimeStone = False
                    else: 
                        self.FinalTimeStone = time.time()
                        if self.FinalTimeStone - self.InicialTimeStone >= 12: 
                            self.stoneBlocksAmount += 1
                            self.canvas.itemconfig(self.mats2, text=f"{self.stoneBlocksAmount}")
                            self.InicialTimeStone = 0
                            self.takeInicalTimeStone = True

                #Metal blocks regeneration
                if self.metalBlocksAmount < self.maxBlocks: 
                    if self.takeInicalTimeMetal: 
                        self.InicialTimeMetal = time.time()
                        self.takeInicalTimeMetal = False
                    else: 
                        self.FinalTimeMetal = time.time()
                        if self.FinalTimeMetal - self.InicialTimeWood >= 12: 
                            self.metalBlocksAmount += 1
                            self.canvas.itemconfig(self.mats3, text=f"{self.metalBlocksAmount}")
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
                self.FinishDefenderTurnbtn.destroy()
                self.musicLogicControler.stopMusic()
                self.musicLogicControler.setUpMusic(os.path.abspath("Code/GraphicalUserInterface/songs/attacker.mp3"))
            else: 
                messagebox.showwarning  ("Eagle Defender", "Debes poner el águila")

""""if __name__ == "__main__":
    root = tk.Tk()
    screenWidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    print(screenWidth, screenheight)
    root.geometry(f"{screenWidth}x{screenheight}")
    user1=User.LoadJson("Frederick24")
    user2=User.LoadJson("Isaac90@gmail.com")
    new = versusGame(root, screenWidth, screenheight, [user2, user1], None)
    root.mainloop()"""
