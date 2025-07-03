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

        # Store the current ride info
        self.ride_info = {
            "pickup": None,
            "dropoff": None,
            "vehicle": None,
            "price": None,
            "duration": None
        }

        self.ride_active = False
        self.ride_timer = None

        # Store multiple completed and canceled rides
        self.completed_rides = []
        self.canceled_rides = []

        # Create header
        pink_div = Frame(self, bg="#ffc4d6", width=390, height=118)
        pink_div.pack(fill=X)
        pink_div.pack_propagate(False)
        Label(pink_div, text="RIDE STATUS", font=self.title_font, bg="#ffc4d6", fg="white").place(relx=0.5, rely=0.6, anchor="center")

        # Create tab buttons
        self.create_tab_buttons()

        # Placeholder for tab content
        self.content_frame = None

        # Bottom navigation bar
        nav_bar = Frame(self, bg="#ffc4d6", width=390, height=65)
        nav_bar.place(y=779)
        nav_bar.pack_propagate(False)
        Button(nav_bar, text="🏠", font=("Arial", 20), bg="#ffc4d6", bd=0,
               activebackground="#ffc4d6", cursor="hand2", command=self.go_home).place(x=40, y=5)
        Button(nav_bar, text="📄", font=("Arial", 20), bg="#ffc4d6", bd=0,
               activebackground="#ffc4d6", cursor="hand2", command=self.go_ride_status).place(x=175, y=5)
        Button(nav_bar, text="👤", font=("Arial", 20), bg="#ffc4d6", bd=0,
               activebackground="#ffc4d6", cursor="hand2", command=self.go_profile).place(x=320, y=5)

        # Show pending rides by default
        self.show_pending()

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
            print("No active ride. Skipping pending view.")
            return

        # Show current ride in pending state
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

        if len(self.completed_rides) == 1:
            # Only one completed ride, no need for scroll
            self.content_frame = Frame(self, bg="white", width=367, height=325)
            self.content_frame.place(relx=0.5, y=197, anchor="n")
            self.content_frame.pack_propagate(False)

            frame = CompletedView(self.content_frame)
            ride = self.completed_rides[-1]
            frame.populate_data(ride["pickup"], ride["dropoff"], ride["vehicle"], ride["price"])
            frame.pack()
        else:
            # Show all completed rides with scroll
            self.content_frame = Frame(self, bg="white", width=367, height=580)
            self.content_frame.place(relx=0.5, y=197, anchor="n")
            self.content_frame.pack_propagate(False)

            canvas = Canvas(self.content_frame, bg="white", highlightthickness=0, width=367, height=580)
            scrollbar = Scrollbar(self.content_frame, orient=VERTICAL, command=canvas.yview,
                                  width=0, troughcolor="white", borderwidth=0)
            canvas.configure(yscrollcommand=scrollbar.set)

            scrollbar.pack(side=RIGHT, fill=Y)
            canvas.pack(side=LEFT, fill=BOTH, expand=True)

            scroll_frame = Frame(canvas, bg="white")
            canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

            def on_configure(event):
                canvas.configure(scrollregion=canvas.bbox("all"))
            scroll_frame.bind("<Configure>", on_configure)

            def _on_mousewheel(event):
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
            canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

            for ride in reversed(self.completed_rides):
                frame = CompletedView(scroll_frame)
                frame.populate_data(ride["pickup"], ride["dropoff"], ride["vehicle"], ride["price"])
                frame.pack(pady=10)

    def show_canceled(self):
        self._clear_content()

        if not self.canceled_rides:
            return

        if len(self.canceled_rides) == 1:
            # One canceled ride, no need for scroll
            self.content_frame = Frame(self, bg="white", width=367, height=325)
            self.content_frame.place(relx=0.5, y=197, anchor="n")
            self.content_frame.pack_propagate(False)

            frame = CanceledView(self.content_frame)
            ride = self.canceled_rides[-1]
            frame.populate_data(ride["pickup"], ride["dropoff"], ride["vehicle"], ride["price"])
            frame.pack()
        else:
            # Show all canceled rides in a scrollable layout
            self.content_frame = Frame(self, bg="white", width=367, height=580)
            self.content_frame.place(relx=0.5, y=197, anchor="n")

            canvas = Canvas(self.content_frame, bg="white", highlightthickness=0, width=367, height=580)
            scrollbar = Scrollbar(self.content_frame, orient=VERTICAL, command=canvas.yview,
                                  width=0, troughcolor="white", borderwidth=0)
            canvas.configure(yscrollcommand=scrollbar.set)

            scrollbar.pack(side=RIGHT, fill=Y)
            canvas.pack(side=LEFT, fill=BOTH, expand=True)

            scroll_frame = Frame(canvas, bg="white")
            canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

            def on_configure(event):
                canvas.configure(scrollregion=canvas.bbox("all"))
            scroll_frame.bind("<Configure>", on_configure)

            def _on_mousewheel(event):
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
            canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

            for ride in reversed(self.canceled_rides):
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
        # Called after booking is confirmed to store info and start countdown
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
        if not all([self.ride_info["pickup"], self.ride_info["dropoff"], self.ride_info["vehicle"], self.ride_info["price"]]):
            print("Incomplete ride info. Ride not added to completed list.")
            return

        self.completed_rides.append({
            "pickup": self.ride_info["pickup"],
            "dropoff": self.ride_info["dropoff"],
            "vehicle": self.ride_info["vehicle"],
            "price": self.ride_info["price"]
        })

        # Reset ride info after completion
        self.ride_info = {
            "pickup": None,
            "dropoff": None,
            "vehicle": None,
            "price": None,
            "duration": None
        }

        self.ride_active = False
        self.ride_timer = None
        self.show_completed()

    def add_canceled_ride(self, pickup, dropoff, vehicle, price):
        # Cancel active ride and add to canceled list
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

    def restore_ride_info(self, pickup, dropoff, vehicle, price, duration_str):
        # Called when returning to the pending screen without starting a new ride
        self.ride_info = {
            "pickup": pickup,
            "dropoff": dropoff,
            "vehicle": vehicle,
            "price": price,
            "duration": duration_str
        }

        self.ride_active = True

        if self.ride_timer is not None:
            self.after_cancel(self.ride_timer)

        seconds = self._parse_duration_to_seconds(duration_str)
        self.ride_timer = self.after(seconds * 1000, self._complete_ride)

        self.show_pending()
