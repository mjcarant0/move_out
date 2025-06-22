from tkinter import *

class InteractivePage(Frame):
    '''
        This module provides the interactive page for Move Out.
        It allows the user to navigate to the login and signup pages.
    '''
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.configure(bg="#ffc4d6")
