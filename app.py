from flask import Flask, jsonify

app = Flask(__name__)

# Función para calcular factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Ruta principal: recibe el número por la URL
@app.route('/factorial/<int:numero>', methods=['GET'])
def calcular_factorial(numero):
    fact = factorial(numero)
    etiqueta = "par" if fact % 2 == 0 else "impar"

    respuesta = {
        "numero_recibido": numero,
        "factorial": fact,
        "etiqueta": etiqueta
    }
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)
