import random
import tkinter as tk
import os

class Mywindow(tk.Tk):
    def __init__(self):
        super().__init__()
        # Set the window fixed size
        self.geometry("800x800")
        self.resizable(False,False)

        # Set the window title
        self.title("OGOXE IoT Manager")

        # Path to the icon starting from the project directory
        icon_path = os.path.join("Icons", "Goute.ico")
        # Set the window icon
        self.iconbitmap(icon_path)