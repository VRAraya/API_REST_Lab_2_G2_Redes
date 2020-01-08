# Se usa flask para construir la API 
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from itertools import cycle
import string

app = Flask(__name__)
# se crea el objeto API
api = Api(app)

# la funcion calcula el digito verificador según un rut
def digVerificator (rut):
  reversed_digits = map(int, reversed(rut))
  factors = cycle(range(2, 8))
  s=sum(d*f for d, f in zip (reversed_digits, factors))
  return (-s) % 11

# Una funcion para verificar el digito proporcionado junto con el rut en el formato xx.xxx.xxx-x
class RUT(Resource):
  def get(self, rutd):
    rutdp=rutd.replace('.',"")
    strRutd = rutdp.split('-')
    dig = digVerificator(strRutd[0])
    if(dig==10 and (strRutd[1]=='k' or strRutd[1]=='K')):
      return jsonify({'isVerify': True}) 
    try:
      int(strRutd[1])
    except:
      return jsonify({'isVerify': False})
    
    if(int(strRutd[1]) == dig):
      return jsonify({'isVerify': True})
      
    return jsonify({'isVerify': False})

#Una funcion para saludar según el sexo y el nombre de la persona
class fullName(Resource):
  def get(self, nombres, apellidoPat, apellidoMat, genero):
    if(genero=='M'):
      fullName = 'Sr. '
    if(genero=='F'):
      fullName = 'Sra. '

    fullName = fullName + nombres.replace('.'," ") + ' ' + apellidoPat + ' ' + apellidoMat
    return jsonify({'fullName': fullName.title()})

#Se agregan las rutas a la API
api.add_resource(RUT,'/RUT/<string:rutd>')
api.add_resource(fullName, '/fullName/<string:nombres>/<string:apellidoPat>/<string:apellidoMat>/<string:genero>')


# funcion driver
if __name__ == '__main__': 
	app.run(debug = True) 
