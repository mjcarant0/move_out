import os
from tkinter import *
from PIL import Image, ImageTk

from .account_page import AccountPage
from .splash_animation import Animation
from .interactive_page import InteractivePage
from .login_page import LoginPage
from .signup_page import SignUpPage
from .home_page import HomePage
from .booking_page import BookingPage

class MainWindow(Tk):
    '''
    This module defines the MainWindow class for the Move Out application.
    It initializes the main Tkinter window, displays all the pages.
    '''
    def __init__(self):
        super().__init__()

        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        # Window properties 
        self.title("Move Out")
        self.geometry("390x844")
        self.resizable(False, False)

        # Logo image for window icon
        logo = Image.open(r"../media/logo.png")
        logo = logo.resize((50, 100))
        logo_img = ImageTk.PhotoImage(logo)
        self.iconphoto(True, logo_img)

        # Show animation then go to interactive page
        self.logo_animation = Animation(self, callback=self.transition_to_interactive_page)
        self.logo_animation.pack(fill=BOTH, expand=True)

    def clear_current_page(self):
        # Hide all packed widgets (previous pages)
        for widget in self.winfo_children():
            widget.pack_forget()

    def transition_to_interactive_page(self):
        # Destroy the splash screen (removes the logo animation)
        self.logo_animation.destroy()

        # Show interactive page
        self.interactive_page = InteractivePage(self)
        self.interactive_page.pack(fill=BOTH, expand=True)

    def show_interactive_page(self):
        # Hide current page
        self.clear_current_page()

        # Show interactive page
        self.interactive_page = InteractivePage(self)
        self.interactive_page.pack(fill=BOTH, expand=True)

    def show_login_page(self):
        # Hide current page
        self.clear_current_page()

        # Create and show the log-in page
        self.login_page = LoginPage(self)
        self.login_page.pack(fill=BOTH, expand=True)

    def show_signup_page(self):
        # Hide current page
        self.clear_current_page()

        # Create and show the sign-up page
        self.signup_page = SignUpPage(self)
        self.signup_page.pack(fill=BOTH, expand=True)

    def show_home_page(self):
        # Hide current page
        self.clear_current_page()

        # Create and show the home page
        self.home_page = HomePage(self)
        self.home_page.pack(fill=BOTH, expand=True)

    def show_account_page(self):
        # Hide current page
        self.clear_current_page()

        # Create and show the account page
        self.account_page = AccountPage(self)
        self.account_page.pack(fill=BOTH, expand=True)

    def show_booking_page(self):
        # Hide current page
        self.clear_current_page()

        # Create and show the booking page
        self.booking_page = BookingPage(self)
        self.booking_page.pack(fill=BOTH, expand=True)
