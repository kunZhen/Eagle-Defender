from tkinter import *
from GraphicalUserInterface.LoginGui import *


class RegisterGui:
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height

        centerX = width / 2
        centerY = height / 2

        font="Helvetica"

        self.registerFrame = Frame(window, width=width, height=height, bg="green")
        self.registerFrame.pack()

        self.registerLb = Label(self.registerFrame, text="Registro de usuario", font=(font, 35))
        self.registerLb.place(x=centerX, y=50, anchor="center")

        self.registerBtn = Button(self.registerFrame, text="Registrar", font=(font, 15), command=self.RegisterUser)
        self.registerBtn.place(x=centerX, y=height - 100, anchor="center")

        # Name
        self.nameLb = Label(self.registerFrame, text="Nombre: ", font=(font, 15))
        self.nameLb.place(x=centerX, y=150, anchor="w")

        self.nameTxt = Entry(self.registerFrame, width=25, font=(font, 15))
        self.nameTxt.place(x=centerX + 25, y=180, anchor="w")

        # User
        self.userLb = Label(self.registerFrame, text="Usuario: ", font=(font, 15))
        self.userLb.place(x=centerX + 350, y=150, anchor="w")

        self.passwordTxt = Entry(self.registerFrame, width=25, font=(font, 15))
        self.passwordTxt.place(x=centerX + 375, y=180, anchor="w")

        # Password
        self.passwordLb = Label(self.registerFrame, text="Contraseña: ", font=(font, 15))
        self.passwordLb.place(x=centerX, y=220, anchor="w")

        self.passwordTxt = Entry(self.registerFrame, width=25, font=(font, 15))
        self.passwordTxt.place(x=centerX + 25, y=250, anchor="w")

        # Mail
        self.mailLb = Label(self.registerFrame, text="Correo electrónico: ", font=(font, 15))
        self.mailLb.place(x=centerX + 350, y=220, anchor="w")

        self.mailTxt = Entry(self.registerFrame, width=25, font=(font, 15))
        self.mailTxt.place(x=centerX + 375, y=250, anchor="w")

        # Age
        self.ageLb = Label(self.registerFrame, text="Edad: ", font=(font, 15))
        self.ageLb.place(x=centerX, y=290, anchor="w")

        self.ageTxt = Entry(self.registerFrame, width=25, font=(font, 15))
        self.ageTxt.place(x=centerX + 25, y=320, anchor="w")

        # Personal questions
        self.q1Lb = Label(self.registerFrame, text="Pregunta 1: ", font=(font, 15))
        self.q1Lb.place(x=centerX, y=395, anchor="w")

        self.q1Txt = Entry(self.registerFrame, width=25, font=(font, 15))
        self.q1Txt.place(x=centerX + 25, y=425, anchor="w")

        self.q2Lb = Label(self.registerFrame, text="Pregunta 2: ", font=(font, 15))
        self.q2Lb.place(x=centerX + 350, y=395, anchor="w")

        self.q2Txt = Entry(self.registerFrame, width=25, font=(font, 15))
        self.q2Txt.place(x=centerX + 375, y=425, anchor="w")

        self.q3Lb = Label(self.registerFrame, text="Pregunta 3: ", font=(font, 15))
        self.q3Lb.place(x=centerX, y=455, anchor="w")

        self.q3Txt = Entry(self.registerFrame, width=25, font=(font, 15))
        self.q3Txt.place(x=centerX + 25, y=485, anchor="w")

        self.q4Lb = Label(self.registerFrame, text="Pregunta 4: ", font=(font, 15))
        self.q4Lb.place(x=centerX + 350, y=455, anchor="w")

        self.q4Txt = Entry(self.registerFrame, width=25, font=(font, 15))
        self.q4Txt.place(x=centerX + 375, y=485, anchor="w")

        self.q5Lb = Label(self.registerFrame, text="Pregunta 5: ", font=(font, 15))
        self.q5Lb.place(x=centerX, y=525, anchor="w")

        self.q5Txt = Entry(self.registerFrame, width=25, font=(font, 15))
        self.q5Txt.place(x=centerX + 25, y=555, anchor="w")

        # Profile picture
        self.profileLb = Label(self.registerFrame, text="Foto de prefil: ", font=(font, 15))
        self.profileLb.place(x=200, y=200, anchor="nw")

        self.photoCanvas = Canvas(self.registerFrame, width=400, height=400)
        self.photoCanvas.place(x=200, y=230, anchor="nw")

        self.profileBtn = Button(self.registerFrame, text="Seleccionar foto", font=(font, 15), command=self.UploadPhoto)
        self.profileBtn.place(x=200, y=650, anchor="nw")

    def RegisterUser(self):
        self.registerFrame.pack_forget()

    def UploadPhoto(self):
        x1, y1 = 25, 25
        x2, y2 = 375, 375
        self.photoCanvas.create_rectangle(x1, y1, x2, y2, fill="red")
