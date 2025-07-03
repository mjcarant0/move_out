from tkinter import *
import tkinter.font as Font
from PIL import Image, ImageTk
import os

class CanceledView(Frame):
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

        # Widgets will be created in .populate_data()
    
    def populate_data(self, pickup, dropoff, vehicle, price):
        # Outer pink box
        lpink_box = Frame(self, bg="#FFE5EC", width=367, height=230)
        lpink_box.pack(pady=(0, 0))
        lpink_box.pack_propagate(False)

        tag_label = Label(lpink_box, text="CANCELED", bg="#FB6F92", fg="white",
                        font=self.tag_font, padx=8, pady=2)
        tag_label.pack(anchor="w", padx=10, pady=(8, 0))

        # Pickup
        pickup_frame = Frame(lpink_box, bg="#FFE5EC")
        pickup_frame.pack(anchor="w", padx=10, pady=(10, 0))

        Label(pickup_frame, image=self.pickup_img, bg="#FFE5EC").pack(side=LEFT, padx=(0, 5))
        Label(pickup_frame, text="Pickup Location", bg="#FFE5EC", fg="black",
            font=self.label_font).pack(side=LEFT)

        Label(lpink_box, text=pickup, wraplength=300, justify=LEFT,
            bg="#FFE5EC", font=self.placeholder_font).pack(anchor="w", padx=35, pady=(5, 10))

        # Drop-off
        dropoff_frame = Frame(lpink_box, bg="#FFE5EC")
        dropoff_frame.pack(anchor="w", padx=10, pady=(5, 0))

        Label(dropoff_frame, image=self.dropoff_img, bg="#FFE5EC").pack(side=LEFT, padx=(0, 5))
        Label(dropoff_frame, text="Drop-off Location", bg="#FFE5EC", fg="black",
            font=self.label_font).pack(side=LEFT)

        Label(lpink_box, text=dropoff, wraplength=300, justify=LEFT,
            bg="#FFE5EC", font=self.placeholder_font).pack(anchor="w", padx=35, pady=(5, 10))

        # Bottom for vehicle and price
        dpink_box = Frame(self, bg="#FB6F92", width=367, height=55)
        dpink_box.pack(pady=(0, 10))
        dpink_box.pack_propagate(False)

        label_section = Frame(dpink_box, bg="#FB6F92")
        label_section.pack(side=LEFT, padx=10, anchor="w")
        Label(label_section, text="Vehicle", bg="#FB6F92", fg="black", font=self.placeholder_font).pack(anchor="w")
        Label(label_section, text="Price", bg="#FB6F92", fg="black", font=self.placeholder_font).pack(anchor="w")

        value_section = Frame(dpink_box, bg="#FB6F92")
        value_section.pack(side=RIGHT, padx=10, anchor="e")
        Label(value_section, text=vehicle, bg="#FB6F92", fg="black", font=self.placeholder_font).pack(anchor="e")
        Label(value_section, text=price, bg="#FB6F92", fg="black", font=self.placeholder_font).pack(anchor="e")
