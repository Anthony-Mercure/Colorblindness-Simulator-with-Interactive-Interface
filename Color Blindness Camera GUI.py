import cv2
import tkinter as tk
from PIL import Image, ImageTk

class Camera_Feed:
    def __init__(self, video_source=0):
        self.cap = cv2.VideoCapture(video_source)
        self.root = tk.Tk()
        self.root.title("Color Blindness Simulator")

        # GUI Filter Options
        self.canvas = tk.Canvas(self.root, width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        self.filter_options = ["Normal", "Protanopia", "Deutanopia", "Tritanopia"]
        self.filter_var = tk.StringVar(value=self.filter_options[0])
        self.filter_menu = tk.OptionMenu(self.root, self.filter_var, *self.filter_options, command=self.update_filter)
        self.filter_menu.pack()
        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit)
        self.quit_button.pack()

        # Video Filters
        self.protanopia_filter = None # insert filter options
        self.deutanopia_filter = None # insert filter options
        self.tritanopia_filter = None # insert filter options
        self.filter = None

        # Start the video feed
        self.update()

    def update(self):
        ret, frame = self.cap.read()
        if ret:
            if self.filter is not None:
                frame = cv2.transform(frame, self.filter)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.root.after(15, self.update)

    def update_filter(self, value):
        if value == self.filter_options[1]:
            self.filter = self.protanopia_filter
        elif value == self.filter_options[2]:
            self.filter = self.deutanopia_filter
        elif value == self.filter_options[3]:
            self.filter = self.tritanopia_filter
        else:
            self.filter = None

    def quit(self):
        self.cap.release()
        self.root.destroy()

# create the window
if __name__ == "__main__":
    player = Camera_Feed()
    player.root.mainloop()