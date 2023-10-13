from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
from tkinter import colorchooser
import tkinter as tk

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

        centerX = width / 2
        centrerY = width / 2

        font = "Helvetica"

        self.colorPalette = ["#8B0000", "#630000", "#1C1C1C", "#000000", "#FFFFFF"]

        # Esta es el frame de esta sección

        self.InformationFrame = Frame(window, width=self.width, height=self.height, bg=self.colorPalette[0])
        self.InformationFrame.pack()

        self.registerLb = Label(self.InformationFrame, text="Registro de usuario", font=(font, 35))
        self.registerLb.config(bg=self.colorPalette[0], fg=self.colorPalette[3])
        self.registerLb.place(x=centerX, y=50, anchor="center")

        self.InformationFrame.grid_rowconfigure(1, minsize=100)
        self.InformationFrame.grid_columnconfigure(0, minsize=200)

        self.registerLb = Label(self.InformationFrame,
                                text="                    En esta sección se debe ingresar su información general                    ",
                                font=(font, 20))
        self.registerLb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])
        self.registerLb.place(x=centerX, y=125, anchor="center")

        # _______________________________Choose favorite color_____________________________________ #

        self.r = None
        self.g = None
        self.g = None
        self.userPalette = None

        self.redLb = Label(self.InformationFrame, text="R: ", font=(font, 15))
        self.redLb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])
        self.greenLb = Label(self.InformationFrame, text="G: ", font=(font, 15))
        self.greenLb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])
        self.blueLb = Label(self.InformationFrame, text="B: ", font=(font, 15))
        self.blueLb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])

        self.redTxt = Entry(self.InformationFrame, width=10, font=(font, 15))
        self.greenTxt = Entry(self.InformationFrame, width=10, font=(font, 15))
        self.blueTxt = Entry(self.InformationFrame, width=10, font=(font, 15))

        self.redLb.place(x=centerX + 300, y=250, anchor="w")
        self.redTxt.place(x=centerX + 320, y=290, anchor="w")
        self.greenLb.place(x=centerX + 300, y=330, anchor="w")
        self.greenTxt.place(x=centerX + 320, y=370, anchor="w")
        self.blueLb.place(x=centerX + 300, y=410, anchor="w")
        self.blueTxt.place(x=centerX + 320, y=450, anchor="w")

        self.canvasColor = Canvas(self.InformationFrame, width=100, height=100)
        self.canvasColor.place(x=centerX + 550, y=330, anchor="center")

        self.colorLb = Label(self.InformationFrame, text="Selecciones un color", font=(font, 15))
        self.colorLb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])
        self.colorLb.place(x=centerX + 330, y=200, anchor="center")

        self.generateBtn = Button(self.InformationFrame, text="Generate", font=(font, 15), command=self.GenerateColor)
        self.generateBtn.config(bg=self.colorPalette[2], fg=self.colorPalette[4])
        self.generateBtn.place(x=centerX + 420, y=500, anchor="center")

        # __________________________________________________________________________________________________________ #

        # _______________________________________Get favorite song__________________________________________________ #

        self.chosenSong = tk.StringVar()
        self.songsAmount = 0

        self.songsListsLb = Label(self.InformationFrame, text="Lista de canciones", font=(font, 11), width=28,
                                  wraplength=275)
        self.songsListsLb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])
        self.songsListsLb.place(x=centerX - 30, y=380 + 440, anchor="n")

        self.songOptions = ttk.Combobox(self.InformationFrame, textvariable=self.chosenSong, height=40, width=40,
                                        values=[])
        self.songOptions.place(x=centerX - 30, y=300 + 440, anchor="center")

        self.songLabel = Label(self.InformationFrame, text="Ingrese su canción favorita", font=(font, 15))
        self.songLabel.config(bg=self.colorPalette[1], fg=self.colorPalette[4])
        self.songLabel.place(x=centerX - 30, y=200 + 440, anchor="center")

        self.nameSongEntry = Entry(self.InformationFrame, width=18, font=(font, 15))
        self.nameSongEntry.place(x=centerX - 30, y=250 + 440, anchor="center")

        self.searchBtn = Button(self.InformationFrame, text="Search", font=(font, 10), command=self.searchSongs)
        self.searchBtn.config(bg=self.colorPalette[2], fg=self.colorPalette[4])
        self.searchBtn.place(x=centerX + 118, y=250 + 440, anchor="center")

        self.saveBtn = Button(self.InformationFrame, text="Esperando...", font=(font, 10), command=self.saveSong)
        self.saveBtn.config(bg=self.colorPalette[2], fg=self.colorPalette[4])
        self.saveBtn.place(x=centerX - 30, y=330 + 440, anchor="center")
        self.saveBtn.config(state="disabled")
        # __________________________________________________________________________________________________________ #

        # _______________________________________Data Information User______________________________________________ #
        self.questionOneLb = Label(self.InformationFrame, text="Ingrese su nombre de usuario", font=(font, 15))
        self.questionOneLb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])
        self.questionOneLb.place(x=centerX - 30, y=200, anchor="center")
        self.questionOneEntry = Entry(self.InformationFrame, width=25, font=(font, 15))
        self.questionOneEntry.place(x=centerX - 30, y=250, anchor="center")

        self.questionTwoLb = Label(self.InformationFrame, text="Ingrese su correo", font=(font, 15))
        self.questionTwoLb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])
        self.questionTwoLb.place(x=centerX - 30, y=300, anchor="center")
        self.questionTwoEntry = Entry(self.InformationFrame, width=25, font=(font, 15))
        self.questionTwoEntry.place(x=centerX - 30, y=350, anchor="center")

        self.questionThreeLb = Label(self.InformationFrame, text="Ingrese su contraseña", font=(font, 15))
        self.questionThreeLb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])
        self.questionThreeLb.place(x=centerX - 30, y=400, anchor="center")
        self.questionThreeEntry = Entry(self.InformationFrame, width=25, font=(font, 15), show="♦")
        self.questionThreeEntry.place(x=centerX - 30, y=450, anchor="center")

        self.questionFourLb = Label(self.InformationFrame, text="Confirme su contraseña", font=(font, 15))
        self.questionFourLb.config(bg=self.colorPalette[1], fg=self.colorPalette[4])
        self.questionFourLb.place(x=centerX - 30, y=500, anchor="center")
        self.questionFourEntry = Entry(self.InformationFrame, width=25, font=(font, 15), show="♦")
        self.questionFourEntry.place(x=centerX - 30, y=550, anchor="center")

        self.nextBtn = Button(self.InformationFrame, text="next", font=(font, 15), command=self.nextPage)
        self.nextBtn.config(bg=self.colorPalette[2], fg=self.colorPalette[4])
        self.nextBtn.place(x=2 * centerX - 100, y=650, anchor="nw")
        # ________________________________________________________________________________________________________ #

        # ____________________________________Photo and biometric information_____________________________________ #
        self.photoCanvas = Canvas(self.InformationFrame, width=400, height=400)
        self.photoCanvas.config(bg=self.colorPalette[1])
        self.photoCanvas.place(x=330, y=400, anchor="center")

        self.imagen = PhotoImage(file=os.path.abspath("Profile/perfil.png"))

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
        self.biometricalBtn.place(x=330, y=650, anchor="center")
        # ________________________________________________________________________________________________________ #

    def nextPage(self):
        answer = messagebox.askyesno("Confirmación", "¿Estás seguro de continuar?")
        if answer:
            try:
                print(User.ValidateExistance(self, self.questionOneEntry.get()))
                if (not (User.ValidateExistance(self, self.questionOneEntry.get())) and (
                        not (User.ValidateExistance(self,
                                                    self.questionTwoEntry.get()))) and self.questionOneEntry.get() != ""):
                    print(self.songs)
                    if self.questionFourEntry.get() == self.questionThreeEntry.get():
                        user = User(self.questionOneEntry.get(),
                                    self.questionThreeEntry.get(),
                                    self.questionTwoEntry.get(),
                                    self.userPalette,
                                    self.songs, " ", " ", "")
                        if user.validation:
                            self.InformationFrame.pack_forget()
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
        self.controler.searchYoutubeSongs(self.nameSongEntry.get())
        self.songOptions['values'] = self.controler.nameSongListForUser
        self.saveBtn.config(text="Guardar")
        self.saveBtn.config(state="normal")
        self.chosenSong.set(self.controler.nameSongListForUser[0])
        self.saveBtn.update()

    def saveSong(self):
        flag = True

        if not self.songsAmount != 3:
            answer = messagebox.askyesno("Confirmación",
                                         "Solo puedes guardar tres canciones, eliminarás la última que esté en la lista, ¿Deseas continuar?")
            if not answer:
                flag = False

        if flag:
            counter = 0
            self.saveBtn.config(state="disabled")
            self.songOptions['values'] = []
            self.saveBtn.config(text="Esperando")

            while counter != len(self.controler.nameSongListForDev):
                print(self.controler.nameSongListForUser[counter], self.chosenSong.get())
                if self.controler.nameSongListForUser[counter] == self.chosenSong.get():
                    if not self.songsAmount != 3:
                        auxList = self.songs
                        self.songs[1] = auxList[0]
                        self.songs[2] = auxList[1]
                        self.songs[0] = [[self.controler.nameSongListForDev[counter]],
                                         [self.controler.nameSongListForUser[counter]],
                                         [self.controler.urlSongList[counter]]]
                    else:
                        self.songs.append([[self.controler.nameSongListForDev[counter]],
                                           [self.controler.nameSongListForUser[counter]],
                                           [self.controler.urlSongList[counter]]])
                        self.songsAmount += 1
                    self.showSong()
                    break
                counter += 1
            self.chosenSong.set("")
            self.chosenSong.set("")

    def showSong(self):
        counter = 0
        auxList = []
        while counter != len(self.songs):
            print(self.songs)
            auxList = auxList + [str(counter + 1) + "." + self.songs[counter][1][0]]
            counter += 1

        auxList = ["Lista de canciones"] + auxList
        info = "\n".join(auxList)
        self.songsListsLb.config(text=info)

    def GenerateColor(self):
        try:
            if (0 <= int(self.redTxt.get()) <= 255
                    and 0 <= int(self.greenTxt.get()) <= 255
                    and 0 <= int(self.blueTxt.get()) <= 255):
                r = int(self.redTxt.get())
                g = int(self.greenTxt.get())
                b = int(self.blueTxt.get())

                color = ColorRGB(r, g, b)
                self.userPalette = GeneratePalette(color.getHex()).GenerateColors()

                self.canvasColor.config(bg=self.userPalette[0])

            else:
                messagebox.showinfo("Mensaje", "Digite un numero entre 0 y 255")

        except Exception as e:
            messagebox.showinfo("Mensaje", f"Error: {e}")

    # Adaptar codigo para que funcione sin la clase user
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