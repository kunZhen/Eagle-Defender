import shutil
from tkinter import * 
import os
from tkinter import filedialog
from facialLogic import facialRecognogtion
from User import *


class RegisterGuiPhoto: 
    def __init__(self,window,width,height,user:User,parentFrame):
        self.window = window
        self.width = width
        self.height = height
        self.user=user
        self.parentFrame=parentFrame

        self.centerX  = width/2
        centerX=self.centerX
        centrerY = width/2

        font="Helvetica"
        #Esta es el frame de esta sección
        self.registerFrame = Frame (window,width=self.width,height=self.height, bg= "green")
        self.registerFrame.pack()

        #Etiqueta
        self.registerLb = Label(self.registerFrame, text="Registro de usuario", font=(font, 35))
        self.registerLb.place(x=centerX, y=50, anchor="center")

        self.registerLb = Label(self.registerFrame, text="En esta sección debe ingresar su foto de perfil e información biométrica", font=(font, 20))
        self.registerLb.place(x=375, y=150, anchor="center")

        self.photoCanvas = Canvas(self.registerFrame, width=400, height=400)
        self.photoCanvas.place(x=centerX-100, y=230, anchor="nw")
        
        self.imagen = PhotoImage(file=os.path.abspath("Eagle%20Defender/rostros/perfil.png")) 
      
        self.photoCanvas.create_image(0, 0, anchor="nw", image=self.imagen)

        self.choosePhotoBtn = Button(self.registerFrame, text="Choose a photo", font=(font, 15),command = self.chooseAPhoto)
        self.choosePhotoBtn.place(x=centerX-200, y=650, anchor="nw")


        self.profileBtn = Button(self.registerFrame, text="Take a photo", font=(font, 15), command = self.takeAPhoto)
        self.profileBtn.place(x=centerX, y=650, anchor="nw")
        
        self.biometricalBtn = Button(self.registerFrame, text="Save your biometrical information", font=(font, 15), command = self.savePhotoInformation)
        self.biometricalBtn.place(x=centerX+200, y=650, anchor="nw")

        self.nextBtn = Button(self.registerFrame, text="Done", font=(font, 15),command = self.comeBack)
        self.nextBtn.place(x=2*centerX-100, y=650, anchor="nw")
        
    def takeAPhoto(self):
        faceInformation = facialRecognogtion(self.user.user)
        faceInformation.getFaceInformation("takeAPhoto")
    def savePhotoInformation(self): 
        faceInformation = facialRecognogtion(self.user.user)
        faceInformation.getFaceInformation("saveInformation")
    
    def chooseAPhoto(self):
        imagePath= filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg *.png *.gif *.bmp *.svg")])
        faceInformation = facialRecognogtion(self.user.user)
        faceInformation.savePhoto(imagePath)
       
        
        self.photoCanvas.delete("all")

        # Cargar la nueva imagen
        newImage = PhotoImage(file=imagePath)
        

        # Mostrar la nueva imagen en el Canvas
        self.photoCanvas.create_image(0, 0, anchor="nw", image=newImage)

        # Asigna la nueva imagen a la variable de instancia
        self.imagen = newImage
    def comeBack(self):
        self.registerFrame.pack_forget()
        self.parentFrame.pack()
        



