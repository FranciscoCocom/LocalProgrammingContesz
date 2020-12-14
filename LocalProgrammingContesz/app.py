from flask import Flask, render_template, request, abort, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

from modelo.models import db
from modelo.models import Categorias, Usuarios, Edicion_Eventos, Alumnos, Equipos, Problemas, Problemas_Propuestos, Problemas_Resueltos, Carreras, Docentes
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


@app.route('/Docentes/consultaDocentes.html')
@login_required
def eliminarDocente(nodocente):
    return 'Eliminando al Docente:' + str(nodocente)


@app.route('/Docentes/consultaDocentes.html/<id>')
@login_required
def consultaDocente(id):
    return 'consultando los datos del docente:' + id


# Inicio del CRUD de alumnos
@app.route('/Alumnos/consultaAlumnos.html/new')
@login_required
def nuevoAlumno():
    return render_template('Alumnos/consultaAlumnos.html')


@app.route('/Alumnos/consultaAlumnos.html', methods=['POST'])
@login_required
def guardar_alumno():
    try:
        name = request.form['nombre']
    except:
        abort(500)
        return name


@app.route('/Alumnos/consultaAlumnos.html')
@login_required
def editarAlumno():
    return render_template('/Alumnos/consultaAlumnos.html')


@app.route('/consultaAlumnos.html')
@login_required
def eliminarAlumno():
    return render_template('Alumnos/consultaAlumnos.html')


@app.route('/consultaAlumnos.html')
def consultarAlumnos():
    return render_template('Alumnos/consultaAlumnos.html')


# fin del CRUD alumnos

# CRUD Categorias aqui lo dejare igual en las rutas
@app.route('/consultaCategorias.html')
@login_required
def nuevaCategoria():
    return render_template('Categorias/consultaCategorias.html')


@app.route('/consultaCategorias.html', methods=['POST'])
@login_required
def agregarCategoria():
    try:
        c = Categorias()
        c.nombre = request.form['nombre']
        c.insertar()
        # return ''
        return redirect(url_for('Categorias/consultarCategorias.html'))
    except:
        abort(500)


@app.route('/categorias.html')
def consultarCategorias():
    c=Categorias()
    categorias = c.consultaGeneral()
    return render_template('Categorias/consultaCategorias.html', categorias=categorias)


@app.route('/categorias/<int:id>')
@login_required
def editarCategoria(id):
    c=Categorias()
    c.idcategoria = id
    categoria = c.consultaIndividual()
    return render_template('Categorias/consultaCategorias.html', categorias=categoria)


@app.route('/categorias', methods=['POST'])
@login_required
def modificarCategorias():
    c=Categorias()
    c.idcategoria = request.form['id']
    c.nombre = request.form['nombre']
    c.actualizar()
    return redirect(url_for("Categorias/consultarCategorias.html"))


@app.route('/categorias/<int:id>')
@login_required
def eliminarCategoria(id):
    c = Categorias()
    c.idcategoria = id
    c.eliminar()
    return redirect(url_for("Categorias/consultarCategorias.html"))
# Fin CRUD

# crud de Salas, se cambiara por edicion eventos
@app.route('/consultaEdicionEventos.html')
def consultarEdicion_Eventos():
    ee = Edicion_Eventos()
    edicion_eventos=ee.consultaGeneral()
    return render_template('Edicion_Eventos/consultaEdicionEventos.html', edicion_eventos=edicion_eventos)


@app.route('/consultaEdicionEventos')
@login_required
def nuevaEdicion_Eventos():
    ee = Edicion_Eventos()
    return render_template('Edicion_Eventos/consultaEdicionEventos.html', edicion_eventos=ee.consultaGeneral())


@app.route('/consultaedicionEventos', methods=['POST'])
@login_required
def guardarEdicion_Eventos():
    ee = Edicion_Eventos()
    ee.nombre = request.form['nombre']
    ee.idevento = request.form['idEvento']
    ee.insertar()
    return redirect(url_for('Edicion_Eventos/consultaEdicionEventos'))

# fin crud eventos


# crud de Carreras
@app.route('/consultaCarreras.html')
def consultarCarreras():
    cr =Carreras()
    carreras=cr.consultaGeneral()
    return render_template('Carreras/consultaCarreras.html', carreras=carreras)


