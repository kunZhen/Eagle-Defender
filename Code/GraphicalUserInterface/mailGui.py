import time
from tkinter import *
import tkinter as tk
from LoginGui import LoginGui

import cv2
from RegisterGui import *
from PrincipalGui import *
from PIL import Image, ImageTk,ImageDraw
from facialLogic import *
from User import *


class mailGui:
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height
        
        font = "Helvetica"

        centerX = width / 2
        centerY = height / 2

        self.mailFrame = Frame(window, width=width, height=height, bg="blue")
        self.mailFrame.pack()

        self.loginLb = Label(self.mailFrame, text="Ingrese su usuario/correo", font=(font, 35))
        self.loginLb.place(x=centerX, y=75, anchor="center")

        self.userLb = Label(self.mailFrame, text="Usuario/Correo: ", font=(font, 15))
        self.userLb.place(x=centerX - 105, y=centerY - 150, anchor="e")

        # Txt: Text box
        self.userTxt = Entry(self.mailFrame, width=25, font=(font, 15))
        self.userTxt.place(x=centerX - 100, y=centerY - 150, anchor="w")

        self.nextBtn = Button(self.mailFrame, text="Continuar", font=(font, 15), command=self.nextPage)
        self.nextBtn.place(x=centerX, y=centerY+150, anchor="center")

        self.nextBtn = Button(self.mailFrame, text="Registrar nuevo usuario", font=(font, 15), command=self.Register)
        self.nextBtn.place(x=centerX, y=centerY,anchor="center")

    def nextPage(self):
        print(self.userTxt.get())
        print(User.ValidateExistence(self,self.userTxt.get()))
        if User.ValidateExistence(self,self.userTxt.get()):
            self.mailFrame.pack_forget()
            app=LoginGui(self.window,self.width,self.height)
            app.showImage()
        else: 
            messagebox.showinfo("Mensaje", "Usuario inexistente")

    def Register(self):
        self.mailFrame.pack_forget()
        register=registerGui(self.window,self.width,self.height,self.mailFrame)

