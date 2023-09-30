from tkinter  import *
from tkinter import messagebox
from registerGUIAnswers import registerGUIAnswers
from User import *

class registerGui: 

    def __init__(self,window,width,height, parentFrame):
       
        self.window = window
        self.width = width
        self.height = height
        self.parentFrame=parentFrame

        centerX  = width/2
        centrerY = width/2

        font="Helvetica"
        
        #Esta es el frame de esta sección
        
        self.InformationFrame = Frame (window,width=self.width,height=self.height, bg= "green")
        self.InformationFrame.pack()
        ##

        # Variable de control para los radio buttons
        self.colorVar = StringVar()
        self.colorVar.set("default")

        # Crear radio button para el color Rojo
        Radiobutton(self.InformationFrame, text="Rojo     ", variable=self.colorVar, font=(font,15), width=8, value="red", command=self.showColor).place(x=centerX+300, y=250, anchor="center")

        # Crear radio button para el color Verde
        Radiobutton(self.InformationFrame, text="Verde   ", variable=self.colorVar, font=(font,15), width=8, value="green", command=self.showColor).place(x=centerX+300, y=300, anchor="center")

        # Crear radio button para el color Azul
        Radiobutton(self.InformationFrame, text="Azul     ", variable=self.colorVar, font=(font,15), width=8,value="blue", command=self.showColor).place(x=centerX+300, y=350, anchor="center")

        # Crear radio button para el color Amarillo
        Radiobutton(self.InformationFrame, text="Amarillo", variable=self.colorVar, font=(font,15), width=8, value="yellow", command=self.showColor).place(x=centerX+300, y=400, anchor="center")

        # Crear radio button para el color naranja
        Radiobutton(self.InformationFrame, text="Naranja", variable=self.colorVar, font=(font,15), width=8, value="orange", command=self.showColor).place(x=centerX+300, y=450, anchor="center")

        # Crear radio button para el color naranja
        Radiobutton(self.InformationFrame, text="Morado", variable=self.colorVar, font=(font,15), width=8, value="violet", command=self.showColor).place(x=centerX+300, y=500, anchor="center")

        self.colorLabel = Label(self.InformationFrame, text="Seleccione su color favorito", font=(font, 15))
        self.colorLabel.place(x=centerX+300, y=200, anchor="center")

        ##

        self.registerLb = Label(self.InformationFrame, text="Registro de usuario", font=(font, 35))
        self.registerLb.place(x=centerX, y=50, anchor="center")

        self.registerLb = Label(self.InformationFrame, text="                    En esta sección se debe ingresar su información general                    ", font=(font, 20))
        self.registerLb.place(x=centerX, y=125, anchor="center")

        self.questionOneLb= Label (self.InformationFrame, text="Ingrese su nombre de usuario", font=(font,15))
        self.questionOneLb.place(x=centerX-300, y=200, anchor="center")
        self.questionOneEntry= Entry(self.InformationFrame,width=25, font=(font, 15))
        self.questionOneEntry.place(x=centerX-300, y=250, anchor="center")

        self.questionTwoLb= Label (self.InformationFrame, text="Ingrese su correo", font=(font,15))
        self.questionTwoLb.place(x=centerX-300, y=300, anchor="center")
        self.questionTwoEntry= Entry(self.InformationFrame,width=25, font=(font, 15))
        self.questionTwoEntry.place(x=centerX-300, y=350, anchor="center")

        self.questionThreeLb= Label (self.InformationFrame, text="Ingrese su contraseña", font=(font,15))
        self.questionThreeLb.place(x=centerX-300, y=400, anchor="center")
        self.questionThreeEntry= Entry(self.InformationFrame,width=25, font=(font, 15))
        self.questionThreeEntry.place(x=centerX-300, y=450, anchor="center")

        self.questionFourLb= Label (self.InformationFrame, text="Confirme su contraseña", font=(font,15))
        self.questionFourLb.place(x=centerX-300, y=500, anchor="center")
        self.questionFourEntry= Entry(self.InformationFrame,width=25, font=(font, 15))
        self.questionFourEntry.place(x=centerX-300, y=550, anchor="center")

        self.nextBtn = Button(self.InformationFrame, text="next", font=(font, 15), command = self.nextPage)
        self.nextBtn.place(x=2*centerX-100, y=650, anchor="nw")

    def nextPage(self):
        answer=messagebox.askyesno("Confirmación", "¿Estás seguro de continuar?")
        if answer:     
            try:
                if not (User.ValidateExistence(self,self.questionTwoEntry.get()) and self.questionOneEntry.get()!=""):
                    if(self.questionFourEntry.get()==self.questionThreeEntry.get())  :
                        user=User(self.questionOneEntry.get(),
                                self.questionThreeEntry.get(),
                                self.questionTwoEntry.get(),
                                self.colorVar.get(),
                                [""]," "," ")
                        if(user.validation):
                            self.InformationFrame.pack_forget()
                            app=registerGUIAnswers(self.window,self.width,self.height,user,self.parentFrame)
                        else: 
                            if user.errorType=="password":
                                requirements = [
                                    "La contraseña no cumple los requisitos:",
                                    "Al menos ocho caracteres",
                                    "Al menos una minúscula o mayúscula",
                                    "Al menos un número",
                                    "Al menos un caracter especial"

                                ]
                                message = "\n".join(requirements)
                                messagebox.showinfo("Mensaje", message)
                            elif user.errorType=="user":
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
