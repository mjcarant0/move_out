import os
from tkinter import *
from PIL import Image, ImageTk
import ttkbootstrap as tb

# Make the script's folder the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create the main window
window = tb.Window(themename="pink")
window.geometry("390x844")
window.title("Move Out")  # Service Name

# Set background color to light pink
window.configure(bg="#ffe6f0")  # very light pink

# Spacer
Label(window, bg="#ffe6f0", height=2).pack()

# Title Label
Label(window, text="HELL YEA", font=("Helvetica", 20, "bold"), bg="#ffe6f0", fg="#cc0066").pack(pady=10)

# Rounded Button
btn1 = tb.Button(window, text="🏠 Dashboard", bootstyle="success-outline", width=25)
btn1.pack(pady=15)
btn2 = tb.Button(window, text="⚙️ Settings", bootstyle="info-outline", width=25)
btn2.pack(pady=15)
btn3 = tb.Button(window, text="🚪 Exit", bootstyle="danger", width=25, command=window.quit)
btn3.pack(pady=15)

# Run the app
window.mainloop()