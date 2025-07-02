import sys
import os
import tkinter.font as Font

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import *
from PIL import Image, ImageTk
from backend.ride_booking import RideBackend
from urllib.request import urlopen
from io import BytesIO

class BookingPage(Frame):
    '''
        This program provides the booking page for Move Out.
        It allows the user to book their chosen ride
        and see the pinned locations in the map.
    '''
    def __init__(self, parent, pickup_location, dropoff_location):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="white")

        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location

        # Fonts
        self.location_font = Font.Font(family="Montserrat", size=11, weight="bold")
        self.distance_font = Font.Font(family="Montserrat", size=10, weight="bold")
        self.selection_font = Font.Font(family="Montserrat", size=10)
        self.price_label_font = Font.Font(family="Montserrat", size=15, weight="bold")
        self.price_font = Font.Font(family="Montserrat", size=15)
        self.back_font = Font.Font(family="League Spartan", size=12, weight="bold")
        self.confirm_font = Font.Font(family="League Spartan", size=12, weight="bold")

        # Back Button Container
        back_con = Frame(self, bg="#ffc4d6", width=390, height=50)
        back_con.pack(padx=0, pady=0, fill=X)
        back_con.pack_propagate(False)
        self.create_back_button(back_con).place(x=10, y=12)

        # Map Container
        self.map_frame = Frame(self, width=390, height=350, bg="gray")
        self.map_frame.pack(pady=0)
        self.map_frame.pack_propagate(False)

        # Map Image
        self.map_img_label = Label(self.map_frame, bg="gray")
        self.map_img_label.pack(expand=True)

        # Option Container
        self.options_frame = Frame(self, width=390, height=350, bg="white")
        self.options_frame.pack(pady=0)
        self.options_frame.pack_propagate(False)

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
        info_row = Frame(self.options_frame, bg="white")
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
        distance_container = Frame(self.options_frame, bg="white", width=350, height=20)
        distance_container.pack(pady=(5, 0))
        Label(distance_container, text="Distance", font=self.distance_font, fg="#8f8f8f", bg="white").place(x=5)
        self.distance_value = Label(distance_container, text="--", font=self.distance_font, fg="#8f8f8f", bg="white")
        self.distance_value.place(x=300)

        # Vehicle Selection Container
        vehicle_section = Frame(self.options_frame, bg="white")
        vehicle_section.pack(fill="x", padx=30, pady=(10, 0))

        self.vehicle_data = [
            ("Motorcycle", os.path.join(base_path, "..", "media", "motor.png")),
            ("4-seater", os.path.join(base_path, "..", "media", "4seater.png")),
            ("6-seater", os.path.join(base_path, "..", "media", "6seater.png"))
        ]

        self.vehicle_imgs = []
        for label_text, image_path in self.vehicle_data:
            try:
                image = Image.open(image_path).resize((40, 40), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                self.vehicle_imgs.append(photo)
                self.create_vehicle_row(vehicle_section, label_text, photo)
            except Exception as e:
                print(f"Error loading image {image_path}: {e}")

        # Price Container
        price_container = Frame(self.options_frame, bg="white", width=350, height=25)
        price_container.pack(pady=(5, 0))
        Label(price_container, text="Price", font=self.price_label_font, fg="black", bg="white").place(x=5)
        self.price_value = Label(price_container, text="\u20b1 000.00", font=self.price_font, fg="black", bg="white")
        self.price_value.place(x=275)

        # Confirm Button Container
        confirm_con = Frame(self, bg="#ff8fab", width=390, height=50)
        confirm_con.place(y=734)
        confirm_con.pack_propagate(False)
        self.create_confirm_button(confirm_con).place(x=300, y=12)

        self.after(100, self.load_static_map)

    # Row and Column for proper image and text alignment (Vehicle Selection)
    def create_vehicle_row(self, parent, label, image):
        row = Frame(parent, bg="white", cursor="hand2")
        row.pack(fill="x", pady=5)
        row.bind("<Button-1>", lambda e, v=label: self.select_vehicle(v))

        Label(row, image=image, bg="white").pack(side="left")
        label_text = Label(row, text=label, font=self.selection_font, fg="#8f8f8f", bg="white")
        label_text.pack(side="left", padx=15)
        price = Label(row, text="\u20b1 000.00", font=self.selection_font, fg="#8f8f8f", bg="white")
        price.pack(side="right")

        label_text.bind("<Button-1>", lambda e, v=label: self.select_vehicle(v))
        price.bind("<Button-1>", lambda e, v=label: self.select_vehicle(v))

        if not hasattr(self, 'vehicle_widgets'):
            self.vehicle_widgets = {}
        self.vehicle_widgets[label] = (label_text, price)

    # Selecting a Vehicle
    def select_vehicle(self, vehicle_name):
        self.selected_vehicle = vehicle_name
        for label_text, price_label in self.vehicle_widgets.values():
            label_text.config(fg="#8f8f8f")
            price_label.config(fg="#8f8f8f")
        if vehicle_name in self.vehicle_widgets:
            self.vehicle_widgets[vehicle_name][0].config(fg="black")
            self.vehicle_widgets[vehicle_name][1].config(fg="black")

    def create_back_button(self, back_con):
        canvas = Canvas(back_con, width=60, height=26, bg="#ffc4d6", highlightthickness=0, cursor="hand2")
        canvas.create_rectangle(0, 0, 60, 26, fill="#f38c9f", outline="#f38c9f", width=2)
        canvas.create_text(30, 13, text="BACK", fill="white", font=self.back_font, anchor="center")
        canvas.bind("<Button-1>", self.on_back_clicked)
        return canvas

    def create_confirm_button(self, confirm_con):
        canvas = Canvas(confirm_con, width=80, height=26, bg="#ffc4d6", highlightthickness=0, cursor="hand2")
        canvas.create_rectangle(0, 0, 80, 26, fill="white", outline="white", width=2)
        canvas.create_text(40, 13, text="CONFIRM", fill="#f38c9f", font=self.confirm_font, anchor="center")
        canvas.bind("<Button-1>", self.on_confirm_clicked)
        return canvas

    def on_back_clicked(self, event):
        if hasattr(self.parent, "show_home_page"):
            self.parent.show_home_page()

    def on_confirm_clicked(self, event):
        if hasattr(self, 'selected_vehicle'):
            vehicle = self.selected_vehicle
            price = self.price_value.cget("text")
            if hasattr(self.parent, "show_looking_page"):
                self.parent.show_looking_page(self.pickup_location, self.dropoff_location, vehicle, price)
        else:
            self.show_vehicle_warning()

    def show_vehicle_warning(self):
        # If already exists, just raise it
        if hasattr(self, 'warning_label') and self.warning_label.winfo_exists():
            self.warning_label.lift()
        else:
            self.warning_label = Label(self.options_frame, text="Please select a vehicle before confirming.",
                                    font=self.selection_font, fg="red", bg="white")
            self.warning_label.pack(pady=(5, 0))

    # Load Static Map Image using Google Maps API
    def load_static_map(self):
        backend = RideBackend("AIzaSyAOKrot0gO67ji8DpUmxN3FdXRBfMsCvRQ")
        map_url = backend.generate_static_map_url(self.pickup_location, self.dropoff_location, use_polyline=True)
        if map_url:
            try:
                with urlopen(map_url) as response:
                    img_data = BytesIO(response.read())
                    img = Image.open(img_data)
                    self.map_photo = ImageTk.PhotoImage(img)
                    self.map_img_label.config(image=self.map_photo)
            except Exception as e:
                print(f"Map image load error: {e}")
                self.map_img_label.config(text="Map not available", fg="white", font=self.distance_font)
        else:
            self.map_img_label.config(text="Map not available", fg="white", font=self.distance_font)
