
# 1- crear el entorno virtual
# python3 -m venv myenv
# source myenv/bin/activate

# 2 - instalar las librerias
# pip3 install adafruit-blinka
# pip3 install adafruit-circuitpython-dht

# 3 - Instalacion de requests dentro del entorno virtual
#     pip3 install requests



import board
import adafruit_dht
import time
import requests
import json

# Configuración del pin del sensor DHT11
pin = board.D4

# Crear un objeto de sensor DHT11
sensor = adafruit_dht.DHT11(pin)

# Configuración de Ubidots
UBIDOTS_TOKEN = "*******" # Please write here your ubidots token
UBIDOTS_URL = f"https://industrial.api.ubidots.com/api/v1.6/devices/raspberry-pi"

def send_to_ubidots(humidity, temperature):
    payload = {
        "temperature": {"value": temperature},
        "humidity": {"value": humidity}
    }

    headers = {
        "X-Auth-Token": UBIDOTS_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.post(UBIDOTS_URL, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        print("Datos enviados correctamente a Ubidots")
    else:
        print(f"Error al enviar datos a Ubidots. Código de estado: {response.status_code}")


try:
    while True:
        # Intenta obtener los datos del sensor
        try:
            temperature_c = sensor.temperature
            humidity = sensor.humidity
            print(f'Temperatura: {temperature_c}°C, Humedad: {humidity}%')
            send_to_ubidots(humidity, temperature_c)
        except RuntimeError as error:
            print(f'Error al leer los datos del sensor: {error}')

        # Espera 2 segundos antes de la próxima lectura
        time.sleep(60)

except KeyboardInterrupt:
    pass
finally:
    sensor.exit()
