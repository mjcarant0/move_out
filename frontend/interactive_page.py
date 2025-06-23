from tkinter import *
from tkinter import ttk
from signup_page import SignUpWindow
from login_page import LoginPage

class InteractivePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="#ffc4d6")

        # Main container that centers everything
        center_frame = Frame(self, bg="#ffc4d6")
        center_frame.place(relx=0.5, rely=0.5, anchor=CENTER) 

        # MOVE OUT title 
        title_label = Label(center_frame,
                          text="MOVE OUT",
                          bg="#ffc4d6",
                          fg="white",
                          font=('Helvetica', 24, 'bold'))
        title_label.pack(pady=(100, 100))

        # Sign Up Button (smaller with white text)
        self.signup_btn = Button(center_frame,
                              text="Sign Up",
                              command=self.show_signup,
                              bg="#ff99b8",
                              fg="white",
                              font=('Helvetica', 12, 'bold'),
                              relief=RAISED,
                              borderwidth=2,
                              padx=15,
                              pady=5)
        self.signup_btn.pack(pady=10, fill=X)

        # Log In Button (smaller with white text)
        self.login_btn = Button(center_frame,
                             text="Log In",
                             command=self.show_login,
                             bg="#ff99b8",
                             fg="white",
                             font=('Helvetica', 12, 'bold'),
                             relief=RAISED,
                             borderwidth=2,
                             padx=15,
                             pady=5)
        self.login_btn.pack(pady=10, fill=X)
        
    def show_signup(self):
        SignUpWindow(self.parent)  # Open the signup window

    def show_login(self):
        self.login_page = LoginPage(self)
        self.login_page.pack(fill="both", expand=True)