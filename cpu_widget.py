import json
import requests
import tkinter as tk
from tkinter import ttk
import time

# === Function to Get CPU Temperature ===
def find_temperature(data):
    """Recursively search for CPU temperature in the JSON tree."""
    if isinstance(data, dict):
        if data.get("Text") == "Temperatures" and "Children" in data:
            return find_temperature(data["Children"])

        if "Text" in data and "CPU Package" in data["Text"]:
            return data["Value"]

        if "Children" in data:
            return find_temperature(data["Children"])

    elif isinstance(data, list):
        for item in data:
            result = find_temperature(item)
            if result:
                return result
    return None

def get_cpu_temperature():
    try:
        url = "http://localhost:8085/data.json"  # OpenHardwareMonitor API
        response = requests.get(url)
        data = response.json()

        temp = find_temperature(data)
        return temp if temp else "N/A"
    except Exception as e:
        return "N/A"

# === GUI Setup ===
class TemperatureApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CPU Temperature Monitor")
        self.geometry("300x200")
        self.configure(bg="#222831")  # Dark background
        self.resizable(False, False)

        # === Styling ===
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 14), background="#222831", foreground="white")
        self.style.configure("TFrame", background="#393E46")
        self.style.configure("Temperature.TLabel", font=("Arial", 24, "bold"), foreground="#FFD369")

        # === Widget Container ===
        self.frame = ttk.Frame(self, padding=20, style="TFrame")
        self.frame.pack(expand=True, fill="both")

        # === Labels ===
        self.label_title = ttk.Label(self.frame, text="CPU Temperature", style="TLabel")
        self.label_title.pack(pady=5)

        self.label_temp = ttk.Label(self.frame, text="-- °C", style="Temperature.TLabel")
        self.label_temp.pack(pady=10)

        # === Start Updating Temperature ===
        self.update_temperature()

    def update_temperature(self):
        temp = get_cpu_temperature()
        self.label_temp.config(text=f"{temp}")

        # Refresh every 5 seconds
        self.after(1000, self.update_temperature)

# === Run the Application ===
if __name__ == "__main__":
    app = TemperatureApp()
    app.mainloop()
