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

        self.registerLb = Label(self.InformationFrame, text="Registro de usuario", font=(font, 35))
        self.registerLb.place(x=centerX, y=50, anchor="center")

        self.registerLb = Label(self.InformationFrame, text="En esta sección se debe ingresar su información general", font=(font, 20))
        self.registerLb.place(x=375, y=125, anchor="center")

        self.questionOneLb= Label (self.InformationFrame, text="Ingrese su nombre", font=(font,15))
        self.questionOneLb.place(x=centerX, y=150, anchor="center")
        self.questionOneEntry= Entry(self.InformationFrame,width=25, font=(font, 15))
        self.questionOneEntry.place(x=centerX, y=200, anchor="center")

        self.questionTwoLb= Label (self.InformationFrame, text="Ingrese su usuario", font=(font,15))
        self.questionTwoLb.place(x=centerX, y=250, anchor="center")
        self.questionTwoEntry= Entry(self.InformationFrame,width=25, font=(font, 15))
        self.questionTwoEntry.place(x=centerX, y=300, anchor="center")

        self.questionThreeLb= Label (self.InformationFrame, text="Ingrese su nickname", font=(font,15))
        self.questionThreeLb.place(x=centerX, y=350, anchor="center")
        self.questionThreeEntry= Entry(self.InformationFrame,width=25, font=(font, 15))
        self.questionThreeEntry.place(x=centerX, y=400, anchor="center")

        self.questionFourLb= Label (self.InformationFrame, text="Ingrese su edad", font=(font,15))
        self.questionFourLb.place(x=centerX, y=450, anchor="center")
        self.questionFourEntry= Entry(self.InformationFrame,width=25, font=(font, 15))
        self.questionFourEntry.place(x=centerX, y=500, anchor="center")

        self.questionFiveLb= Label (self.InformationFrame, text="Ingrese su correo", font=(font,15))
        self.questionFiveLb.place(x=centerX, y=550, anchor="center")
        self.questionFiveEntry= Entry(self.InformationFrame,width=25, font=(font, 15))
        self.questionFiveEntry.place(x=centerX, y=600, anchor="center")

        self.questionSixLb= Label (self.InformationFrame, text="Ingrese su contraseña", font=(font,15))
        self.questionSixLb.place(x=centerX, y=650, anchor="center")
        self.questionSixEntry= Entry(self.InformationFrame,width=25, font=(font, 15))
        self.questionSixEntry.place(x=centerX, y=700, anchor="center")



        self.nextBtn = Button(self.InformationFrame, text="next", font=(font, 15), command = self.nextPage)
        self.nextBtn.place(x=2*centerX-100, y=650, anchor="nw")

    def nextPage(self):
        answer=messagebox.askyesno("Confirmación", "¿Estás seguro de continuar?")
        if answer:     
            try:
                if not (User.ValidateExistence(self,self.questionTwoEntry.get())):
                    user=User(self.questionTwoEntry.get(),
                            self.questionOneEntry.get(),
                            self.questionThreeEntry.get(),
                            self.questionSixEntry.get(),
                            self.questionFourEntry.get(),
                            self.questionFiveEntry.get()," "," "," ")
                    if(user.validation):
                        self.InformationFrame.pack_forget()
                        app=registerGUIAnswers(self.window,self.width,self.height,user,self.parentFrame)
                        
                    else: 
                        messagebox.showinfo("Mensaje", "Datos incorrectos")
                else: 
                     messagebox.showinfo("Mensaje", "Usuario existente")

            except Exception as e:
                print(e)
                messagebox.showinfo("Mensaje", "Datos incorrectos")
            
            

"""     
root = Tk()
widthScreen = root.winfo_screenwidth()
heightScreen = root.winfo_screenheight()
root.geometry(f"{widthScreen}x{heightScreen}")
root.resizable(False, False)

root.title("Eagle Defender")




root.mainloop()
"""