from tkinter import *
import tkinter.font as Font

from backend.edit_account import EditAccountHandler
from backend.validators import InputValidator  # Added for phone formatting

class AccountPage(Frame):
    def __init__(self, parent, current_user_phone):
        super().__init__(parent)
        self.parent = parent
        self.current_user_phone = current_user_phone  # Store phone of logged-in user
        self.configure(bg="white")

        self.account_handler = EditAccountHandler()  # Handler for backend operations

        # Fonts
        self.title_font = Font.Font(family="Poppins", size=35, weight="bold")
        self.label_font = Font.Font(family="Montserrat", size=12)
        self.input_font = Font.Font(family="Montserrat", size=10)
        self.button_font = Font.Font(family="League Spartan", size=10, weight="bold")

        # Pink header
        pink_div = Frame(self, bg="#ffc4d6", width=390, height=380)
        pink_div.place(x=0, y=0)

        Label(
            pink_div,
            text="ACCOUNT",
            font=self.title_font,
            fg="white",
            bg="#ffc4d6",
            justify=LEFT,
        ).place(relx=0.5, y=70, anchor="n")

        canvas = Canvas(pink_div, width=200, height=200, bg="#ffc4d6", highlightthickness=0)
        canvas.place(relx=0.5, y=150, anchor="n")
        canvas.create_oval(0, 0, 200, 200, fill="white", outline="white")
        canvas.create_text(100, 100, text="👤", font=("Arial", 70), fill="#ffc4d6")

        # First Name Entry
        self.first_name_entry = Entry(
            self,
            font=self.input_font,
            bd=1,
            relief=SOLID,
            fg="gray",
            width=35,
            state=DISABLED,
        )
        self.first_name_entry.insert(0, "First Name")
        self.first_name_entry.place(x=70, y=400, width=250, height=35)
        self.first_name_entry.bind(
            "<FocusIn>",
            lambda e: self.clear_placeholder(self.first_name_entry, "First Name"),
        )
        self.first_name_entry.bind(
            "<FocusOut>",
            lambda e: self.restore_placeholder(self.first_name_entry, "First Name"),
        )

        # Last Name Entry
        self.last_name_entry = Entry(
            self,
            font=self.input_font,
            bd=1,
            relief=SOLID,
            fg="gray",
            width=35,
            state=DISABLED,
        )
        self.last_name_entry.insert(0, "Last Name")
        self.last_name_entry.place(x=70, y=450, width=250, height=35)
        self.last_name_entry.bind(
            "<FocusIn>",
            lambda e: self.clear_placeholder(self.last_name_entry, "Last Name"),
        )
        self.last_name_entry.bind(
            "<FocusOut>",
            lambda e: self.restore_placeholder(self.last_name_entry, "Last Name"),
        )

        # Phone Number
        self.phone_frame = Frame(self, bg="white", bd=1, relief=SOLID)
        self.phone_frame.place(x=70, y=510, width=250, height=35)

        Label(self.phone_frame, text="🇵🇭 +63", font=self.input_font, bg="white").pack(
            side=LEFT, padx=5
        )
        self.phone_entry = Entry(
            self.phone_frame,
            font=self.input_font,
            fg="gray",
            bg="white",
            bd=0,
            state=DISABLED,
        )
        self.phone_entry.insert(0, "Phone Number")
        self.phone_entry.pack(side=LEFT, fill=X, expand=True)
        self.phone_entry.bind(
            "<FocusIn>",
            lambda e: self.clear_placeholder(self.phone_entry, "Phone Number"),
        )
        self.phone_entry.bind(
            "<FocusOut>",
            lambda e: self.restore_placeholder(self.phone_entry, "Phone Number"),
        )

        # Edit PIN
        self.pin_entry = Entry(
            self,
            font=self.input_font,
            bd=1,
            relief=SOLID,
            fg="gray",
            width=35,
            state=DISABLED,
            show="*",
        )
        self.pin_entry.insert(0, "****")
        self.pin_entry.place(x=70, y=570, width=250, height=35)
        self.pin_entry.bind(
            "<FocusIn>",
            lambda e: self.clear_placeholder(self.pin_entry, "Edit PIN (4 digits only)"),
        )
        self.pin_entry.bind(
            "<FocusOut>",
            lambda e: self.restore_placeholder(
                self.pin_entry, "Edit PIN (4 digits only)"
            ),
        )

        # Confirm PIN
        self.cpin_entry = Entry(
            self,
            font=self.input_font,
            bd=1,
            relief=SOLID,
            fg="gray",
            width=35,
            state=DISABLED,
            show="*",
        )
        self.cpin_entry.insert(0, "****")
        self.cpin_entry.bind(
            "<FocusIn>",
            lambda e: self.clear_placeholder(
                self.cpin_entry, "Confirm PIN (4 digits only)"
            ),
        )
        self.cpin_entry.bind(
            "<FocusOut>",
            lambda e: self.restore_placeholder(
                self.cpin_entry, "Confirm PIN (4 digits only)"
            ),
        )

        # Error labels for phone and pin
        self.phone_error = Label(
            self, text="", fg="red", bg="white", font=("Montserrat", 8)
        )
        self.pin_error = Label(
            self, text="", fg="red", bg="white", font=("Montserrat", 8)
        )

        # Edit & Save Buttons
        self.edit_label = Label(
            self,
            text="✎ Edit",
            font=("Arial", 8),
            bg="white",
            fg="black",
            cursor="hand2",
        )
        self.edit_label.place(x=277, y=620)
        self.edit_label.bind("<Button-1>", self.enable_editing)

        self.save_label = Label(
            self,
            text="💾 Save",
            font=("Arial", 8),
            bg="white",
            fg="black",
            cursor="hand2",
        )
        self.save_label.place(x=310, y=660)
        self.save_label.bind("<Button-1>", self.save_info)
        self.save_label.place_forget()

        # Log out Button
        Button(
            self,
            text="LOG OUT",
            font=self.button_font,
            bg="#f38c9f",
            fg="white",
            activebackground="#ffc4d6",
            bd=0,
            cursor="hand2",
            command=self.go_interactive,
        ).place(x=70, y=700, width=250, height=25)

        # Bottom Nav Bar
        nav_bar = Frame(self, bg="#ffc4d6", width=390, height=65)
        nav_bar.place(x=0, y=779)

        Button(
            nav_bar,
            text="🏠",
            font=("Arial", 20),
            bg="#ffc4d6",
            bd=0,
            activebackground="#ffc4d6",
            cursor="hand2",
            command=self.go_home,
        ).place(x=40, y=5)
        Button(
            nav_bar,
            text="📄",
            font=("Arial", 20),
            bg="#ffc4d6",
            bd=0,
            activebackground="#ffc4d6",
            cursor="hand2",
            command=self.go_ride_status,
        ).place(x=175, y=5)
        Button(
            nav_bar,
            text="👤",
            font=("Arial", 20),
            bg="#ffc4d6",
            bd=0,
            activebackground="#ffc4d6",
            cursor="hand2",
            command=self.go_profile,
        ).place(x=320, y=5)

        self.load_user_info()  # Load data when account page opens

    # Data Loading
    def load_user_info(self):
        """Fetch user details from DB and populate the form."""
        from backend.database_manager import DatabaseManager

        db = DatabaseManager()
        formatted_phone = InputValidator.format_phone_number(self.current_user_phone)

        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT first_name, last_name, phone_number, pin FROM users WHERE phone_number = ?",
            (formatted_phone,),
        )
        row = cursor.fetchone()
        conn.close()

        if row:
            first, last, phone, pin = row

            # Temporarily enable entries so we can insert values
            self.first_name_entry.config(state=NORMAL)
            self.last_name_entry.config(state=NORMAL)
            self.phone_entry.config(state=NORMAL)
            self.pin_entry.config(state=NORMAL)
            self.cpin_entry.config(state=NORMAL)

            self.first_name_entry.delete(0, END)
            self.first_name_entry.insert(0, first)

            self.last_name_entry.delete(0, END)
            self.last_name_entry.insert(0, last)

            self.phone_entry.delete(0, END)
            self.phone_entry.insert(0, phone[3:])  # Remove +63 for display

            self.pin_entry.delete(0, END)
            self.pin_entry.insert(0, pin)

            self.cpin_entry.delete(0, END)
            self.cpin_entry.insert(0, pin)

            # Re‑disable fields
            self.first_name_entry.config(state=DISABLED)
            self.last_name_entry.config(state=DISABLED)
            self.phone_entry.config(state=DISABLED)
            self.pin_entry.config(state=DISABLED)
            self.cpin_entry.config(state=DISABLED)

    # Edit and Save 
    def enable_editing(self, event=None):
        self.first_name_entry.config(state=NORMAL)
        self.last_name_entry.config(state=NORMAL)
        self.phone_entry.config(state=NORMAL)
        self.pin_entry.config(state=NORMAL, show="")
        self.cpin_entry.config(state=NORMAL, show="")
        self.cpin_entry.place(x=70, y=620, width=250, height=35)
        self.edit_label.place_forget()
        self.save_label.place(x=277, y=660)

    def save_info(self, event=None):
        # Clear previous error messages
        self.phone_error.place_forget()
        self.pin_error.place_forget()

        first = self.first_name_entry.get().strip()
        last = self.last_name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        pin = self.pin_entry.get().strip()
        cpin = self.cpin_entry.get().strip()

        # Validate PINs match
        if pin != cpin:
            self.pin_error.config(text="PIN and Confirm PIN do not match.")
            self.pin_error.place(x=70, y=655)
            return

        # Format phone numbers
        formatted_new_phone = InputValidator.format_phone_number(phone)
        formatted_old_phone = InputValidator.format_phone_number(self.current_user_phone)

        # Check for duplicate phone if changed
        from backend.database_manager import DatabaseManager
        db = DatabaseManager()
        conn = db.get_connection()
        cursor = conn.cursor()

        if formatted_new_phone != formatted_old_phone:
            cursor.execute("SELECT * FROM users WHERE phone_number = ?", (formatted_new_phone,))
            if cursor.fetchone():
                self.phone_error.config(text="This phone number is already registered.")
                self.phone_error.place(x=70, y=545)
                conn.close()
                return

        # Perform update in DB
        cursor.execute("""
            UPDATE users 
            SET first_name = ?, last_name = ?, phone_number = ?, pin = ?
            WHERE phone_number = ?
        """, (first, last, formatted_new_phone, pin, formatted_old_phone))

        conn.commit()
        conn.close()

        # Update current_user_phone immediately
        self.current_user_phone = phone

        # Lock entries again
        self.first_name_entry.config(state=DISABLED)
        self.last_name_entry.config(state=DISABLED)
        self.phone_entry.config(state=DISABLED)
        self.pin_entry.config(state=DISABLED, show="*")
        self.cpin_entry.config(state=DISABLED, show="*")
        self.cpin_entry.place_forget()
        self.save_label.place_forget()
        self.edit_label.place(x=277, y=620)

    # Placeholder Helpers
    def clear_placeholder(self, entry_widget, placeholder_text):
        if entry_widget.get() == placeholder_text:
            entry_widget.delete(0, END)
            entry_widget.config(fg="black")

    def restore_placeholder(self, entry_widget, placeholder_text):
        if not entry_widget.get():
            entry_widget.insert(0, placeholder_text)
            entry_widget.config(fg="gray")

    # Navigation Buttons
    def go_interactive(self):
        if hasattr(self.parent, "show_interactive_page"):
            self.parent.show_interactive_page()

    def go_home(self):  # go to home page
        if hasattr(self.parent, "show_home_page"):
            self.parent.show_home_page()

    def go_ride_status(self):  # go to ride status page
        if hasattr(self.parent, "show_ride_status_page"):
            self.parent.show_ride_status_page()

    def go_profile(self):  # go to account page
        if hasattr(self.parent, "show_account_page"):
            self.parent.show_account_page()
