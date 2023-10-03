#Import dependencies
import os
import sys
import tkinter
import random
from tkinter import messagebox
import LoginGui

#Import developed modules
sys.path.append("Code")
from User import *

class PassRetrieve:
    """
    Allows the creation of a window for password retrieval

    Atributes:
        - window (Tk): is the root screen of the ongoing app
        - width
        - height
        
    Methods:

    """

    def __init__(self, window, width, height, username:str, parentFrame:LoginGui):
        """
        Creates an instance of the password retrieval screen

        Parameters:
            - window (Tk): root screen
            - width (float): screen width size
            - height (float): screen height size
            - username (String): user which wants to retrieve password
            - lan (Stranguage): language in which the screen should display
        """
     # JSON file retrieval
        self.name = username
        currentData:User = User.LoadJson(username)
        self.user:User=currentData
        self.parentFrame=parentFrame
        qaList = currentData.answers

     # Generate two random for numbers for question-answer retrieval from list
        limit = len(qaList)

        randomNumOne=random.randint(0,limit-1)
        randomNumTwo=random.randint(0,limit-1)

        while randomNumOne==randomNumTwo: 
            randomNumTwo=random.randint(0,limit-1)

        randomInts = [randomNumOne,randomNumTwo]
        
     # Save the questions into an array for displaying later
        self.questions=["¿Qué fue lo primero que aprendí a cocinar?",
                        "¿Qué país deseo visitar?",
                        "¿Nombre de mi mejor amigo?",
                        "¿Nombre de mi primera mascota?",
                        "¿A qué me quería dedicar cuando era niño?"]
        
        self.chosenQuestion=[]
        self.correctAnswers= []
        for i in range(0,limit):
            if (i==randomInts[0]):
                self.chosenQuestion.append(self.questions[i])
                self.correctAnswers.append(qaList[i])
            if (i==randomInts[1]):
                self.chosenQuestion.append(self.questions[i])
                self.correctAnswers.append(qaList[i])
        print(self.chosenQuestion)
    
     # Initiation of window properties
        self.state = True
        self.window = window
        self.width = width
        self.height = height
        font = "Helvetica"
     # Set screen frame
        self.screenFrame = tkinter.Frame(self.window, width=self.width, height=self.height, bg="#8B0000")
        self.screenFrame.pack()
     # Set screen objects
        centerX  = width/2

        self.headerTitle = tkinter.Label(self.screenFrame, text="                        Recuperación de constraseña                        ", font=(font, 35))
        self.headerTitle.place(x=centerX, y=50, anchor="center")

        self.promptText = tkinter.Label(self.screenFrame, text="Responda las preguntas para poder restablecer su contraseña",font=(font, 15))
        self.promptText.place(x=self.width//2-600, y=150)                 

        self.entryQ2 = tkinter.Entry(self.screenFrame, font=(font, 15), width=35)
        self.entryQ2.place(x=265, y=400)
        self.entryQ1 = tkinter.Entry(self.screenFrame, font=(font, 15), width= 35)
        self.entryQ1.place(x=265, y=250)

        self.questionOneLb= tkinter.Label(self.screenFrame, font=(font,15), width=35, text=self.chosenQuestion[0])
        self.questionOneLb.place(x=265,y=200)
        self.questionTwoLb= tkinter.Label(self.screenFrame, font=(font,15), width=35, text=self.chosenQuestion[1])
        self.questionTwoLb.place(x=265,y=350)
        
        #Write new password (1)
        passSpace = [self.width//2+110, 250]
        confirmation1 = tkinter.Label(self.screenFrame, text="Escriba su nueva contraseña", font= (font, 15), bg="white")
        confirmation1.place(x=passSpace[0], y=passSpace[1]-100)

        self.newPass1 = tkinter.Entry(self.screenFrame,show="*", font = (font, 15))
        self.newPass1.place(x=passSpace[0], y=passSpace[1]-50)

        #Write confirmatoon of password (2)
        confirmation2 = tkinter.Label(self.screenFrame, text="Escriba nuevamente la nueva contraseña", font=(font, 15), bg="white")
        confirmation2.place(x=passSpace[0], y=passSpace[1])

        self.newPass2 = tkinter.Entry(self.screenFrame, show="*", font=(font, 15))
        self.newPass2.place(x=passSpace[0], y=passSpace[1]+50)

        #Place screen buttons
        leaveButton = tkinter.Button(self.screenFrame,text="Cancelar", command= self.endScreen, font=(font, 15), width=10)
        leaveButton.place(x=centerX-60, y=700)

        self.validateButton = tkinter.Button(self.screenFrame, text="Confirmar", command=self.checkAnswers, font=(font, 15), width=10)
        self.validateButton.place(x=centerX-60, y=650)


    def checkAnswers(self):
        """
        Verifies if the written answers are the same as the ones saved on the user file
        """
        ans1 = self.correctAnswers[0]
        ans2 = self.correctAnswers[1]

        if self.entryQ1.get()==ans1 and self.entryQ2.get()==ans2: 
            if self.newPass1.get()!="" and self.newPass2.get()!="": 
                if self.newPass1.get()==self.newPass2.get():
                    if User.ValidatePassword(self.newPass1.get()):
                        self.user.SetUser(None,self.newPass1.get(),None)
                        self.screenFrame.pack_forget()
                        self.parent.pack()
                    else:
                        requirements = [
                                    "La contraseña no cumple los requisitos:",
                                    "Al menos ocho caracteres",
                                    "Al menos una minúscula o mayúscula",
                                    "Al menos un número",
                                    "Al menos un caracter especial"

                                ]
                        message = "\n".join(requirements)
                        messagebox.showerror("Error", message)
                    
                else: 
                    messagebox.showerror("Error", "Las contraseñas no coinciden")
            else: 
                messagebox.showerror("Error", "Los espacios de la contraseña están vacíos")
        else: 
            messagebox.showerror("Error", "Las respuestas no son correctas")
    def endScreen(self):
        self.screenFrame.pack_forget()
        self.parentFrame.pack()

#Test code for testing
def main():
    root = tkinter.Tk()
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.geometry(f"{screenWidth}x{screenHeight}")
    root.resizable(False, False)
    root.title("Eagle Defender")

    test = PassRetrieve(root, screenWidth, screenHeight, "Kun", None)
    root.mainloop()


#Calls the 
main()
