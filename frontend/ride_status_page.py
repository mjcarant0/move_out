from tkinter import *
import tkinter.font as Font

from .ride_status_pending import PendingView
from .ride_status_completed import CompletedView
from .ride_status_canceled import CanceledView

class RideStatusPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="white")

        self.title_font = Font.Font(family="Poppins", size=20, weight="bold")
        self.tab_font = Font.Font(family="Montserrat", size=12, weight="bold")
        self.placeholder_font = Font.Font(family="Montserrat", size=9)

        # Ride info
        self.ride_info = {
            "pickup": None,
            "dropoff": None,
            "vehicle": None,
            "price": None,
            "duration": None
        }

        self.ride_active = False
        self.ride_timer = None

        self.completed_rides = []  # Store multiple completed rides
        self.canceled_rides = []   # Store multiple canceled rides

        # Header
        pink_div = Frame(self, bg="#ffc4d6", width=390, height=118)
        pink_div.pack(fill=X)
        pink_div.pack_propagate(False)
        Label(pink_div, text="RIDE STATUS", font=self.title_font, bg="#ffc4d6", fg="white").place(relx=0.5, rely=0.6, anchor="center")

        # Tabs
        self.create_tab_buttons()

        # Placeholder for content
        self.content_frame = None

        # Navigation bar
        nav_bar = Frame(self, bg="#ffc4d6", width=390, height=65)
        nav_bar.place(y=779)
        nav_bar.pack_propagate(False)
        Button(nav_bar, text="🏠", font=("Arial", 20), bg="#ffc4d6", bd=0,
               activebackground="#ffc4d6", cursor="hand2", command=self.go_home).place(x=40, y=5)
        Button(nav_bar, text="📄", font=("Arial", 20), bg="#ffc4d6", bd=0,
               activebackground="#ffc4d6", cursor="hand2", command=self.go_ride_status).place(x=175, y=5)
        Button(nav_bar, text="👤", font=("Arial", 20), bg="#ffc4d6", bd=0,
               activebackground="#ffc4d6", cursor="hand2", command=self.go_profile).place(x=320, y=5)

        self.show_pending()  # Default view

    def create_tab_buttons(self):
        Button(self, text="PENDING", bg="#FB6F92", fg="white", font=self.tab_font,
               bd=0, activebackground="#fba4bd", command=self.show_pending).place(relx=0.18, y=135, anchor="n", width=111, height=27)

        Button(self, text="COMPLETED", bg="#FB6F92", fg="white", font=self.tab_font,
               bd=0, activebackground="#fba4bd", command=self.show_completed).place(relx=0.5, y=135, anchor="n", width=111, height=27)

        Button(self, text="CANCELED", bg="#FB6F92", fg="white", font=self.tab_font,
               bd=0, activebackground="#fba4bd", command=self.show_canceled).place(relx=0.82, y=135, anchor="n", width=111, height=27)

    def show_pending(self):
        self._clear_content()

        if not self.ride_active:
            print("No active ride — skipping pending view")
            return

        self.content_frame = Frame(self, bg="#FFE5EC", width=367, height=325)
        self.content_frame.place(relx=0.5, y=197, anchor="n")
        self.content_frame.pack_propagate(False)

        PendingView(
            self.content_frame,
            pickup=self.ride_info["pickup"],
            dropoff=self.ride_info["dropoff"],
            vehicle=self.ride_info["vehicle"],
            price=self.ride_info["price"]
        ).pack(fill=BOTH, expand=True)

    def show_completed(self):
        self._clear_content()

        if not self.completed_rides:
            return

        self.content_frame = Frame(self, bg="#FFE5EC", width=367, height=325)
        self.content_frame.place(relx=0.5, y=197, anchor="n")
        self.content_frame.pack_propagate(False)

        canvas = Canvas(self.content_frame, bg="#FFE5EC", highlightthickness=0)
        scrollbar = Scrollbar(self.content_frame, orient=VERTICAL, command=canvas.yview)
        scroll_frame = Frame(canvas, bg="#FFE5EC")

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        for ride in self.completed_rides:
            frame = CompletedView(scroll_frame)
            frame.populate_data(ride["pickup"], ride["dropoff"], ride["vehicle"], ride["price"])
            frame.pack(pady=10)

    def show_canceled(self):
        self._clear_content()

        if not self.canceled_rides:
            return

        self.content_frame = Frame(self, bg="#FFE5EC", width=367, height=325)
        self.content_frame.place(relx=0.5, y=197, anchor="n")
        self.content_frame.pack_propagate(False)

        canvas = Canvas(self.content_frame, bg="#FFE5EC", highlightthickness=0)
        scrollbar = Scrollbar(self.content_frame, orient=VERTICAL, command=canvas.yview)
        scroll_frame = Frame(canvas, bg="#FFE5EC")

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        for ride in self.canceled_rides:
            frame = CanceledView(scroll_frame)
            frame.populate_data(ride["pickup"], ride["dropoff"], ride["vehicle"], ride["price"])
            frame.pack(pady=10)

    def _clear_content(self):
        if self.content_frame:
            self.content_frame.destroy()
            self.content_frame = None

    def go_home(self):
        if hasattr(self.parent, "show_home_page"):
            self.parent.show_home_page()

    def go_ride_status(self):
        if hasattr(self.parent, "show_ride_status_page"):
            self.parent.show_ride_status_page()

    def go_profile(self):
        if hasattr(self.parent, "show_account_page"):
            self.parent.show_account_page()

    def set_ride_details(self, pickup, dropoff, vehicle, price, duration_str):
        self.ride_info = {
            "pickup": pickup,
            "dropoff": dropoff,
            "vehicle": vehicle,
            "price": price,
            "duration": duration_str
        }

        self.ride_active = True
        self.show_pending()

        seconds = self._parse_duration_to_seconds(duration_str)
        self.ride_timer = self.after(seconds * 1000, self._complete_ride)

    def _complete_ride(self):
        # ✅ Move ride info into completed rides
        self.completed_rides.append({
            "pickup": self.ride_info["pickup"],
            "dropoff": self.ride_info["dropoff"],
            "vehicle": self.ride_info["vehicle"],
            "price": self.ride_info["price"]
        })

        # ✅ Clear ride info and state
        self.ride_info = {
            "pickup": None,
            "dropoff": None,
            "vehicle": None,
            "price": None,
            "duration": None
        }

        self.ride_active = False
        self.ride_timer = None

        # ✅ Automatically switch to COMPLETED tab
        self.show_completed()

    def add_canceled_ride(self, pickup, dropoff, vehicle, price):
        self.ride_active = False

        if self.ride_timer is not None:
            self.after_cancel(self.ride_timer)
            self.ride_timer = None

        self.ride_info = {
            "pickup": None,
            "dropoff": None,
            "vehicle": None,
            "price": None,
            "duration": None
        }

        self.canceled_rides.append({
            "pickup": pickup,
            "dropoff": dropoff,
            "vehicle": vehicle,
            "price": price
        })

        self.show_canceled()

    def _parse_duration_to_seconds(self, duration_str):
        duration_str = duration_str.lower()
        if "hour" in duration_str:
            parts = duration_str.split()
            hours = int(parts[0])
            minutes = int(parts[2]) if len(parts) > 2 else 0
            return hours * 3600 + minutes * 60
        elif "min" in duration_str:
            return int(duration_str.split()[0]) * 60
        return 0
