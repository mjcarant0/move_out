from tkinter import *
import tkinter.font as Font

class BookingPage(Frame):
    '''
        This program provides the booking page for Move Out.
        It allows the user to book their chosen ride
        and see the pinned locations in the map.
    '''
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="white")

        # Fonts
        self.label_font = Font.Font(family="Montserrat", size=11, weight="bold")
        self.value_font = Font.Font(family="Montserrat", size=10)
        self.price_font = Font.Font(family="Montserrat", size=12, weight="bold")
        self.confirm_font = Font.Font(family="League Spartan", size=12, weight="bold")

        # Back Button Container
        back_con = Frame(self, bg="#ffc4d6", width=390, height=50)
        back_con.pack(padx=0, pady=0, fill=X)
        back_con.pack_propagate(False)

        # Map Container
        self.map_frame = Frame(self, width=390, height=350, bg="gray")
        self.map_frame.pack(pady=0)
        self.map_frame.pack_propagate(False)

        # Options Container
        self.options_frame = Frame(self, width=390, height=200, bg="white")
        self.options_frame.pack(pady=0)
        self.options_frame.pack_propagate(False)

        # Confirm Button Container
        confirm_con = Frame(self, bg="#ff8fab", width=390, height=50)
        confirm_con.place(y=734)
        confirm_con.pack_propagate(False)




