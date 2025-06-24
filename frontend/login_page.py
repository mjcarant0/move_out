from tkinter import *
from tkinter.font import Font

class LoginPage(Frame):
     def __init__(self, parent):
          super().__init__(parent, bg="#ffc4d6")
          self.parent = parent

          # Adjusted fonts for smaller layout
          self.title_font = Font(family="Poppins", size=20, weight="bold")
          self.welcome_font = Font(family="League spartan", size=9, weight="bold")
          self.login_font = Font(family="League spartan", size=45, weight="bold")
          self.phone_font = Font(family="Montserrat", size=9)

               # MOVE OUT Title
          Label(self, text="MOVE OUT", font=self.title_font, bg="#ffc4d6", fg="white").pack(pady=(80, 40))

               # White box (larger and lower)
          white_box = Frame(self, bg="white", width=300, height=370)
          white_box.pack(pady=(20, 0))
          white_box.pack_propagate(False)

               # Welcome Back + LOG IN
          Label(white_box, text="Welcome Back!", font=self.welcome_font, fg="#ff99b8", bg="white").pack(pady=(30, 0))
          Label(white_box, text="LOG IN", font=self.login_font, fg="#ff99b8", bg="white").pack(pady=(0, 25))

               # Phone input field
          phone_frame = Frame(white_box, bg="white")
          phone_frame.pack(pady=(30, 10), padx=15, fill=X)

          Label(phone_frame, text="🇵🇭 +63", bg="white", font=self.phone_font).pack(side=LEFT)
          Entry(phone_frame, font=self.phone_font, bd=1, relief=SOLID, width=18).pack(
               side=LEFT, fill=X, expand=True, padx=(8, 0), ipady=4)

               # Canvas login button
          self.create_login_button(white_box).pack(pady=(20, 20))

               # Add line separator
          line = Frame(white_box, bg="#ffc4d6", height=1, width=270)
          line.pack(pady=(10, 10))

               # Dont have an account yet
          Label(white_box, text="Don't have an account yet?", font=self.welcome_font, fg="#ff99b8", bg="white").pack(pady=(10, 0))

               # Canvas login button
          self.create_signup_button(white_box).pack(pady=(10, 20))

     def create_login_button(self, parent):
          canvas = Canvas(
               parent,
               width=156,
               height=26,
               bg="#ffc4d6",
               highlightthickness=0,
               cursor="hand2"
          )
          canvas.create_rectangle(0, 0, 156, 26, fill="#f38c9f", outline="#f38c9f", width=1)
          canvas.create_text(78, 13, text="LOG IN", fill="white", font=("League Spartan", 10, "bold"))
          return canvas
     
     def create_signup_button(self, parent):
          canvas = Canvas(
               parent,
               width=156,
               height=26,
               bg="#ffc4d6",
               highlightthickness=0,
               cursor="hand2"
          )
          canvas.create_rectangle(0, 0, 156, 26, fill="#ffffff", outline="#f38c9f", width=1)
          canvas.create_text(78, 13, text="SIGN UP", fill="white", font=("League Spartan", 10, "bold"))
          return canvas

# Smaller main window
root = Tk()
root.title("Move Out App")
root.geometry("320x600")
root.configure(bg="#ffc4d6")
root.resizable(False, False)

login_page = LoginPage(root)
login_page.pack(fill=BOTH, expand=True)

root.mainloop()