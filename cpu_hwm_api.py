import json
import requests
import time

def find_temperature(data):
    """Recursively search for CPU temperature in the JSON tree."""
    if isinstance(data, dict):
        if data.get("Text") == "Temperatures" and "Children" in data:
            return find_temperature(data["Children"])  # Dive deeper

        if "Text" in data and "CPU Package" in data["Text"]:  # Match CPU temperature sensor
            return data["Value"]

        if "Children" in data:
            return find_temperature(data["Children"])  # Continue searching

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
        return temp if temp else "Température non disponible"
    except Exception as e:
        return f"Erreur : {e}"

while True:
    temp = get_cpu_temperature()
    print(f"Température CPU : {temp}°C")
    time.sleep(5)
