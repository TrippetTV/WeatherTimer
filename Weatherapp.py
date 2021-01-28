import socket
import tkinter as tk
from tkinter import font

import requests
from PIL import Image, ImageTk
import socket
import os

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button




# import gi
# gi.require_version('Gtk', '4.0')
# from gi.repository import Gtk

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(("0.0.0.0", 3000))
# sock.listen(1)
# client, addr = sock.accept()

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
    weather_key = "2e2538867f008716b765cecaa05c33cb"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "metric"}
    response = requests.get(url, params=params)
    weather_json = response.json()

    label['text'] = format_response(response.json())

    icon_name = weather_json["weather"][0]["icon"]
    open_image(icon_name)


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
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

textbox = tk.Entry(frame, font=("Courier", 12))
textbox.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=("Courier", 12), command=lambda: get_weather(textbox.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(weather, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, font=("Courier", 12), anchor="nw", justify="left", bd=4)
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

weather.mainloop()


class FirstKivy(App):
    def build(self):
        return Label(text="Hello Kivy!")
