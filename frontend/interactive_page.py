from tkinter import *

class InteractivePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.configure(bg="#ffc4d6")
