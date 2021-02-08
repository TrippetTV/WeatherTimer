import tkinter as tk
from tkinter import ttk
from tkinter import font
import threading
import time as time
import datetime
import calendar
import requests
from PIL import Image, ImageTk


# import socket
# import os


def timer():
    tmp = time.thread_time()

    currentTime = time.localtime()
    print(time.asctime(currentTime))
    print(type(currentTime))
    return


timer_t = threading.Thread(target=timer()).start()

# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.button import Button

# import gi
# gi.require_version('Gtk', '4.0')
# from gi.repository import Gtk


weather = tk.Tk()
weather.title("Trippet's Weather")

HEIGHT = 1080
WIDTH = 960


def format_response(weather_json):
    try:
        city = weather_json["name"]
        conditions = weather_json["weather"][0]["description"]
        temp = weather_json["main"]["temp"]
        final_str = "City: %s \nConditions: %s \nTemperature (°C): %s" % (city, conditions, temp)
    except:
        final_str = "There was a problem retrieving that information"
        print(weather_json)
    return final_str


# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def get_weather(city):
    try:
        weather_key = "2e2538867f008716b765cecaa05c33cb"
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"APPID": weather_key, "q": city, "units": "metric"}
        response = requests.get(url, params=params)
        weather_json = response.json()

        label['text'] = format_response(response.json())

        icon_name = weather_json["weather"][0]["icon"]
        open_image(icon_name)
    except:
        return


def open_image(icon):
    size = int(lower_frame.winfo_height() * 0.25)
    img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


bg_color = "white"

canvas = tk.Canvas(weather, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(weather, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.74, relheight=0.05, anchor="n")

textbox = tk.Entry(frame, font=("Courier", 12))
textbox.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=("Courier", 12), command=lambda: get_weather(textbox.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(weather, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, font=("Courier", 12), anchor="nw", justify="left", bd=4, bg=bg_color)
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

tiny_frame = tk.Frame(label, bg=bg_color, bd=2)
tiny_frame.place(relx=.75, rely=0.75, relwidth=.25, relheight=.25)

when = tk.StringVar
# TODO make timerbutton a combobox top right just above lower frame
timerbutton = ttk.Combobox(canvas, text="Prepare Forecast", font=("Courier", 12), textvariable=when)
timerbutton["values"] = ("Forecast in 1 hour",
                         "Forecast in 2 hours",
                         "Forecast in 3 hours",
                         "Forecast in 4 hours",
                         "Forecast in 6 hours",
                         "Forecast in 10 hours",
                         "Forecast in 12 hours",
                         "Forecast in 24 hours")

timerbutton.bind("<<ComboboxSelected>>", get_weather(textbox.get()))
timerbutton.place(relx=0.75, rely=.15, relwidth=.2, relheight=0.05, anchor="n")

weather.mainloop()

# HEADERSIZE = 10
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind((socket.gethostname(), 3000))
# sock.listen(1)
# client, addr = sock.accept()
#
# clientsocket.send(bytes("", "utf-8"))
#
# while True:
#     request = ""
#     new_request = True
#     while True:
#         request = sock.recv(16)
#         if new_request:
#             print(f"new message length{request[:HEADERSIZE]}")
#         reqlen = int(request[:HEADERSIZE])
#         new_request = False
#
#     request += request.decode("utf-8")
#
#     if len(request) - HEADERSIZE == msglen:
#         print(f"Full Message Recieved{request}")
#         get_weather()
