from flask import Flask
app=Flask(__name__)

@app.route('/')
def inicio():
    return 'Bienvenido a FLASK'

@app.route('/registrarUsuario')
def registrarUsuario():
    return 'Registrando un usuario'

@app.route('/registrarProducto')
def regsitrarProducto():
    return 'registrando un producto'

@app.route('/cerrarSesion')
def cerrarSesion():
    return '<h1>Cerrando la Sesion, bye</h1><table border="1"><th>id</th></table>'

if __name__=='__main__':
    app.run(debug=True)