from tkinter import *
import tkinter.font as tkFont

class FAQItem(Frame):
    def __init__(self, parent, question, answer):
        super().__init__(parent, bg="#ffc4d6")
        self.question = question
        self.answer_text = answer
        self.is_expanded = False

        self.question_button = Button(
            self, 
            text=self.question, 
            font=("Montserrat", 12), 
            bg="#f38c9f", 
            fg="white",
            anchor="w", 
            command=self.toggle,
            relief=FLAT,
            padx=10
        )
        self.question_button.pack(fill="x", pady=(5, 0))

        self.answer_label = Label(
            self, 
            text=self.answer_text, 
            font=("Montserrat", 10),
            wraplength=320, 
            justify="left", 
            bg="white", 
            fg="black",
            padx=10,
            pady=5
        )

    def toggle(self):
        if self.is_expanded:
            self.answer_label.pack_forget()
        else:
            self.answer_label.pack(fill="x", padx=10, pady=(0, 5))
        self.is_expanded = not self.is_expanded

    def clear_placeholder(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, END)

    def restore_placeholder(self, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)

# Main app
root = Tk()
root.title("Help Center - FAQ")
root.geometry("390x844")
root.config(bg="#ffc4d6")

# Main heading
heading = Label(root, text="HELP CENTER", font=('Poppins', 30, 'bold'), fg="#f38c9f", bg="#ffc4d6")
heading.pack(pady=0)

# White box container
white_box = Frame(root, bg="white", width=390, height=100)
white_box.pack(pady=(0, 0))
white_box.pack_propagate(False)

# Subheading
subheading = Label(white_box, text="HOW CAN WE HELP YOU TODAY?", font=('League spartan', 15, 'bold'), fg="#ffc4d6", bg="white")
subheading.pack(pady=5)

# Search bar
search_frame = Frame(white_box, bd=1, relief=SOLID, bg="#ffc4d6")
search_frame.pack(pady=10, fill=X, padx=20)
search_var = StringVar()
search_entry = Entry(search_frame, textvariable=search_var)
search_entry.pack(fill=X, ipady=5)
search_entry.insert(0, "Search...")
search_entry.bind("<FocusIn>", lambda e: FAQItem.clear_placeholder(None, search_entry, "Search..."))
search_entry.bind("<FocusOut>", lambda e: FAQItem.restore_placeholder(None, search_entry, "Search..."))

# FAQ Items
faq_data = [
    ("How do I look or ride?", 
     """1. It looks a little over long for
2. I don't see the original drop-off location
3. I have 70 people together
4. Choose multiple followups. Get classified or can be selected
5. Do not open your left to cover the same time
6. Your first time booked Passer will be a driver."""),
    
    ("Where can I see my ride status?", 
     """At the bottom center of the screen, tap the 'Ride Status' button.

You can view your Pending, Canceled, and Completed rides there"""),
     
    ("How do I cancel a ride I booked?", 
     """Tap the bottom center button to go to Ride Status.

In the Pending section, tap the "CANCEL" button next to the ride you want to cancel"""),
     
    ("How do I know if my ride is confirmed?", 
     """After booking, a confirmation message will appear.

You can also check Ride Status > Pending to see your current ride"""),
     
    ("Can I change my pickup or trip off after booking?", 
     """No, once a ride is confirmed, you cannot change the location.

You’ll need to cancel the ride and book again with the correct details""")
]

# Create FAQ items
for q, a in faq_data:
    item = FAQItem(root, q, a)
    item.pack(fill="x", padx=20, pady=2)

root.mainloop()