import tkinter as tk
import os

def on_escape(event=None, root=None):
    print("escaped")
    root.destroy()


def init():
    print("Initializing Display")
    if os.environ.get('DISPLAY', '') == '':
        print('WARNING: No display found. Using :0.0')
        os.environ.__setitem__('DISPLAY', ':0.0')

def run():


    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.attributes("-fullscreen", True)
    root.wm_attributes("-topmost", True)

    root.bind("<Escape>", on_escape)
    root.after(50000, root.destroy)

    canvas = tk.Canvas(root)
    canvas.pack(fill='both', expand=True)

    canvas.create_oval((0,0, screen_width, screen_height), fill='red', outline='')

    root.mainloop()


