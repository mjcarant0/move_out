from tkinter import *
from tkinter.font import Font
from tkinter import ttk

class LoginPage(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ffc4d6")
        self.parent = parent

        self.title_font = Font(family="Poppins", size=20, weight="bold")
        self.welcome_font = Font(family="League spartan", size=10, weight="bold")
        self.login_font = Font(family="Poppins", size=45, weight="bold")
        self.phone_font = Font(family="Montserrat", size=9)
        self.button_font = Font(family="League Spartan", size=10, weight="bold")

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

        # Welcome Back + LOG IN
        Label(white_box, text="Welcome Back!", font=self.welcome_font, fg="#ff99b8", bg="white").pack(pady=(30, 0))
        Label(white_box, text="LOG IN", font=self.login_font, fg="#ff99b8", bg="white").pack(pady=(0, 25))

        # Phone input field
        phone_frame = Frame(white_box, bg="white")
        phone_frame.pack(pady=(30, 10), padx=15, fill=X)

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
        self.selected_country.set("🇵🇭 +63")  # Default value
        self.country_combo.pack(side=LEFT)

        # PHONE NUMBER Entry
        self.phone_entry = Entry(phone_frame, font=self.phone_font, bd=1, relief=SOLID, width=18, fg="gray")
        self.phone_entry.insert(0, "Mobile Phone")
        self.phone_entry.pack(side=LEFT, fill=X, expand=True, padx=(8, 0), ipady=5)
        self.phone_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.phone_entry, "Mobile Phone"))
        self.phone_entry.bind("<FocusOut>", lambda e: self.restore_placeholder(self.phone_entry, "Mobile Phone"))

        # Login button
        Button(white_box, text="LOGIN", font=self.button_font, bg="#f38c9f", fg="white",
            activebackground="#ffc4d6", bd=0, cursor="hand2", command=self.on_login_clicked).place(x=70, y=240, width=160, height=25)

        # Line separator
        line = Frame(white_box, bg="#ffc4d6", height=1, width=270)
        line.pack(pady=(70, 10))

        # Don't have an account
        Label(white_box, text="Don't have an account yet?", font=self.welcome_font, fg="#ff99b8", bg="white").pack(pady=(0, 0))

        # Sign up button
        Button(white_box, text="SIGN UP", font=self.button_font, bg="#f38c9f", fg="white",
            activebackground="#ffc4d6", bd=0, cursor="hand2", command=self.on_signup_clicked).place(x=70, y=360, width=160, height=25)

    def clear_placeholder(self, entry_widget, placeholder_text):
        if entry_widget.get() == placeholder_text:
            entry_widget.delete(0, END)
            entry_widget.config(fg="black")

    def restore_placeholder(self, entry_widget, placeholder_text):
        if not entry_widget.get():
            entry_widget.insert(0, placeholder_text)
            entry_widget.config(fg="gray")

    def on_login_clicked(self): # When login button is clicked, navigate to the home page
        if hasattr(self.parent, "show_home_page"):
            self.parent.show_home_page()

    def on_signup_clicked(self): # When Signup button is clicked, navigate to the signup page
        if hasattr(self.parent, "show_signup_page"):
            self.parent.show_signup_page()