from flask import Flask,render_template,request,abort,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin
from sqlalchemy import Integer,String,Column,ForeignKey, Date, Time

app = Flask(__name__)
app.secret_key = "Secret Key"

#Configuración de la gestion Usuarios con Flask-Login
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view="inicio"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:eltolok.1@localhost/localprogrammingcontesz'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

#Apartir de aquí van las tablas de las bases de datos
#-----------------------------------USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS---------------------------

class Usuarios(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    sexo = db.Column(db.String(1))
    telefono = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    estatus = db.Column(db.String(50))
    tipousuario = db.Column(db.String(50))
    contraseña = db.Column(db.String(50))


    def __init__(self, nombre, sexo, telefono, correo, estatus, tipousuario, contraseña):
        self.nombre = nombre
        self.sexo = sexo
        self.telefono = telefono
        self.correo = correo
        self.estatus = estatus
        self.tipousuario = tipousuario
        self.contraseña = contraseña

    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return False
    def is_active(self):
        if self.estatus=='activo':
            return True
        else:
            return False
    def is_admin(self):
        if self.tipousuario=='docente':
            return True
        else:
            return False
    def getTipo(self):
        return self.tipo
    def get_id(self):
        return self.id
    def validar(self,correo,contraseña):
        user=Usuarios.query.filter_by(correo=correo,contraseña=contraseña).first()
        return user

#Apartir de aquí van las funciones y rutas de la aplicación
#rutas para el ingreso a la aplicacion

@login_manager.user_loader
def load_user(id):
    return Usuarios.query.get(int(id))

@app.route('/')
def inicio():
    #return 'Bienvenido a FLASK'
    if current_user.is_authenticated:
        return render_template('principal.html')
    else:
        return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    #return 'Procesando las credenciales.'
    user = Usuarios.query.filter_by(correo=request.form['correo'], contraseña=request.form['contraseña']).first()
    if user!=None:
        login_user(user)
        return render_template('principal.html')
    else:
        return 'Usuario invalido'


@app.route('/logout')
def logout():
    logout_user()
    return render_template('index.html')

@app.route('/principal')
def principal():
    return render_template("principal.html")


@app.route('/insertUsuarios', methods = ['POST'])
def insertUsuarios():

    if request.method == 'POST':
        nombre = request.form['nombre']
        sexo = request.form['sexo']
        telefono = request.form['telefono']
        correo = request.form['correo']
        estatus = request.form['estatus']
        tipousuario = request.form['tipousuario']
        contraseña = request.form['contraseña']

        my_usuario = Usuarios(nombre, sexo, telefono, correo, estatus, tipousuario, contraseña)
        db.session.add(my_usuario)
        db.session.commit()

        return redirect(url_for('consultarUsuarios'))
        #return render_template("Usuarios/consultaUsuarios.html")



@app.route('/actualizarUsuarios', methods = ['GET', 'POST'])
def actualizarUsuarios():
    if request.method == 'POST':
        my_usuarios = Usuarios.query.get(request.form.get('id'))

        my_usuarios.nombre = request.form['nombre']
        my_usuarios.sexo = request.form['sexo']
        my_usuarios.telefono = request.form['telefono']
        my_usuarios.correo = request.form['correo']
        my_usuarios.estatus = request.form['estatus']
        my_usuarios.tipousuario = request.form['tipousuario']
        my_usuarios.contraseña = request.form['contraseña']

        db.session.commit()

        return redirect(url_for('consultarUsuarios'))

@app.route('/eliminarUsuarios/<id>/', methods = ['GET', 'POST'])
def eliminarUsuarios(id):
    my_usuarios = Usuarios.query.get(id)
    db.session.delete(my_usuarios)
    db.session.commit()

    return redirect(url_for('consultarUsuarios'))


@app.route('/usuarios')
def consultarUsuarios():
    all_usuarios = Usuarios.query.all()
    return render_template("Usuarios/consultaUsuarios.html", usuarios = all_usuarios)
#-----------------------------------USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS USUARIOS---------------------------


#-----------------------------------DOCENTES DOCENTES DOCENTES DOCENTES DOCENTES DOCENTES---------------------------

class Docentes (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nousuario = db.Column(db.Integer)
    escolaridad = db.Column(db.String(50))
    especialidad = db.Column(db.String(50))
    cedula = db.Column(db.Integer)
    idcarrera = db.Column(db.Integer, foreing_key =True)

    def __init__(self, nousuario,escolaridad,especialidad,cedula,idcarrera):
        self.nousuario = nousuario
        self.escolaridad = escolaridad
        self.especialidad = especialidad
        self.cedula = cedula
        self.idcarrera = idcarrera


@app.route('/insertDocentes', methods=['POST'])
def insertDocentes():
    if request.method == 'POST':
        nousuario = request.form['nousuario']
        escolaridad = request.form['escolaridad']
        especialidad = request.form['especialidad']
        cedula = request.form['cedula']
        idcarrera = request.form['idcarrera']

        my_docente = Docentes(nousuario, escolaridad, especialidad, cedula, idcarrera)
        db.session.add(my_docente)
        db.session.commit()

        return redirect(url_for('consultarDocentes'))

@app.route('/docentes')
def consultarDocentes():
    all_docentes = Docentes.query.all()
    return render_template("Docentes/consultaDocentes.html", docentes = all_docentes)

@app.route('/actualizarDocentes', methods=['GET', 'POST'])
def actualizarDocentes():
    if request.method == 'POST':
        my_docente = Docentes.query.get(request.form.get('id'))

        my_docente.nousuario = request.form['nousuario']
        my_docente.escolaridad = request.form['escolaridad']
        my_docente.especialidad = request.form['especialidad']
        my_docente.cedula = request.form['cedula']
        my_docente.idcarrera = request.form['idcarrera']

        db.session.commit()

        return redirect(url_for('consultarDocentes'))


@app.route('/eliminarDocentes/<id>/', methods=['GET', 'POST'])
def eliminarDocentes(id):
    my_docente = Docentes.query.get(id)
    db.session.delete(my_docente)
    db.session.commit()

    return redirect(url_for('consultarDocentes'))
#-----------------------------------DOCENTES DOCENTES DOCENTES DOCENTES DOCENTES DOCENTES---------------------------


#-----------------------------------ALUMNOS ALUMNOS ALUMNOS ALUMNOS ALUMNOS ALUMNOS---------------------------
class Alumnos (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nousuario = db.Column(db.Integer, foreing_key =True)
    semestre = db.Column(db.Integer)
    idcarrera = db.Column(db.Integer, foreing_key =True)

    def __init__(self, nousuario,semestre,idcarrera):
        self.nousuario = nousuario
        self.semestre = semestre
        self.idcarrera = idcarrera

@app.route('/insertAlumnos', methods = ['POST'])
def insertAlumnos():

    if request.method == 'POST':
        nousuario = request.form['nousuario']
        semestre = request.form['semestre']
        idcarrera = request.form['idcarrera']

        my_alumno = Alumnos(nousuario,semestre, idcarrera)
        db.session.add(my_alumno)
        db.session.commit()

        return redirect(url_for('consultarAlumnos'))


@app.route('/actualizarAlumnos', methods=['GET', 'POST'])
def actualizarAlumnos():
    if request.method == 'POST':
        my_alumno = Alumnos.query.get(request.form.get('id'))

        my_alumno.nousuario = request.form['nousuario']
        my_alumno.semestre = request.form['semestre']
        my_alumno.idcarrera = request.form['idcarrera']

        db.session.commit()

        return redirect(url_for('consultarAlumnos'))

@app.route('/eliminarAlumnos/<id>/', methods=['GET', 'POST'])
def eliminarAlumnos(id):
    my_alumno = Alumnos.query.get(id)
    db.session.delete(my_alumno)
    db.session.commit()

    return redirect(url_for('consultarAlumnos'))

@app.route('/alumnos')
def consultarAlumnos():
    all_alumnos = Alumnos.query.all()
    return render_template("Alumnos/consultaAlumnos.html", alumnos = all_alumnos)
#-----------------------------------ALUMNOS ALUMNOS ALUMNOS ALUMNOS ALUMNOS ALUMNOS---------------------------


'''

#CATEGORIAS//////////////////////////////////////////////////////////
class Categorias (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    semestreLimite = db.Column(db.Integer)

    def __init__(self, nombre, semestreLimite):
        self.nombre = nombre
        self.semestreLimite = semestreLimite

@app.route('/insertCategorias', methods = ['POST'])
def insertCategorias():

    if request.method == 'POST':
        nombre = request.form['nombre']
        semestreLimite = request.form['semestreLimite']

        my_categoria = Categorias(nombre,semestreLimite)
        db.session.add(my_categoria)
        db.session.commit()

        return redirect(url_for('consultarCategorias'))

@app.route('/actualizarCategorias', methods=['GET', 'POST'])
def actualizarCategorias():
    if request.method == 'POST':
        my_categoria = Categorias.query.get(request.form.get('id'))
        my_categoria.nombre = request.form['nombre']
        my_categoria.semestreLimite = request.form['semestreLimite']

        db.session.commit()

        return redirect(url_for('consultarCategorias'))

@app.route('/eliminarCategorias/<id>/', methods=['GET', 'POST'])
def eliminarCategorias(id):
    my_categoria = Categorias.query.get(id)
    db.session.delete(my_categoria)
    db.session.commit()

    return redirect(url_for('consultarCategorias'))
#--------------------------------------------------------------------------

#CARRERAS/////////////////////////////////////
class Carreras (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    siglas = db.Column(db.String(5))

    def __init__(self, nombre, siglas):
        self.nombre = nombre
        self.siglas = siglas

@app.route('/insertCarreras', methods = ['POST'])
def insertCarreras():

    if request.method == 'POST':
        nombre = request.form['nombre']
        siglas = request.form['siglas']

        my_carrera = Carreras(nombre,siglas)
        db.session.add(my_carrera)
        db.session.commit()

        return redirect(url_for('consultarCarreras'))

@app.route('/actualizarCarreras', methods=['GET', 'POST'])
def actualizarCarreras():
    if request.method == 'POST':
        my_carrera = Carreras.query.get(request.form.get('id'))
        my_carrera.nombre = request.form['nombre']
        my_carrera.siglas = request.form['siglas']

        db.session.commit()

        return redirect(url_for('consultarCarreras'))

@app.route('/eliminarCarreras/<id>/', methods=['GET', 'POST'])
def eliminarCarreras(id):
    my_carrera = Carreras.query.get(id)
    db.session.delete(my_carrera)
    db.session.commit()

    return redirect(url_for('consultarCarreras'))
#----------------------------------------------------------

#EDICION_EVENTOS///////////////////////////
class EdicionEventos (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    fecharegistro = db.Column(db.Date)
    fechaevento = db.Column(db.Date)
    horainicio = db.Column(db.Time)
    horafin = db.Column(db.Time)

    def __init__(self,nombre,fecharegistro,fechaevento,horainicio,horafin):
        self.nombre = nombre
        self.fecharegistro = fecharegistro
        self.fechaevento = fechaevento
        self.horainicio = horainicio
        self.horafin = horafin

@app.route('/insertEdicionEventos', methods = ['POST'])
def insertEdicionEventos():

    if request.method == 'POST':
        nombre = request.form['nombre']
        fecharegistro = request.form['fecharegistro']
        fechaevento = request.form['fechaevento']
        horainicio = request.form['horainicio']
        horafin = request.form['horafin']

        my_edicioneventos = EdicionEventos(nombre,fecharegistro,fechaevento,horainicio,horafin)
        db.session.add(my_edicioneventos)
        db.session.commit()

        return redirect(url_for('consultarEdicionEventos'))

@app.route('/actualizarEdicionEventos', methods=['GET', 'POST'])
def actualizarEdicionEventos():
    if request.method == 'POST':
        my_edicioneventos = EdicionEventos.query.get(request.form.get('id'))
        my_edicioneventos.nombre = request.form['nombre']
        my_edicioneventos.fecharegistro = request.form['fecharegistro']
        my_edicioneventos.fechaevento = request.form['fechaevento']
        my_edicioneventos.horainicio = request.form['horainicio']
        my_edicioneventos.horafin = request.form['horafin']
        db.session.commit()

        return redirect(url_for('consultarEdicionEventos'))

@app.route('/eliminarEdicionEventos/<id>/', methods=['GET', 'POST'])
def eliminarEdicionEventos(id):
    my_edicioneventos = EdicionEventos.query.get(id)
    db.session.delete(my_edicioneventos)
    db.session.commit()

    return redirect(url_for('consultarEdicionEventos'))
#-----------------------------------------------------------------

#EQUIPOS////////////////////////////////////////////////////////////////////////
class Equipos (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    nodocente = db.Column(db.Integer, foreign_key=True)
    puntosobtenidos = db.Column(db.Integer)
    problemasresueltos = db.Column(db.Integer)
    nocontrolintegrante1 = db.Column(db.Integer, foreign_key=True)
    nocontrolintegrante2 = db.Column(db.Integer, foreign_key=True)
    nocontrolintegrante3 = db.Column(db.Integer, foreign_key=True)
    idcategoria = db.Column(db.Date, foreign_key=True)
    idedicion = db.Column(db.Date, foreign_key=True)

    def __init__(self,nombre,nodocente,puntosobtenidos,problemasresueltos,nocontrolintegrante1,nocontrolintegrante2,nocontrolintegrante3,idcategoria,idedicion):
        self.nombre = nombre
        self.nodocente=nodocente
        self.puntosobtenidos=puntosobtenidos
        self.problemasresueltos=problemasresueltos
        self.nocontrolintegrante1=nocontrolintegrante1
        self.nocontrolintegrante2=nocontrolintegrante2
        self.nocontrolintegrante3=nocontrolintegrante3
        self.idcategoria=idcategoria
        self.idedicion=idedicion

@app.route('/insertEquipos', methods = ['POST'])
def insertEquipos():

    if request.method == 'POST':
        nombre = request.form['nombre']
        nodocente=request.form['nodocente']
        puntosobtenidos=request.form['puntosobtenidos']
        problemasresueltos=request.form['problemasresueltos']
        nocontrolintegrante1=request.form['nocontrolintegrante1']
        nocontrolintegrante2=request.form['nocontrolintegrante2']
        nocontrolintegrante3=request.form['nocontrolintegrante3']
        idcategoria=request.form['idcategoria']
        idedicion=request.form['idedicion']

        my_equipo = Equipos(nombre, nodocente,puntosobtenidos,problemasresueltos,nocontrolintegrante1,nocontrolintegrante2,nocontrolintegrante3,idcategoria,idedicion)
        db.session.add(my_equipo)
        db.session.commit()

        return redirect(url_for('consultarEquipos'))

@app.route('/actualizarEquipos', methods=['GET', 'POST'])
def actualizarEquipos():
    if request.method == 'POST':
        my_equipo = EdicionEventos.query.get(request.form.get('id'))
        my_equipo.nombre = request.form['nombre']
        my_equipo.nodocente = request.form['nodocente']
        my_equipo.puntosobtenidos = request.form['puntosobtenidos']
        my_equipo.problemasresueltos = request.form['problemasresueltos']
        my_equipo.nocontrolintegrante1 = request.form['nocontrolintegrante1']
        my_equipo.nocontrolintegrante2 = request.form['nocontrolintegrante2']
        my_equipo.nocontrolintegrante3 = request.form['nocontrolintegrante3']
        my_equipo.idcategoria = request.form['idcategoria']
        my_equipo.idedicion = request.form['idedicion']
        db.session.commit()

        return redirect(url_for('consultarEquipos'))

@app.route('/eliminarEquipos/<id>/', methods=['GET', 'POST'])
def eliminarEquipos(id):
    my_equipo = Equipos.query.get(id)
    db.session.delete(my_equipo)
    db.session.commit()

    return redirect(url_for('consultarEquipos'))
#---------------------------------------------------------------------------------

#PROBLEMAS////////////////////////////////////////////////////////////////77
class Problemas (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombreproblema = db.Column(db.String(50))
    puntos = db.Column(db.Integer)
    tiempomaximo=db.Column(db.Time)
    descripcion=db.Column(db.String(200))

    def __init__(self, nombreproblema, puntos,tiempomaximo,descripcion):
        self.nombreproblema = nombreproblema
        self.puntos = puntos
        self.tiempomaximo=tiempomaximo
        self.descripcion=descripcion

@app.route('/insertProblemas', methods = ['POST'])
def insertProblemas():

    if request.method == 'POST':
        nombreproblema = request.form['nombreproblema']
        puntos = request.form['puntos']
        tiempomaximo = request.form['tiempomaximo']
        descripcion = request.form['descripcion']


        my_problema = Problemas(nombreproblema,puntos,tiempomaximo,descripcion)
        db.session.add(my_problema)
        db.session.commit()

        return redirect(url_for('consultarProblemas'))

@app.route('/actualizarProblemas', methods=['GET', 'POST'])
def actualizarProblemas():
    if request.method == 'POST':
        my_problema = Problemas.query.get(request.form.get('id'))
        my_problema.nombreproblema = request.form['nombreproblema']
        my_problema.puntos = request.form['puntos']
        my_problema.tiempomaximo = request.form['tiempomaximo']
        my_problema.descripcion = request.form['descripcion']

        db.session.commit()

        return redirect(url_for('consultarProblemas'))

@app.route('/eliminarProblemas/<id>/', methods=['GET', 'POST'])
def eliminarProblemas(id):
    my_problema = Problemas.query.get(id)
    db.session.delete(my_problema)
    db.session.commit()

    return redirect(url_for('consultarProblemas'))
#-----------------------------------------------------------------------

#PROBLEMAS_PROPUESTOS//////////////////////////////////////////////
class ProblemasPropuestos (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    noproblemas = db.Column(db.Integer,foreing_key=True)
    noedicion = db.Column(db.Integer,foreing_key=True)
    color=db.Column(db.String(7))

    def __init__(self, noproblemas, noedicion,color):
        self.noproblemas = noproblemas
        self.noedicion = noedicion
        self.color=color

@app.route('/insertProblemasPropuestos', methods = ['POST'])
def insertProblemasPropuestos():

    if request.method == 'POST':
        noproblemas = request.form['noproblemas']
        noedicion = request.form['noedicion']
        color = request.form['color']

        my_problemapropuesto = Problemas(noproblemas,noedicion,color)
        db.session.add(my_problemapropuesto)
        db.session.commit()

        return redirect(url_for('consultarProblemasPropuestos'))

@app.route('/actualizarProblemasPropuestos', methods=['GET', 'POST'])
def actualizarProblemasPropuestos():
    if request.method == 'POST':
        my_problemapropuesto = ProblemasPropuestos.query.get(request.form.get('id'))
        my_problemapropuesto.noproblemas = request.form['noproblemas']
        my_problemapropuesto.noedicion = request.form['noedicion']
        my_problemapropuesto.color = request.form['color']

        db.session.commit()

        return redirect(url_for('consultarProblemasPropuestos'))

@app.route('/eliminarProblemasPropuestos/<id>/', methods=['GET', 'POST'])
def eliminarProblemasPropuestos(id):
    my_problemapropuesto = ProblemasPropuestos.query.get(id)
    db.session.delete(my_problemapropuesto)
    db.session.commit()

    return redirect(url_for('consultarProblemasPropuestos'))
#------------------------------------------------------------------------

#PROBLEMAS RESUELTOS//////////////////////////////////////////////////////////
class ProblemasResueltos (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tiempoejecucion = db.Column(db.Time)
    noequipo = db.Column(db.Integer,foreign_key=True)
    puntos=db.Column(db.Integer)
    noproblemaspropuestos=db.Column(db.Integer,foreign_key=True)

    def __init__(self, tiempoejecucion, noequipo,puntos,noproblemaspropuestos):
        self.tiempoejecucion = tiempoejecucion
        self.noequipo=noequipo
        self.puntos = puntos
        self.noproblemaspropuestos=noproblemaspropuestos

@app.route('/insertProblemasResueltos', methods = ['POST'])
def insertProblemasResueltos():

    if request.method == 'POST':
        tiempoejecucion = request.form['tiempoejecucion']
        noequipo = request.form['noequipo']
        puntos = request.form['puntos']
        noproblemaspropuestos = request.form['noproblemaspropuestos']


        my_problemaresuelto = ProblemasResueltos(tiempoejecucion,noequipo,puntos,noproblemaspropuestos)
        db.session.add(my_problemaresuelto)
        db.session.commit()

        return redirect(url_for('consultarProblemasResueltos'))

@app.route('/actualizarProblemasResueltos', methods=['GET', 'POST'])
def actualizarProblemasResueltos():
    if request.method == 'POST':
        my_problemaresuelto = ProblemasResueltos.query.get(request.form.get('id'))
        my_problemaresuelto.teimpoejecucion = request.form['tiempoejecucion']
        my_problemaresuelto.noequipo = request.form['noequipo']
        my_problemaresuelto.puntos = request.form['puntos']
        my_problemaresuelto.problemaspropuestos = request.form['problemaspropuestos']

        db.session.commit()

        return redirect(url_for('consultarProblemasResueltos'))

@app.route('/eliminarProblemasResueltos/<id>/', methods=['GET', 'POST'])
def eliminarProblemasResueltos(id):
    my_problemaresuelto = ProblemasResueltos.query.get(id)
    db.session.delete(my_problemaresuelto)
    db.session.commit()

    return redirect(url_for('consultarProblemasResueltos'))
#----------------------------------------------------------------
@app.route('/docentes')
def consultarDocentes():
    all_docentes = Docentes.query.all()
    return render_template("Docentes/consultaDocentes.html", docentes=all_docentes)


@app.route('/usuarios')
def consultarUsuarios():
    all_usuarios = Usuarios.query.all()
    return render_template("Usuarios/consultaUsuarios.html", usuarios = all_usuarios)

@app.route('/alumnos')
def consultarAlumnos():
    all_alumnos = Alumnos.query.all()
    return render_template("Alumnos/consultaAlumnos.html", alumnos=all_alumnos)

@app.route('/carreras')
def consultarCarreras():
    all_carreras = Carreras.query.all()
    return render_template("Carreras/consultaCarreras.html", carreras=all_carreras)

@app.route('/categorias')
def consultarCategorias():
    all_categorias = Categorias.query.all()
    return render_template("Categorias/consultaCategorias.html", categorias=all_categorias)

@app.route('/edicioneventos')
def consultarEdicionEventos():
    all_edicioneventos = EdicionEventos.query.all()
    return render_template("Edicion_Eventos/consultaEdicionEventos.html", edicioneventos=all_edicioneventos)

@app.route('/equipos')
def consultarEquipos():
    all_equipos = Equipos.query.all()
    return render_template("Equipos/consultaEquipos.html",equipos=all_equipos)

@app.route('/problemas')
def consultarProblemas():
    all_problemas = Problemas.query.all()
    return render_template("Problemas/consultaProblemas.html", problemas=all_problemas)

@app.route('/problemaspropuestos')
def consultarProblemasPropuestos():
    all_problemaspropuestos = ProblemasPropuestos.query.all()
    return render_template("ProblemasPropuestos/consultaProblemasPropuestos.html", problemaspropuestos=all_problemaspropuestos)

@app.route('/problemasresueltos')
def consultarProblemasResueltos():
    all_problemasresueltos = ProblemasResueltos.query.all()
    return render_template("ProblemasResueltos/consultaProblemasResueltos.html",problemasresueltos=all_problemasresueltos)

@app.errorhandler(404)
def error_404(e):
    return render_template('comunes/error_404.html'), 404


@app.errorhandler(500)
def error_500(e):
    return render_template('comunes/error_500.html'), 500
'''
if __name__ == "__main__":
    app.run(debug=True)