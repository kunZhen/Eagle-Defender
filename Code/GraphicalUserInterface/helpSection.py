import helpSectionSecondPart
from PIL import Image, ImageTk
import tkinter as tk

class HelpSection: 
    def __init__(self, window, width, height, parent):
        self.window = window
        self.width = width
        self.height = height

        self.centerX = width / 2
        self.centerY = height / 2
        self.parent=parent
        font = "Helvetica"

        colorPalette = ["#8B0000", "#630000", "#1C1C1C", "#000000", "#FFFFFF"]

        # Imagen del aguila
        self.eagle = Image.open("Code/GraphicalUserInterface/sprites/Eagle.png").resize((50,50))
        self.eagle = ImageTk.PhotoImage(self.eagle)

        # Imagenes del Defensor

        self.cross = Image.open("Code/GraphicalUserInterface/sprites/defender/cross.png").resize((50,50))
        self.cross = ImageTk.PhotoImage(self.cross)

        self.metal = Image.open("Code/GraphicalUserInterface/sprites/defender/metal1.png").resize((50,50))
        self.metal = ImageTk.PhotoImage(self.metal)

        self.stone = Image.open("Code/GraphicalUserInterface/sprites/defender/stone1.png").resize((50,50))
        self.stone = ImageTk.PhotoImage(self.stone)

        self.wood = Image.open("Code/GraphicalUserInterface/sprites/defender/wood1.png").resize((50,50))
        self.wood = ImageTk.PhotoImage(self.wood)

        # Imagenes del Atacante

        self.goblin = Image.open("Code/GraphicalUserInterface/sprites/attacker/Goblin1.png").resize((50,50))
        self.goblin = ImageTk.PhotoImage(self.goblin)

        self.fireball = Image.open("Code/GraphicalUserInterface/sprites/attacker/Fireball.png").resize((50,50))
        self.fireball = ImageTk.PhotoImage(self.fireball)

        self.powderball = Image.open("Code/GraphicalUserInterface/sprites/attacker/Powderball.png").resize((50,50))
        self.powderball = ImageTk.PhotoImage(self.powderball)

        self.waterball = Image.open("Code/GraphicalUserInterface/sprites/attacker/Waterball.png").resize((50,50))
        self.waterball = ImageTk.PhotoImage(self.waterball)

        # frames are used to facilitate the creation and deletion of screens
        self.initialFrame = tk.Frame(self.window, width=self.width, height=self.height, bg="black")
        self.initialFrame.pack()

        # is replaced by the logo
        # Lb: Label. Specify the type of element
        self.Canvas = tk.Canvas(self.initialFrame, width=self.width, height=self.height, bg=colorPalette[2])
        self.Canvas.pack()
        self.Canvas.config(borderwidth=0, highlightthickness=0)

        self.returnBtn = tk.Button(self.Canvas, text="Continuar", command=self.nextPage)
        self.returnBtn.place(x=self.width/2-50, y=self.height-75)
        
        # Create images on the canvas
        self.Canvas.create_image(self.centerX - (self.width / 2.5), self.centerY - (self.height / 3), image=self.eagle) 

        self.Canvas.create_image(self.centerX - (self.width / 2.5), self.centerY - (self.height / 4) + 100, image=self.cross)
        self.Canvas.create_image(self.centerX - (self.width / 2.5), self.centerY - (self.height / 6) + 200, image=self.metal) 
        self.Canvas.create_image(self.centerX - (self.width / 2.5) + 75, self.centerY - (self.height / 6) + 200, image=self.stone)
        self.Canvas.create_image(self.centerX - (self.width / 2.5) + 150, self.centerY - (self.height / 6) + 200, image=self.wood)

        self.Canvas.create_image(self.centerX - (self.width / 2.5), self.centerY + 200, image=self.goblin)
        self.Canvas.create_image(self.centerX - (self.width / 2.5), self.centerY - (self.height / 13) + 400, image=self.fireball)
        self.Canvas.create_image(self.centerX - (self.width / 2.5) + 75, self.centerY - (self.height / 13) + 400, image=self.powderball)
        self.Canvas.create_image(self.centerX - (self.width / 2.5) + 150, self.centerY - (self.height / 13) + 400, image=self.waterball)

        self.Canvas.create_text(self.centerX, self.centerY - (self.height / 3), text="Águila que coloca el defensor", font=(font, 20), fill="white")
        self.Canvas.create_text(self.centerX, self.centerY - (self.height / 4) + 100, text="Defensor: colocas obstáculos que protegen al águila", font=(font, 20), fill="white")
        self.Canvas.create_text(self.centerX, self.centerY - (self.height / 6) + 200, text="Obstáculos: metal, piedra y madera", font=(font, 20), fill="white")
        self.Canvas.create_text(self.centerX, self.centerY + 200, text="Atacante: lanza poderes que derriban los obstáculos con el fin de atacar el águila", font=(font, 20), fill="white")
        self.Canvas.create_text(self.centerX, self.centerY - (self.height / 13) + 400, text="Poderes: fuego, pólvora y agua", font=(font, 20), fill="white")

        self.Canvas.create_text(self.centerX, 60, text="Instrucciones del juego", font=(font, 50), fill=colorPalette[1])
    
    def nextPage(self):
        self.initialFrame.pack_forget()
        self.frame = helpSectionSecondPart.HelpSection(self.window, self.width, self.height, self.parent)