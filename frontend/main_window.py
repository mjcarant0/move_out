import os
from PIL import Image, ImageTk
import ttkbootstrap as tb
from home_page import launch_homepage

# Set working directory to current file
os.chdir(os.path.abspath(os.path.dirname(__file__)))

# Create themed window with fixed phone-like size and soft pink background
window = tb.Window(themename="vapor")
window.geometry("390x844")
window.title("Move Out")
window.configure(bg="#ffe6f0")

# Logo image
try:
    logo = Image.open(os.path.join("media", "logo.png"))
    logo = logo.resize((50, 100)) 
    logo_img = ImageTk.PhotoImage(logo)
    window.iconphoto(True, logo_img)
except Exception as e:
    print(f"Error loading logo: {e}")

# Launch homepage content
launch_homepage(window)

# Start the app loop
window.mainloop()