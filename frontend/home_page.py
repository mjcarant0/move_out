from tkinter import *
import tkinter.font as Font
from tkinter import ttk

class HomePage(Frame):
    '''
        This program provides the home page for Move Out.
        It allows the user to book their chosen ride.
    '''
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="white")

        self.title_font = Font.Font(family="Poppins", size=28, weight="bold")
        self.label_font = Font.Font(family="Montserrat", size=12, weight="bold")
        self.proceed_font = Font.Font(family="League Spartan", size=10, weight="bold")
        self.placeholder_font = Font.Font(family="Montserrat", size=9)
        self.price_label_font = Font.Font(family="Montserrat", size=15, weight="bold")
        self.price_font = Font.Font(family="Montserrat", size=15)
        self.dropdown_font = Font.Font(family="Poppins", size=20, weight="bold")

        # Pink Divider
        pink_div = Frame(self, bg="#ffc4d6", width=390, height=315)
        pink_div.pack(fill=X)
        pink_div.pack_propagate(False)

        Label(pink_div, text="SECURELY BOOK YOUR\nRIDE", font=self.title_font, bg="#ffc4d6", fg="white", justify="left").pack(anchor="w", pady=(60, 20), padx=25)
 
        # Light Pink Container
        lpink_box = Frame(self, bg="#ffe5ec", width=300, height=280)
        lpink_box.place(x=45, y=157)
        lpink_box.pack_propagate(False)

        # Pickup container
        pickup_box = Frame(lpink_box, bg="white", width=250, height=65)
        pickup_box.pack(pady=(40, 0))
        pickup_box.pack_propagate(False)

        Label(pickup_box, text="Pickup", font=self.label_font, fg="black", bg="white").place(x=5, y=5)

        # Pickup Input
        self.pickup_entry = Entry(pickup_box, font=self.placeholder_font, fg="#bdbdbd", bg="white", bd=0, relief="flat", highlightthickness=0)
        self.pickup_entry.insert(0, "Search Pickup Location")
        self.pickup_entry.place(x=5, y=30, width=240, height=25)
        self.pickup_entry.bind("<FocusIn>", lambda e: self._clear_placeholder(self.pickup_entry, "Search Pickup Location"))
        self.pickup_entry.bind("<FocusOut>", lambda e: self._add_placeholder(self.pickup_entry, "Search Pickup Location"))

        # Drop-off container
        dropoff_box = Frame(lpink_box, bg="white", width=250, height=65)
        dropoff_box.pack(pady=(20, 0))
        dropoff_box.pack_propagate(False)

        Label(dropoff_box, text="Drop-off", font=self.label_font, fg="black", bg="white").place(x=5, y=5)

        # Drop-off Input
        self.dropoff_entry = Entry(dropoff_box, font=self.placeholder_font, fg="#bdbdbd", bg="white", bd=0, relief="flat", highlightthickness=0)
        self.dropoff_entry.insert(0, "Search Drop-off Location")
        self.dropoff_entry.place(x=5, y=30, width=240, height=25)
        self.dropoff_entry.bind("<FocusIn>", lambda e: self._clear_placeholder(self.dropoff_entry, "Search Drop-off Location"))
        self.dropoff_entry.bind("<FocusOut>", lambda e: self._add_placeholder(self.dropoff_entry, "Search Drop-off Location"))

        self.create_proceed_button(lpink_box).pack(pady=(20, 0))

        # Bottom Nav Bar
        nav_bar = Frame(self, bg="#ffc4d6", width=390, height=65)
        nav_bar.place(x=0, y=779)

        Button(nav_bar, text="🏠", font=("Arial", 20), bg="#ffc4d6", bd=0,
               activebackground="#ffc4d6", cursor="hand2", command=self.go_home).place(x=40, y=5)
        Button(nav_bar, text="📄", font=("Arial", 20), bg="#ffc4d6", bd=0,
               activebackground="#ffc4d6", cursor="hand2", command=self.go_documents).place(x=175, y=5)
        Button(nav_bar, text="👤", font=("Arial", 20), bg="#ffc4d6", bd=0,
               activebackground="#ffc4d6", cursor="hand2", command=self.go_profile).place(x=320, y=5)

    def create_proceed_button(self, lpink_box):
        canvas = Canvas(lpink_box, width=250, height=26, bg="#ffc4d6", highlightthickness=0, cursor="hand2")
        canvas.create_rectangle(0, 0, 250, 26, fill="#f38c9f", outline="#f38c9f", width=2)
        canvas.create_text(125, 13, text="PROCEED", fill="white", font=("League Spartan", 10, "bold"))
        
        return canvas
    
    def clear_placeholder(self, entry_widget, placeholder_text):
        if entry_widget.get() == placeholder_text:
            entry_widget.delete(0, END)
            entry_widget.config(fg="black")

    def restore_placeholder(self, entry_widget, placeholder_text):
        if not entry_widget.get():
            entry_widget.insert(0, placeholder_text)
            entry_widget.config(fg="gray")

    def go_home(self):
        if hasattr(self.parent, "show_home_page"):
            self.parent.show_home_page()

    def go_documents(self):
        print("Go documents")

    def go_profile(self):
        if hasattr(self.parent, "show_account_page"):
            self.parent.show_account_page()