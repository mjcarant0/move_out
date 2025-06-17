import tkinter as tk

def create_rounded_button(parent, text, command=None, bg="#ffffff", fg="#000000", parent_bg=None):
    # Create a frame to contain the canvas (this helps isolate the button)
    frame = tk.Frame(parent, bg=parent_bg or parent["bg"], highlightthickness=0, bd=0)
    frame.pack(pady=15)
    
    # Create canvas with complete isolation
    canvas = tk.Canvas(frame, width=260, height=50,
                      bg=parent_bg or parent["bg"],
                      highlightthickness=0,
                      bd=0,
                      takefocus=0,
                      selectborderwidth=0,
                      relief='flat')
    
    canvas.pack()

    radius = 25
    x0, y0, x1, y1 = 5, 5, 255, 45

    # Create button background
    button_id = canvas.create_rounded_rect(x0, y0, x1, y1, radius, fill=bg, outline=bg)
    
    # Text
    text_id = canvas.create_text(130, 25, text=text, fill=fg, 
                               font=("Helvetica", 12, "bold"))

    # Click handler
    def on_click(event):
        # Flash effect (optional)
        canvas.itemconfig(button_id, fill=bg)  # Keep original color or use a darker shade
        if command: 
            command()

    # Bind events
    canvas.bind("<Button-1>", on_click)
    canvas.tag_bind(text_id, "<Button-1>", on_click)

    return frame

# Helper function to create rounded rectangle
def create_rounded_rect(self, x1, y1, x2, y2, r=25, **kwargs):
    points = [
        x1+r, y1,
        x2-r, y1,
        x2, y1,
        x2, y1+r,
        x2, y2-r,
        x2, y2,
        x2-r, y2,
        x1+r, y2,
        x1, y2,
        x1, y2-r,
        x1, y1+r,
        x1, y1,
        x1+r, y1
    ]
    return self.create_polygon(points, **kwargs, smooth=True)

# Add the method to Canvas class
tk.Canvas.create_rounded_rect = create_rounded_rect