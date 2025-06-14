import os
from tkinter import *
from PIL import Image, ImageTk

# Make the script's folder the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create the main window
window = Tk()
window.geometry("390x844")
window.title("Move Out")  # Service Name

# Logo image
logo = Image.open(r"../media/logo.png")
logo = logo.resize((50, 100)) 
logo_img = ImageTk.PhotoImage(logo)

window.iconphoto(True, logo_img)

window.mainloop()