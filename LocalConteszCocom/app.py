from flask import Flask,render_template,request,abort,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin


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

class Data(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))


    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

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

@app.route('/principal')
def principal():
    return render_template("principal.html")

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

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

        return render_template("principal.html")

@app.route('/hola')
def consultarData():
    return render_template("prueba.html")

@app.route('/docentes')
def consultarDocentes():
    return render_template("Docentes/consultaDocentes.html")

@app.route('/usuarios')
def consultarUsuarios():
    return render_template("Usuarios/consultaUsuarios.html")

if __name__ == "__main__":
    app.run(debug=True)