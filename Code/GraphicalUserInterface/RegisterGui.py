from tkinter import *
from tkinter import messagebox, filedialog, colorchooser
from tkinter.ttk import Combobox

from facialLogic import facialRecognogtion
from GeneratePalette import GeneratePalette
from ColorRGB import ColorRGB
from registerGUIAnswers import registerGUIAnswers
from User import *
from musicLogic import *


class registerGui:
    def __init__(self, window, width, height, parentFrame):
        self.window = window
        self.width = width
        self.height = height
        self.parentFrame = parentFrame

        self.songs = []
        self.controler = musicLogic()

        secX1 = width / 4 - 100
        secX2 = 2 * width / 4
        secX3 = 3 * width / 4 + 100

        self.font = "Helvetica"

        self.colorPalette = ["#8B0000", "#630000", "#1C1C1C", "#000000", "#FFFFFF"]

        self.informationFrame = Frame(self.window, width=self.width, height=self.height, bg=self.colorPalette[0])
        self.informationFrame.pack()

        self.titleLb = Label(self.informationFrame, text="Registro de usuario\nIngresar su información general",
                             font=(self.font, 35))
        self.titleLb.config(bg=self.colorPalette[0], fg=self.colorPalette[3])

        self.nextBtn = Button(self.informationFrame, text="Siguiente", font=(self.font, 15), command=self.nextPage)
        self.nextBtn.config(bg=self.colorPalette[2], fg=self.colorPalette[4])

        self.titleLb.place(x=secX2, y=25, anchor="n")
        self.nextBtn.place(x=width - 100, y=height - 200, anchor="se")

        # -----------------------------------------User Information-------------------------------------------------- #
        self.userLb = Label(self.informationFrame, text="Nombre de Usuario:", font=(self.font, 15))
        self.userLb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])
        self.userTxt = Entry(self.informationFrame, width=20, font=(self.font, 15))

        self.mailLb = Label(self.informationFrame, text="Correo:", font=(self.font, 15))
        self.mailLb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])
        self.mailTxt = Entry(self.informationFrame, width=20, font=(self.font, 15))

        self.password1Lb = Label(self.informationFrame, text="Contraseña:", font=(self.font, 15))
        self.password1Lb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])
        self.password1Txt = Entry(self.informationFrame, show="♦", width=20, font=(self.font, 15))

        self.showPasswordBtn = Button(self.informationFrame, text="👁", font=(self.font, 15), command=self.ShowPassword)
        self.showPasswordBtn.config(bg=self.colorPalette[2], fg=self.colorPalette[4])

        self.password2Lb = Label(self.informationFrame, text="Confirme contraseña:", font=(self.font, 15))
        self.password2Lb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])
        self.password2Txt = Entry(self.informationFrame, show="♦", width=20, font=(self.font, 15))

        self.userLb.place(x=secX1 - 2.5, y=250, anchor="ne")
        self.userTxt.place(x=secX1 + 2.5, y=250, anchor="nw")
        self.mailLb.place(x=secX1 - 2.5, y=290, anchor="ne")
        self.mailTxt.place(x=secX1 + 2.5, y=290, anchor="nw")
        self.password1Lb.place(x=secX1 - 2.5, y=330, anchor="ne")
        self.password1Txt.place(x=secX1 + 2.5, y=330, anchor="nw")
        self.password2Lb.place(x=secX1 - 2.5, y=370, anchor="ne")
        self.password2Txt.place(x=secX1 + 2.5, y=370, anchor="nw")
        self.showPasswordBtn.place(x=secX1 + 2.5, y=410, anchor="nw")
        # ----------------------------------------------------------------------------------------------------------- #

        # -----------------------------------------Password Information---------------------------------------------- #
        self.requirements = [
            "Requisitos de contraseña:\n",
            "❌ - 8 caracteres",
            "❌ - carácter en minúscula",
            "❌ - carácter en MAYÚSCULA",
            "❌ - carácter numérico",
            "❌ - carácter especial"
        ]

        self.password1Txt.bind("<KeyRelease>", self.PassInfo)
        message = "\n".join(self.requirements)

        self.passInfoLb = Label(self.informationFrame, text=message, font=(self.font, 20))
        self.passInfoLb.config(bg=self.colorPalette[2], fg=self.colorPalette[4])
        self.passInfoLb.place(x=secX1, y=500, anchor="n")
        # ----------------------------------------------------------------------------------------------------------- #

        # ---------------------------------------------Edit Color---------------------------------------------------- #
        self.userPalette = None

        self.colorCanvas = Canvas(self.informationFrame, width=300, height=150)
        self.colorLb = Label(self.informationFrame, text="Color favorito:", font=(self.font, 15))
        self.colorLb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])
        self.colorBtn = Button(self.informationFrame, text="Seleccionar color", font=(self.font, 15),
                               command=self.GenerateColor)
        self.colorBtn.config(bg=self.colorPalette[2], fg=self.colorPalette[4])

        self.colorLb.place(x=secX3, y=250, anchor="ne")
        self.colorCanvas.place(x=secX3, y=300, anchor="n")
        self.colorBtn.place(x=secX3, y=475, anchor="n")
        # ----------------------------------------------------------------------------------------------------------- #

        # _______________________________________Get favorite song__________________________________________________ #

        self.chosenSong = StringVar()
        self.songsAmount = 0

        self.songsListsLb = Label(self.informationFrame, text="Lista de canciones", font=(self.font, 11), width=30,
                                  wraplength=275)
        self.songsListsLb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])

        self.songOptions = Combobox(self.informationFrame, textvariable=self.chosenSong, height=40, width=40,
                                    values=[])
        self.songLabel = Label(self.informationFrame, text="Canción favorita", font=(self.font, 15))
        self.songLabel.config(bg=self.colorPalette[1], fg=self.colorPalette[4])

        self.nameSongEntry = Entry(self.informationFrame, width=18, font=(self.font, 15))
        self.searchBtn = Button(self.informationFrame, text="🔍", font=(self.font, 10), command=self.searchSongs)
        self.searchBtn.config(bg=self.colorPalette[2], fg=self.colorPalette[4])
        self.saveBtn = Button(self.informationFrame, text="Esperando...", font=(self.font, 10), command=self.saveSong)
        self.saveBtn.config(bg=self.colorPalette[2], fg=self.colorPalette[4], state="disabled")

        self.songLabel.place(x=secX3, y=550, anchor="center")
        self.nameSongEntry.place(x=secX3 - 30, y=600, anchor="center")
        self.searchBtn.place(x=secX3 + 105, y=600, anchor="center")
        self.songOptions.place(x=secX3, y=650, anchor="center")
        self.saveBtn.place(x=secX3, y=680, anchor="center")
        self.songsListsLb.place(x=secX3, y=730, anchor="center")
        # __________________________________________________________________________________________________________ #

        # ____________________________________Photo and biometric information_____________________________________ #
        """self.photoCanvas = Canvas(self.InformationFrame, width=400, height=400)
        self.photoCanvas.config(bg=self.colorPalette[1])
        self.photoCanvas.place(x=330, y=400, anchor="center")

        self.imagen = PhotoImage(file=os.path.abspath("Code/GraphicalUserInterface/Profile/perfil.png"))

        self.photoCanvas.create_image(0, 0, anchor="nw", image=self.imagen)

        self.addBtn = Button(self.photoCanvas, text="+", font=(font, 15), command=self.takeAPhoto)
        self.addBtn.config(bg=self.colorPalette[4])
        self.addBtn.place(x=340, y=400, anchor="se")

        self.profileBtn = Button(self.photoCanvas, text="✎", font=(font, 15), command=self.chooseAPhoto)
        self.profileBtn.config(bg=self.colorPalette[4])
        self.profileBtn.place(x=400, y=400, anchor="se")

        self.biometricalBtn = Button(self.InformationFrame, text="Datos biómetricos", font=(font, 15),
                                     command=self.savePhotoInformation)
        self.biometricalBtn.config(bg=self.colorPalette[4])
        self.biometricalBtn.place(x=330, y=650, anchor="center")"""
        # ________________________________________________________________________________________________________ #

    def nextPage(self):
        answer = messagebox.askyesno("Confirmación", "¿Estás seguro de continuar?")
        if answer:
            try:
                print(User.ValidateExistance(self, self.userTxt.get()))
                if (not (User.ValidateExistance(self, self.userTxt.get())) and (
                        not (User.ValidateExistance(self, self.mailTxt.get()))) and self.userTxt.get() != ""):
                    print(self.songs)
                    if self.password2Txt.get() == self.password1Txt.get():
                        user = User(self.userTxt.get(),
                                    self.password1Txt.get(),
                                    self.mailTxt.get(),
                                    self.userPalette,
                                    self.songs, " ", " ", "")
                        if user.validation:
                            self.informationFrame.pack_forget()
                            app = registerGUIAnswers(self.window, self.width, self.height, user, self.parentFrame)
                        else:
                            if user.errorType == "password":
                                requirements = [
                                    "La contraseña no cumple los requisitos:",
                                    "Al menos ocho caracteres",
                                    "Al menos una minúscula o mayúscula",
                                    "Al menos un número",
                                    "Al menos un caracter especial"

                                ]
                                message = "\n".join(requirements)
                                messagebox.showinfo("Mensaje", message)
                            elif user.errorType == "user":
                                requirements = [
                                    "El nombre de usuario no cumple los requisitos:",
                                    "No más de 10 carácteres caracteres",
                                    "No utilizar lenguaje soez"
                                ]
                                message = "\n".join(requirements)
                                messagebox.showinfo("Mensaje", message)
                            else:
                                requirements = [
                                    "Formato incorrecto:",
                                    "No ingresó un correo"]
                                message = "\n".join(requirements)
                                messagebox.showinfo("Mensaje", message)
                    else:
                        messagebox.showinfo("Mensaje", "La contraseña no coincide")
                else:
                    messagebox.showinfo("Mensaje", "Usuario existente")

            except Exception as e:
                print(e)
                messagebox.showinfo("Mensaje", "Datos incorrectos")

    def searchSongs(self):
        self.saveBtn.config(text="Cargando...")
        self.saveBtn.update()
        self.controler.searchSong(self.nameSongEntry.get())
        self.songOptions['values'] = self.controler.nameSongListForUser
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
                                
            while counter!= len(self.controler.nameSongListForUser):
                if self.controler.nameSongListForUser[counter]==self.chosenSong.get():
                    if not self.songsAmount!=3:
                        auxFirstSong=self.songs[0]
                        auxSecondSong=self.songs[1]
                        self.songs[1]=auxFirstSong
                        self.songs[2]=auxSecondSong
                        self.songs[0]=[[self.controler.nameSongListForUser[counter]],
                                        [self.controler.urlSongList[counter]]]
                    else:
                        self.songs=[[[self.controler.nameSongListForUser[counter]],
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
        self.songsListsLb.config(text=info)

    def GenerateColor(self):
        color = colorchooser.askcolor()
        self.userPalette = GeneratePalette(color[1]).GenerateColors()
        self.colorCanvas.config(bg=self.userPalette[0])

    def ShowPassword(self):
        if self.showPasswordBtn["text"] == "👁":
            self.password1Txt["show"] = ""
            self.password2Txt["show"] = ""
            self.showPasswordBtn["text"] = "❌"
        else:
            self.password1Txt["show"] = "♦"
            self.password2Txt["show"] = "♦"
            self.showPasswordBtn["text"] = "👁"

    def PassInfo(self, event):
        passTxt = self.password1Txt.get()
        if len(passTxt) >= 8:
            self.requirements[1] = "✔ - 8 caracteres"
        else:
            self.requirements[1] = "❌ - 8 caracteres"
        if any(c.islower() for c in passTxt):
            self.requirements[2] = "✔ - carácter en minúscula"
        else:
            self.requirements[2] = "❌ - carácter en minúscula"
        if any(c.isupper() for c in passTxt):
            self.requirements[3] = "✔ - carácter en MAYÚSCULA"
        else:
            self.requirements[3] = "❌ - carácter en MAYÚSCULA"
        if any(c.isdigit() for c in passTxt):
            self.requirements[4] = "✔ - carácter en numérico"
        else:
            self.requirements[4] = "❌ - carácter en numérico"
        if any(c in string.punctuation for c in passTxt):
            self.requirements[5] = "✔ - carácter especial"
        else:
            self.requirements[5] = "❌ - carácter especial"

        message = "\n".join(self.requirements)
        self.passInfoLb.config(text=message)

    # Adaptar codigo para que funcione sin la clase user
    """def takeAPhoto(self):
        faceInformation = facialRecognogtion(self.userTxt.get())
        faceInformation.getFaceInformation("takeAPhoto")

    def savePhotoInformation(self):
        faceInformation = facialRecognogtion(self.userTxt.get())
        faceInformation.getFaceInformation("saveInformation")
        self.done = True

    def chooseAPhoto(self):
        imagePath = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg *.png *.gif *.bmp *.svg")])
        faceInformation = facialRecognogtion(self.userTxt.get())
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
        self.imagen = resizedImage"""
