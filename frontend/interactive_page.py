from tkinter import *
import tkinter.font as tkFont

class InteractivePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="#ffc4d6")

        # Title
        title_font = tkFont.Font(family="Poppins", weight="bold", size=24)
        self.title_label = Label(
            self,
            text="MOVE OUT",
            font=title_font,
            fg="white",
            bg="#ffc4d6"
        )
        self.title_label.place(x=109, y=398)

        # LOG IN Button
        self.login_button = self.create_login_button()
        self.login_button.place(x=115, y=705)

        # SIGN UP Button
        self.signup_button = self.create_signup_button()
        self.signup_button.place(x=115, y=735)

    def login_clicked(self, event):
        pass  # Navigation logic later

    def signup_clicked(self, event):
        pass  # Navigation logic later

    def create_login_button(self):
        canvas = Canvas(
            self,
            width=156,
            height=26,
            bg="#ffc4d6",
            highlightthickness=0,
            cursor="hand2"
        )
        canvas.create_rectangle(0, 0, 156, 26, fill="#f38c9f", outline="#f38c9f", width=1)
        canvas.create_text(78, 13, text="LOG IN", fill="white", font=("League Spartan", 10, "bold"))
        canvas.bind("<Button-1>", self.login_clicked)
        return canvas

    def create_signup_button(self):
        canvas = Canvas(
            self,
            width=156,
            height=26,
            bg="#ffc4d6",
            highlightthickness=0,
            cursor="hand2"
        )
        canvas.create_rectangle(0, 0, 156, 26, outline="#f38c9f", width=1.5)
        canvas.create_text(78, 13, text="SIGN UP", fill="#f38c9f", font=("League Spartan", 10, "bold"))
        canvas.bind("<Button-1>", self.signup_clicked)
        return canvas
