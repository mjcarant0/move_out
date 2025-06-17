from button import create_rounded_button

def launch_homepage(window):
    # Set window and global options to prevent any highlights
    window.configure(bg="#ffe6f0", highlightthickness=0)
    window.option_add('*highlightThickness', 0)
    window.option_add('*highlightColor', '#ffe6f0')
    window.option_add('*highlightBackground', '#ffe6f0')
    
    # Spacer and title
    from tkinter import Label
    Label(window, bg="#ffe6f0", text="").pack(pady=10)
    Label(window, text="HELL YEA", font=("Helvetica", 20, "bold"),
          bg="#ffe6f0", fg="#cc0066").pack(pady=10)

    # Create buttons
    create_rounded_button(window, "⚙️ Settings", bg="#ccffcc", fg="#006600", parent_bg="#ffe6f0")
    create_rounded_button(window, "🚪 Exit", bg="#ffcccc", fg="#660000", parent_bg="#ffe6f0", command=window.quit)