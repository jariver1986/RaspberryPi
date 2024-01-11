import board
import adafruit_dht
import time

# 1- crear el entorno virtual
# python3 -m venv myenv
# source myenv/bin/activate

# 2 - instalar las librerias
# pip3 install adafruit-blinka
# pip3 install adafruit-circuitpython-dht

# Configuración del pin del sensor DHT11
pin = board.D4

# Crear un objeto de sensor DHT11
sensor = adafruit_dht.DHT11(pin)

try:
    while True:
        # Intenta obtener los datos del sensor
        try:
            temperature_c = sensor.temperature
            humidity = sensor.humidity
            print(f'Temperatura: {temperature_c}°C, Humedad: {humidity}%')
        except RuntimeError as error:
            print(f'Error al leer los datos del sensor: {error}')

        # Espera 2 segundos antes de la próxima lectura
        time.sleep(2)

except KeyboardInterrupt:
    pass
finally:
    sensor.exit()
