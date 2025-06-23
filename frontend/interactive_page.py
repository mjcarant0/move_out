from tkinter import *
import tkinter.font as tkFont

class InteractivePage(Frame):
    '''
        This module provides the interactive page for Move Out.
        It allows the user to navigate to the login and signup pages.
    '''
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.configure(bg="#ffc4d6")

        title_font = tkFont.Font(family="Poppins", weight="bold", size=24)
        self.title_label = Label(self, text="MOVE OUT", font=title_font, fg="white", bg="#ffc4d6")
        self.title_label.place(x=109, y=398)