import os.path
from tkinter import *
from tkinter import ttk, filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
from tkinter import colorchooser
from User import *
import tkinter
from User import *
from facialLogic import *
from musicLogic import *
import tkinter.simpledialog
from PrincipalGui import *
import PrincipalGui
from GeneratePalette import GeneratePalette
from ColorRGB import ColorRGB


class modificateDataGui:
    def __init__(self, window, width, height, user, parent: PrincipalGui, number):
        self.window = window
        self.width = width
        self.height = height
        self.user: User = User.LoadJson(user)
        self.auxUser: User = user
        self.songs = self.user.music
        self.controler = musicLogic()
        self.parent: PrincipalGui = parent
        self.number = number

        self.font = "Helvetica"
        colorPalette = ["#323232", "#4A4A4A", "#FFFFFF", "#FF0000"]

        secX1 = width / 4 - 100
        secX2 = 2 * width / 4
        secX3 = 3 * width / 4 + 100

        self.dataFrame = Frame(self.window, width=self.width, height=self.height, bg=self.user.color[0])
        self.dataFrame.pack()

        self.titleLb = Label(self.dataFrame, text=f"Pᴇʀsᴏɴᴀʟɪᴢᴀᴄɪᴏ́ɴ ᴅᴇ Usᴜᴀʀɪᴏ\n{self.user.user}",
                             font=(self.font, 30))
        self.titleLb.config(bg=colorPalette[0], fg=colorPalette[2])
        self.titleLb.place(x=secX2, y=75, anchor="center")

        # -----------------------------------------Edit and Exit Button---------------------------------------------- #
        self.configBtn = Button(self.dataFrame, text="Editar", font=(self.font, 15), command=self.ConfigUser)
        self.configBtn.config(bg=colorPalette[1], fg=colorPalette[2])
        self.closeBtn = Button(self.dataFrame, text="Cerrar", font=(self.font, 15), command=self.Close)
        self.closeBtn.config(bg=colorPalette[1], fg=colorPalette[2])

        self.configBtn.place(x=width - 25, y=height - 200, anchor="e")
        self.closeBtn.place(x=width - 25, y=height - 150, anchor="e")
        # ----------------------------------------------------------------------------------------------------------- #

        # -----------------------------------------User Information-------------------------------------------------- #
        self.userLb = Label(self.dataFrame, text="Nombre de Usuario:", font=(self.font, 15))
        self.userLb.config(bg=colorPalette[0], fg=colorPalette[2])
        self.userTxt = Entry(self.dataFrame, width=20, font=(self.font, 15))
        self.userTxt.insert(0, self.user.user)
        self.userTxt.config(state="disabled")

        self.mailLb = Label(self.dataFrame, text="Correo:", font=(self.font, 15))
        self.mailLb.config(bg=colorPalette[0], fg=colorPalette[2])
        self.mailTxt = Entry(self.dataFrame, width=20, font=(self.font, 15))
        self.mailTxt.insert(0, self.user.mail)
        self.mailTxt.config(state="disabled")

        self.password1Lb = Label(self.dataFrame, text="Contraseña:", font=(self.font, 15))
        self.password1Lb.config(bg=colorPalette[0], fg=colorPalette[2])
        self.password1Txt = Entry(self.dataFrame, show="♦", width=20, font=(self.font, 15), state="disabled")

        self.showPasswordBtn = Button(self.dataFrame, text="<)", font=(self.font, 15), state="disabled",
                                      command=self.ShowPassword)
        self.showPasswordBtn.config(bg=colorPalette[1], fg=colorPalette[2])
        self.infoPasswordBtn = Button(self.dataFrame, text="!", font=(self.font, 15), state="disabled",
                                      command=self.InfoPassword)
        self.infoPasswordBtn.config(bg=colorPalette[3], fg=colorPalette[2])

        self.password2Lb = Label(self.dataFrame, text="Confirme contraseña:", font=(self.font, 15))
        self.password2Lb.config(bg=colorPalette[0], fg=colorPalette[2])
        self.password2Txt = Entry(self.dataFrame, show="♦", width=20, font=(self.font, 15), state="disabled")

        self.userLb.place(x=secX1 - 2.5, y=250, anchor="ne")
        self.userTxt.place(x=secX1 + 2.5, y=250, anchor="nw")
        self.mailLb.place(x=secX1 - 2.5, y=290, anchor="ne")
        self.mailTxt.place(x=secX1 + 2.5, y=290, anchor="nw")
        self.password1Lb.place(x=secX1 - 2.5, y=330, anchor="ne")
        self.password1Txt.place(x=secX1 + 2.5, y=330, anchor="nw")
        self.password2Lb.place(x=secX1 - 2.5, y=370, anchor="ne")
        self.password2Txt.place(x=secX1 + 2.5, y=370, anchor="nw")
        self.showPasswordBtn.place(x=secX1 + 57.5, y=410, anchor="nw")
        self.infoPasswordBtn.place(x=secX1 + 2.5, y=410, anchor="nw")
        # ----------------------------------------------------------------------------------------------------------- #

        # --------------------------------------------Profile Information-------------------------------------------- #
        self.profileCanvas = Canvas(self.dataFrame, width=400, height=400, bg=self.user.color[1])
        self.editBtn = Button(self.profileCanvas, text="✎", font=(self.font, 15), state="disabled",
                              command=self.chooseAPhoto)
        self.editBtn.config(bg=colorPalette[1], fg=colorPalette[2])
        self.addBtn = Button(self.profileCanvas, text="+", font=(self.font, 15), state="disabled" ,
                             command=self.takeAPhoto)
        self.addBtn.config(bg=colorPalette[1], fg=colorPalette[2])

        self.profileCanvas.place(x=secX1, y=400, anchor="n")
        self.editBtn.place(x=400, y=400, anchor="se")
        self.addBtn.place(x=340, y=400, anchor="se")
        # ----------------------------------------------------------------------------------------------------------- #

        # ---------------------------------------------Edit Color---------------------------------------------------- #
        self.userPalette = self.user.color

        self.colorCanvas = Canvas(self.dataFrame, width=300, height=150, bg=self.user.color[0])
        self.colorLb = Label(self.dataFrame, text="Color favorito:", font=(self.font, 15))
        self.colorLb.config(bg=colorPalette[0], fg=colorPalette[2])
        self.colorBtn = Button(self.dataFrame, text="Seleccionar color", font=(self.font, 15), state="disabled",
                               command=self.GenerateColor)
        self.colorBtn.config(bg=colorPalette[1], fg=colorPalette[2])

        self.colorCanvas.place(x=secX2, y=200, anchor="n")
        self.colorLb.place(x=secX2, y=150, anchor="ne")
        self.colorBtn.place(x=secX2, y=375, anchor="n")
        # ----------------------------------------------------------------------------------------------------------- #

        # --------------------------------------------------Edit Song------------------------------------------------ #
        self.chosenSong = StringVar()
        self.songListLb = Label(self.dataFrame, text="Lista de canciones", font=(self.font, 11), width=28,
                                wraplength=275)
        self.songListLb.config(bg=colorPalette[0], fg=colorPalette[2])
        self.songsAmount = len(self.songs)
        print(self.songsAmount)

        self.songLabel = Label(self.dataFrame, text="Canción favorita:", font=(self.font, 15))
        self.songLabel.config(bg=colorPalette[0], fg=colorPalette[2])

        self.songOptions = ttk.Combobox(self.dataFrame, textvariable=self.chosenSong, height=40, width=40, values=[], state="disabled")
        self.songTxt = Entry(self.dataFrame, width=18, font=(self.font, 15), state="disabled")
        self.searchBtn = Button(self.dataFrame, text="Buscar", font=(self.font, 15), state="disabled", command=self.searchSongs)
        self.searchBtn.config(bg=colorPalette[1], fg=colorPalette[2])
        self.saveBtn = Button(self.dataFrame, text="Esperando...", font=(self.font, 10), state="disabled", command=self.saveSong)
        self.saveBtn.config(bg=colorPalette[1], fg=colorPalette[2])

        self.songLabel.place(x=secX2, y=470, anchor="center")
        self.songTxt.place(x=secX2 - 30, y=510, anchor="center")
        self.searchBtn.place(x=secX2 + 125, y=510, anchor="center")
        self.songOptions.place(x=secX2 - 30, y=550, anchor="center")
        self.songListLb.place(x=secX2, y=590, anchor="center")
        self.saveBtn.place(x=secX2, y=630, anchor="center")

        self.showSong()
        # ----------------------------------------------------------------------------------------------------------- #

        # ----------------------------------Edit Avatar, Animation and Textures-------------------------------------- #
        self.avatarCanvas = Canvas(self.dataFrame, width=450, height=200)
        self.avatarCanvas.config(bg=self.user.color[1])
        self.animationCanvas = Canvas(self.dataFrame, width=300, height=300)
        self.animationCanvas.config(bg=self.user.color[1])
        self.textureCanvas = Canvas(self.dataFrame, width=300, height=300)
        self.textureCanvas.config(bg=self.user.color[1])

        self.avatarOpt = {"Goblin": 1, "Shaman": 2, "Champion": 3}
        self.animationOpt = {"Animacion leve": "S", "Animacion moderada": "M", "Animacion brusca": "L"}
        self.textureOpt = {"Bloques rusticos": 1, "Bloques modernos": 2, "Bloques medievales": 3}

        self.animationIndex = 0
        if self.user.animation == "M":
            self.animationIndex = 1
        elif self.user.animation == "L":
            self.animationIndex = 2

        self.avatarCB = ttk.Combobox(self.dataFrame, font=(self.font, 15), values=list(self.avatarOpt.keys()))
        self.avatarCB.current(self.user.avatar - 1)
        self.avatarCB.config(state="disabled")
        self.animationCB = ttk.Combobox(self.dataFrame, font=(self.font, 15), values=list(self.animationOpt.keys()))
        self.animationCB.current(0)
        self.animationCB.config(state="disabled")
        self.textureCB = ttk.Combobox(self.dataFrame, font=(self.font, 15), values=list(self.textureOpt.keys()))
        self.textureCB.current(self.user.textures - 1)
        self.textureCB.config(state="disabled")

        self.avatarCB.place(x=secX2, y=730, anchor="center")
        self.avatarCanvas.place(x=secX2, y=750, anchor="n")
        self.textureCanvas.place(x=secX3, y=520, anchor="n")
        self.animationCB.place(x=secX3, y=150, anchor="center")
        self.animationCanvas.place(x=secX3, y=170, anchor="n")
        self.textureCB.place(x=secX3, y=500, anchor="center")
        # ----------------------------------------------------------------------------------------------------------- #

        self.widgets = [self.userTxt, self.mailTxt, self.password1Txt, self.password2Txt,
                        self.showPasswordBtn, self.infoPasswordBtn, self.editBtn, self.addBtn, self.colorBtn,
                        self.songTxt, self.searchBtn, self.avatarCB, self.animationCB, self.textureCB, self.songOptions]

