from tkinter import *
import tkinter.font as Font

class RideStatus(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="white")

        self.suggestions_box = None
        self.active_entry = None

        self.title_font = Font.Font(family="Poppins", size=20, weight="bold")
        self.label_font = Font.Font(family="Montserrat", size=12, weight="bold")
        self.proceed_font = Font.Font(family="League Spartan", size=10, weight="bold")
        self.placeholder_font = Font.Font(family="Montserrat", size=9)

        pink_div = Frame(self, bg="#ffc4d6", width=390, height=118)
        pink_div.pack(fill=X)
        pink_div.pack_propagate(False)

        Label(pink_div, text="RIDE STATUS", font=self.title_font, bg="#ffc4d6", fg="white").place(relx=0.5, rely=0.6, anchor="center")

        lpink_box = Frame(self, bg="#FFE5EC", width=367, height=203)
        lpink_box.place(relx=0.5, y=197, anchor="n")
        lpink_box.pack_propagate(False)

        self.warning_label = Label(lpink_box, text="", fg="red", bg="#ffe5ec", font=self.placeholder_font)
        self.warning_label.pack(pady=(10, 0))

        dpink_box = Frame(self, bg="#FB6F92", width=367, height=55)
        dpink_box.place(relx=0.5, y=400, anchor="n")
        dpink_box.pack_propagate(False)

        # Left button
        dpink_button1 = Frame(self, bg="#FB6F92", width=111, height=27)
        dpink_button1.place(relx=0.18, y=135, anchor="n")  # Left aligned
        dpink_button1.pack_propagate(False)
        
        label = Label(dpink_button1, text="PENDING", bg="#FB6F92", fg="white", font=("Montserrat", 12, "bold"))
        label.pack()

        # Middle button
        dpink_button2 = Frame(self, bg="#FB6F92", width=111, height=27)
        dpink_button2.place(relx=0.5, y=135, anchor="n")  # Center
        dpink_button2.pack_propagate(False)

        label = Label(dpink_button2, text="COMPLETED", bg="#FB6F92", fg="white", font=("Montserrat", 12, "bold"))
        label.pack()

        # Right button
        dpink_button3 = Frame(self, bg="#FB6F92", width=111, height=27)
        dpink_button3.place(relx=0.82, y=135, anchor="n")  # Right aligned
        dpink_button3.pack_propagate(False)

        label = Label(dpink_button3, text="CANCELED", bg="#FB6F92", fg="white", font=("Montserrat", 12, "bold"))
        label.pack()

        # Cancel Button
        lpink_button = Frame(self, bg="#FFC4D6", width=367, height=17, cursor="hand2")
        lpink_button.place(relx=0.5, y=455, anchor="n")
        lpink_button.pack_propagate(False)

        label = Label(lpink_button, text="CANCEL", bg="#FFC4D6", fg="black", font=("Montserrat", 7, "bold"))
        label.pack()

        lpink_button.bind("<Button-1>", lambda e: self.on_proceed_clicked())
        label.bind("<Button-1>", lambda e: self.on_proceed_clicked())

        # Navigation bar
        nav_bar = Frame(self, bg="#ffc4d6", width=390, height=65)
        nav_bar.place(y=719)
        nav_bar.pack_propagate(False)
    
        Button(nav_bar, text="🏠", font=("Arial", 20), bg="#ffc4d6", bd=0, activebackground="#ffc4d6", cursor="hand2", command=self.go_home).place(x=40, y=5)
        Button(nav_bar, text="📄", font=("Arial", 20), bg="#ffc4d6", bd=0, activebackground="#ffc4d6", cursor="hand2", command=self.go_documents).place(x=175, y=5)
        Button(nav_bar, text="👤", font=("Arial", 20), bg="#ffc4d6", bd=0, activebackground="#ffc4d6", cursor="hand2", command=self.go_profile).place(x=320, y=5)

    def go_home(self):
        print("Go Home")

    def go_documents(self):
        print("Go Documents")

    def go_profile(self):
        print("Go Profile")
