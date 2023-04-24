import cv2
import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from modified_color_filters import rgb_to_lms, filter_options

# Camera Feed class
class Camera_Feed:
    def __init__(self, video_source=0):
        # Video Feed Capture
        self.cap = cv2.VideoCapture(video_source)
        # set Video Frame Width
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        # set Video Fram Height
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.root = tk.Tk()
        self.root.title("Color Blindness Simulator")
        # Create GUI to hold Video Feed
        self.init_gui()
        # Video Filter Options Menu
        self.filter = filter_options[self.filter_var.get()]
        self.update()
     
     # Create canvas to hold Video Feed
    def init_gui(self):
        # Define color scheme
        bg_color = "springgreen"
        fg_color = "maroon"
        active_bg_color = "maroon"
        active_fg_color = "maroon"

        # Create main container frame
        main_frame = tk.Frame(self.root, bg=bg_color)
        main_frame.pack(fill="both", expand=True)

        # Create canvas to hold Video Feed
        canvas_frame = tk.Frame(main_frame, bg=bg_color)
        canvas_frame.pack(side="top", padx=10, pady=10)
        self.canvas = tk.Canvas(canvas_frame, width=640, height=480)
        self.canvas.pack()

        # Create filter options menu
        filter_frame = tk.Frame(main_frame, bg=bg_color)
        filter_frame.pack(side="left", fill="y", padx=10)
        filter_label = tk.Label(filter_frame, text="Filter Options", font=("Times", 20), fg=fg_color, bg=bg_color)
        filter_label.pack(side="top", pady=10)
        self.filter_var = tk.StringVar(value=list(filter_options.keys())[0])
        self.filter_menu = tk.OptionMenu(filter_frame, self.filter_var, *filter_options.keys(), command=self.update_filter)
        self.filter_menu.config(bg=bg_color, fg=fg_color, activebackground=active_bg_color, activeforeground=active_fg_color)
        self.filter_menu.pack(side="top", pady=10)

        # Create quit button
        self.quit_button = tk.Button(main_frame, text="Quit", font=("Times", 15), bg=bg_color, fg=active_fg_color, command=self.quit)
        self.quit_button.pack(side="bottom", pady=10)

    # Update Method
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

    # Update Filter Method
    def update_filter(self, value):
        # When a new filter is selected, move to this filter option
        self.filter = filter_options[value]
    
    # End Video Feed & GUI when selected Method
    def quit(self):
        self.cap.release()
        self.root.destroy()

### Main Program ###
if __name__ == "__main__":
    player = Camera_Feed()
    player.root.mainloop()
