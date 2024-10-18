from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de presentación
@app.route('/presentacion')
def presentacion():
    # Datos que se mostrarán en la plantilla de presentación
    datos = {
        "nombre": " ",
        "instagram": "@",
        "otra_red": "@",
        "edad": None
    }
    return render_template('presentacion.html', **datos)

# Comprobamos que el archivo se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)
