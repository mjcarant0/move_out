from tkinter import *
import tkinter.font as Font

class PendingView(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#FFE5EC")

class CompletedView(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#FFE5EC")

class CanceledView(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#FFE5EC")


class RideStatusPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="white")

        self.title_font = Font.Font(family="Poppins", size=20, weight="bold")
        self.tab_font = Font.Font(family="Montserrat", size=12, weight="bold")
        self.placeholder_font = Font.Font(family="Montserrat", size=9)

        # Header
        pink_div = Frame(self, bg="#ffc4d6", width=390, height=118)
        pink_div.pack(fill=X)
        pink_div.pack_propagate(False)
        Label(pink_div, text="RIDE STATUS", font=self.title_font, bg="#ffc4d6", fg="white").place(relx=0.5, rely=0.6, anchor="center")

        # Tab buttons
        self.create_tab_buttons()

        # Content Frame
        self.content_frame = Frame(self, bg="#FFE5EC", width=367, height=203)
        self.content_frame.place(relx=0.5, y=197, anchor="n")
        self.content_frame.pack_propagate(False)

        # Cancel Button
        cancel_button = Frame(self, bg="#FFC4D6", width=367, height=17, cursor="hand2")
        cancel_button.place(relx=0.5, y=455, anchor="n")
        cancel_button.pack_propagate(False)
        Label(cancel_button, text="CANCEL", bg="#FFC4D6", fg="black", font=("Montserrat", 7, "bold")).pack()

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
        # Tabs background bar
        tab_bar = Frame(self, bg="#FB6F92", width=367, height=55)
        tab_bar.place(relx=0.5, y=400, anchor="n")
        tab_bar.pack_propagate(False)

        # Buttons
        Button(self, text="PENDING", bg="#FB6F92", fg="white", font=self.tab_font,
               bd=0, activebackground="#fba4bd", command=self.show_pending).place(relx=0.18, y=135, anchor="n", width=111, height=27)

        Button(self, text="COMPLETED", bg="#FB6F92", fg="white", font=self.tab_font,
               bd=0, activebackground="#fba4bd", command=self.show_completed).place(relx=0.5, y=135, anchor="n", width=111, height=27)

        Button(self, text="CANCELED", bg="#FB6F92", fg="white", font=self.tab_font,
               bd=0, activebackground="#fba4bd", command=self.show_canceled).place(relx=0.82, y=135, anchor="n", width=111, height=27)

    def show_pending(self):
        self._clear_content()
        PendingView(self.content_frame).pack(fill=BOTH, expand=True)

    def show_completed(self):
        self._clear_content()
        CompletedView(self.content_frame).pack(fill=BOTH, expand=True)

    def show_canceled(self):
        self._clear_content()
        CanceledView(self.content_frame).pack(fill=BOTH, expand=True)

    def _clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def go_home(self):
        if hasattr(self.parent, "show_home_page"):
            self.parent.show_home_page()

    def go_ride_status(self):
        if hasattr(self.parent, "show_ride_status_page"):
            self.parent.show_ride_status_page()

    def go_profile(self):
        if hasattr(self.parent, "show_account_page"):
            self.parent.show_account_page()