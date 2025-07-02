'''
        This module provides the splash animation for Move Out.
        It will display a gif in the splash screen.
'''

import os
from tkinter import *
from PIL import Image, ImageTk

class Animation(Frame):
    def __init__(self, parent, callback=None):
        super().__init__(parent)
        self.callback = callback

        self.pack(fill=BOTH, expand=True)

        # Relative path to the GIF
        current_dir = os.path.dirname(__file__)
        media_dir = os.path.join(current_dir, '..', 'media')
        gif_path = os.path.join(media_dir, 'splash-animation.gif')  

        try:
            # Load the GIF
            self.gif_image = Image.open(gif_path)
            self.frames = []
            self.frame_durations = []
            for i in range(self.gif_image.n_frames):
                self.gif_image.seek(i)
                self.frames.append(ImageTk.PhotoImage(self.gif_image.copy()))
                self.frame_durations.append(self.gif_image.info['duration'])
        except Exception as e:
            print(f"Error loading GIF: {e}")

        self.gif_label = Label(self)
        self.gif_label.pack(fill=BOTH, expand=True)

        # Play the GIF once when the program starts
        self.play_gif()

    def play_gif(self):
        """ Display the GIF once when the page loads. """
        frame_idx = 0

        def update_frame():
            nonlocal frame_idx
            self.gif_label.config(image=self.frames[frame_idx])
            next_duration = self.frame_durations[frame_idx] 
            frame_idx += 1
            if frame_idx < len(self.frames):
                self.after(next_duration, update_frame) 
            else:
                if self.callback:
                    self.callback()

        # Start the animation
        update_frame()
