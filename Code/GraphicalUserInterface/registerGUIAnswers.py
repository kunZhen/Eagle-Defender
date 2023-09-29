from tkinter import *
from tkinter import messagebox
from User import *
from registerGUIPhoto import RegisterGuiPhoto

class registerGUIAnswers: 
    
    def __init__(self,window,width,height,user:User, parentFrame):
        self.window = window
        self.width = width
        self.height = height
        self.user=user 
        self.parentFrame=parentFrame

        centerX  = width/2
        centrerY = width/2

        font="Helvetica"
        #Esta es el frame de esta sección
        

        self.AnswersFrame = Frame (window,width=self.width,height=self.height, bg= "green")
        self.AnswersFrame.pack()

        self.registerLb = Label(self.AnswersFrame, text="En esta sección debe responder al menos una pregunta", font=(font, 20))
        self.registerLb.place(x=375, y=150, anchor="center")

        self.questionOneLb= Label (self.AnswersFrame, text="¿Qué fue lo primero que aprendí a cocinar", font=(font,15))
        self.questionOneLb.place(x=centerX, y=150, anchor="center")
        self.questionOneEntry= Entry(self.AnswersFrame,width=25, font=(font, 15))
        self.questionOneEntry.place(x=centerX, y=200, anchor="center")

        self.questionTwoLb= Label (self.AnswersFrame, text="¿Qué país deseo visitar?", font=(font,15))
        self.questionTwoLb.place(x=centerX, y=250, anchor="center")
        self.questionTwoEntry= Entry(self.AnswersFrame,width=25, font=(font, 15))
        self.questionTwoEntry.place(x=centerX, y=300, anchor="center")

        self.questionThreeLb= Label (self.AnswersFrame, text="¿Nombre de mi mejor amigo?", font=(font,15))
        self.questionThreeLb.place(x=centerX, y=350, anchor="center")
        self.questionThreeEntry= Entry(self.AnswersFrame,width=25, font=(font, 15))
        self.questionThreeEntry.place(x=centerX, y=400, anchor="center")

        self.questionFourLb= Label (self.AnswersFrame, text="¿Nombre de mi primera mascota?", font=(font,15))
        self.questionFourLb.place(x=centerX, y=450, anchor="center")
        self.questionFourEntry= Entry(self.AnswersFrame,width=25, font=(font, 15))
        self.questionFourEntry.place(x=centerX, y=500, anchor="center")

        self.questionFiveLb= Label (self.AnswersFrame, text="¿A qué me quería dedicar cuando era niño?", font=(font,15))
        self.questionFiveLb.place(x=centerX, y=550, anchor="center")
        self.questionFiveEntry= Entry(self.AnswersFrame,width=25, font=(font, 15))
        self.questionFiveEntry.place(x=centerX, y=600, anchor="center")
        
        self.nextBtn = Button(self.AnswersFrame, text="next", font=(font, 15), command = self.nextPage)
        self.nextBtn.place(x=2*centerX-100, y=650, anchor="nw")

        

    def nextPage(self):
        print(self.user)
        questions=[self.questionOneEntry.get(),self.questionTwoEntry.get(),self.questionThreeEntry.get(),self.questionFourEntry.get(), self.questionFiveEntry.get()]
        self.user.SetAnswer(questions)
        answer=messagebox.askyesno("Confirmación", "¿Estás seguro de continuar?")
        if answer:
            if self.notEmpy(questions):
                self.AnswersFrame.pack_forget()
                app=RegisterGuiPhoto(self.window,self.width,self.height,self.user,self.parentFrame)
            else:
                messagebox.showinfo("Mensaje", "Debe responder al menos una pregunta") 
            
    
    def notEmpy(self,questions): 
        counter = 0
        while counter!=5: 
            if(questions[counter]!=""):
                return True
            counter+=1
        return False



