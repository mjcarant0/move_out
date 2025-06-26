from tkinter import *
import tkinter.font as Font

class HomePage(Frame):
    '''
        This program provides the home page for Move Out.
        It allows the user to book their chosen ride.
    '''
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="white")

        self.title_font = Font.Font(family="Poppins", size=28, weight="bold")
        self.label_font = Font.Font(family="Montserrat", size=9, weight="bold")
        self.proceed_font = Font.Font(family="League Spartan", size=10, weight="bold")
        self.placeholder_font = Font.Font(family="Montserrat", size=9)
        self.price_font = Font.Font(family="Montserrat", size=9)
        self.dropdown_font = Font.Font(family="Poppins", size=20, weight="bold")

        # Pink Divider
        pink_div = Frame(self, bg="#ffc4d6", width=390, height=315)
        pink_div.pack(fill=X)
        pink_div.pack_propagate(False)

        Label(pink_div, text="SECURELY BOOK YOUR\nRIDE", font=self.title_font, bg="#ffc4d6", fg="white", justify="left").pack(anchor="w", pady=(60, 20), padx=25)
 
        # Light Pink Container
        lpink_box = Frame(self, bg="#ffe5ec", width=300, height=380)
        lpink_box.place(x=45, y=157)
        lpink_box.pack_propagate(False)

        # Navigation Bar
        nav_bar = Frame(self, bg="#ffc4d6", width=390, height=65)
        nav_bar.place(y=719)
        nav_bar.pack_propagate(False)