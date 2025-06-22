import os
from tkinter import *
from PIL import Image, ImageTk
from splash_animation import Animation
from interactive_page import InteractivePage

class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        # Window properties
        self.title("Move Out")
        self.geometry("390x844")
        self.resizable(False, False)

        # Logo image for window icon
        logo = Image.open(r"../media/logo.png")
        logo = logo.resize((50, 100))
        logo_img = ImageTk.PhotoImage(logo)
        self.iconphoto(True, logo_img)

        # Adding animation with callback to transition
        self.logo_animation = Animation(self, callback=self.transition_to_interactive_page)
        self.logo_animation.pack(fill=BOTH, expand=True)

    def transition_to_interactive_page(self):
        # Destroy the splash screen (removes the logo animation)
        self.logo_animation.destroy()

        # Create and show the InteractivePage
        self.interactive_page = InteractivePage(self)
        self.interactive_page.pack(fill=BOTH, expand=True)

# Run the application
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
