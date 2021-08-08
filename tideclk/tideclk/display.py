import tkinter as tk

def on_escape(event=None, root=None):
    print("escaped")
    root.destroy()


def init():
    print("Initializing Display")

def run():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screeheight()

    root.attributes("-fullscreen", True)
    root.wm_attributes("-topmost", True)

    root.bind("<Escape>", on_escape)
    root.after(500000, root.destroy)

    canvas = tk.Canvas(root)
    canvas.pack(fill='both', expand=True)

    canvas.create_oval((0,0, screen_width, screen_height), fill='red', outline='')

    root.mainloop()


