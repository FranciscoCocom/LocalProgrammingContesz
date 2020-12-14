from flask import Flask, render_template, request, abort, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

from modelo.models import db
from modelo.models import Categorias, Usuarios, Edicion_Eventos, Alumnos
#Equipos, Problemas, Problemas_Propuestos, Problemas_Resueltos, Carreras,  Docentes,
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'ConT3sz'
#db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234/ConTESZ'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Configuración de la gestion Usuarios con Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "inicio"


# rutas para el ingreso a la aplicacion

@login_manager.user_loader
def load_user(id):
    return Usuarios.query.get(int(id))


@app.route('/')
def inicio():
    # return 'Bienvenido a FLASK'
    if current_user.is_authenticated:
        return render_template('principal.html')
    else:
        return render_template('indexPrueba.html')


@app.route('/login', methods=['POST'])
def login():
    # return 'Procesando las credenciales.'
    u = Usuarios()
    usuario = u.validar(request.form['email'], request.form['password'])
    if usuario != None:
        login_user(usuario)
        return render_template('principal.html')
    else:
        return 'Usuario invalido'


@app.route('/cerrarSesion')
@login_required
def cerrarSesion():
    if current_user.is_authenticated:
        logout_user()
    else:
        abort(404)
    return redirect(url_for("inicio"))


# fin de las rutas del acceso al sistema
@app.route('/Usuarios/consultaUsuarios.html')
def registrarUsuario():
    return render_template('Usuarios/consultaUsuarios.html')


@app.route('/consultaUsuarios', methods=['post'])
def guardarUsuario():
    usuario = Usuarios()
    usuario.nousuario = request.form['noUsuario']
    usuario.nombre = request.form['nombre']
    usuario.sexo = request.form['sexo']
    usuario.telefono = request.form['telefono']
    usuario.email = request.form['email']
    usuario.estatus = request.form['estatus']
    usuario.tipousuarioo = request.form['tipo']
    usuario.password_hash = request.form['password']
    usuario.insertar()
    return render_template('index.html')


@app.route('/registrarProducto')
def regsitrarProducto():
    return 'registrando un producto'


@app.route('/consultaDocentes')
@login_required
def eliminarDocente(nodocente):
    return 'Eliminando al Docente:' + str(nodocente)


@app.route('/consultaDocentes/<id>')
@login_required
def consultaDocente(id):
    return 'consultando los datos del docente:' + id


# Inicio del CRUD de alumnos
@app.route('/alumnos/new')
@login_required
def nuevoAlumno():
    return render_template('Alumnos/altaAlumno.html')


@app.route('/consultaAlumnos', methods=['POST'])
@login_required
def guardar_alumno():
    try:
        name = request.form['nombre']
    except:
        abort(500)
        return name


@app.route('/consultaAlumnos')
@login_required
def editarAlumno():
    return render_template('Alumnos/consultaAlumnos.html')


@app.route('/consultaAlumnos')
@login_required
def eliminarAlumno():
    return render_template('Alumnos/consultaAlumnos.html')


@app.route('/consultaAlumnos')
def consultarAlumnos():
    return render_template('Alumnos/consultaAlumnos.html')


# fin del CRUD alumnos

# CRUD Categorias aqui lo dejare igual en las rutas
@app.route('/categorias/new')
@login_required
def nuevaCategoria():
    return render_template('Categorias/consultaCategorias.html')


@app.route('/categorias/save', methods=['POST'])
@login_required
def agregarEdificio():
    try:
        c = Categorias()
        c.nombre = request.form['nombre']
        c.insertar()
        # return ''
        return redirect(url_for('consultarCategorias'))
    except:
        abort(500)


@app.route('/categorias')
def consultarCategorias():
    c=Categorias()
    categorias = c.consultaGeneral()
    return render_template('Categorias/consultaCategorias.html', categorias=categorias)


@app.route('/categorias/edit/<int:id>')
@login_required
def editarCategoria(id):
    c=Categorias()
    c.idcategoria = id
    categoria = c.consultaIndividual()
    return render_template('Categorias/consultaCategorias.html', categorias=categoria)


@app.route('/categorias/modificar', methods=['POST'])
@login_required
def modificarCategorias():
    c=Categorias()
    c.idcategoria = request.form['id']
    c.nombre = request.form['nombre']
    c.actualizar()
    return redirect(url_for("consultarCategorias"))


@app.route('/categorias/delete/<int:id>')
@login_required
def eliminarCategoria(id):
    c = Categorias()
    c.idcategoria = id
    c.eliminar()
    return redirect(url_for("consultarCategorias"))
# Fin CRUD

# crud de Salas, se cambiara por edicion eventos
@app.route('/edicion_eventos')
def consultarEdicion_Eventos():
    ee = Edicion_Eventos()
    edicion_eventos=ee.consultaGeneral()
    return render_template('Edicion_Eventos/consultaEdicion_Eventos.html', edicion_eventos=edicion_eventos)


@app.route('/edicion_eventos/new')
@login_required
def nuevaEdicion_Eventos():
    ee = Edicion_Eventos()
    return render_template('Edicion_Eventos/consultaEdicion_Eventos.html', edicion_eventos=ee.consultaGeneral())


@app.route('/edicion_eventos/save', methods=['POST'])
@login_required
def guardarEdicion_Eventos():
    ee = Edicion_Eventos()
    ee.nombre = request.form['nombre']
    ee.idevento = request.form['idEvento']
    ee.insertar()
    return redirect(url_for('consultaEdicion_Eventos'))

# fin crud salas

# CRUD Opciones (Ajax)
"""
@app.route("/opciones")
def opciones():
    return render_template('Opciones/opciones.html')

@app.route('/opciones/consultaGeneral')
def consultarOpciones():
    opcion = Opcion()
    lista = []
    for o in opcion.consultaGeneral():
        lista.append({"idOpcion": o.idOpcion, "nombre": o.nombre, "descripcion": o.descripcion})
    return json.dumps(lista)

@app.route('/opciones/guardar/<data>', methods=['get'])
def guaradarOpcion(data):
    opcion = Opcion()
    datos = json.loads(data)
    opcion.nombre = datos['nombre']
    opcion.descripcion = datos['descripcion']
    opcion.insertar()
    return 'Opcion agregada con exito'

@app.route('/opciones/<int:id>')
def consultarOpcion(id):
    opcion = Opcion()
    opcion.idOpcion = id
    opcion = opcion.consultaIndividual()
    dicOpcion = {"idOpcion": opcion.idOpcion, "nombre": opcion.nombre, "descripcion": opcion.descripcion}
    return json.dumps(dicOpcion)

@app.route('/opciones/modificar/<data>', methods=['get'])
def modifcarOpcion(data):
    opcion = Opcion()
    datos = json.loads(data)
    opcion.idOpcion = datos['idOpcion']
    opcion.nombre = datos['nombre']
    opcion.descripcion = datos['descripcion']
    opcion.actualizar()
    return 'Opcion modificada con exito'

@app.route('/opciones/delete/<int:id>')
def eliminarOpcion(id):
    opcion = Opcion()
    opcion.idOpcion = id
    opcion.eliminar()
    return 'Opcion eliminada con exito'
"""
#creo que fin ajax


@app.errorhandler(404)
def error_404(e):
    return render_template('comunes/error_404.html'), 404


@app.errorhandler(500)
def error_500(e):
    return render_template('comunes/error_500.html'), 500


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
