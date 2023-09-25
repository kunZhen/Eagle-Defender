from tkinter import *
from GraphicalUserInterface.RegisterGui import *
from GraphicalUserInterface.PrincipalGui import *


class LoginGui:
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height

        font = "Helvetica"

        centerX = width / 2
        centerY = height / 2

        self.loginFrame = Frame(window, width=width, height=height, bg="blue")
        self.loginFrame.pack()

        self.loginLb = Label(self.loginFrame, text="Inicio de sesion", font=(font, 35))
        self.loginLb.place(x=centerX, y=75, anchor="center")

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

        self.registerBtn = Button(self.loginFrame, text="Registrar nuevo usuario", font=(font, 15), command=self.Register)
        self.registerBtn.place(x=centerX, y=centerY + 400, anchor="center")

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
        register = RegisterGui(self.window, self.width, self.height)
        self.loginFrame.pack()

