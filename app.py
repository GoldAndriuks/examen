from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        telefono = request.form['telefono']
        ciudad = request.form['ciudad']
        CP = request.form['CP']
        estado = request.form['estado']

        es_nuevo = not os.path.exists('resultados.csv') or os.stat('resultados.csv').st_size == 0

        with open('resultados.csv', mode='a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            if es_nuevo:
                escritor.writerow(['Nombre', 'Apellido', 'Correo', 'Contraseña', 'Teléfono', 'Ciudad', 'CP', 'Estado'])
            escritor.writerow([nombre, apellido, correo, contraseña, telefono, ciudad, CP, estado])

        return """
        <h2>¡Registro exitoso!</h2>
        <a href="/">Volver</a>
        """
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
