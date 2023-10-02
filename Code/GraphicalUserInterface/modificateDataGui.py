from tkinter import *
from tkinter import ttk
from User import *
import tkinter

class modificateDataGui:
    def __init__(self, window, width, height,users):
        self.window = window
        self.width = width
        self.height = height
        self.users=users

        font = "Helvetica"

        centerX = width / 2
        centerY = height / 2

        self.dataFrame = Frame(window, width=width, height=height, bg="purple")
        self.dataFrame.pack()


        self.dataLb = Label(self.dataFrame, text="         Cambio de datos         ", font=(font, 35))
        self.dataLb.place(x=centerX, y=50, anchor="center")

        self.registerLb = Label(self.dataFrame, text="                                   En esta sección puede" 
                                +" modificar su información general                                          ", font=(font, 20))
        self.registerLb.place(x=centerX, y=125, anchor="center")
        
        
         #_________________________________General data__________________________________________#
        self.questionOneLb= Label (self.dataFrame, text="Ingrese su nombre de usuario", font=(font,15))
        self.questionOneLb.place(x=centerX-500, y=200, anchor="center")
        self.questionOneEntry= Entry(self.dataFrame,width=25, font=(font, 15))
        self.questionOneEntry.place(x=centerX-500, y=250, anchor="center")

        self.questionTwoLb= Label (self.dataFrame, text="Ingrese su correo", font=(font,15))
        self.questionTwoLb.place(x=centerX-500, y=300, anchor="center")
        self.questionTwoEntry= Entry(self.dataFrame,width=25, font=(font, 15))
        self.questionTwoEntry.place(x=centerX-500, y=350, anchor="center")

        self.questionThreeLb= Label (self.dataFrame, text="Ingrese su contraseña", font=(font,15))
        self.questionThreeLb.place(x=centerX-500, y=400, anchor="center")
        self.questionThreeEntry= Entry(self.dataFrame,width=25, font=(font, 15))
        self.questionThreeEntry.place(x=centerX-500, y=450, anchor="center")

        self.questionFourLb= Label (self.dataFrame, text="Confirme su contraseña", font=(font,15))
        self.questionFourLb.place(x=centerX-500, y=500, anchor="center")
        self.questionFourEntry= Entry(self.dataFrame,width=25, font=(font, 15))
        self.questionFourEntry.place(x=centerX-500, y=550, anchor="center")

        self.nextBtn = Button(self.dataFrame, text="next", font=(font, 15))
        self.nextBtn.place(x=2*centerX-100, y=650, anchor="nw")
        #_____________________________________________________________________________________#

        #_______________________________Change favorite color_________________________________#
        self.colorVar = StringVar()
        self.colorVar.set("default")

        Radiobutton(self.dataFrame, text="Rojo     ", variable=self.colorVar, font=(font,15), width=8, value="red", command=self.showColor).place(x=centerX-225, y=250, anchor="center")
        Radiobutton(self.dataFrame, text="Verde   ", variable=self.colorVar, font=(font,15), width=8, value="green", command=self.showColor).place(x=centerX-225, y=300, anchor="center")
        Radiobutton(self.dataFrame, text="Azul     ", variable=self.colorVar, font=(font,15), width=8,value="blue", command=self.showColor).place(x=centerX-225, y=350, anchor="center")
        Radiobutton(self.dataFrame, text="Amarillo", variable=self.colorVar, font=(font,15), width=8, value="yellow", command=self.showColor).place(x=centerX-225, y=400, anchor="center")
        Radiobutton(self.dataFrame, text="Naranja", variable=self.colorVar, font=(font,15), width=8, value="orange", command=self.showColor).place(x=centerX-225, y=450, anchor="center")
        Radiobutton(self.dataFrame, text="Morado", variable=self.colorVar, font=(font,15), width=8, value="violet", command=self.showColor).place(x=centerX-225, y=500, anchor="center")

        self.colorLabel = Label(self.dataFrame, text="Seleccione su color favorito", font=(font, 15))
        self.colorLabel.place(x=centerX-225, y=200, anchor="center")
        #____________________________________________________________________________________#



        #__________________________Change Favorite Song______________________________________#
        self.chosenSong = tkinter.StringVar()

        self.songLabel = Label(self.dataFrame, text="Cambiar canción favorita", font=(font, 15))
        self.songLabel.place(x=centerX-375, y=620, anchor="center")

        self.songOptions = ttk.Combobox(self.dataFrame, textvariable=self.chosenSong, height= 40, width=40, values=[])
        self.songOptions.place(x=centerX-375, y=720, anchor="center")

        self.nameSongEntry= Entry(self.dataFrame,width=18, font=(font, 15))
        self.nameSongEntry.place(x=centerX-405, y=670, anchor="center")

        self.searchBtn = Button(self.dataFrame, text="Search", font=(font, 10))
        self.searchBtn.place(x=centerX-297, y=656, anchor="nw") 
        
        self.saveBtn = Button(self.dataFrame, text="Esperando...", font=(font, 10))
        self.saveBtn.place(x=centerX-415, y=740, anchor="nw")
        self.saveBtn.config(state="disabled")
        #____________________________________________________________________________________#

        #____________________________Change Image Information________________________________#  
        self.photoCanvas = Canvas(self.dataFrame, width=400, height=400)
        self.photoCanvas.place(x=centerX, y=185, anchor="nw")
        
        self.imagen = PhotoImage(file=os.path.abspath("perfiles/perfil.png")) 
      
        self.photoCanvas.create_image(0, 0, anchor="nw", image=self.imagen)

        self.choosePhotoBtn = Button(self.dataFrame, text="Foto de perfil", width= 15,font=(font, 15))
        self.choosePhotoBtn.place(x=centerX+450, y=185, anchor="nw")


        self.profileBtn = Button(self.dataFrame, text="Tómate una foto", width= 15,font=(font, 15))
        self.profileBtn.place(x=centerX+450, y=285, anchor="nw")
        
        self.biometricalBtn = Button(self.dataFrame, text="Datos biómetricos", width= 15,font=(font, 15))
        self.biometricalBtn.place(x=centerX+450, y=385, anchor="nw")
        #____________________________________________________________________________________#
      
    def showColor(self):
        pass

if __name__ == '__main__':
    root = Tk()
    # take the dimensions of the computer screen
    widthScreen = root.winfo_screenwidth()
    heightScreen = root.winfo_screenheight()

    # set game screen size
    root.geometry(f"{widthScreen}x{heightScreen}")
    root.resizable(False, False)

    root.title("Eagle Defender")

    app =modificateDataGui(root, widthScreen, heightScreen,["Usuario 1", "Usuario 2"])

    root.mainloop()
