'''
    Entry point for the Move Out application.

    This script initializes and runs the main application window.
'''
from frontend.main_window import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
