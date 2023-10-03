from tkinter import *
from modificateDataGui import *



class PrincipalGui:
    def __init__(self, window, width, height,users):
        self.window = window
        self.width = width
        self.height = height
        self.users=users

        font = "Helvetica"

        centerX = width / 2
        centerY = height / 2

        self.principalFrame = Frame(window, width=width, height=height, bg="purple")
        self.principalFrame.pack()

        self.titleLb = Label(self.principalFrame, text="Eagle Defender", font=(font, 50))
        self.titleLb.place(x=centerX, y=75, anchor="center")

        self.user1Btn = Button(self.principalFrame, text=users[0], font=(font, 15), command= self.changeDataUser1)
        self.user2Btn = Button(self.principalFrame, text=users[1], font=(font, 15), command= self.changeDataUser2)
        self.user1Btn.place(x=75, y=75, anchor="nw")
        self.user2Btn.place(x=width - 75, y=75, anchor="ne")

        self.playBtn = Button(self.principalFrame, text="Jugar", font=(font, 15))
        self.hallFameBtn = Button(self.principalFrame, text="Salón de la Fama", font=(font, 15))
        self.helpBtn = Button(self.principalFrame, text="Sección de ayuda", font=(font, 15))
        self.playBtn.place(x=centerX, y=centerY + 150, anchor="center")
        self.hallFameBtn.place(x=centerX, y=centerY + 200, anchor="center")
        self.helpBtn.place(x=centerX, y=centerY + 250, anchor="center")
    def changeDataUser1(self): 
        self.principalFrame.pack_forget()
        app=modificateDataGui(self.window,self.width,self.height,self.users[0],self,0)
    def changeDataUser2(self): 
        self.principalFrame.pack_forget()
        app=modificateDataGui(self.window,self.width,self.height,self.users[1],self,1)
    def updateLb(self):
        self.user1Btn.config(text=self.users[0])
        self.user2Btn.config(text=self.users[1])

"""if __name__ == '__main__':
    root = Tk()
    # take the dimensions of the computer screen
    widthScreen = root.winfo_screenwidth()
    heightScreen = root.winfo_screenheight()

    # set game screen size
    root.geometry(f"{widthScreen}x{heightScreen}")
    root.resizable(False, False)

    root.title("Eagle Defender")

    app =PrincipalGui(root, widthScreen, heightScreen,["Is2", "Is2"] )

    root.mainloop()"""

