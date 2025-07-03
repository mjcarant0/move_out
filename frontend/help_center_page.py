"""
Help Center – FAQ UI for the MOVE OUT application using Tkinter.

This module defines the HelpCenterPage class, which provides a
searchable list of FAQs with expandable answers
"""

import os

from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk

from backend.backend_faq import search_faqs


class FAQItem(Frame):
    def __init__(self, parent, question, answer, q_font, a_font):
        super().__init__(parent, bg="#ffc4d6")
        self.is_expanded = False

        self.question_button = Button(
            self,
            text=question,
            font=q_font,
            bg="#f38c9f",
            fg="white",
            anchor="w",
            command=self.toggle,
            relief=FLAT,
            padx=10,
            wraplength=320,
            justify="left"
        )
        self.question_button.pack(fill="x", pady=(5, 0), ipady=10)

        self.answer_label = Label(
            self,
            text=answer,
            font=a_font,
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

    @staticmethod
    def clear_placeholder(entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, END)
            entry.config(fg="black")

    @staticmethod
    def restore_placeholder(entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="#BDBDBD")


class HelpCenterPage(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ffc4d6")
        self.parent = parent  # ✅ Added this line to fix AttributeError

        self.title_font = Font(family="Poppins", size=30, weight="bold")
        self.subheading_font = Font(family="League Spartan", size=15, weight="bold")
        self.question_font = Font(family="Montserrat", size=12, weight="bold")
        self.answer_font = Font(family="Montserrat", size=10)

        self.pack(fill=BOTH, expand=True)

        # Load back icon
        image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'media', 'back-button.png'))
        arrow_img = Image.open(image_path).resize((32, 32), Image.Resampling.LANCZOS)
        self.back_icon = ImageTk.PhotoImage(arrow_img)

        # Back button at top-left
        icon_label = Label(self, image=self.back_icon, bg="#ffc4d6", cursor="hand2")
        icon_label.place(x=15, y=45)
        icon_label.bind("<Button-1>", lambda e: self.parent.show_home_page())  # Replace with actual navigation later

        # Title centered
        title_label = Label(
            self,
            text="HELP CENTER",
            font=self.title_font,
            fg="#f38c9f",
            bg="#ffc4d6"
        )
        title_label.pack(pady=(30, 10))

        # White box container
        white_box = Frame(self, bg="white", width=390, height=100)
        white_box.pack(pady=(0, 0))
        white_box.pack_propagate(False)

        Label(white_box, text="HOW CAN WE HELP YOU TODAY?",
              font=self.subheading_font, fg="#ffc4d6", bg="white").pack(pady=5)

        # Search bar
        search_frame = Frame(white_box, bg="#BDBDBD", highlightbackground="#BDBDBD", highlightthickness=1)
        search_frame.pack(pady=10, fill=X, padx=20)

        self.search_var = StringVar()
        search_entry = Entry(search_frame, textvariable=self.search_var, font=self.question_font,
                             fg="#BDBDBD", bg="white", relief=FLAT)
        search_entry.pack(fill=X, ipady=5)
        search_entry.insert(0, "Search...")
        search_entry.bind("<FocusIn>", lambda e: FAQItem.clear_placeholder(search_entry, "Search..."))
        search_entry.bind("<FocusOut>", lambda e: FAQItem.restore_placeholder(search_entry, "Search..."))
        search_entry.bind("<Return>", lambda e: self.display_faqs(self.search_var.get().strip()))

        # Scrollable canvas
        canvas_frame = Frame(self, bg="#ffc4d6")
        canvas_frame.pack(fill=BOTH, expand=True)

        self.canvas = Canvas(canvas_frame, bg="#ffc4d6", highlightthickness=0, width=390)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.faq_frame = Frame(self.canvas, bg="#ffc4d6")
        self.faq_window = self.canvas.create_window((0, 0), window=self.faq_frame, anchor="nw", width=390)

        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.faq_window, width=e.width))
        self.faq_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Scroll events
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))
        self.canvas.bind_all("<Button-4>", lambda e: self.canvas.yview_scroll(-1, "units"))  
        self.canvas.bind_all("<Button-5>", lambda e: self.canvas.yview_scroll(1, "units"))   

        self.display_faqs("")

    def display_faqs(self, keyword=""):
        for widget in self.faq_frame.winfo_children():
            widget.destroy()

        faqs = search_faqs(keyword)

        if not faqs:
            Label(self.faq_frame, text="No results found.",
                  font=self.question_font, bg="#ffc4d6").pack(pady=20, fill="x")
            return

        for q, a in faqs:
            item = FAQItem(self.faq_frame, q, a, self.question_font, self.answer_font)
            item.pack(fill="x", padx=20, pady=2)