from musicLogic import musicLogic

"""music = musicLogic()
music.fileName = "default1.mp4"
music.downloadYoutubeAudio("https://www.youtube.com/watch?v=sBRgqBgFXNw&list=PLq_Mq0PPDkP2bgzeZkrLx9KG9wJYzH8no&index=1")
music.setUpVideoMusic(f"Code/GraphicalUserInterface/songs/{music.fileName}")

music.fileName = "default2.mp4"
music.downloadYoutubeAudio("https://www.youtube.com/watch?v=IDNOPGLceno&list=PLq_Mq0PPDkP2bgzeZkrLx9KG9wJYzH8no&index=2")
music.setUpVideoMusic(f"Code/GraphicalUserInterface/songs/{music.fileName}")

music.fileName = "default3.mp4"
music.downloadYoutubeAudio("https://www.youtube.com/watch?v=W_ktv-wDI9I&list=PLq_Mq0PPDkP2bgzeZkrLx9KG9wJYzH8no&index=3")
music.setUpVideoMusic(f"Code/GraphicalUserInterface/songs/{music.fileName}")"""

import tkinter as tk

def key_pressed(event):
    key = event.keysym
    print(f"Key pressed: {key}")

root = tk.Tk()
root.title("Key Event Example")

root.bind("<Key>", key_pressed)

root.mainloop()