@app.route('/consultaCarreras')
@login_required
def nuevaCarrera():
    cr = Carreras
    return render_template('Carreras/consultaCarreras.html', carreras=cr.consultaGeneral())


@app.route('/consultaCarreras', methods=['POST'])
@login_required
def guardarCarreras():
    cr = Carreras()
    cr.nombre = request.form['nombre']
    cr.idcarrera = request.form['idcarrera']
    cr.insertar()
    return redirect(url_for('Carreras/consultaCarreras'))
# fin crud carreras


# crud de Equipos
@app.route('/consultaEquipos.html')
def consultarEquipos():
    e=Equipos()
    equipos=e.consultaGeneral()
    return render_template('Equipos/consultaEquipos.html', equipos=equipos)


@app.route('/consultaEquipos.html')
@login_required
def nuevoEquipo():
    e=Equipos()
    return render_template('Equipos/consultaEquipos.html', equipos=e.consultaGeneral())


@app.route('/consultaEquipos.html', methods=['POST'])
@login_required
def guardarEquipos():
    e=Equipos()
    e.idequipo=request.fom['idequipo']
    e.nombre = request.form['nombre']
    e.insertar()
    return redirect(url_for('Equipos/consultaEquipos'))
# fin crud EQUIPOS


# crud de PROBLEMAS
@app.route('/consultaProblemas.html')
def consultarProblemas():
    p=Problemas()
    problemas=p.consultaGeneral()
    return render_template('Problemas/consultaProblemas.html', problemas=problemas)

@app.route('/consultaProblemas.html')
@login_required
def nuevoProblema():
    p=Problemas()
    return render_template('Problemas/consultaProblemas.html', problemas=p.consultaGeneral())

@app.route('/consultaProblemas.html', methods=['POST'])
@login_required
def guardarProblemas():
    p=Problemas()
    p.idproblema=request.fom['idproblema']
    p.nombreproblema = request.form['nombre']
    p.insertar()
    return redirect(url_for('Problemas/consultaProblemas'))
# fin crud PROBLEMAS


# crud de PROBLEMAS_PROPUESTOS
@app.route('/consultaProblemasPropuestos.html')
def consultarProblemasPropuestos():
    pp=Problemas_Propuestos()
    problemasprop=pp.consultaGeneral()
    return render_template('Problemas_Propuestos/consultaProblemasPropuestos.html', problemaspropuestos=problemasprop)

@app.route('/consultaProblemasPropuestos.html')
@login_required
def nuevoProblemaPropuesto():
    pp=Problemas_Propuestos()
    return render_template('Problemas_Propuestos/consultaProblemasPropuestos.html', problemaspropuestos=pp.consultaGeneral())

@app.route('/consultaProblemasPropuestos.html', methods=['POST'])
@login_required
def guardarProblemasPropuestos():
    pp=Problemas_Propuestos()
    pp.noproblemaspropuestos =request.fom['idproblema']
    pp.insertar()
    return redirect(url_for('Problemas_Propuestos/consultaProblemas.html'))
# fin crud EQUIPOS


# crud de PROBLEMAS_RESUELTOS
@app.route('/consultaProblemasResueltos.html')
def consultarProblemasResueltos():
    pr = Problemas_Resueltos
    problemasresueltos = pr.consultaGeneral()
    return render_template('Problemas_Resueltos/consultaProblemasResueltos.html', problemasresueltos=problemasresueltos)


@app.route('/consultaProblemasResueltos.html')
@login_required
def nuevoProblemaResuelto():
    pr = Problemas_Resueltos
    return render_template('Problemas_Resueltos/consultaProblemasResueltos.html',
                           problemasresueltos=pr.consultaGeneral())


@app.route('/consultaProblemasResueltos.html', methods=['POST'])
@login_required
def guardarProblemasResueltos():
    pr = Problemas_Resueltos()
    pr.problemaresuelto = request.fom['idproblema']
    pr.insertar()
    return redirect(url_for('Problemas_Resueltos/consultaProblemasResueltos.html'))


# fin crud EQUIPOS


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
