import time
import os
from PIL import ImageGrab
import tkinter as tk
from tkinter import messagebox

class TakeScreenshots:
    def __init__(self, master):
        self.master = master
        self.master.title("Take Screenshot Looper")
        self.master.geometry('400x300')
        # Entry widgets for user input
        tk.Label(master, text="Object File Name:").pack()
        self.mob_entry = tk.Entry(master)
        self.mob_entry.insert(0, "example")
        self.mob_entry.pack()

        tk.Label(master, text="Monitor (left, top, right, bottom):").pack()
        self.monitor_entry = tk.Entry(master)
        self.monitor_entry.insert(0, "40, 0, 800, 640")
        self.monitor_entry.pack()

        tk.Label(master, text="Display Time (seconds):").pack()
        self.display_time_entry = tk.Entry(master)
        self.display_time_entry.insert(0, "0.5")
        self.display_time_entry.pack()

        tk.Label(master, text="Initial Image Index:").pack()
        self.img_entry = tk.Entry(master)
        self.img_entry.insert(0, "0")
        self.img_entry.pack()

        tk.Label(master, text="Directory:").pack()
        self.directory_entry = tk.Entry(master)
        self.directory_entry.insert(0, "./datasets/osrs/")
        self.directory_entry.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_capture)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_capture, state=tk.DISABLED)
        self.stop_button.pack()

        self.img = 0
        self.is_capturing = False

        self.ensure_dir()

    def ensure_dir(self):
        self.directory = self.directory_entry.get()
        #print(self.directory)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def start_capture(self):
        self.status_label.config(text="Running", fg='#8fce00')
        self.master.iconify()
        time.sleep(0.2)
        self.mob = self.mob_entry.get()
        monitor_values = list(map(int, self.monitor_entry.get().split(',')))
        self.monitor = tuple(monitor_values)
        self.display_time = float(self.display_time_entry.get())
        self.img = int(self.img_entry.get())
        self.directory = self.directory_entry.get()

        self.is_capturing = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.capture_images()

    def stop_capture(self):
        self.status_label.config(text="Stopped", fg='#f44336')
        self.is_capturing = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def capture_images(self):
        while self.is_capturing:
            try:
                # grab screen
                im = ImageGrab.grab(bbox=self.monitor)
                # save image file
                im.save(os.path.join(self.directory, f'{self.mob}_{self.img}.jpg'))
                self.img += 1
                time.sleep(self.display_time)
                self.master.update()
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.is_capturing = False

if __name__ == "__main__":
    root = tk.Tk()
    app = TakeScreenshots(root)
    root.mainloop()