# Se usa flask para construir la API 
from flask import Flask, jsonify, request
from itertools import cycle

app = Flask(__name__)

# la funcion calcula el digito verificador según un rut
def digVerificator (rut):
  reversed_digits = map(int, reversed(rut))
  factors = cycle(range(2, 8))
  s=sum(d*f for d, f in zip (reversed_digits, factors))
  return (-s) % 11

# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
	if(request.method == 'GET'): 

		data = "hello world"
		return jsonify({'data': data}) 


# Una funcion para verificar el digito proporcionado junto con el rut en el formato xx.xxx.xxx-x
@app.route('/RUT/<string:rutd>', methods = ['GET'])
def verifyRut(rutd):
  strRutd = rutd.split('-')
  dig = digVerificator(strRutd[0])

  if(dig==10 and strRutd[1]=='k'):
    return jsonify({'isVerify': True}) 
  
  if(int(strRutd[1]) == dig):
    return jsonify({'isVerify': True})

  return jsonify({'isVerify': False})

@app.route('/fullName/<string:nombres>/<string:apellidos>/<string:genero>', methods = ['GET'])
def fullName(nombres, apellidos, genero):
  if(genero=='M'):
    fullName = 'Sr. '
  if(genero=='F'):
    fullName = 'Sra. '

  fullName = fullName + nombres + ' ' + apellidos
  return jsonify({'fullName': fullName.title()})


# funcion driver
if __name__ == '__main__': 
	app.run(debug = True) 
