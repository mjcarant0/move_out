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

        # Title
        title_font = tkFont.Font(family="Poppins", weight="bold", size=24)
        self.title_label = Label(
            self,
            text="MOVE OUT",
            font=title_font,
            fg="white",
            bg="#ffc4d6"
        )
        self.title_label.place(relx=0.5, y=398, anchor="n")  # center X only

        # LOG IN Button
        self.login_button = self.create_login_button()
        self.login_button.place(relx=0.5, y=705, anchor="n")  # center X only

        # SIGN UP Button
        self.signup_button = self.create_signup_button()
        self.signup_button.place(relx=0.5, y=735, anchor="n")  # center X only

    def login_clicked(self, event):
        # Show the login page
        self.parent.show_login_page()

    def signup_clicked(self, event):
        # Show the signup page
        self.parent.show_signup_page()

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
