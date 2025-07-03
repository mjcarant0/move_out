'''
Sign Up Page UI for the MOVE OUT application using Tkinter.

This module defines the SignUpPage class, which provides a styled user interface
for account registration, including fields for first name, last name, mobile number,
PIN entry, and navigation back to login.
'''

from tkinter import *
from tkinter.font import Font
from tkinter import ttk

from backend.signup import SignupHandler

class SignUpPage(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ffc4d6")
        self.parent = parent
        self.signup_handler = SignupHandler() # Access backend logic for creating new user accounts

        self.title_font = Font(family="Poppins", size=20, weight="bold")
        self.create_font = Font(family="League spartan", size=10, weight="bold")
        self.signup_font = Font(family="Poppins", size=45, weight="bold")
        self.phone_font = Font(family="Montserrat", size=9)
        self.button_font = Font(family="League Spartan", size=10, weight="bold")

        # MOVE OUT Title
        Label(self, text="MOVE OUT", font=self.title_font, bg="#ffc4d6", fg="white").pack(pady=(100, 0))

        # White box container
        white_box = Frame(self, bg="white", width=300, height=520)
        white_box.pack(pady=(80, 0))
        white_box.pack_propagate(False)

        # Create your Account + Sign Up
        Label(white_box, text="Create Your Account", font=self.create_font, fg="#ff99b8", bg="white").pack(pady=(30, 0))
        Label(white_box, text="SIGN UP", font=self.signup_font, fg="#ff99b8", bg="white").pack(pady=(0, 5))

       # FIRST NAME Entry
        first_border = Frame(white_box, bg="#BDBDBD")
        first_border.pack(pady=(0, 10), padx=10, fill=X)

        first_inner = Frame(first_border, bg="white")
        first_inner.pack(fill=BOTH, padx=1, pady=1)

        self.first_name_entry = Entry(first_inner, font=self.phone_font, bd=0, fg="gray", bg="white")
        self.first_name_entry.insert(0, "First Name")
        self.first_name_entry.pack(fill=X, ipady=5)
        self.first_name_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.first_name_entry, "First Name"))
        self.first_name_entry.bind("<FocusOut>", lambda e: self.restore_placeholder(self.first_name_entry, "First Name"))

        # LAST NAME Entry
        last_border = Frame(white_box, bg="#BDBDBD")
        last_border.pack(pady=(0, 10), padx=10, fill=X)

        last_inner = Frame(last_border, bg="white")
        last_inner.pack(fill=BOTH, padx=1, pady=1)

        self.last_name_entry = Entry(last_inner, font=self.phone_font, bd=0, fg="gray", bg="white")
        self.last_name_entry.insert(0, "Last Name")
        self.last_name_entry.pack(fill=X, ipady=5)
        self.last_name_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.last_name_entry, "Last Name"))
        self.last_name_entry.bind("<FocusOut>", lambda e: self.restore_placeholder(self.last_name_entry, "Last Name"))

       # Phone input field (matching login page layout)
        phone_frame = Frame(white_box, bg="white")
        phone_frame.pack(pady=(0, 10), padx=10, fill=X)

        # Country selector with same border and size as login
        self.selected_country = StringVar()
        country_border = Frame(phone_frame, bg="#BDBDBD")
        country_border.pack(side=LEFT, padx=(0, 1))

        country_frame = Frame(country_border, bg="white", width=40, height=26)
        country_frame.pack(padx=1, pady=1)
        country_frame.pack_propagate(False)

        self.country_code_label = Label(
            country_frame,
            text="🇵🇭 +63",
            font=self.phone_font,
            bg="white",
            fg="black"
        )
        self.country_code_label.pack(expand=True)

        # Phone number input styled like login
        phone_border = Frame(phone_frame, bg="#BDBDBD")
        phone_border.pack(side=LEFT, fill=X, expand=True, padx=(8, 0))
        phone_inner = Frame(phone_border, bg="white")
        phone_inner.pack(fill=BOTH, padx=1, pady=1)

        self.phone_entry = Entry(phone_inner, font=self.phone_font, bd=0, width=18, fg="gray", bg="white")
        self.phone_entry.insert(0, "Mobile Phone")
        self.phone_entry.pack(fill=X, ipady=5)
        self.phone_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.phone_entry, "Mobile Phone"))
        self.phone_entry.bind("<FocusOut>", lambda e: self.restore_placeholder(self.phone_entry, "Mobile Phone"))

        # PIN input
        pin_border = Frame(white_box, bg="#BDBDBD")
        pin_border.pack(pady=(0, 10), padx=10, fill=X)
        pin_inner = Frame(pin_border, bg="white")
        pin_inner.pack(fill=BOTH, padx=1, pady=1)

        self.pin_entry = Entry(pin_inner, font=self.phone_font, bd=0, fg="gray", bg="white", show="*")
        self.pin_entry.insert(0, "PIN (4 digits only)")
        self.pin_entry.config(show="")
        self.pin_entry.pack(fill=X, ipady=5)
        self.pin_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.pin_entry, "PIN (4 digits only)"))
        self.pin_entry.bind("<FocusOut>", lambda e: self.restore_placeholder(self.pin_entry, "PIN (4 digits only)"))
        
        # Confirm PIN input
        cpin_border = Frame(white_box, bg="#BDBDBD")
        cpin_border.pack(pady=(0, 10), padx=10, fill=X)
        cpin_inner = Frame(cpin_border, bg="white")
        cpin_inner.pack(fill=BOTH, padx=1, pady=1)
        
        self.cpin_entry = Entry(cpin_inner, font=self.phone_font, bd=0, fg="gray", bg="white", show="*")
        self.cpin_entry.insert(0, "Confirm PIN (4 digits only)")
        self.cpin_entry.config(show="")
        self.cpin_entry.pack(fill=X, ipady=5)
        self.cpin_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.cpin_entry, "Confirm PIN (4 digits only)"))
        self.cpin_entry.bind("<FocusOut>", lambda e: self.restore_placeholder(self.cpin_entry, "Confirm PIN (4 digits only)"))

        # Store placeholders for error resets
        self.placeholders = {
            self.first_name_entry: "First Name",
            self.last_name_entry: "Last Name",
            self.phone_entry: "Mobile Phone",
            self.pin_entry: "PIN (4 digits only)",
            self.cpin_entry: "Confirm PIN (4 digits only)",
        }

        # Sign up button
        Button(white_box, text="SIGN UP", font=self.button_font, bg="#f38c9f", fg="white",
               activebackground="#ffc4d6", bd=0, cursor="hand2", command=self.on_signup_clicked).place(x=70, y=380, width=160, height=25)

        # Line separator 
        line = Frame(white_box, bg="#ffc4d6", height=1, width=270)
        line.pack(pady=(60, 10))  # Increased top margin

        # Already have an account 
        Label(white_box, text="Already have an Account?", font=self.create_font, fg="#ff99b8", bg="white").pack(pady=(5, 20))

        # Log in button
        self.login_button = self.create_login_button()
        self.login_button.place(relx=0.5, y=705, anchor="n")

    def create_login_button(self):
        canvas = Canvas(
            self,
            width=156,
            height=26,
            bg="white",
            highlightthickness=0,
            cursor="hand2"
        )
        canvas.create_rectangle(0, 0, 156, 26, outline="#f38c9f", width=2)
        canvas.create_text(78, 13, text="LOGIN", fill="#f38c9f", font=("League Spartan", 10, "bold"))
        canvas.bind("<Button-1>", lambda e: self.on_login_clicked())
        return canvas

    def clear_placeholder(self, entry_widget, placeholder_text):
        # Also clears inline error text (which is flagged by entry_widget.is_error)
        if entry_widget.get() == placeholder_text or getattr(entry_widget, "is_error", False):
            entry_widget.delete(0, END)
            entry_widget.config(fg="black", highlightthickness=0)

            # Re‑mask PIN fields once the user starts typing again
            if "PIN" in placeholder_text:
                entry_widget.config(show="*")
            else:
                entry_widget.config(show="")

            entry_widget.is_error = False

    def restore_placeholder(self, entry_widget, placeholder_text):
        if not entry_widget.get():
            entry_widget.insert(0, placeholder_text)
            entry_widget.config(fg="gray")

            # Un‑mask so the placeholder is readable
            entry_widget.config(show="")

    def clear_error_styles(self):
        for entry in [
            self.first_name_entry,
            self.last_name_entry,
            self.phone_entry,
            self.pin_entry,
            self.cpin_entry,
        ]:
            entry.config(highlightthickness=0)
            if getattr(entry, "is_error", False):
                entry.delete(0, END)
                self.restore_placeholder(entry, self.placeholders[entry])
                entry.is_error = False

    def set_error_style(self, entry_widget, message):
        entry_widget.config(highlightthickness=1, highlightbackground="red", highlightcolor="red")
        entry_widget.delete(0, END)
        entry_widget.insert(0, message)
        entry_widget.config(fg="red", show="")
        entry_widget.is_error = True  # Flag to clear it later

    def on_signup_clicked(self):  
        '''
            Runs when the SIGN UP button is clicked.
            Collects input, sends it to the backend,
            shows error messages if something is wrong,
            or goes to login if sign up is successful.
        '''
        
        self.clear_error_styles() # Reset previous messages

        first_name  = self.first_name_entry.get().strip()
        last_name   = self.last_name_entry.get().strip()
        raw_country = self.country_code_label.cget("text")
        country_code = raw_country.split()[-1]
        phone_number = self.phone_entry.get().strip()
        pin          = self.pin_entry.get().strip()
        confirm_pin  = self.cpin_entry.get().strip()

        if first_name == "First Name":
            first_name = ""
        if last_name == "Last Name":
            last_name = ""
        if phone_number == "Mobile Phone":
            phone_number = ""
        if pin == "PIN (4 digits only)":
            pin = ""
        if confirm_pin == "Confirm PIN (4 digits only)":
            confirm_pin = ""

        result = self.signup_handler.create_user(
            first_name, last_name, country_code,
            phone_number, pin, confirm_pin
        )

        if result["success"]:
            # When Signup button is clicked, navigate to the Login page
            if hasattr(self.parent, "show_login_page"):
                self.parent.show_login_page()

        else:
            # Show error message to user
            message = result["message"]
            
            if "already registered" in message:
                self.set_error_style(self.phone_entry, "Phone number already exists.")
            elif "do not match" in message:
                self.set_error_style(self.cpin_entry, "PIN and Confirm PIN do not match.")
            elif "Confirm PIN must be exactly 4 digits" in message:
                self.set_error_style(self.cpin_entry, "Confirm PIN must be 4 digits.")
            elif "PIN must be exactly 4 digits" in message:
                self.set_error_style(self.pin_entry, "PIN must be 4 digits.")
            elif "Invalid phone number" in message or "Invalid phone number format" in message:
                self.set_error_style(self.phone_entry, "Phone number must be 10 digits.")
            elif "Please select a valid country code" in message:
                self.set_error_style(self.phone_entry, "Invalid country code.")
            elif "Invalid first name" in message:
                self.set_error_style(self.first_name_entry, "First name is invalid.")
            elif "Invalid last name" in message:
                self.set_error_style(self.last_name_entry, "Last name is invalid.")

    def on_login_clicked(self):  # When Login button is clicked, navigate to the Login page
        if hasattr(self.parent, "show_login_page"):
            self.parent.show_login_page()