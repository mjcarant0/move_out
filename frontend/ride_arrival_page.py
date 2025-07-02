import sys
import os
import tkinter.font as Font

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import *
from PIL import Image, ImageTk
from backend.ride_booking import RideBackend
from urllib.request import urlopen
from io import BytesIO

class RideArrivalPage(Frame):
    '''
        This program provides the Ride Arrival page for Move Out.
        It displays the ride details, map, and allows the user to cancel the ride.
        It also shows the booking ID, estimated duration, and distance.
    '''
    def __init__(self, parent, pickup_location, dropoff_location, selected_vehicle, selected_price):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="white")

        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location    
        self.selected_vehicle = selected_vehicle
        self.selected_price = selected_price

        # [Added] RideBackend instantiated to access backend methods like booking ID, distance, duration
        self.backend = RideBackend("AIzaSyAOKrot0gO67ji8DpUmxN3FdXRBfMsCvRQ")

        # Fonts
        self.booking_info_font = Font.Font(family="Montserrat", size=12)
        self.loading_font = Font.Font(family="Montserrat", size=15, weight="bold")
        self.location_font = Font.Font(family="Montserrat", size=11, weight="bold")
        self.distance_font = Font.Font(family="Montserrat", size=10, weight="bold")
        self.selection_font = Font.Font(family="Montserrat", size=12, weight="bold")
        self.back_font = Font.Font(family="League Spartan", size=12, weight="bold")
        self.cancel_font = Font.Font(family="League Spartan", size=12, weight="bold")

        # Back Button Container
        back_con = Frame(self, bg="#ffc4d6", width=390, height=50)
        back_con.pack(padx=0, pady=0, fill=X)
        back_con.pack_propagate(False)
        self.create_back_button(back_con).place(x=10, y=12)

        # Map Container
        self.map_frame = Frame(self, width=390, height=350, bg="#8f8f8f")
        self.map_frame.pack(pady=0)
        self.map_frame.pack_propagate(False)

        # Map Image
        self.map_img_label = Label(self.map_frame, bg="#8f8f8f")
        self.map_img_label.pack(expand=True)

        # Option Container
        self.options_frame = Frame(self, width=390, height=350, bg="white")
        self.options_frame.pack(pady=0)
        self.options_frame.pack_propagate(False)

        # [Added] Ride Info Container to display booking ID, duration, and status message
        info_frame = Frame(self.options_frame, bg="#eeeeee", width=390, height=100)
        info_frame.pack()
        info_frame.pack_propagate(False)

        Label(info_frame, text="Booking ID", font=self.booking_info_font, fg="#8f8f8f", bg="#eeeeee").place(x=25, y=10)
        self.booking_id_label = Label(info_frame, text=".....", font=self.booking_info_font, fg="#8f8f8f", bg="#eeeeee")
        self.booking_id_label.place(x=300, y=10)

        Label(info_frame, text="Estimated Ride Duration", font=self.booking_info_font, fg="#8f8f8f", bg="#eeeeee").place(x=25, y=35)
        self.duration_label = Label(info_frame, text=".....", font=self.booking_info_font, fg="#8f8f8f", bg="#eeeeee")
        self.duration_label.place(x=310, y=35)

        Label(info_frame, text="Rider is on the way...", font=self.loading_font, fg="#8f8f8f", bg="#eeeeee").place(anchor="center", x=195, y=72)

        # Location Display
        location_frame = Frame(self.options_frame, bg="white", width=390, height=110)
        location_frame.pack()
        location_frame.pack_propagate(False)

        # Base path for image files
        base_path = os.path.dirname(__file__)
        pickup_path = os.path.join(base_path, "..", "media", "pickup.png")
        dropoff_path = os.path.join(base_path, "..", "media", "dropoff.png")
        line_path = os.path.join(base_path, "..", "media", "line.png")

        pickup_image = Image.open(pickup_path).resize((15, 15), Image.LANCZOS)
        dropoff_image = Image.open(dropoff_path).resize((15, 15), Image.LANCZOS)
        line_image = Image.open(line_path).resize((10, 20), Image.LANCZOS)

        self.pickup_img = ImageTk.PhotoImage(pickup_image)
        self.dropoff_img = ImageTk.PhotoImage(dropoff_image)
        self.line_img = ImageTk.PhotoImage(line_image)

        # Row and Column for proper image and text alignment
        info_row = Frame(location_frame, bg="white")
        info_row.pack(anchor="w", padx=30, pady=(25, 0))
        icon_column = Frame(info_row, bg="white")
        icon_column.pack(side="left", anchor="n")
        Label(icon_column, image=self.pickup_img, bg="white").pack()
        Label(icon_column, image=self.line_img, bg="white").pack()
        Label(icon_column, image=self.dropoff_img, bg="white").pack()

        label_column = Frame(info_row, bg="white")
        label_column.pack(side="left", anchor="n", padx=10)
        Label(label_column, text="Pickup", font=self.location_font, fg="#8f8f8f", bg="white", anchor="w").pack(anchor="w")
        Label(label_column, text="Drop-off", font=self.location_font, fg="#8f8f8f", bg="white", anchor="w").pack(anchor="w", pady=(22, 0))

        # Distance Info Container
        distance_container = Frame(location_frame, bg="white", width=350, height=20)
        distance_container.pack(pady=(5, 0))
        Label(distance_container, text="Distance", font=self.distance_font, fg="#8f8f8f", bg="white").place(x=5)
        self.distance_value = Label(distance_container, text="--", font=self.distance_font, fg="#8f8f8f", bg="white")
        self.distance_value.place(x=290)

        # [Changed] Shows selected vehicle as static info instead of interactive rows
        vehicle_frame = Frame(self.options_frame, bg="white", width=390, height=60)
        vehicle_frame.pack()
        vehicle_frame.pack_propagate(False)

        vehicle_to_image = {
            "Motorcycle": "motor.png",
            "4-seater": "4seater.png",
            "6-seater": "6seater.png"
        }

        try:
            image_filename = vehicle_to_image.get(self.selected_vehicle)
            if image_filename:
                vehicle_img_path = os.path.join(base_path, "..", "media", image_filename)
                vehicle_image = Image.open(vehicle_img_path).resize((40, 40))
                self.vehicle_icon = ImageTk.PhotoImage(vehicle_image)
            else:
                print(f"[Warning] No image mapped for vehicle: {self.selected_vehicle}")
                self.vehicle_icon = None
        except Exception as e:
            print(f"[Error] Failed to load vehicle image: {e}")
            self.vehicle_icon = None

        Label(vehicle_frame, image=self.vehicle_icon, bg="white").place(x=30, y=10)
        Label(vehicle_frame, text=self.selected_vehicle, font=self.selection_font, fg="#8f8f8f", bg="white").place(x=85, y=20)
        Label(vehicle_frame, text=self.selected_price, font=self.selection_font, fg="#8f8f8f", bg="white").place(x=300, y=20)

        # [Replaced] CONFIRM button with CANCEL button to go back to HomePage
        cancel_con = Frame(self, bg="#ff8fab", width=390, height=50)
        cancel_con.place(y=734)
        cancel_con.pack_propagate(False)
        self.create_cancel_button(cancel_con).place(x=300, y=12)

        self.after(100, self.load_static_map)

        # [Added] Populate backend data like booking ID, estimated duration, and distance
        self.after(300, self.populate_backend_info)

    def create_back_button(self, container):
        canvas = Canvas(container, width=60, height=26, bg="#ffc4d6", highlightthickness=0, cursor="hand2")
        canvas.create_rectangle(0, 0, 60, 26, fill="#f38c9f", outline="#f38c9f", width=2)
        canvas.create_text(30, 13, text="BACK", fill="white", font=self.back_font)
        canvas.bind("<Button-1>", self.on_back_clicked)
        return canvas

    def create_cancel_button(self, container):
        canvas = Canvas(container, width=80, height=26, bg="#ffc4d6", highlightthickness=0, cursor="hand2")
        canvas.create_rectangle(0, 0, 80, 26, fill="white", outline="white", width=2)
        canvas.create_text(40, 13, text="CANCEL", fill="#f38c9f", font=self.cancel_font)
        canvas.bind("<Button-1>", self.on_cancel_clicked)
        return canvas

    def on_back_clicked(self, event):
        # [Changed] Goes back to BookingPage instead of HomePage
        if hasattr(self.parent, "show_booking_page"):
            self.parent.show_booking_page(self.pickup_location, self.dropoff_location)

    def on_cancel_clicked(self, event):
        # [Added] Goes back to HomePage on cancel
        if hasattr(self.parent, "show_home_page"):
            self.parent.show_home_page()

    def load_static_map(self):
        map_url = self.backend.generate_static_map_url(self.pickup_location, self.dropoff_location, use_polyline=True)
        if map_url:
            try:
                with urlopen(map_url) as response:
                    img_data = BytesIO(response.read())
                    img = Image.open(img_data)
                    self.map_photo = ImageTk.PhotoImage(img)
                    self.map_img_label.config(image=self.map_photo)
            except Exception as e:
                print(f"Map image error: {e}")
                self.map_img_label.config(text="Map unavailable", fg="white", font=self.booking_info_font)

    # [Added] Calls backend methods to fill in booking ID, ride duration, and distance
    def populate_backend_info(self):
        booking_id = self.backend.generate_booking_id()
        duration = self.backend.get_estimated_duration(self.pickup_location, self.dropoff_location)
        distance = self.backend.get_distance_km(self.pickup_location, self.dropoff_location)

        self.booking_id_label.config(text=booking_id)
        self.duration_label.config(text=duration)
        self.distance_value.config(text=f"{distance:.2f} km")
