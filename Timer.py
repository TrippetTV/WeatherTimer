import tkinter as tk
from tkinter import font
import requests

timer = tk.Tk()
timer.title("Trippet's Timer")

HEIGHT = 590
WIDTH = 960

bg_color = "white"

canvas = tk.Canvas(timer, height=HEIGHT, width=WIDTH)

frame = tk.Frame(timer, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.75, anchor="n")


timer.mainloop()
