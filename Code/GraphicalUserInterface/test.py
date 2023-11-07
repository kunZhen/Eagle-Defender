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
from PIL import Image, ImageTk, ImageDraw

# Create a tkinter window
root = tk.Tk()
root.title("Image Inside Circle")

# Create a canvas widget
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Load an image using PIL (Pillow)
image = Image.open("Code/GraphicalUserInterface/sprites/Eagle.png")  # Replace with your image file
image.thumbnail((200, 200))  # Resize the image to fit inside the circle

# Create a circular mask
mask = Image.new("L", (200, 200), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, 200, 200), fill=255)

# Apply the circular mask to the image
image.putalpha(mask)

# Convert the image to a PhotoImage object for tkinter
image_tk = ImageTk.PhotoImage(image)

# Create a circular region on the canvas
canvas.create_oval(50, 50, 250, 250, fill="white")

# Display the cropped image inside the circular region on the canvas
canvas.create_image(150, 150, image=image_tk)

# Start the tkinter main loop
root.mainloop()