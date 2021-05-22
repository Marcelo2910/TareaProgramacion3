# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------
# Archivo: gui.py
# Implementación de Arquitecturas Micro Servicios.
# Autor(es): Perla Velasco & Jorge Alfonso Solís.
# Version: 1.0 Marzo 2021
# Descripción:
#
#   Este archivo define la interfaz gráfica del usuario. Recibe un parámetro que define el 
#   Microservicio que se desea utilizar.
#   
#                                             gui.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Porporcionar la in-  | - Consume servicios    |
#           |          GUI          |    terfaz gráfica con la|   para proporcionar    |
#           |                       |    que el usuario hará  |   información al       |
#           |                       |    uso del sistema.     |   usuario.             |
#           +-----------------------+-------------------------+------------------------+
#

from flask import Flask, render_template
import json, requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Se definen las llaves de cada microservicio

key_m1 = "45d72e44c2e64875953924c9f3760994"
headers_m1 = {"authorization": key_m1}

key_m2 = "37d9e213282b4988b0aa5bfcca29e85f"
header_m2 = {"authorization": key_m2}

key_m3 = "fc43d12329674898812fc92d0d76f2ec"
header_m3 = {"authorization": key_m3}

key_m4 = "65374f3de25c4dd0859ccdb1cf5ef92e"
header_m4 = {"authorization": key_m4}

key_m5 = "6904bb38c6ac46a1b4df057c01ea39f6"
header_m5 = {"authorization": key_m5, "content-type": "application/json"}

key_m6 = "4e7a494c5ace4285b49352413610adb8"
header_m6 = {"authorization": key_m6}


# Se definen las url para cada micro servicio.
# Se reemplaza el 127.0.0.1 del localhost por host.docker.internal para hacer la conexión
# con los microservicios dentro de los contenedores de Docker.

# Url para el microservicio 1
url_microservice1 = 'http://host.docker.internal:8080/hello/python'
# Url para el microservicio 2
url_microservice2 = 'http://host.docker.internal:8080/hello/dart'
# Url para el microservicio 3
url_microservice3 = 'http://host.docker.internal:8080/hello/django'
# Url para el microservicio 4
url_microservice4 = 'http://host.docker.internal:8080/catalogo/'
# Url para el microservicio 5
url_microservice5 = 'http://host.docker.internal:8080/cart'
# Url para el microservicio 6
url_microservice6 = 'http://host.docker.internal:8080/order'


# Método que muestra la página de inicio del sistema
@app.route("/", defaults={'api': None}, methods=['GET'])
@app.route("/<api>", methods=['GET'])
def index(api):

    # Se verifica si se recibió la variable api
    if api:
        try:
            api = int(api)
        except Exception as e:
            api = 0
            json_result = {"prueba":"prueba"}
            
        if int(api) == 1:
            # Se llama al microservicio enviando como parámetro la url y el header  
            ms1 = requests.get(url_microservice1, headers=headers_m1)
            # Se convierte la respuesta a json
            json = ms1.json()
            # Se crea el json que será enviado al template
            json_result = {'ms1': json}
        elif int(api) == 2:
            # Se llama al microservicio enviando como parámetro la url y el header
            ms2 = requests.get(url_microservice2, headers=header_m2)
            # Se convierte la respuesta a json
            json = ms2.json()
            # Se crea el json que será enviado al template
            json_result = {'ms2': json}
        elif int(api) == 3:
            # Se llama al microservicio enviando como parámetro la url y el header 
            ms3 = requests.get(url_microservice3, headers=header_m3)
            # Se convierte la respuesta a json
            json = ms3.json()
            # Se crea el json que será enviado al template
            json_result = {'ms3': json}
        elif int(api) == 4:
            # Se llama al microservicio enviando como parámetro la url y el header 
            ms4 = requests.get(url_microservice4, headers=header_m4)
            # Se convierte la respuesta a json
            json = ms4.json()
            # Se crea el json que será enviado al template
            json_result = {'ms4': json}
        elif int(api) == 5:
            # Se llama al microservicio enviando como parámetro la url y el header 
            ms4 = requests.get(url_microservice4, headers=header_m4)
            ms5 = requests.get(url_microservice5, headers=header_m5, data=ms4.json())
            # Se convierte la respuesta a   json
            json = ms5.json()
            # Se crea el json que será enviado al template
            json_result = {'ms5': json}
        elif int(api) == 6:
            # Se llama al microservicio enviando como parámetro la url y el header 
            ms6 = requests.get(url_microservice6, headers=header_m6)
            # Se convierte la respuesta a json
            json = ms6.json()
            # Se crea el json que será enviado al template
            json_result = {'ms6': json}
                
        return render_template("index.html", result=json_result)

        # crear proyecto
        # crear modelos (app)
        # crear vistas
        # correr la migfracion
        # api_rest
    
    # Si no se recibe, simplemente se regresa el template index.html sin datos.
    else:
        json_result = {'prueba':'prueba'}
        return render_template("index.html", result=json_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')