import os
import tkinter
from PIL import Image, ImageTk
import tkinter as tk

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

        self.logo = tk.PhotoImage(file=os.path.abspath("Code/GraphicalUserInterface/GameData/EagleDefender.png"))

        self.attackerControls = Image.open("Code/GraphicalUserInterface/GameData/Control-Attacker2.png").resize((780,700))
        self.attackerControls = ImageTk.PhotoImage(self.attackerControls)

        self.defenderControls = Image.open("Code/GraphicalUserInterface/GameData/Control-Defender2.png").resize((780,700))
        self.defenderControls = ImageTk.PhotoImage(self.defenderControls)

        # frames are used to facilitate the creation and deletion of screens
        self.initialFrame = tk.Frame(window, width=self.width, height=self.height, bg="black")
        self.initialFrame.pack()

        # is replaced by the logo
        # Lb: Label. Specify the type of element
        self.titleCanvas = tk.Canvas(self.initialFrame, width=self.width, height=self.height, bg=colorPalette[1])
        self.titleCanvas.pack()
        self.titleCanvas.config(borderwidth=0, highlightthickness=0)

        self.titleLb = tk.Label(self.titleCanvas, text="Eagle Defender", font=(font, 50))
        self.titleLb.config(bg=colorPalette[1], fg=colorPalette[3])
        self.titleLb.place(x=centerX, y=100, anchor="center")
        # Create images on the canvas
        self.titleCanvas.create_image(self.width//2, self.height//2, image=self.logo) # (Logo)
        self.titleCanvas.create_image(self.width//2+530, self.height//2-75, image=self.attackerControls) # (Attacker controls)
        self.titleCanvas.create_image(self.width//2-530, self.height//2-75, image=self.defenderControls) # (Defender controls)


        self.titleLb = tk.Label(self.titleCanvas, text="Cargando datos...", font=(font, 50))
        self.titleLb.config(bg=colorPalette[1], fg=colorPalette[3])
        self.titleLb.place(x=centerX, y=2*centerY-200, anchor="center")
