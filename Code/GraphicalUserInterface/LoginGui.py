import time
from tkinter import *
import tkinter as tk

import cv2
from RegisterGui import *
from PrincipalGui import *
from PIL import Image, ImageTk, ImageDraw
from facialLogic import *
from User import User
from passRetrieve import *

from musicLogic import musicLogic


class LoginGui:
    def __init__(self, window, width, height, user: User, parentFrame):
        self.window = window
        self.width = width
        self.height = height
        self.allow = tk.StringVar()
        self.allow.set("True")
        self.faceAproved = tk.StringVar()
        self.faceAproved.set("False")
        self.user = user

        self.parentFrame = parentFrame
        self.userOne = None
        self.userTwo = None

        font = "Helvetica"

        colorPalette = ["#8B0000", "#630000", "#1C1C1C", "#000000", "#FFFFFF"]

        centerX = width / 2
        centerY = height / 2

        self.loginFrame = Frame(window, width=width, height=height, bg=colorPalette[0])
        self.loginFrame.pack()

        self.loginLb = Label(self.loginFrame,
                             text="                                Inicio de sesión                                ",
                             font=(font, 35))
        self.loginLb.config(bg=colorPalette[0], fg=colorPalette[3])
        self.loginLb.place(x=centerX - 20, y=75, anchor="center")

        self.photoCanvas = Canvas(self.loginFrame, width=600, height=600)
        self.photoCanvas.config(bg=colorPalette[1])
        self.photoCanvas.place(x=150 + centerX, y=130, anchor="nw")

        self.userLb = Label(self.loginFrame,
                            text="Hola jugador " + self.user.user + ", por favor ingrese su contraseña:", width=60,
                            font=(font, 16))
        self.userLb.config(bg=colorPalette[1], fg=colorPalette[4])
        self.userLb.place(x=centerX + 130, y=150, anchor="e")

        # Txt: Text box
        self.userTxt = Entry(self.loginFrame, width=25, font=(font, 15), show="♦")
        self.userTxt.place(x=centerX - 380, y=200, anchor="w", height=40)

        self.passwordBtn = Button(self.loginFrame, text="Continuar", font=(font, 15), command=self.nextPass)
        self.passwordBtn.config(bg=colorPalette[2], fg=colorPalette[4])
        self.passwordBtn.place(x=centerX - 240, y=300, anchor="n", width=350)
        self.passwordBtn.config(state="disabled")

        self.recoverBtn = Button(self.loginFrame, text="Recuperar contraseña", font=(font, 15), command=self.Validate)
        self.recoverBtn.config(bg=colorPalette[2], fg=colorPalette[4])
        self.recoverBtn.place(x=centerX - 240, y=400, anchor="center", width=350)
        self.recoverBtn.config(state="disabled")

        self.faceLb = Label(self.loginFrame, text="No se detectó su rostro", width=40, font=(font, 16))
        self.faceLb.config(bg=colorPalette[1], fg=colorPalette[4])
        self.faceLb.place(x=centerX + 720, y=640, anchor="e")

    def next(self):
        self.loginFrame.destroy()
        if self.userTwo is None:
            self.loginFrame.pack_forget()
            self.parentFrame.pack()
        else:
            principal = PrincipalGui(self.window, self.width, self.height, [self.userOne, self.userTwo])

    def nextPass(self):
        if self.userTwo is None and self.userTxt.get() == self.user.password:
            self.allow.set("False")
            self.loginFrame.pack_forget()
            self.parentFrame.pack()

        elif self.userTxt.get() == self.user.password == self.user.password:
            self.allow.set("False")
            self.loginFrame.pack_forget()
            principal = PrincipalGui(self.window, self.width, self.height, [self.userOne, self.userTwo])

    def Validate(self):
        self.loginFrame.pack_forget()
        recover = PassRetrieve(self.window, self.width, self.height, self.user.user, self.loginFrame)

    def showImage(self):
        inicialTime = time.time()
        frequence = 10
        cap = cv2.VideoCapture(0)

        face_cascade = cv2.CascadeClassifier(os.path.abspath('Code/haarcascade_frontalface_default.xml'))
        print(self.allow.get())
        while self.allow.get() == "True":
            currentTime = time.time()
            transcurredTime = -inicialTime + currentTime

            ret, frame = cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0, 5))
                roi_gray = gray[y:y + w, x:x + w]

            if len(faces) != 0:
                cv2.imwrite("Code/GraphicalUserInterface/Faces/" + self.user.user + "LOG.jpg", roi_gray)
                controler = facialRecognogtion(self.user.user)
                flag = controler.comparation()
                if flag and transcurredTime < frequence:
                    self.faceLb.config(text="Se reconoció su rostro")
                    self.loginFrame.pack_forget()
                    self.next()
                    break

            # Crear una máscara circular
            mask = Image.new("L", (frame.shape[1], frame.shape[0]), 0)
            draw = ImageDraw.Draw(mask)
            radius = min(mask.width, mask.height) // 2
            center = (mask.width // 2, mask.height // 2)
            draw.ellipse((center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius), fill=255)

            # Aplicar la máscara a la imagen
            frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            frame_pil.putalpha(mask)

            # Convierte Image de PIL a PhotoImage de tkinter
            frame_tk = ImageTk.PhotoImage(image=frame_pil)

            colorPallete=["#8B0000", "#630000", "#1C1C1C", "#000000", "#FFFFFF"]
            self.photoCanvas.configure(bg=colorPallete[0], highlightbackground=colorPallete[0])

            # Mostrar la imagen en el Canvas
            self.photoCanvas.create_image(0, 0, anchor="nw", image=frame_tk)
            self.window.update()
            self.faceLb.config(text="Analizando...")

            if transcurredTime >= frequence:
                self.faceLb.config(text="No se reconoció su rostro")
                self.recoverBtn.config(state="normal")
                self.passwordBtn.config(state="normal")