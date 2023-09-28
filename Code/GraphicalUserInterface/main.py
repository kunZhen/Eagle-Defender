from tkinter import *
from InitialGui import InitialGui

if __name__ == '__main__':
    root = Tk()
    # take the dimensions of the computer screen
    widthScreen = root.winfo_screenwidth()
    heightScreen = root.winfo_screenheight()

    # set game screen size
    root.geometry(f"{widthScreen}x{heightScreen}")
    root.resizable(False, False)

    root.title("Eagle Defender")

    app = InitialGui(root, widthScreen, heightScreen)

    root.mainloop()
