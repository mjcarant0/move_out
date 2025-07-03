'''
Login Page UI for the MOVE OUT application using Tkinter.

This module defines the LoginPage class, which provides the graphical interface for user login, 
including mobile number, PIN entry, and navigation to signup.
'''

from tkinter import *
from tkinter.font import Font
from tkinter import ttk

from backend.login import LoginHandler

class LoginPage(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ffc4d6")
        self.parent = parent
        self.login_handler = LoginHandler() # Access backend logic for user accounts

        self.title_font = Font(family="Poppins", size=20, weight="bold")
        self.welcome_font = Font(family="League spartan", size=10, weight="bold")
        self.login_font = Font(family="Poppins", size=45, weight="bold")
        self.phone_font = Font(family="Montserrat", size=9)
        self.button_font = Font(family="League Spartan", size=10, weight="bold")

        # MOVE OUT Title
        Label(self, text="MOVE OUT", font=self.title_font, bg="#ffc4d6", fg="white").pack(pady=(100, 0))

        # White box container
        white_box = Frame(self, bg="white", width=300, height=420)
        white_box.pack(pady=(100, 0))
        white_box.pack_propagate(False)

        # Welcome Back + LOG IN
        Label(white_box, text="Welcome Back!", font=self.welcome_font, fg="#ff99b8", bg="white").pack(pady=(30, 0))
        Label(white_box, text="LOG IN", font=self.login_font, fg="#ff99b8", bg="white").pack(pady=(0, 20))

        # Phone input field
        phone_frame = Frame(white_box, bg="white")
        phone_frame.pack(pady=(0, 10), padx=10, fill=X)

        # Country selector with larger box size
        self.selected_country = StringVar()
        country_border = Frame(phone_frame, bg="#BDBDBD")
        country_border.pack(side=LEFT, padx=(0, 1))

        # Set a fixed width in pixels
        country_frame = Frame(country_border, bg="white", width=40, height=26)
        country_frame.pack(padx=1, pady=1)
        country_frame.pack_propagate(False)  # Prevent resizing to fit contents

        self.country_code_label = Label(
            country_frame,
            text="🇵🇭 +63",
            font=self.phone_font,
            bg="white",
            fg="black"
        )
        self.country_code_label.pack(expand=True)

        # PHONE NUMBER Entry
        phone_border = Frame(phone_frame, bg="#BDBDBD")
        phone_border.pack(side=LEFT, fill=X, expand=True, padx=(8, 0))
        phone_inner = Frame(phone_border, bg="white")
        phone_inner.pack(fill=BOTH, padx=1, pady=1)

        self.phone_entry = Entry(phone_inner, font=self.phone_font, bd=0, width=18, fg="gray", bg="white")
        self.phone_entry.insert(0, "Mobile Phone")
        self.phone_entry.pack(fill=X, ipady=5)
        self.phone_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.phone_entry, "Mobile Phone"))
        self.phone_entry.bind("<FocusOut>", lambda e: self.restore_placeholder(self.phone_entry, "Mobile Phone"))
        self.phone_entry.placeholder_text = "Mobile Phone"

        # PIN Entry
        pin_border = Frame(white_box, bg="#BDBDBD")
        pin_border.pack(pady=(0, 10), padx=10, fill=X)
        pin_inner = Frame(pin_border, bg="white")
        pin_inner.pack(fill=BOTH, padx=1, pady=1)

        self.pin_entry = Entry(pin_inner, font=self.phone_font, bd=0, fg="gray", bg="white", show="")
        self.pin_entry.insert(0, "PIN (4 digits only)")
        self.pin_entry.pack(fill=X, ipady=5)
        self.pin_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.pin_entry, "PIN (4 digits only)"))
        self.pin_entry.bind("<FocusOut>", lambda e: self.restore_placeholder(self.pin_entry, "PIN (4 digits only)"))
        self.pin_entry.placeholder_text = "PIN (4 digits only)"

        # Login button
        Button(white_box, text="LOGIN", font=self.button_font, bg="#f38c9f", fg="white",
            activebackground="#ffc4d6", bd=0, cursor="hand2", command=self.on_login_clicked).place(x=70, y=280, width=160, height=25)

        # Line separator
        line = Frame(white_box, bg="#ffc4d6", height=1, width=270)
        line.pack(pady=(60, 10))

        # Don't have an account
        Label(white_box, text="Don't have an account yet?", font=self.welcome_font, fg="#ff99b8", bg="white").pack(pady=(0, 0))

        # Sign up button
        self.signup_button = self.create_signup_button()
        self.signup_button.place(relx=0.5, y=620, anchor="n")

    def clear_placeholder(self, entry_widget, placeholder_text):
        if entry_widget.get() == placeholder_text or getattr(entry_widget, "is_error", False):
            entry_widget.delete(0, END)
            entry_widget.config(fg="black")
            if entry_widget == self.pin_entry:
                entry_widget.config(show="*")
            entry_widget.is_error = False

    def restore_placeholder(self, entry_widget, placeholder_text):
        if not entry_widget.get():
            entry_widget.insert(0, placeholder_text)
            entry_widget.config(fg="gray")
            if entry_widget == self.pin_entry:
                entry_widget.config(show="")


    def set_error_style(self, entry_widget, message):
        '''
        Apply red border and error text inside the entry widget.
        Used when login fails or phone/PIN is invalid.
        '''
        entry_widget.config(highlightthickness=1, highlightbackground="red", highlightcolor="red")
        entry_widget.delete(0, END)
        entry_widget.insert(0, message)
        entry_widget.config(fg="red", show="")
        entry_widget.is_error = True

    def clear_error_styles(self):
        '''
        Reset all styles of login fields (e.g., after retrying login).
        Clears red borders and restores placeholder text if needed.
        '''
        for entry in [self.phone_entry, self.pin_entry]:
            entry.config(highlightthickness=0)
            if getattr(entry, "is_error", False):
                entry.delete(0, END)
                self.restore_placeholder(entry, entry.placeholder_text)
                entry.is_error = False

    def on_login_clicked(self):
        '''
        Runs when the LOGIN button is clicked.
        Collects input, sends to backend,
        shows error message if login fails,
        or navigates to home if successful.
        '''
        self.clear_error_styles()  # Reset previous warning messages

        phone_number = self.phone_entry.get().strip()
        pin = self.pin_entry.get().strip()

        if phone_number == "Mobile Phone":
            phone_number = ""
        if pin == "PIN (4 digits only)":
            pin = ""

        result = self.login_handler.authenticate_user(phone_number, pin)

        if result["success"]:
            self.parent.current_user_phone = phone_number
            if hasattr(self.parent, "show_home_page"):
                self.parent.show_home_page()
        else:
            message = result["message"]
            if "User not found" in message:
                self.set_error_style(self.phone_entry, "You don't have an account.")
                self.set_error_style(self.pin_entry, "You don't have an account.")
            elif "Incorrect PIN" in message:
                self.set_error_style(self.phone_entry, "Invalid Number or PIN")
                self.set_error_style(self.pin_entry, "Invalid Number or PIN")
            elif "Invalid phone number" in message:
                self.set_error_style(self.phone_entry, "Phone number must be 10 digits.")
            elif "PIN must be exactly 4 digits" in message:
                self.set_error_style(self.pin_entry, "PIN must be 4 digits.")

    def create_signup_button(self):
        canvas = Canvas(
            self,
            width=156,
            height=26,
            bg="white",
            highlightthickness=0,
            cursor="hand2"
        )
        canvas.create_rectangle(0, 0, 156, 26, outline="#f38c9f", width=2)
        canvas.create_text(78, 13, text="SIGN UP", fill="#f38c9f", font=("League Spartan", 10, "bold"))
        canvas.bind("<Button-1>", lambda e: self.on_signup_clicked())
        return canvas

    def on_signup_clicked(self):  # When Signup button is clicked, navigate to the signup page
        if hasattr(self.parent, "show_signup_page"):
            self.parent.show_signup_page()
