import shutil
from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox
from facialLogic import facialRecognogtion
from User import *


class RegisterGuiPhoto:
    def __init__(self, window, width, height, user: User, parentFrame):
        self.window = window
        self.width = width
        self.height = height
        self.user = user
        self.parentFrame = parentFrame
        self.done = False
        self.centerX = width / 2
        centerX = self.centerX
        centrerY = width / 2

        font = "Helvetica"

        colorPalette = ["#8B0000", "#630000", "#1C1C1C", "#000000", "#FFFFFF"]

        self.registerFrame = Frame(window, width=self.width, height=self.height, bg=colorPalette[0])
        self.registerFrame.pack()

        self.titleLb = Label(self.registerFrame, text=" Registro de usuario: \n Información de imagen ")
        self.titleLb.config(bg=colorPalette[0], fg=colorPalette[3], font=(font, 35))
        self.titleLb.place(x=centerX, y=25, anchor="n")

        self.profileCanvas = Canvas(self.registerFrame, width=400, height=400)
        self.profileCanvas.config(bg=colorPalette[1])

        self.imagen = PhotoImage(file=os.path.abspath("Code/GraphicalUserInterface/Profile/perfil.png"))
        self.profileCanvas.create_image(0, 0, anchor="nw", image=self.imagen)

        self.editBtn = Button(self.profileCanvas, text="✎", font=(font, 15), command=self.chooseAPhoto)
        self.editBtn.config(bg=colorPalette[2], fg=colorPalette[4])

        self.addBtn = Button(self.profileCanvas, text="📷", font=(font, 15), command=self.takeAPhoto)
        self.addBtn.config(bg=colorPalette[2], fg=colorPalette[4])

        self.bioBtn = Button(self.registerFrame, text="Datos biómetricos", width=30, font=(font, 15),
                             command=self.savePhotoInformation)
        self.bioBtn.config(bg=colorPalette[2], fg=colorPalette[4])

        self.nextBtn = Button(self.registerFrame, text="Finalizar", width=30, font=(font, 15), command=self.comeBack)
        self.nextBtn.config(bg=colorPalette[2], fg=colorPalette[4])

        self.profileCanvas.place(x=centerX, y=400, anchor="center")
        self.editBtn.place(x=400, y=400, anchor="se")
        self.addBtn.place(x=340, y=400, anchor="se")
        self.bioBtn.place(x=centerX, y=650, anchor="center")
        self.nextBtn.place(x=centerX, y=750, anchor="center")

    # ------------------------------------------------------------------------------------------------------------------- #

    def takeAPhoto(self):
        faceInformation = facialRecognogtion(self.user.user)
        faceInformation.getFaceInformation("takeAPhoto")

    def savePhotoInformation(self):
        faceInformation = facialRecognogtion(self.user.user)
        faceInformation.getFaceInformation("saveInformation")
        self.done = True

    def chooseAPhoto(self):
        imagePath = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg *.png *.gif *.bmp *.svg")])
        faceInformation = facialRecognogtion(self.user.user)
        faceInformation.savePhoto(imagePath)

        self.profileCanvas.delete("all")

        # Cargar la nueva imagen
        newImage = PhotoImage(file=imagePath)

        # Obtener el tamaño del Canvas
        canvasWidth = self.profileCanvas.winfo_width()
        canvasHeight = self.profileCanvas.winfo_height()

        # Redimensionar la imagen al tamaño del Canvas
        resizedImage = newImage.subsample(newImage.width() // canvasWidth, newImage.height() // canvasHeight)

        # Mostrar la nueva imagen en el Canvas
        self.profileCanvas.create_image(0, 0, anchor="nw", image=resizedImage)

        # Asigna la nueva imagen redimensionada a la variable de instancia
        self.imagen = resizedImage

    def comeBack(self):
        if self.done:
            self.registerFrame.pack_forget()
            self.parentFrame.pack()
        else:
            messagebox.showwarning("Datos biométricos",
                                   "Debe guardar sus datos biométricos (toque el botón 'Datos biométricos')")
