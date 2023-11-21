import os
from PIL import Image, ImageTk
import tkinter as tk

class HelpSection: 
    def __init__(self, window, width, height, parent):
        self.window = window
        self.width = width
        self.height = height

        centerX = width / 2
        centerY = height / 2
        self.parent=parent
        font = "Helvetica"

        colorPalette = ["#8B0000", "#630000", "#1C1C1C", "#000000", "#FFFFFF"]

        self.attackerControls = Image.open("Code/GraphicalUserInterface/GameData/Control-Attacker.png").resize((700,650))
        self.attackerControls = ImageTk.PhotoImage(self.attackerControls)

        self.defenderControls = Image.open("Code/GraphicalUserInterface/GameData/Control-Defender.png").resize((700,650))
        self.defenderControls = ImageTk.PhotoImage(self.defenderControls)

        # frames are used to facilitate the creation and deletion of screens
        self.initialFrame = tk.Frame(self.window, width=self.width, height=self.height, bg="black")
        self.initialFrame.pack()

        # is replaced by the logo
        # Lb: Label. Specify the type of element
        self.Canvas = tk.Canvas(self.initialFrame, width=self.width, height=self.height, bg=colorPalette[1])
        self.Canvas.pack()
        self.Canvas.config(borderwidth=0, highlightthickness=0)

        self.returnBtn = tk.Button(self.Canvas, text="Retornar al menu", command=self.backToMenu )
        self.returnBtn.place(x=self.width/2-50, y=self.height-75)
        
        # Create images on the canvas
        self.Canvas.create_image(self.width//2+530, self.height//2-75, image=self.attackerControls) # (Attacker controls)
        self.Canvas.create_image(self.width//2-530, self.height//2-75, image=self.defenderControls) # (Defender controls)
        self.Canvas.create_text(centerX, 60, text="Controles de juego", font=(font, 50))
    
    def backToMenu(self):
        self.initialFrame.pack_forget()
        self.parent.pack()