# ------------------------------------------------------------------------------------------------------------------- #
    def ConfigUser(self):
        if self.configBtn["text"] == "Editar":
            self.configBtn["text"] = "Guardar"
            self.closeBtn.config(state="disabled")
            for widget in self.widgets:
                if isinstance(widget, (Entry, Button, ttk.Combobox)):
                    widget.config(state="normal")
        else:
            self.SaveUser()
            self.configBtn["text"] = "Editar"
            self.closeBtn.config(state="normal")
            self.password1Txt.delete(0, "end")
            self.password2Txt.delete(0, "end")
            self.ShowPassword()
            for widget in self.widgets:
                if isinstance(widget, (Entry, Button, ttk.Combobox)):
                    widget.config(state="disabled")

    def ShowPassword(self):
        if self.showPasswordBtn["text"] == "<)":
            self.password1Txt["show"] = ""
            self.password2Txt["show"] = ""
            self.showPasswordBtn["text"] = "❌"
        else:
            self.password1Txt["show"] = "♦"
            self.password2Txt["show"] = "♦"
            self.showPasswordBtn["text"] = "<)"

    def InfoPassword(self):
        requirements = [
            "La contraseña debe tener los siguientes caracteres:",
            "Mínimo 8 caracteres",
            "Al menos un carácter en minúscula",
            "Al menos un carácter en MAYÚSCULA",
            "Al menos un carácter numérico",
            "Al menos un carácter especial"
        ]
        message = "\n".join(requirements)
        messagebox.showinfo("Requisitos de contraseña", message)

    def Close(self):
        self.dataFrame.pack_forget()
        self.parent.users[self.number] = self.user.user
        self.parent.updateLb()
        self.parent.principalFrame.pack()

    def SaveUser(self):
        flagUser = True
        flagMail = True
        flagPassword = True
        if self.userTxt.get() != self.user.user:
            password = simpledialog.askstring("Contraseña", "Ingresa la contraseña:", show="*")
            if password != self.user.password:
                flagUser = False
                messagebox.showinfo("Contraseña", "Contraseña incorrecta")
            if not User.ValidateUser(self.userTxt.get()) and flagUser:
                requirements = [
                    "El nombre de usuario no cumple los requisitos:",
                    "No más de 10 carácteres",
                    "No utilizar lenguaje soez"
                ]
                message = "\n".join(requirements)
                messagebox.showinfo("Mensaje", message)
                flagUser = False
        if self.mailTxt.get() != self.user.mail and flagUser:
            if not User.ValidateMail(self.mailTxt.get()):
                requirements = [
                    "Formato incorrecto:",
                    "No ingresó un correo"]
                message = "\n".join(requirements)
                messagebox.showinfo("Mensaje", message)
                flagMail = False
        if self.password1Txt.get() != "" and flagMail:
            if not User.ValidatePassword(self.password1Txt.get()):
                requirements = [
                    "La contraseña no cumple los requisitos:",
                    "Al menos ocho caracteres",
                    "Al menos una minúscula o mayúscula",
                    "Al menos un número",
                    "Al menos un caracter especial"
                ]
                message = "\n".join(requirements)
                messagebox.showinfo("Mensaje", message)
                flagPassword = False
            if self.password1Txt.get() != self.password2Txt.get():
                messagebox.showinfo("Mensaje", "la contraseña no coincide")
                flagPassword = False
        if flagUser and flagMail and flagPassword:
            newUser = self.userTxt.get()
            newMail = self.mailTxt.get()
            newPassword = self.password1Txt.get()
            newColor = self.userPalette
            newSong = self.songs
            newAvatar = None
            newAnimation = None
            newTexture = None
            if newUser == self.user.user:
                newUser = None
            if newMail != self.user.mail:
                newMail = None
            if newPassword != self.user.password:
                newPassword = None
            if newColor is None:
                newColor = None
            if newSong == self.user.music:
                newSong = None
            if newAvatar == self.user.avatar:
                newAvatar = None
            if newAnimation == self.user.animation:
                newAnimation = None
            if newTexture == self.user.textures:
                newTexture = None

            self.user.SetUser(newUser, newPassword, newMail)
            self.user.SetAttributes(newColor, newSong, None, None, None, newAvatar,
                                    newAnimation, newTexture)

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

    def searchSongs(self):
        self.saveBtn.config(text="Cargando...")
        self.saveBtn.update()
        self.controler.searchSong(self.nameSongEntry.get())
        # Iterate over list
        tempList = self.controler.nameSongListForUser
        newSongs = []
        for tuple in tempList:
            newSongs.append(tuple[0])
        self.songOptions['values'] = newSongs
        self.saveBtn.config(text="Guardar")
        self.saveBtn.config(state="normal")
        self.chosenSong.set(self.controler.nameSongListForUser[0][0])
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
                                
            while counter!= len(self.controler.nameSongListForUser):
                if self.controler.nameSongListForUser[counter][0]==self.chosenSong.get():
                    if not self.songsAmount!=3:
                        auxFirstSong=self.songs[0]
                        auxSecondSong=self.songs[1]
                        self.songs[1]=auxFirstSong
                        self.songs[2]=auxSecondSong
                        self.songs[0]=[[self.controler.nameSongListForUser[counter][0], 
                                        self.controler.nameSongListForUser[counter][1]],
                                        [self.controler.urlSongList[counter]]]
                    else:
                        self.songs=[[[self.controler.nameSongListForUser[counter][0], 
                                        self.controler.nameSongListForUser[counter][1]],
                                        [self.controler.urlSongList[counter] ]]]+self.songs
                        self.songsAmount+=1
                    self.showSong()
                    break
                counter+=1
            self.chosenSong.set("")
    
    def showSong(self):
        counter = 0
        auxList = []
        print(self.songs)
        while counter != len(self.songs):
            print(self.songs)
            auxList = auxList + [str(counter + 1) + "." + self.songs[counter][0][0]]
            counter += 1

        auxList = ["Lista de canciones"] + auxList
        info = "\n".join(auxList)
        self.songListLb.config(text=info)

    def GenerateColor(self):
        color = colorchooser.askcolor()
        self.userPalette = GeneratePalette(color[1]).GenerateColors()
        self.colorCanvas.config(bg=self.userPalette[0])
