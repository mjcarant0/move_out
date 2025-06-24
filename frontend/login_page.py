from tkinter import *
from tkinter.font import Font

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
            ("🇵🇭", "+63", "Philippines"),
            ("🇺🇸", "+1", "United States"),
            ("🇬🇧", "+44", "United Kingdom"),
            ("🇮🇳", "+91", "India"),
            ("🇨🇦", "+1", "Canada"),
            ("🇦🇺", "+61", "Australia"),
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

        # Country selector
        self.selected_country = StringVar(value="🇵🇭 +63")
        self.country_btn = Button(phone_frame, textvariable=self.selected_country, font=self.phone_font,
                                  relief=SOLID, bd=1, bg="white", command=self.show_country_picker, padx=6)
        self.country_btn.pack(side=LEFT)

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
        canvas.create_rectangle(0, 0, 156, 26, fill="#f38c9f", outline="#f38c9f", width=1)
        canvas.create_text(78, 13, text="LOG IN", fill="white", font=("League Spartan", 10, "bold"))
        return canvas

    def create_signup_button(self, parent):
        canvas = Canvas(parent, width=156, height=26, bg="#ffc4d6", highlightthickness=0, cursor="hand2")
        canvas.create_rectangle(0, 0, 156, 26, fill="white", outline="#f38c9f", width=1)
        canvas.create_text(78, 13, text="SIGN UP", fill="#f38c9f", font=("League Spartan", 10, "bold"))
        return canvas
    
    def show_country_picker(self):
        popup = Toplevel(self)
        popup.title("Select Country Code")
        popup.geometry("250x200")
        popup.grab_set()

        listbox = Listbox(popup, font=self.phone_font)
        listbox.pack(fill=BOTH, expand=True)

        for flag, code, name in self.country_list:
            listbox.insert(END, f"{flag} {code} - {name}")

        def on_select(event):
            index = listbox.curselection()
            if index:
                flag, code, name = self.country_list[index[0]]
                self.selected_country.set(f"{flag} {code}")
                popup.destroy()

        listbox.bind("<<ListboxSelect>>", on_select)

# Main window
root = Tk()
root.title("Move Out App")
root.geometry("390x844")
root.configure(bg="#ffc4d6")
root.resizable(False, False)

login_page = LoginPage(root)
login_page.pack(fill=BOTH, expand=True)

root.mainloop()