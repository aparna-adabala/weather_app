import tkinter as tk
import requests
from tkinter import messagebox
API_KEY = "9ccd5beb9c7e9d0fa332e3f4763120a6"
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            messagebox.showerror("Error", data["message"])
            return
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        result = f"Weather: {weather}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
        weather_result.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")
# GUI Setup
app = tk.Tk()
app.title("Weather App")
app.geometry("350x300")
app.resizable(False, False)
tk.Label(app, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(app, font=("Arial", 14), justify="center")
city_entry.pack(pady=5)
tk.Button(app, text="Get Weather", font=("Arial", 12), command=get_weather).pack(pady=10)
weather_result = tk.Label(app, text="", font=("Arial", 12), justify="left")
weather_result.pack(pady=10)
app.mainloop()