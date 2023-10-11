from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
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

        colorPalette = ["#8B0000", "#630000", "#1C1C1C", "#000000", "#FFFFFF"]

        # Esta es el frame de esta sección

        self.InformationFrame = Frame(window, width=self.width, height=self.height, bg=colorPalette[0])
        self.InformationFrame.pack()

        self.registerLb = Label(self.InformationFrame, text="Registro de usuario", font=(font, 35))
        self.registerLb.config(bg=colorPalette[0], fg=colorPalette[3])
        self.registerLb.place(x=centerX, y=50, anchor="center")

        self.InformationFrame.grid_rowconfigure(1, minsize=100)
        self.InformationFrame.grid_columnconfigure(0, minsize=200)

        self.registerLb = Label(self.InformationFrame,
                                text="                    En esta sección se debe ingresar su información general                    ",
                                font=(font, 20))
        self.registerLb.config(bg=colorPalette[1], fg=colorPalette[4])
        self.registerLb.place(x=centerX, y=125, anchor="center")

        # _______________________________Choose favorite color_____________________________________#

        self.colorVar = StringVar()
        self.colorVar.set("default")

        Radiobutton(self.InformationFrame, text="Rojo     ", variable=self.colorVar, font=(font, 15), width=8,
                    value="red", command=self.showColor).place(x=centerX + 330, y=250, anchor="center")
        Radiobutton(self.InformationFrame, text="Verde   ", variable=self.colorVar, font=(font, 15), width=8,
                    value="green", command=self.showColor).place(x=centerX + 330, y=300, anchor="center")
        Radiobutton(self.InformationFrame, text="Azul     ", variable=self.colorVar, font=(font, 15), width=8,
                    value="blue", command=self.showColor).place(x=centerX + 330, y=350, anchor="center")
        Radiobutton(self.InformationFrame, text="Amarillo", variable=self.colorVar, font=(font, 15), width=8,
                    value="yellow", command=self.showColor).place(x=centerX + 330, y=400, anchor="center")
        Radiobutton(self.InformationFrame, text="Naranja", variable=self.colorVar, font=(font, 15), width=8,
                    value="orange", command=self.showColor).place(x=centerX + 330, y=450, anchor="center")
        Radiobutton(self.InformationFrame, text="Morado", variable=self.colorVar, font=(font, 15), width=8,
                    value="violet", command=self.showColor).place(x=centerX + 330, y=500, anchor="center")

        self.colorLabel = Label(self.InformationFrame, text="Seleccione su color favorito", font=(font, 15))
        self.colorLabel.config(bg=colorPalette[1], fg=colorPalette[4])
        self.colorLabel.place(x=centerX + 330, y=200, anchor="center")

        # ________________________________________________________________________________________________________#

        # _____________________________________Get favority song__________________________________________________#

        self.chosenSong = tk.StringVar()
        self.songsAmount = 0

        self.songsListsLb = Label(self.InformationFrame, text="Lista de canciones", font=(font, 11), width=28,
                                  wraplength=275)
        self.songsListsLb.config(bg=colorPalette[1], fg=colorPalette[4])
        self.songsListsLb.place(x=centerX + 10, y=380, anchor="center")

        self.songOptions = ttk.Combobox(self.InformationFrame, textvariable=self.chosenSong, height=40, width=40,
                                        values=[])
        self.songOptions.place(x=centerX + 10, y=300, anchor="center")

        self.songLabel = Label(self.InformationFrame, text="Ingrese su canción favorita", font=(font, 15))
        self.songLabel.config(bg=colorPalette[1], fg=colorPalette[4])
        self.songLabel.place(x=centerX + 10, y=200, anchor="center")

        self.nameSongEntry = Entry(self.InformationFrame, width=18, font=(font, 15))
        self.nameSongEntry.place(x=centerX - 20, y=250, anchor="center")

        self.searchBtn = Button(self.InformationFrame, text="Search", font=(font, 10), command=self.searchSongs)
        self.searchBtn.config(bg=colorPalette[2], fg=colorPalette[4])
        self.searchBtn.place(x=centerX + 88, y=238, anchor="nw")

        self.saveBtn = Button(self.InformationFrame, text="Esperando...", font=(font, 10), command=self.saveSong)
        self.saveBtn.config(bg=colorPalette[2], fg=colorPalette[4])
        self.saveBtn.place(x=centerX - 30, y=330, anchor="nw")
        self.saveBtn.config(state="disabled")
        # ________________________________________________________________________________________________________#

        # _____________________________________General Questions Section___________________________________________#
        self.questionOneLb = Label(self.InformationFrame, text="Ingrese su nombre de usuario", font=(font, 15))
        self.questionOneLb.config(bg=colorPalette[1], fg=colorPalette[4])
        self.questionOneLb.place(x=centerX - 330, y=200, anchor="center")
        self.questionOneEntry = Entry(self.InformationFrame, width=25, font=(font, 15))
        self.questionOneEntry.place(x=centerX - 330, y=250, anchor="center")

        self.questionTwoLb = Label(self.InformationFrame, text="Ingrese su correo", font=(font, 15))
        self.questionTwoLb.config(bg=colorPalette[1], fg=colorPalette[4])
        self.questionTwoLb.place(x=centerX - 330, y=300, anchor="center")
        self.questionTwoEntry = Entry(self.InformationFrame, width=25, font=(font, 15))
        self.questionTwoEntry.place(x=centerX - 330, y=350, anchor="center")

        self.questionThreeLb = Label(self.InformationFrame, text="Ingrese su contraseña", font=(font, 15))
        self.questionThreeLb.config(bg=colorPalette[1], fg=colorPalette[4])
        self.questionThreeLb.place(x=centerX - 330, y=400, anchor="center")
        self.questionThreeEntry = Entry(self.InformationFrame, width=25, font=(font, 15))
        self.questionThreeEntry.place(x=centerX - 330, y=450, anchor="center")

        self.questionFourLb = Label(self.InformationFrame, text="Confirme su contraseña", font=(font, 15))
        self.questionFourLb.config(bg=colorPalette[1], fg=colorPalette[4])
        self.questionFourLb.place(x=centerX - 330, y=500, anchor="center")
        self.questionFourEntry = Entry(self.InformationFrame, width=25, font=(font, 15))
        self.questionFourEntry.place(x=centerX - 330, y=550, anchor="center")

        self.nextBtn = Button(self.InformationFrame, text="next", font=(font, 15), command=self.nextPage)
        self.nextBtn.config(bg=colorPalette[2], fg=colorPalette[4])
        self.nextBtn.place(x=2 * centerX - 100, y=650, anchor="nw")
        # ________________________________________________________________________________________________________#

    def nextPage(self):
        answer = messagebox.askyesno("Confirmación", "¿Estás seguro de continuar?")
        if answer:
            try:
                print(User.ValidateExistance(self, self.questionOneEntry.get()))
                if (not (User.ValidateExistance(self, self.questionOneEntry.get())) and (
                not (User.ValidateExistance(self, self.questionTwoEntry.get()))) and self.questionOneEntry.get() != ""):
                    print(self.songs)
                    if (self.questionFourEntry.get() == self.questionThreeEntry.get()):
                        user = User(self.questionOneEntry.get(),
                                    self.questionThreeEntry.get(),
                                    self.questionTwoEntry.get(),
                                    self.colorVar.get(),
                                    self.songs, " ", " ", "")
                        if (user.validation):
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

    def showColor(self):
        color = self.colorVar.get()
        self.colorLabel.config(bg=color)

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
