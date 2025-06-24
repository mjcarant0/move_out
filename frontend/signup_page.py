from tkinter import *
from tkinter.font import Font
from tkinter import ttk

class SignUpPage(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ffc4d6")
        self.parent = parent

        self.title_font = Font(family="Poppins", size=20, weight="bold")
        self.create_font = Font(family="League spartan", size=10, weight="bold")
        self.signup_font = Font(family="Poppins", size=45, weight="bold")
        self.phone_font = Font(family="Montserrat", size=9)

        # Country code list
        self.country_list = [
        ("🇧🇳", "+673", "Brunei"),
        ("🇰🇭", "+855", "Cambodia"),
        ("🇮🇩", "+62", "Indonesia"),
        ("🇱🇦", "+856", "Laos"),
        ("🇲🇾", "+60", "Malaysia"),
        ("🇲🇲", "+95", "Myanmar"),
        ("🇵🇭", "+63", "Philippines"),
        ("🇸🇬", "+65", "Singapore"),
        ("🇹🇭", "+66", "Thailand"),
        ("🇹🇱", "+670", "Timor-Leste"),
        ("🇻🇳", "+84", "Vietnam")
        ]

        # MOVE OUT Title
        Label(self, text="MOVE OUT", font=self.title_font, bg="#ffc4d6", fg="white").pack(pady=(100, 0))

        # White box container
        white_box = Frame(self, bg="white", width=300, height=420)
        white_box.pack(pady=(100, 0))
        white_box.pack_propagate(False)

        # Create your Account + Sign Up
        Label(white_box, text="Create Your Account", font=self.create_font, fg="#ff99b8", bg="white").pack(pady=(30, 0))
        Label(white_box, text="SIGN UP", font=self.signup_font, fg="#ff99b8", bg="white").pack(pady=(0, 10))

        # FIRST NAME Entry
        self.first_name_entry = Entry(white_box, font=self.phone_font, bd=1, relief=SOLID, fg="gray", width=35)
        self.first_name_entry.insert(0, "First Name")
        self.first_name_entry.pack(pady=(0, 10), padx=20, fill=X, ipady=5)
        self.first_name_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.first_name_entry, "First Name"))
        self.first_name_entry.bind("<FocusOut>", lambda e: self.restore_placeholder(self.first_name_entry, "First Name"))

        # LAST NAME Entry
        self.last_name_entry = Entry(white_box, font=self.phone_font, bd=1, relief=SOLID, fg="gray", width=35)
        self.last_name_entry.insert(0, "Last Name")
        self.last_name_entry.pack(pady=(0, 10), padx=20, fill=X, ipady=5)
        self.last_name_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.last_name_entry, "Last Name"))
        self.last_name_entry.bind("<FocusOut>", lambda e: self.restore_placeholder(self.last_name_entry, "Last Name"))

        # Phone input field
        phone_frame = Frame(white_box, bg="white")
        phone_frame.pack(pady=(10, 10), padx=15, fill=X)

        # Country selector using Combobox
        self.selected_country = StringVar()
        self.country_combo = ttk.Combobox(
            phone_frame,
            textvariable=self.selected_country,
            font=self.phone_font,
            state="readonly",
            width=6,
            values=[f"{flag} {code}" for flag, code, _ in self.country_list]
        )
        self.selected_country.set("🇵🇭 +63")
        self.country_combo.pack(side=LEFT)

        # PHONE NUMBER Entry
        self.phone_entry = Entry(phone_frame, font=self.phone_font, bd=1, relief=SOLID, width=18, fg="gray")
        self.phone_entry.insert(0, "Mobile Phone")
        self.phone_entry.pack(side=LEFT, fill=X, expand=True, padx=(8, 0), ipady=5)
        self.phone_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.phone_entry, "Mobile Phone"))
        self.phone_entry.bind("<FocusOut>", lambda e: self.restore_placeholder(self.phone_entry, "Mobile Phone"))

        # Sign up button
        self.create_signup_button(white_box).pack(pady=(10, 10))

        # Line separator
        line = Frame(white_box, bg="#ffc4d6", height=1, width=270)
        line.pack(pady=(10, 10))

        # Already have an account
        Label(white_box, text="Already have an Account?", font=self.create_font, fg="#ff99b8", bg="white").pack(pady=(0, 0))

        # Log in button
        self.create_login_button(white_box).pack(pady=(5, 20))

    def clear_placeholder(self, entry_widget, placeholder_text):
        if entry_widget.get() == placeholder_text:
            entry_widget.delete(0, END)
            entry_widget.config(fg="black")

    def restore_placeholder(self, entry_widget, placeholder_text):
        if not entry_widget.get():
            entry_widget.insert(0, placeholder_text)
            entry_widget.config(fg="gray")

    def create_signup_button(self, parent):
        canvas = Canvas(parent, width=156, height=26, bg="#ffc4d6", highlightthickness=0, cursor="hand2")
        canvas.create_rectangle(0, 0, 156, 26, fill="#f38c9f", outline="#f38c9f", width=2)
        canvas.create_text(78, 13, text="SIGN UP", fill="white", font=("League Spartan", 10, "bold"))
        canvas.bind("<Button-1>", self.on_signup_clicked)
        return canvas

    def on_signup_clicked(self, event):  # When login button is clicked, navigate to the home page
        if hasattr(self.parent, "show_home_page"):
            self.parent.show_home_page()

    def create_login_button(self, parent):
        canvas = Canvas(parent, width=156, height=26, bg="#ffc4d6", highlightthickness=0, cursor="hand2")
        canvas.create_rectangle(0, 0, 156, 26, fill="white", outline="#f38c9f", width=2)
        canvas.create_text(78, 13, text="LOG IN", fill="#f38c9f", font=("League Spartan", 10, "bold"))
        canvas.bind("<Button-1>", self.on_login_clicked)
        return canvas

    def on_login_clicked(self, event): # When Login button is clicked, navigate to the Login page
        if hasattr(self.parent, "show_login_page"):
            self.parent.show_login_page()