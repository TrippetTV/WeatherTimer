from tkinter import *
from tkinter import ttk
from tkinter import font
import threading
import time as time
import datetime
import calendar
import requests
from PIL import Image, ImageTk


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

HEIGHT = 1080
WIDTH = 960

weather = Tk()
weather.title("Trippet's Weather")

Grid.rowconfigure(weather, 0, weight=1)
Grid.columnconfigure(weather, 0, weight=1)


# Formats current forecast to make it more readable
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


# Formats the future forecast to make it more readable
def format_forecast(weather_json):
    final_str = "Weather forecast for: " + weather_json["city"]["name"] + " is\n"

    for i in weather_json["list"]:
        try:
            hour = i["dt_txt"]
            conditions = i["weather"][0]["description"]  # .get("description")
            temp = i["main"]["temp"]  # .get("temp")
            final_str += "Hour: %s \nConditions: %s \nTemperature (°C): %s \n\n" % (hour, conditions, temp)
        except:
            final_str = "There was a problem retrieving that information"
            print(weather_json)
    return final_str


# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def get_weather(city):
    # Shows lower frame and makes top frame smaller
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")
    frame.place_forget()
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")
    # API CALL
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


def get_forecast(city):
    # Shows lower frame and makes top frame smaller
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")
    frame.place_forget()
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")
    # API CALL
    try:
        weather_key = "2e2538867f008716b765cecaa05c33cb"
        url = "https://api.openweathermap.org/data/2.5/forecast"
        params = {"APPID": weather_key, "q": city, "units": "metric"}
        response = requests.get(url, params=params)
        weather_json = response.json()

        label['text'] = format_forecast(response.json())
    except:
        return


def open_image(icon):
    size = int(lower_frame.winfo_height() * 0.25)
    img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


def quick_alarm():
    # Hide label to show gridframe
    label.place_forget()
    gridframe = Frame(lower_frame)
    gridframe.pack(fill="both", expand=True)

    for i in range(2):
        Grid.rowconfigure(gridframe, i, weight=3)
        for j in range(3):
            Grid.columnconfigure(gridframe, j, weight=2)
            # Top left
            if i == 0 and j == 0:
                Button(gridframe, text="60 Min", font=("Courier", 10)).grid(row=i, column=j, sticky=NSEW)
            # Top middle
            if i == 0 and j == 1:
                Button(gridframe, text="30 Min", font=("Courier", 10)).grid(row=i, column=j, sticky=NSEW)
            # Top right
            if i == 0 and j == 2:
                Button(gridframe, text="15 Min", font=("Courier", 10)).grid(row=i, column=j, sticky=NSEW)
            # Bottom left
            if i == 1 and j == 0:
                Button(gridframe, text="10 Min", font=("Courier", 10)).grid(row=i, column=j, sticky=NSEW)
            # Bottom middle
            if i == 1 and j == 1:
                Button(gridframe, text="5 Min", font=("Courier", 10)).grid(row=i, column=j, sticky=NSEW)
            # Bottom right
            if i == 1 and j == 2:
                Button(gridframe, text="1 Min", font=("Courier", 10)).grid(row=i, column=j, sticky=NSEW)


def onFrameConfigure(canvas):
    """Reset the scroll region to encompass the inner frame"""
    canvas.configure(scrollregion=canvas.bbox("all"))


# Just because
bg_color = "white"
# The whole intended screen
canvas = Canvas(weather, height=HEIGHT, width=WIDTH)
canvas.pack()
# The top frame
frame = Frame(weather, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.74, relheight=0.15, anchor="n")
# Where you shall input city
textbox = Entry(frame, font=("Courier", 12))
textbox.bind("<FocusIn>", lambda args: textbox.delete(0, "end"))
textbox.bind("<<FocusOut>>", lambda args: textbox.delete(0, "end"), textbox.insert(0, "City Name"))
textbox.place(relwidth=1, relheight=.5)
# Button to get current forecast
button1 = Button(frame, text="Current Forecast", font=("Courier", 10), command=lambda: get_weather(textbox.get()))
button1.place(relx=0, rely=.5, relwidth=0.5, relheight=0.5, anchor="nw")
# Button to get the future forecasts 3 hours at a time
button1 = Button(frame, text="Future Forecast", font=("Courier", 10), command=lambda: get_forecast(textbox.get()))
button1.place(relx=0.5, rely=.5, relwidth=0.5, relheight=0.5, anchor="nw")

# The big lower frame initially hidden
lower_frame = Frame(weather, bg="#80c1ff", bd=10)
lower_frame.place_forget()

# # Scroll area
# scrollarea = Canvas(weather, width=WIDTH, height=HEIGHT / 1.5, scrollregion=canvas.bbox("all"))
# scrollframe = Frame(scrollarea, bg="#80c1ff")
#
# # Scrollbar for when text is too long to fit in one screen
# vbar = Scrollbar(lower_frame, orient="vertical", command=scrollarea.yview)
# vbar.pack(side=RIGHT, fill="y")
#
# # Link scrollbar to canvas
# scrollarea.config(width=WIDTH, height=HEIGHT / 1.5)
# scrollarea.config(yscrollcommand=vbar.set)
# scrollarea.pack(side=BOTTOM, expand=True, fill="both")
# scrollarea.create_window((4, 4), window=scrollframe, anchor="n")
#
# scrollframe.bind("<Configure>", lambda event, scrollarea=scrollarea: onFrameConfigure(scrollarea))
#
# scrollframe.pack(expand=True, fill="both")

# Where the weather will be shown
label = Label(lower_frame, font=("Courier", 12), anchor="nw", justify="left", bd=4, bg=bg_color)
label.place(relwidth=1, relheight=1)

# top right of lower_frame
weather_icon = Canvas(label, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)
# The frame in the bottom left of lower_frame
tiny_frame = Frame(label, bg=bg_color, bd=2)
tiny_frame.place(relx=.74, rely=0.74, relwidth=.25, relheight=.25)
# Button to show the grid of buttons for quick alarm
button2 = Button(tiny_frame, text="Quick Alarm", command=lambda: quick_alarm())
button2.place(relwidth=1, relheight=1)

weather.mainloop()
