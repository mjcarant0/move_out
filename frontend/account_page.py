from tkinter import *
import tkinter.font as Font

class AccountEditPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg="white")

        # Fonts
        self.title_font = Font.Font(family="Poppins", size=35, weight="bold")
        self.label_font = Font.Font(family="Montserrat", size=12)
        self.input_font = Font.Font(family="Montserrat", size=10)
        self.button_font = Font.Font(family="League Spartan", size=10, weight="bold")

        # Pink header
        pink_div = Frame(self, bg="#ffc4d6", width=390, height=380)
        pink_div.place(x=0, y=0)

        # Title
        Label(pink_div, text="ACCOUNT", font=self.title_font, fg="white", bg="#ffc4d6", justify=LEFT)\
            .place(relx=0.5, y=70, anchor="n")

        # Circle icon
        canvas = Canvas(pink_div, width=200, height=200, bg="#ffc4d6", highlightthickness=0)
        canvas.place(relx=0.5, y=150, anchor="n")
        canvas.create_oval(0, 0, 200, 200, fill="white", outline="white")
        canvas.create_text(100, 100, text="👤", font=("Arial", 70), fill="#ffc4d6")

        # First Name
        self.first_name_entry = Entry(self, font=self.input_font, bd=1, relief=SOLID, fg="gray")
        self.first_name_entry.insert(0, "First Name")
        self.first_name_entry.place(x=70, y=400, width=250, height=35)
        self.first_name_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.first_name_entry, "First Name"))
        self.first_name_entry.bind("<FocusOut>", lambda e: self.restore_placeholder(self.first_name_entry, "First Name"))

        # Last Name
        self.last_name_entry = Entry(self, font=self.input_font, bd=1, relief=SOLID, fg="gray")
        self.last_name_entry.insert(0, "Last Name")
        self.last_name_entry.place(x=70, y=455, width=250, height=35)
        self.last_name_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.last_name_entry, "Last Name"))
        self.last_name_entry.bind("<FocusOut>", lambda e: self.restore_placeholder(self.last_name_entry, "Last Name"))

        # Phone field
        phone_frame = Frame(self, bg="white", bd=1, relief="solid")
        phone_frame.place(x=70, y=510, width=250, height=35)
        Label(phone_frame, text="🇵🇭 +63", font=self.input_font, bg="white")\
            .pack(side=LEFT, padx=5)
        self.phone_entry = Entry(phone_frame, font=self.input_font, fg="#bdbdbd", bg="white", bd=0)
        self.phone_entry.insert(0, "Phone Number")
        self.phone_entry.pack(side=LEFT, fill=X, expand=True)
        self.phone_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.phone_entry, "Phone Number"))
        self.phone_entry.bind("<FocusOut>", lambda e: self.restore_placeholder(self.phone_entry, "Phone Number"))

        # Edit label
        Label(self, text="✎ Edit", font=("Arial", 8), bg="white", fg="black")\
            .place(x=310, y=550)

        # Log out button
        Button(self, text="Log Out", font=self.button_font, bg="#f38c9f", fg="white",
               activebackground="#ffc4d6", bd=0, cursor="hand2")\
            .place(x=70, y=590, width=250, height=35)

        # Navigation Bar
        nav_bar = Frame(self, bg="#ffc4d6", width=390, height=65)
        nav_bar.place(x=0, y=779)

        Button(nav_bar, text="🏠", font=("Arial", 20), bg="#ffc4d6", bd=0,
               activebackground="#ffc4d6", cursor="hand2", command=self.go_home).place(x=40, y=5)
        Button(nav_bar, text="📄", font=("Arial", 20), bg="#ffc4d6", bd=0,
               activebackground="#ffc4d6", cursor="hand2", command=self.go_history).place(x=175, y=5)
        Button(nav_bar, text="👤", font=("Arial", 20), bg="#ffc4d6", bd=0,
               activebackground="#ffc4d6", cursor="hand2", command=self.go_profile).place(x=320, y=5)

    def clear_placeholder(self, entry_widget, placeholder_text):
        if entry_widget.get() == placeholder_text:
            entry_widget.delete(0, END)
            entry_widget.config(fg="black")

    def restore_placeholder(self, entry_widget, placeholder_text):
        if not entry_widget.get():
            entry_widget.insert(0, placeholder_text)
            entry_widget.config(fg="gray")

    def go_home(self):
        print("home")

    def go_history(self):
        print("history")

    def go_profile(self):
        print("profile")

# Run as standalone
if __name__ == "__main__":
    root = Tk()
    root.geometry("390x844")
    root.resizable(False, False)
    root.title("Account")
    app = AccountEditPage(root)
    app.place(x=0, y=0, width=390, height=844)
    root.mainloop()