from flask import Flask,render_template,request,abort,redirect,url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:eltolok.1@localhost/localprogrammingcontesz'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class usuarios(db.Model):
    idUsuario = db.Column(db.Integer, primary_key = True)
    nombreCompleto = db.Column(db.String(100))
    sexo = db.Column(db.String(1))
    telefono = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    estatus = db.Column(db.String(50))
    tipoUsuario = db.Column(db.String(50))
    contraseña = db.Column(db.String(50))

    def __init__(self,nombreCompleto,sexo,telefono,correo,estatus,tipoUsuario,contraseña):
        self.nombreCompleto = nombreCompleto
        self.sexo = sexo
        self.telefono = telefono
        self.correo = correo
        self.estatus = estatus
        self.tipoUsuario = tipoUsuario
        self.contraseña = contraseña

        my_usuarios = usuarios(nombreCompleto,sexo,telefono,correo,estatus,tipoUsuario,contraseña)
        db.session.add(my_usuarios)
        db.session.commit()

        return redirect(url_for('index.html'))

@app.route('/')
def principal():
    return render_template("principal.html")

@app.route('/insert', methods = ['post'])
def insert():

    if request.method == 'post':
        nombreCompleto = request.form['nombre']
        sexo = request.form['sexo']
        telefono = request.form['telefono']
        correo = request.form['email']
        estatus = request.form['estatus']
        tipoUsuarip = request.form['tipousuario']
        constraseña = request.form['password']



@app.route('/docentes')
def consultarDocentes():
    return render_template("Docentes/consultaDocentes.html")

@app.route('/usuarios')
def consultarUsuarios():
    return render_template("Usuarios/consultaUsuarios.html")

if __name__ == "__main__":
    app.run(debug=True)