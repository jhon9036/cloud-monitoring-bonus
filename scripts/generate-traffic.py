import requests
import time

BASE_URL = "http://localhost:3000"

endpoints = [
    "/",
    "/api/datos",
    "/api/lento"
]

print("Generando tráfico a la API... Presiona Ctrl+C para detener.")

try:
    while True:
        for endpoint in endpoints:
            url = BASE_URL + endpoint
            try:
                response = requests.get(url)
                print(f"{endpoint} -> {response.status_code}")
            except Exception as e:
                print(f"Error en {endpoint}: {e}")
            time.sleep(1)
except KeyboardInterrupt:
    print("Tráfico detenido.")