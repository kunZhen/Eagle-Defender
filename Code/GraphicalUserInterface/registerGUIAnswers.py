from tkinter import *
from tkinter import messagebox
from User import *
from registerGUIPhoto import RegisterGuiPhoto


class registerGUIAnswers:

    def __init__(self, window, width, height, user: User, parentFrame):
        self.window = window
        self.width = width
        self.height = height
        self.user = user
        self.parentFrame = parentFrame

        centerX = width / 2
        centrerY = width / 2

        font = "Helvetica"

        colorPalette = ["#8B0000", "#630000", "#1C1C1C", "#000000", "#FFFFFF"]

        # Esta es el frame de esta sección

        self.AnswersFrame = Frame(window, width=self.width, height=self.height, bg=colorPalette[0])
        self.AnswersFrame.pack()

        self.registerLb = Label(self.AnswersFrame, text="Preguntas para la recuperación de contraseña",
                                font=(font, 35))
        self.registerLb.config(bg=colorPalette[0], fg=colorPalette[3])
        self.registerLb.place(x=centerX, y=50, anchor="center")

        self.registerLb = Label(self.AnswersFrame,
                                text="                Responder todas las preguntas               ",
                                font=(font, 20))
        self.registerLb.config(bg=colorPalette[1], fg=colorPalette[4])
        self.registerLb.place(x=centerX, y=125, anchor="center")

        self.questionOneLb = Label(self.AnswersFrame, text="¿Qué fue lo primero que aprendí a cocinar?", width=35,
                                   font=(font, 15))
        self.questionOneLb.config(bg=colorPalette[1], fg=colorPalette[4])
        self.questionOneLb.place(x=centerX, y=180, anchor="center")
        self.questionOneEntry = Entry(self.AnswersFrame, width=25, font=(font, 15))
        self.questionOneEntry.place(x=centerX, y=220, anchor="center")

        self.questionTwoLb = Label(self.AnswersFrame, text="¿Qué país deseo visitar?", width=35, font=(font, 15))
        self.questionTwoLb.config(bg=colorPalette[1], fg=colorPalette[4])
        self.questionTwoLb.place(x=centerX, y=270, anchor="center")
        self.questionTwoEntry = Entry(self.AnswersFrame, width=25, font=(font, 15))
        self.questionTwoEntry.place(x=centerX, y=320, anchor="center")

        self.questionThreeLb = Label(self.AnswersFrame, text="¿Nombre de mi mejor amigo?", width=35, font=(font, 15))
        self.questionThreeLb.config(bg=colorPalette[1], fg=colorPalette[4])
        self.questionThreeLb.place(x=centerX, y=370, anchor="center")
        self.questionThreeEntry = Entry(self.AnswersFrame, width=25, font=(font, 15))
        self.questionThreeEntry.place(x=centerX, y=420, anchor="center")

        self.questionFourLb = Label(self.AnswersFrame, text="¿Nombre de mi primera mascota?", width=35, font=(font, 15))
        self.questionFourLb.config(bg=colorPalette[1], fg=colorPalette[4])
        self.questionFourLb.place(x=centerX, y=470, anchor="center")
        self.questionFourEntry = Entry(self.AnswersFrame, width=25, font=(font, 15))
        self.questionFourEntry.place(x=centerX, y=520, anchor="center")

        self.questionFiveLb = Label(self.AnswersFrame, text="¿A qué me quería dedicar cuando era niño?", width=35,
                                    font=(font, 15))
        self.questionFiveLb.config(bg=colorPalette[1], fg=colorPalette[4])
        self.questionFiveLb.place(x=centerX, y=570, anchor="center")
        self.questionFiveEntry = Entry(self.AnswersFrame, width=25, font=(font, 15))
        self.questionFiveEntry.place(x=centerX, y=620, anchor="center")

        self.nextBtn = Button(self.AnswersFrame, text="next", font=(font, 15), command=self.nextPage)
        self.nextBtn.config(bg=colorPalette[2], fg=colorPalette[4])
        self.nextBtn.place(x=2 * centerX - 100, y=670, anchor="nw")

    def nextPage(self):
        print(self.user)
        questions = [self.questionOneEntry.get(), self.questionTwoEntry.get(), self.questionThreeEntry.get(),
                     self.questionFourEntry.get(), self.questionFiveEntry.get()]
        answer = messagebox.askyesno("Confirmación", "¿Estás seguro de continuar?")
        if answer:
            if self.notEmpy(questions):
                self.user.SetAttributes(None, None, questions, None, None, None, None)
                self.AnswersFrame.pack_forget()
                app=RegisterGuiPhoto(self.window,self.width,self.height,self.user, self.parentFrame)
            else:
                messagebox.showinfo("Mensaje", "Debe responder todas las preguntas")

    def notEmpy(self, questions):
        counter = 0
        questionsAmount = 0
        while counter != 5:
            if questions[counter] != "":
                questionsAmount += 1
            counter += 1
        if questionsAmount == 5:
            return True
        return False
