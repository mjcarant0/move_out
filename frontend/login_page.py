from tkinter import *
from tkinter.font import Font
from tkinter import ttk

class LoginPage(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ffc4d6")
        self.parent = parent

        self.title_font = Font(family="Poppins", size=20, weight="bold")
        self.welcome_font = Font(family="League spartan", size=12, weight="bold")
        self.login_font = Font(family="Poppins", size=45, weight="bold")
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
        Label(self, text="MOVE OUT", font=self.title_font, bg="#ffc4d6", fg="white").pack(pady=(150, 40))

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

        # Phone Entry
        Entry(phone_frame, font=self.phone_font, bd=1, relief=SOLID, width=18).pack(
            side=LEFT, fill=X, expand=True, padx=(8, 0), ipady=4
        )

        # Login button
        self.create_login_button(white_box).pack(pady=(20, 20))

        # Line separator
        line = Frame(white_box, bg="#ffc4d6", height=1, width=270)
        line.pack(pady=(10, 10))

        # Don't have an account
        Label(white_box, text="Don't have an account yet?", font=self.welcome_font, fg="#ff99b8", bg="white").pack(pady=(10, 0))

        # Sign up button
        self.create_signup_button(white_box).pack(pady=(10, 20))

    def create_login_button(self, parent):
        canvas = Canvas(parent, width=156, height=26, bg="#ffc4d6", highlightthickness=0, cursor="hand2")
        canvas.create_rectangle(0, 0, 156, 26, fill="#f38c9f", outline="#f38c9f", width=2)
        canvas.create_text(78, 13, text="LOG IN", fill="white", font=("League Spartan", 10, "bold"))
        
        canvas.bind("<Button-1>", self.on_login_clicked)
        return canvas

    def on_login_clicked(self, event): # When login button is clicked, navigate to the home page
        if hasattr(self.parent, "show_home_page"):
            self.parent.show_home_page()

    def create_signup_button(self, parent):
        canvas = Canvas(parent, width=156, height=26, bg="#ffc4d6", highlightthickness=0, cursor="hand2")
        canvas.create_rectangle(0, 0, 156, 26, fill="white", outline="#f38c9f", width=2)
        canvas.create_text(78, 13, text="SIGN UP", fill="#f38c9f", font=("League Spartan", 10, "bold"))
        
        canvas.bind("<Button-1>", self.on_signup_clicked)
        return canvas

    def on_signup_clicked(self, event): # When login button is clicked, navigate to the signup page
        if hasattr(self.parent, "show_signup_page"):
            self.parent.show_signup_page()