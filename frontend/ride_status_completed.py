from tkinter import *
import tkinter.font as Font
from PIL import Image, ImageTk
import os

class CompletedView(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="white")

        self.label_font = Font.Font(family="Montserrat", size=12, weight="bold")
        self.placeholder_font = Font.Font(family="Montserrat", size=9)
        self.tag_font = Font.Font(family="Montserrat", size=9, weight="bold")

        # Load icons
        base_path = os.path.dirname(__file__)
        pickup_path = os.path.join(base_path, "..", "media", "pickup.png")
        dropoff_path = os.path.join(base_path, "..", "media", "dropoff.png")

        self.pickup_img = ImageTk.PhotoImage(Image.open(pickup_path).resize((18, 18)))
        self.dropoff_img = ImageTk.PhotoImage(Image.open(dropoff_path).resize((18, 18)))

        # Outer pink box
        self.lpink_box = Frame(self, bg="#FFE5EC", width=367, height=230)
        self.lpink_box.pack(pady=(0, 0))
        self.lpink_box.pack_propagate(False)

        self.tag_label = Label(self.lpink_box, text="COMPLETED", bg="#FB6F92", fg="white", font=self.tag_font, padx=8, pady=2)
        self.tag_label.pack(anchor="w", padx=10, pady=(8, 0))

        # Pickup
        self.pickup_frame = Frame(self.lpink_box, bg="#FFE5EC")
        self.pickup_frame.pack(anchor="w", padx=10, pady=(10, 0))
        Label(self.pickup_frame, image=self.pickup_img, bg="#FFE5EC").pack(side=LEFT, padx=(0, 5))
        Label(self.pickup_frame, text="Pickup Location", bg="#FFE5EC", fg="black", font=self.label_font).pack(side=LEFT)

        self.pickup_label = Label(self.lpink_box, wraplength=300, justify=LEFT, bg="#FFE5EC", font=self.placeholder_font)
        self.pickup_label.pack(anchor="w", padx=35, pady=(5, 10))

        # Drop-off
        self.dropoff_frame = Frame(self.lpink_box, bg="#FFE5EC")
        self.dropoff_frame.pack(anchor="w", padx=10, pady=(5, 0))
        Label(self.dropoff_frame, image=self.dropoff_img, bg="#FFE5EC").pack(side=LEFT, padx=(0, 5))
        Label(self.dropoff_frame, text="Drop-off Location", bg="#FFE5EC", fg="black", font=self.label_font).pack(side=LEFT)

        self.dropoff_label = Label(self.lpink_box, wraplength=300, justify=LEFT, bg="#FFE5EC", font=self.placeholder_font)
        self.dropoff_label.pack(anchor="w", padx=35, pady=(5, 10))

        # Bottom pink box for vehicle & price
        self.dpink_box = Frame(self, bg="#FB6F92", width=367, height=55)
        self.dpink_box.pack(pady=(0, 0))
        self.dpink_box.pack_propagate(False)

        label_section = Frame(self.dpink_box, bg="#FB6F92")
        label_section.pack(side=LEFT, padx=10, anchor="w")
        Label(label_section, text="Vehicle", bg="#FB6F92", fg="black", font=self.placeholder_font).pack(anchor="w")
        Label(label_section, text="Price", bg="#FB6F92", fg="black", font=self.placeholder_font).pack(anchor="w")

        self.value_section = Frame(self.dpink_box, bg="#FB6F92")
        self.value_section.pack(side=RIGHT, padx=10, anchor="e")
        self.vehicle_label = Label(self.value_section, text="", bg="#FB6F92", fg="black", font=self.placeholder_font)
        self.vehicle_label.pack(anchor="e")
        self.price_label = Label(self.value_section, text="", bg="#FB6F92", fg="black", font=self.placeholder_font)
        self.price_label.pack(anchor="e")

    # Accepts data from the pending ride and fills the labels
    def populate_data(self, pickup, dropoff, vehicle, price):
        self.pickup_label.config(text=pickup)
        self.dropoff_label.config(text=dropoff)
        self.vehicle_label.config(text=vehicle)
        self.price_label.config(text=price)
