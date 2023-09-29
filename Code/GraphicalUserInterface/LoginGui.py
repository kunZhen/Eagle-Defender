import time
from tkinter import *
import tkinter as tk

import cv2
from RegisterGui import *
from PrincipalGui import *
from PIL import Image, ImageTk,ImageDraw


class LoginGui:
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height
        self.allow=tk.StringVar()
        self.allow.set("True")


        font = "Helvetica"

        centerX = width / 2
        centerY = height / 2

        self.loginFrame = Frame(window, width=width, height=height, bg="blue")
        self.loginFrame.pack()

        self.loginLb = Label(self.loginFrame, text="Inicio de sesion", font=(font, 35))
        self.loginLb.place(x=centerX, y=75, anchor="center")

        self.photoCanvas = Canvas(self.loginFrame, width=600, height=600)
        self.photoCanvas.place(x=150+centerX, y=100, anchor="nw")
        

        self.userLb = Label(self.loginFrame, text="Usuario/Correo: ", font=(font, 15))
        self.userLb.place(x=centerX - 105, y=centerY - 150, anchor="e")

        # Txt: Text box
        self.userTxt = Entry(self.loginFrame, width=25, font=(font, 15))
        self.userTxt.place(x=centerX - 100, y=centerY - 150, anchor="w")

        self.faceBtn = Button(self.loginFrame, text="Reconocimiento facial", font=(font, 15), command=self.Facial)
        self.faceBtn.place(x=centerX, y=centerY - 100, anchor="n")

        self.enablePasswordBtn = Button(self.loginFrame, text="Usar otro método para ingresar", font=(font, 15),
                                        command=self.EnablePassword)
        self.enablePasswordBtn.place(x=centerX, y=centerY + 50, anchor="n")

        self.passwordLb = Label(self.loginFrame, text="Ingrese contraseña", font=(font, 15))

        self.passwordTxt = Entry(self.loginFrame, width=25, font=(font, 15))

        self.validateBtn = Button(self.loginFrame, text="Continuar", font=(font, 15), command=self.Validate)
        self.validateBtn.place(x=centerX,y=centerY+100, anchor="center")

        self.registerBtn = Button(self.loginFrame, text="Registrar nuevo usuario", font=(font, 15), command=self.Register)
        self.registerBtn.place(x=centerX, y=centerY + 150, anchor="center")

    def Facial(self):
        self.loginFrame.destroy()
        principal = PrincipalGui(self.window, self.width, self.height)

    def EnablePassword(self):
        self.passwordLb.place(x=self.width/2, y=self.height/2 + 150, anchor="n")
        self.passwordTxt.place(x=self.width / 2, y=self.height / 2 + 200, anchor="n")
        self.validateBtn.place(x=self.width / 2, y=self.height / 2 + 250, anchor="n")

    def Validate(self):
        self.loginFrame.destroy()
        principal = PrincipalGui(self.window, self.width, self.height)

    def Register(self):
        self.loginFrame.pack_forget()
        register=registerGui(self.window,self.width,self.height,self.loginFrame)
    def showImage(self):
        inicialTime = time.time()
        frequence = 10
        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        while self.allow.get() == "True":
            currentTime = time.time()
            transcurredTime = -inicialTime + currentTime
            print(transcurredTime)

            ret, frame = cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0, 5))
                roi_gray = gray[y:y + w, x:x + w]

            if len(faces) != 0:
                cv2.imwrite("rostros/isaacLOG.jpg", roi_gray)

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

            self.photoCanvas.configure(bg='blue', highlightbackground='blue')

            # Mostrar la imagen en el Canvas
            self.photoCanvas.create_image(0, 0, anchor="nw", image=frame_tk)
            self.window.update()

            if transcurredTime >= frequence:
                pass