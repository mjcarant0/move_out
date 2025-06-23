from tkinter import *
from tkinter.font import Font

class LoginPage(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ffc4d6")  # Pink background
        self.parent = parent
        
        # Custom fonts
        title_font = Font(family="Courier", size=24, weight="bold")
        subtitle_font = Font(family="Courier", size=14)
        button_font = Font(family="Courier", size=12, weight="bold")
        
        # Layout configuration
        self.pack_propagate(False)  # Keep fixed size
        self.pack(expand=True, fill=BOTH)
        
        # MOVE OUT (top center)
        Label(self, 
             text="MOVE OUT",
             font=title_font,
             bg="#ffc4d6",
             fg="black").pack(pady=(40,10))
        
        # Welcome Back! (centered)
        Label(self,
             text="Welcome Back!",
             font=subtitle_font,
             bg="#ffc4d6",
             fg="black").pack(pady=10)
        
        # First LOG IN (centered)
        Label(self,
             text="LOG IN",
             font=title_font,
             bg="#ffc4d6",
             fg="black").pack(pady=10)
        
        # Sign Up button (centered)
        Button(self,
              text="Log in",
              font=button_font,
              bg="#ff99b8",  # Darker pink
              fg="black",
              relief=RAISED,
              borderwidth=3,
              padx=30,
              pady=5).pack(pady=10)