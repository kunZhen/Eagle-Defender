from tkinter import *
from tkinter import ttk,filedialog,messagebox
from User import *
import tkinter
from User import *
from facialLogic import *
from musicLogic import *
import tkinter.simpledialog
from PrincipalGui import *
import PrincipalGui

class modificateDataGui:
    def __init__(self, window, width, height,user, parent:PrincipalGui, number):
        self.window = window
        self.width = width
        self.height = height
        self.user:User=User.LoadJson(user)
        self.auxUser:User=user
        self.songs=self.user.music
        self.controler=musicLogic()
        self.parent:PrincipalGui=parent
        self.number=number

        font = "Helvetica"

        centerX = width / 2
        centerY = height / 2

        self.dataFrame = Frame(window, width=width, height=height, bg="purple")
        self.dataFrame.pack()


        self.dataLb = Label(self.dataFrame, text=f"         Cambio de datos ({self.user.user})        ", font=(font, 35))
        self.dataLb.place(x=centerX, y=50, anchor="center")

        self.registerLb = Label(self.dataFrame, text="                                   En esta sección puede" 
                                +" modificar su información general                                          ", font=(font, 20))
        self.registerLb.place(x=centerX, y=125, anchor="center")
        
        
         #_________________________________General data__________________________________________#
        self.questionOneLb= Label (self.dataFrame, text="Cambiar su nombre de usuario", font=(font,15))
        self.questionOneLb.place(x=centerX-500, y=200, anchor="center")
        self.questionOneEntry= Entry(self.dataFrame,width=25, font=(font, 15))
        self.questionOneEntry.place(x=centerX-500, y=250, anchor="center")

        self.questionTwoLb= Label (self.dataFrame, text="Cambiar su correo", font=(font,15))
        self.questionTwoLb.place(x=centerX-500, y=300, anchor="center")
        self.questionTwoEntry= Entry(self.dataFrame,width=25, font=(font, 15))
        self.questionTwoEntry.place(x=centerX-500, y=350, anchor="center")

        self.questionThreeLb= Label (self.dataFrame, text="Cambiar su contraseña", font=(font,15))
        self.questionThreeLb.place(x=centerX-500, y=400, anchor="center")
        self.questionThreeEntry= Entry(self.dataFrame,width=25, font=(font, 15))
        self.questionThreeEntry.place(x=centerX-500, y=450, anchor="center")

        self.questionFourLb= Label (self.dataFrame, text="Confirme su contraseña", font=(font,15))
        self.questionFourLb.place(x=centerX-500, y=500, anchor="center")
        self.questionFourEntry= Entry(self.dataFrame,width=25, font=(font, 15))
        self.questionFourEntry.place(x=centerX-500, y=550, anchor="center")

        self.nextBtn = Button(self.dataFrame, text="Terminar", font=(font, 15), command= self.nextPage)
        self.nextBtn.place(x=2*centerX-100, y=650, anchor="nw")
        #_____________________________________________________________________________________#

        #_______________________________Change favorite color_________________________________#
        self.colorVar = StringVar()
        self.colorVar.set("default")

        Radiobutton(self.dataFrame, text="Rojo     ", variable=self.colorVar, font=(font,15), width=8, value="red", command=self.showColor).place(x=centerX-225, y=250, anchor="center")
        Radiobutton(self.dataFrame, text="Verde   ", variable=self.colorVar, font=(font,15), width=8, value="green", command=self.showColor).place(x=centerX-225, y=300, anchor="center")
        Radiobutton(self.dataFrame, text="Azul     ", variable=self.colorVar, font=(font,15), width=8,value="blue", command=self.showColor).place(x=centerX-225, y=350, anchor="center")
        Radiobutton(self.dataFrame, text="Amarillo", variable=self.colorVar, font=(font,15), width=8, value="yellow", command=self.showColor).place(x=centerX-225, y=400, anchor="center")
        Radiobutton(self.dataFrame, text="Naranja", variable=self.colorVar, font=(font,15), width=8, value="orange", command=self.showColor).place(x=centerX-225, y=450, anchor="center")
        Radiobutton(self.dataFrame, text="Morado", variable=self.colorVar, font=(font,15), width=8, value="violet", command=self.showColor).place(x=centerX-225, y=500, anchor="center")

        self.colorLabel = Label(self.dataFrame, text="Cambie su color favorito", font=(font, 15))
        self.colorLabel.place(x=centerX-225, y=200, anchor="center")
        #____________________________________________________________________________________#

        #__________________________Change Favorite Song______________________________________#
        self.chosenSong = tkinter.StringVar()
        self.songsListsLb = Label(self.dataFrame, text="Lista de canciones", font=(font, 11), width=28 ,wraplength=275)
        self.songsListsLb.place(x=centerX-50, y=650, anchor="center")
        self.songsAmount=len(self.songs)
        print(self.songsAmount)

        self.songLabel = Label(self.dataFrame, text="Cambiar canción favorita", font=(font, 15))
        self.songLabel.place(x=centerX-375, y=620, anchor="center")

        self.songOptions = ttk.Combobox(self.dataFrame, textvariable=self.chosenSong, height= 40, width=40, values=[])
        self.songOptions.place(x=centerX-375, y=720, anchor="center")

        self.nameSongEntry= Entry(self.dataFrame,width=18, font=(font, 15))
        self.nameSongEntry.place(x=centerX-405, y=670, anchor="center")

        self.searchBtn = Button(self.dataFrame, text="Search", font=(font, 10), command=self.searchSongs)
        self.searchBtn.place(x=centerX-297, y=656, anchor="nw") 
        
        self.saveBtn = Button(self.dataFrame, text="Esperando...", font=(font, 10), command=self.saveSong)
        self.saveBtn.place(x=centerX-415, y=740, anchor="nw")
        self.saveBtn.config(state="disabled")
        #____________________________________________________________________________________#

        #____________________________Change Image Information________________________________#  
        self.photoCanvas = Canvas(self.dataFrame, width=400, height=400)
        self.photoCanvas.place(x=centerX, y=185, anchor="nw")
        
        self.imagen = PhotoImage(file=os.path.abspath("perfiles/perfil.png")) 
      
        self.photoCanvas.create_image(0, 0, anchor="nw", image=self.imagen)

        self.choosePhotoBtn = Button(self.dataFrame, text="Foto de perfil", width= 15,font=(font, 15),command=self.chooseAPhoto)
        self.choosePhotoBtn.place(x=centerX+450, y=185, anchor="nw")


        self.profileBtn = Button(self.dataFrame, text="Tómate una foto", width= 15,font=(font, 15), command=self.takeAPhoto)
        self.profileBtn.place(x=centerX+450, y=285, anchor="nw")
        
        self.biometricalBtn = Button(self.dataFrame, text="Datos biómetricos", width= 15,font=(font, 15), command=self.savePhotoInformation)
        self.biometricalBtn.place(x=centerX+450, y=385, anchor="nw")
        #____________________________________________________________________________________#

        self.showSong()
      
    def showColor(self):
        color = self.colorVar.get()
        self.colorLabel.config(bg=color)
    def takeAPhoto(self):
        faceInformation = facialRecognogtion(self.user.user)
        faceInformation.getFaceInformation("takeAPhoto")
    def savePhotoInformation(self): 
        password = tkinter.simpledialog.askstring("Contraseña", "Ingresa la contraseña:", show="*")
        if password == self.user.password:
            faceInformation = facialRecognogtion(self.user.user)
            faceInformation.getFaceInformation("saveInformation")
        else:
            messagebox.showinfo("Contraseña", "Contraseña Incorrecta")
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
    def showSong(self):
        counter=0
        auxList=[]
        while counter!= len(self.songs):
            auxList=auxList+[str(counter+1)+"."+self.songs[counter][1][0]]
            counter+=1
        
        auxList=["Lista de canciones"]+auxList
        info="\n".join(auxList)
        self.songsListsLb.config(text=info)
    def searchSongs(self): 
        self.saveBtn.config(text="Cargando...")
        self.saveBtn.update()
        self.controler.searchYoutubeSongs(self.nameSongEntry.get())
        self.songOptions['values']=self.controler.nameSongListForUser
        self.saveBtn.config(text="Guardar")
        self.saveBtn.config(state="normal")
        self.chosenSong.set(self.controler.nameSongListForUser[0])
        self.saveBtn.update()
 
    def saveSong(self):
        flag=True
        
        if not self.songsAmount!=3: 
            answer=messagebox.askyesno("Confirmación", "Solo puedes guardar tres canciones, eliminarás la última que esté en la lista, ¿Deseas continuar?")
            if not answer: 
                flag=False
            
        if flag:
            counter=0
            self.saveBtn.config(state="disabled")
            self.songOptions['values']=[]
            self.saveBtn.config(text="Esperando")
                                
            while counter!= len(self.controler.nameSongListForDev):
                print(self.controler.nameSongListForUser[counter],self.chosenSong.get())
                if self.controler.nameSongListForUser[counter]==self.chosenSong.get():
                    if not self.songsAmount!=3:
                        auxList=self.songs
                        self.songs[1]=auxList[0]
                        self.songs[2]=auxList[1]
                        self.songs[0]=[[self.controler.nameSongListForDev[counter]],
                                        [self.controler.nameSongListForUser[counter]],
                                        [self.controler.urlSongList[counter]]]
                    else:
                        self.songs.append([[self.controler.nameSongListForDev[counter]],
                                        [self.controler.nameSongListForUser[counter]],
                                        [self.controler.urlSongList[counter]]])
                        self.songsAmount+=1
                    self.showSong()
                    break
                counter+=1
            self.chosenSong.set("")
            self.chosenSong.set("")
    
    def nextPage(self):
        if True: 
            if True:  
                flagUser=True
                flagMail=True
                flagPassword=True   
                if self.questionOneEntry.get()!="":
                    password = tkinter.simpledialog.askstring("Contraseña", "Ingresa la contraseña:", show="*")
                    if not password==self.user.password:
                        flagUser=False
                        messagebox.showinfo("Contraseña", "Contraseña incorrecta")
                    if not User.ValidateUser(self.questionOneEntry.get()) and flagUser:
                        requirements = [
                                    "El nombre de usuario no cumple los requisitos:",
                                    "No más de 10 carácteres",
                                    "No utilizar lenguaje soez"
                                ]
                        message = "\n".join(requirements)
                        messagebox.showinfo("Mensaje", message)
                        flagUser=False
                if self.questionTwoEntry.get()!="" and flagUser:
                    if not User.ValidateMail(self.questionTwoEntry.get()):
                        requirements = [
                                    "Formato incorrecto:",
                                    "No ingresó un correo"]
                        message = "\n".join(requirements)
                        messagebox.showinfo("Mensaje", message)
                        flagMail=False
                if self.questionThreeEntry.get()!="" and flagMail: 
                    if not User.ValidatePassword(self.questionThreeEntry.get()): 
                        requirements = [
                                    "La contraseña no cumple los requisitos:",
                                    "Al menos ocho caracteres",
                                    "Al menos una minúscula o mayúscula",
                                    "Al menos un número",
                                    "Al menos un caracter especial"

                                ]
                        message = "\n".join(requirements)
                        messagebox.showinfo("Mensaje", message)
                        flagPassword=False
                    if not self.questionThreeEntry.get()==self.questionFourEntry.get():
                        messagebox.showinfo("Mensaje", "la contraseña no coincide")
                        flagPassword=False

                if flagMail and flagUser and flagPassword:
                    password=self.user.password
                    mail=self.user.mail
                    user=self.user.user
                    color=self.user.color
                    if self.questionThreeEntry.get()!="":
                        password=self.questionThreeEntry.get()
                    if self.questionTwoEntry.get()!="":
                        mail=self.questionTwoEntry.get()
                    if self.questionOneEntry.get()!="":
                        user=self.questionOneEntry.get()
                    if not self.colorVar.get()=="default":
                        color=self.colorVar.get()
                    User.DeleteJson(self.user.mail,self.user.user)
                    newUser:User=User(user,password,mail,color,self.songs,self.user.answers,"","")
             
                    control= facialRecognogtion(newUser.user)
                    control.overWriteBiometricalData(self.user.user)
                 
                    try:
                        control= facialRecognogtion(newUser.user)
                        control.overWritePerfil(self.auxUser.user)
                    except Exception: 
                        print (Exception)
                    self.user=newUser            
                    self.dataFrame.pack_forget()
                    self.parent.users[self.number]=self.user.user
                    self.parent.updateLb()
                    self.parent.principalFrame.pack()
