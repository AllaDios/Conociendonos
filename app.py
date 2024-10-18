from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Puedes manejar la lógica de generación del QR aquí
        nombre = request.form.get('nombre')
        instagram = request.form.get('instagram')
        otra_red = request.form.get('otra-red')
        edad = request.form.get('edad')

        # Redirigir a la página de presentación con parámetros
        return render_template('presentacion.html', nombre=nombre, instagram=instagram, otra_red=otra_red, edad=edad)
    
    return render_template('index.html')

@app.route('/presentacion')
def presentacion():
    return render_template('presentacion.html')

if __name__ == '__main__':
    app.run(debug=True)

