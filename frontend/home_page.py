from tkinter import *
import tkinter.font as Font

class HomePage(Frame):
    '''
        This program provides the home page for Move Out.
        It allows the user to book their chosen ride.
    '''
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="white")

        self.suggestions_box = None
        self.active_entry = None

        self.title_font = Font.Font(family="Poppins", size=28, weight="bold")
        self.label_font = Font.Font(family="Montserrat", size=12, weight="bold")
        self.proceed_font = Font.Font(family="League Spartan", size=10, weight="bold")
        self.placeholder_font = Font.Font(family="Montserrat", size=9)

        # Pink Divider
        pink_div = Frame(self, bg="#ffc4d6", width=390, height=315)
        pink_div.pack(fill=X)
        pink_div.pack_propagate(False)

        Label(pink_div, text="SECURELY BOOK YOUR\nRIDE", font=self.title_font, bg="#ffc4d6", fg="white", justify="left").pack(anchor="w", pady=(60, 20), padx=25)
 
        # Light Pink Container
        lpink_box = Frame(self, bg="#ffe5ec", width=300, height=280)
        lpink_box.place(x=45, y=157)
        lpink_box.pack_propagate(False)

        self.warning_label = Label(lpink_box, text="", fg="red", bg="#ffe5ec", font=self.placeholder_font)
        self.warning_label.pack(pady=(10, 0))

        # Navigation Bar
        nav_bar = Frame(self, bg="#ffc4d6", width=390, height=65)
        nav_bar.place(y=719)
        nav_bar.pack_propagate(False)

        Button(nav_bar, text="🏠", font=("Arial", 20), bg="#ffc4d6", bd=0,
               activebackground="#ffc4d6", cursor="hand2", command=self.go_home).place(x=40, y=5)
        Button(nav_bar, text="📄", font=("Arial", 20), bg="#ffc4d6", bd=0,
               activebackground="#ffc4d6", cursor="hand2", command=self.go_documents).place(x=175, y=5)
        Button(nav_bar, text="👤", font=("Arial", 20), bg="#ffc4d6", bd=0,
               activebackground="#ffc4d6", cursor="hand2", command=self.go_profile).place(x=320, y=5)

        # Pickup container
        pickup_box = Frame(lpink_box, bg="white", width=250, height=65)
        pickup_box.pack(pady=(40, 0))
        pickup_box.pack_propagate(False)

        Label(pickup_box, text="Pickup", font=self.label_font, fg="#f38c9f", bg="white").place(x=5, y=5)

        # Pickup Input
        self.pickup_entry = Entry(pickup_box, font=self.placeholder_font, fg="#bdbdbd", bg="white", bd=0, relief="flat", highlightthickness=0)
        self.pickup_entry.insert(0, "Search Pickup Location")
        self.pickup_entry.place(x=5, y=30, width=240, height=25)
        self.pickup_entry.bind("<FocusIn>", lambda e: self._clear_placeholder(self.pickup_entry, "Search Pickup Location"))
        self.pickup_entry.bind("<FocusOut>", lambda e: self._add_placeholder(self.pickup_entry, "Search Pickup Location"))
        self.pickup_entry.bind("<KeyRelease>", lambda e: self.show_suggestions(e, self.pickup_entry))

        # Drop-off container
        dropoff_box = Frame(lpink_box, bg="white", width=250, height=65)
        dropoff_box.pack(pady=(20, 0))
        dropoff_box.pack_propagate(False)

        Label(dropoff_box, text="Drop-off", font=self.label_font, fg="#f38c9f", bg="white").place(x=5, y=5)

        # Drop-off Input
        self.dropoff_entry = Entry(dropoff_box, font=self.placeholder_font, fg="#bdbdbd", bg="white", bd=0, relief="flat", highlightthickness=0)
        self.dropoff_entry.insert(0, "Search Drop-off Location")
        self.dropoff_entry.place(x=5, y=30, width=240, height=25)
        self.dropoff_entry.bind("<FocusIn>", lambda e: self._clear_placeholder(self.dropoff_entry, "Search Drop-off Location"))
        self.dropoff_entry.bind("<FocusOut>", lambda e: self._add_placeholder(self.dropoff_entry, "Search Drop-off Location"))
        self.dropoff_entry.bind("<KeyRelease>", lambda e: self.show_suggestions(e, self.dropoff_entry))

        self.create_proceed_button(lpink_box).pack(pady=(20, 0))

    def create_proceed_button(self, lpink_box):
        canvas = Canvas(lpink_box, width=250, height=26, bg="#ffc4d6", highlightthickness=0, cursor="hand2")
        canvas.create_rectangle(0, 0, 250, 26, fill="#f38c9f", outline="#f38c9f", width=2)
        canvas.create_text(125, 13, text="PROCEED", fill="white", font=("League Spartan", 10, "bold"))

        canvas.bind("<Button-1>", self.on_proceed_clicked)
        return canvas

    def on_proceed_clicked(self, event):
        pickup = self.pickup_entry.get().strip()
        dropoff = self.dropoff_entry.get().strip()

        if pickup == "" or pickup == "Search Pickup Location" or dropoff == "" or dropoff == "Search Drop-off Location":
            self.warning_label.config(text="Please fill out both Pickup and Drop-off locations.")
            return
        else:
            self.warning_label.config(text="")  # Clear warning if inputs are valid

        if hasattr(self.parent, "show_booking_page"):
            self.parent.show_booking_page(pickup, dropoff)

    def _clear_placeholder(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, END)
            entry.config(fg="black")

    def _add_placeholder(self, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg="gray")

    def go_home(self):
        if hasattr(self.parent, "show_home_page"):
            self.parent.show_home_page()

    def go_documents(self):
        print("Go documents")

    def go_profile(self):
        if hasattr(self.parent, "show_account_page"):
            self.parent.show_account_page()

    def show_suggestions(self, event, entry):
        text = entry.get()
        if text in ["", "Search Pickup Location", "Search Drop-off Location"]:
            if self.suggestions_box:
                self.suggestions_box.destroy()
            return

        try:
            suggestions = self.parent.backend.autocomplete_place(text)
        except Exception as e:
            print("Autocomplete error:", e)
            suggestions = []

        if self.suggestions_box:
            self.suggestions_box.destroy()

        self.suggestions_box = Listbox(self, height=min(5, len(suggestions)), bg="white", fg="black", font=self.placeholder_font)
        self.suggestions_box.place(x=entry.winfo_rootx() - self.winfo_rootx(),
                                   y=entry.winfo_rooty() - self.winfo_rooty() + entry.winfo_height(),
                                   width=entry.winfo_width())

        for suggestion in suggestions:
            self.suggestions_box.insert(END, suggestion)

        self.active_entry = entry
        self.suggestions_box.bind("<<ListboxSelect>>", self.select_suggestion)

    def select_suggestion(self, event):
        if self.suggestions_box and self.active_entry:
            selected = self.suggestions_box.get(self.suggestions_box.curselection())
            self.active_entry.delete(0, END)
            self.active_entry.insert(0, selected)
            self.suggestions_box.destroy()