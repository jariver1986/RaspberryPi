# -*- coding: utf-8 -*-

import requests
import time

#Primero crear una variable de entorno
# python3 -m venv myenv
# source myenv/bin/activate
# sudo apt update
# pip install requests

# API Key de tu canal de ThingSpeak
API_KEY = 'MUYLHT4B3KY29K2U'

def obtener_temperatura():
    temp_file = open("/sys/class/thermal/thermal_zone0/temp")
    cpu_temp = temp_file.read()
    temp_file.close()
    return float(cpu_temp) / 1000

def enviar_a_thingspeak(temperatura):
    THINGSPEAK_URL = f'https://api.thingspeak.com/update?api_key={API_KEY}&field1={temperatura}'
    response = requests.get(THINGSPEAK_URL)
    return response.status_code

while True:
    # Obtener la temperatura de la CPU
    temperatura_cpu = obtener_temperatura()

    # Mostrar la temperatura en la consola (opcional)
    print(f'Temperatura de la CPU: {temperatura_cpu} C')

    # Enviar la temperatura a ThingSpeak
    codigo_respuesta = enviar_a_thingspeak(temperatura_cpu)

    # Comprobar si los datos se enviaron correctamente
    if codigo_respuesta == 200:
        print('Datos enviados a ThingSpeak')
    else:
        print('Error al enviar datos a ThingSpeak')

    # Esperar 5 segundos antes de la próxima lectura y envío de datos
    time.sleep(15)
