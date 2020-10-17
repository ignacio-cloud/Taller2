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
@app.route('/agregarFuncion', methods = ['POST'])
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

#creamos otra ruta, con funcion.
#metodo GET obtenemos informacion de la lista.
@app.route('/obtenerFunciones',methods = ['GET'])
def obtenerFunciones():
    #creo una lista json.
    json_funciones = []
    global funciones
    #recorro toda la lista agregando los datos convertidos a json.
    for funcion in funciones:
        json_funciones.append({"nombre": funcion.nombre, "horario": funcion.horario, "disponible": funcion.isDisponible()})
    #ya puedo retornar la lista en formato json.
    return jsonify({json_funciones})

#colocamos el metodo main, donde va a entrar la applicacion.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)