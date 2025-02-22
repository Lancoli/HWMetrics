import psutil
import time

def get_cpu_temperature():
    try:
        sensors = psutil.sensors_temperatures()
        if not sensors:
            return "Température non disponible"

        for name, entries in sensors.items():
            for entry in entries:
                if entry.current:  # Vérifie qu'une valeur est bien disponible
                    return entry.current

        return "Température non disponible"
    except AttributeError:
        return "Température non supportée sur ce système"

while True:
    temp = get_cpu_temperature()
    print(f"Température CPU : {temp}°C")
    time.sleep(2)  # Rafraîchissement toutes les 2 secondes
