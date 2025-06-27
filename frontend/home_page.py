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
        lpink_box = Frame(self, bg="#ffe5ec", width=300, height=430)
        lpink_box.place(x=45, y=157)
        lpink_box.pack_propagate(False)

        # Navigation Bar
        nav_bar = Frame(self, bg="#ffc4d6", width=390, height=65)
        nav_bar.place(y=719)
        nav_bar.pack_propagate(False)

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

        # Vehicle container
        vehicle_box = Frame(lpink_box, bg="white", width=250, height=65)
        vehicle_box.pack(pady=(20, 0))
        vehicle_box.pack_propagate(False)

        Label(vehicle_box, text="Vehicle", font=self.label_font, fg="black", bg="white").place(x=5, y=5)

        self.vehicle_var = StringVar()
        self.vehicle_combo = ttk.Combobox(vehicle_box, textvariable=self.vehicle_var, state="readonly", font=self.dropdown_font,
                                          values=["Select a Vehicle", "Motor", "Car (4-Seater)", "Van (6-Seater)"], style="Pink.TCombobox")
        self.vehicle_combo.current(0)
        self.vehicle_combo.pack(fill="x", pady=(0, 24), ipady=8)

        # Line
        line = Frame(lpink_box, bg="#ffc4d6", width=250, height=2)
        line.pack(pady=(30, 0))
        line.pack_propagate(False)

        # Price container
        price_container = Frame(lpink_box, bg="#ffe5ec", width=250, height=25)
        price_container.pack(pady=(10, 0))

        # Price Label
        Label(price_container, text="Price", font=self.price_label_font, fg="black", bg="#ffe5ec").place(x=5)

        # Price Value
        self.price_value = Label(price_container, text="₱ 000.00", font=self.price_font, fg="black", bg="#ffe5ec")
        self.price_value.place(x=175)

        self.create_proceed_button(lpink_box).pack(pady=(20, 0))

    def create_proceed_button(self, lpink_box):
        canvas = Canvas(lpink_box, width=250, height=26, bg="#ffc4d6", highlightthickness=0, cursor="hand2")
        canvas.create_rectangle(0, 0, 250, 26, fill="#f38c9f", outline="#f38c9f", width=2)
        canvas.create_text(125, 13, text="PROCEED", fill="white", font=("League Spartan", 10, "bold"))
        
        return canvas
    
    def _clear_placeholder(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, END)
            entry.config(fg="black")

    def _add_placeholder(self, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg="gray")