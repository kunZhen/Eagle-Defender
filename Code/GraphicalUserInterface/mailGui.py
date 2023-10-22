import time
from tkinter import *
import tkinter as tk
from LoginGui import LoginGui

import cv2
from RegisterGui import *
from PrincipalGui import *
from PIL import Image, ImageTk, ImageDraw
from facialLogic import *
from User import *


class mailGui:
    def __init__(self, window, width, height, userAmount):
        self.window = window
        self.width = width
        self.height = height
        self.userOneName = ""
        self.userTwoName = ""
        font = "Helvetica"

        centerX = width / 2
        centerY = height / 2

        colorPalette = ["#8B0000", "#630000", "#1C1C1C", "#000000", "#FFFFFF"]

        self.mailFrame = Frame(window, width=width, height=height, bg=colorPalette[0])
        self.mailFrame.pack()
        self.userAmount = userAmount

        self.loginLb = Label(self.mailFrame, text="Ingrese su usuario/correo" + f" (Usuario {self.userAmount})",
                             font=(font, 35))
        self.loginLb.config(bg=colorPalette[0], fg=colorPalette[3])
        self.loginLb.place(x=centerX, y=75, anchor="center")

        self.userLb = Label(self.mailFrame, text="Usuario/Correo: ", font=(font, 15))
        self.userLb.config(bg=colorPalette[1], fg=colorPalette[4])
        self.userLb.place(x=centerX - 105, y=centerY - 75, anchor="e")

        # Txt: Text box
        self.userTxt = Entry(self.mailFrame, width=25, font=(font, 15))
        self.userTxt.place(x=centerX - 100, y=centerY - 75, anchor="w")

        self.nextBtn = Button(self.mailFrame, text="Ingresar", font=(font, 15), command=self.nextPage)
        self.nextBtn.config(bg=colorPalette[2], fg=colorPalette[4])
        self.nextBtn.place(x=centerX, y=centerY, anchor="center")

        self.nextBtn = Button(self.mailFrame, text="Registrar nuevo usuario", font=(font, 15), command=self.Register)
        self.nextBtn.config(bg=colorPalette[2], fg=colorPalette[4])
        self.nextBtn.place(x=centerX, y=centerY + 100, anchor="center")

    def nextPage(self):
        answer = messagebox.askyesno("Confirmación", "¿Estás seguro de continuar?")
        if answer:
            if self.userTxt.get() == "":
                messagebox.showwarning("Contenido vacío", "No ha introducido un usuario")
            elif self.userTxt.get() == self.userOneName:
                messagebox.showwarning("", "usuario ingresado")
            elif User.ValidateExistance(self, self.userTxt.get()):
                user = User.LoadJson(self.userTxt.get())
                app = LoginGui(self.window, self.width, self.height, user, self.mailFrame)
                print(self.userOneName)
                if self.userAmount == 1:
                    self.userOneName = user.user
                    self.userAmount = 2
                    self.userTxt.delete(0, "end")

                    self.loginLb.config(text="Ingrese su usuario/correo" + f" (Usuario {self.userAmount})")
                else:
                    self.userTwoName = user.user
                    app.userTwo = self.userTwoName
                    app.userOne = self.userOneName

                self.mailFrame.pack_forget()
                app.showImage()
            else:
                messagebox.showinfo("Mensaje", "Usuario inexistente")

    def Register(self):
        answer = messagebox.askyesno("Confirmación", "¿Estás seguro de continuar?")
        if answer:
            self.mailFrame.pack_forget()
            register = registerGui(self.window, self.width, self.height, self.mailFrame)
