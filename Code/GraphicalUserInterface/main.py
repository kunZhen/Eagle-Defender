from tkinter import *


from mailGui import mailGui
from InitialGui import InitialGui

if __name__ == '__main__':
    root = Tk()
    # take the dimensions of the computer screen
    widthScreen = root.winfo_screenwidth() - 25
    heightScreen = root.winfo_screenheight() - 25

    # set game screen size
    root.geometry(f"{widthScreen}x{heightScreen}")
    root.resizable(False, False)

    root.title("Eagle Defender")

    #app = InitialGui(root, widthScreen, heightScreen    root.mainloop()
 
    root.mainloop()
    
