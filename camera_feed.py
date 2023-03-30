# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:20:32 2023

@author: shane
"""

import cv2
import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from color_filters import rgb_to_lms, filter_options

class Camera_Feed:
    def __init__(self, video_source=0):
        self.cap = cv2.VideoCapture(video_source)
        self.root = tk.Tk()
        self.root.title("Color Blindness Simulator")
        self.init_gui()
        self.filter = filter_options[self.filter_var.get()]
        self.update()

    def init_gui(self):
        self.canvas = tk.Canvas(self.root, width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        self.filter_var = tk.StringVar(value=list(filter_options.keys())[0])
        self.filter_menu = tk.OptionMenu(self.root, self.filter_var, *filter_options.keys(), command=self.update_filter)
        self.filter_menu.pack()
        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit)
        self.quit_button.pack()

    def update(self):
        ret, frame = self.cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            mean = np.mean(gray)
            gamma = np.log10(0.5) / np.log10(mean / 255.0)
            gamma_table = (np.array([((i / 255.0) ** gamma) * 255
                                     for i in np.arange(0, 256)]).astype("uint8"))
            frame = cv2.LUT(frame, gamma_table)
            lms_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            lms_frame = cv2.transform(lms_frame, rgb_to_lms)

            lms_frame = cv2.transform(lms_frame, self.filter)

            lms_to_rgb = np.linalg.inv(rgb_to_lms)
            transformed_frame = cv2.transform(lms_frame, lms_to_rgb)

            self.photo = ImageTk.PhotoImage(image=Image.fromarray(transformed_frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.root.after(15, self.update)

    def update_filter(self, value):
        self.filter = filter_options[value]

    def quit(self):
        self.cap.release()
        self.root.destroy()

if __name__ == "__main__":
    player = Camera_Feed()
    player.root.mainloop()
