import shutil
from tkinter import * 
import os
from tkinter import filedialog
from tkinter import messagebox
from facialLogic import facialRecognogtion
from User import *


class RegisterGuiPhoto: 
    def __init__(self,window,width,height,user:User,parentFrame):
        self.window = window
        self.width = width
        self.height = height
        self.user=user
        self.parentFrame=parentFrame
        self.done=False
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

        self.registerLb = Label(self.registerFrame, text="                Está sección es para guardar su información de imagen               ", font=(font, 20))
        self.registerLb.place(x=centerX, y=125, anchor="center")

        self.photoCanvas = Canvas(self.registerFrame, width=400, height=400)
        self.photoCanvas.place(x=centerX-200, y=230, anchor="nw")
        
        self.imagen = PhotoImage(file=os.path.abspath("perfiles\perfil.png")) 
      
        self.photoCanvas.create_image(0, 0, anchor="nw", image=self.imagen)

        self.choosePhotoBtn = Button(self.registerFrame, text="Foto de perfil", width= 25,font=(font, 15),command = self.chooseAPhoto)
        self.choosePhotoBtn.place(x=centerX-460, y=650, anchor="nw")


        self.profileBtn = Button(self.registerFrame, text="Tómate una foto", width= 25,font=(font, 15), command = self.takeAPhoto)
        self.profileBtn.place(x=centerX-145, y=650, anchor="nw")
        
        self.biometricalBtn = Button(self.registerFrame, text="Datos biómetricos", width= 25,font=(font, 15), command = self.savePhotoInformation)
        self.biometricalBtn.place(x=centerX+170, y=650, anchor="nw")

        self.nextBtn = Button(self.registerFrame, text="Terminar",width= 30, font=(font, 15),command = self.comeBack)
        self.nextBtn.place(x=centerX-170, y=750, anchor="nw")
        
    def takeAPhoto(self):
        faceInformation = facialRecognogtion(self.user.user)
        faceInformation.getFaceInformation("takeAPhoto")
    def savePhotoInformation(self): 
        faceInformation = facialRecognogtion("a")
        faceInformation.getFaceInformation("saveInformation")
    
    def chooseAPhoto(self):
        imagePath = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg *.png *.gif *.bmp *.svg")])
        faceInformation = facialRecognogtion(self.user.user)
        faceInformation.savePhoto(imagePath)
    
        self.photoCanvas.delete("all")

        # Cargar la nueva imagen
        newImage = PhotoImage(file=imagePath)

        # Obtener el tamaño del Canvas
        canvasWidth = self.photoCanvas.winfo_width()
        canvasHeight = self.photoCanvas.winfo_height()

        # Redimensionar la imagen al tamaño del Canvas
        resizedImage = newImage.subsample(newImage.width() // canvasWidth, newImage.height() // canvasHeight)

        # Mostrar la nueva imagen en el Canvas
        self.photoCanvas.create_image(0, 0, anchor="nw", image=resizedImage)

        # Asigna la nueva imagen redimensionada a la variable de instancia
        self.imagen = resizedImage

    def comeBack(self):
        if self.done:
            self.registerFrame.pack_forget()
            self.parentFrame.pack()
        else:
            messagebox.showwarning("Datos biométricos",  "Debe guardar sus datos biométricos (toque el botón 'Datos biométricos')")
root = Tk()
widthScreen = root.winfo_screenwidth()
heightScreen = root.winfo_screenheight()
root.geometry(f"{widthScreen}x{heightScreen}")
root.resizable(False, False)

root.title("Eagle Defender")

app=RegisterGuiPhoto(root,widthScreen,heightScreen, NONE, NONE)


root.mainloop()


