from flask import Flask, request, jsonify
import json
#importamos la clase funcion.
from Funcion import Funcion

#para problemas de distribuidor (seguridad)
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)
#termina 

#creo una lista para almacenar las funciones.
funciones = []

#creando rutas 
#sirve para que cuando entre a la pagina principal no tire error.
@app.route('/', methods = ['GET'])
def inicio():
    return 'Bienvenido'

#creamos otra ruta, con funcion.
@app.route('agregarFuncion', methods = ['POST'])
def agregarFuncion():
    #almacena la peticion.
    cuerpo = request.get_json()
    #ya obtenido el json. guardamos.
    nombre = cuerpo['nombre']
    horario = cuerpo['horario']
    #creamos la nueva funcion.
    nueva_funcion = Funcion(nombre, horario)
    #llamos a la lista global.
    global funciones
    #agrego la funcion con el metodo append()
    funciones.append(nueva_funcion)
    #retorna obj python a json
    return jsonify({
        'mensaje': 'agregado correctamente.'
    })
