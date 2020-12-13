from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,String,Column,ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()




class Categorias(db.Model):
    __tablename__ = 'Categorias'
    idcategoria=Column(Integer, primary_key=True)
    nombre=Column(String, unique=True)
    semestrelimite=Column(Integer)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        categoria=self.consultaIndividual()
        db.session.delete(categoria)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def consultaIndividual(self):
        return self.query.get(self.idcategoria)
    equipos=relationship('Equipos', backref='categoria', lazy="dynamic")
    pass

class Carreras(db.Model):
    __tablename__='Carreras'
    idcarrea=Column(Integer,primary_key=True)
    nombre=Column(String,unique=True)
    siglas=Column(String,unique=True)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        carrera = self.consultaIndividual()
        db.session.delete(carrera)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.idcarrea)
    alumnos=relationship('Alumno', backref='carrera', lazy='dynamic')
    docentes=relationship('Docente', backref='carrera', lazy='dynamic')

class Usuarios(UserMixin,db.Model):
    __tablename__='Usuarios'
    nousuario=Column(Integer,primary_key=True)
    nombre=Column(String,nullable=False)
    sexo=Column(String,nullable=False)
    telefono=Column(String,nullable=False)
    email = Column(String, nullable=False)
    estatus = Column(String, nullable=False)
    tipousuario = Column(String, nullable=False)
    password_hash = Column(String(128), nullable=False)

    #Métodos para el cifrado de la contraseña

    @property
    def password(self):
        raise AttributeError('El atributo password no es un atributo de lectura')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def validarPassword(self, password):
        return check_password_hash(self.password_hash, password)

    #metodos del CRUD
    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self.consultaIndividual())
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.idUsuario)
    #Metodos para el perfilamiento de los usuarios

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def is_active(self):
        if self.estatus == 'Activo':
            return True
        else:
            return False

    def is_admin(self):
        if self.tipousuario == 'Administrador':
            return True
        else:
            return False

    def is_docente(self):
        if self.tipousuario == 'Docente':
            return True
        else:
            return False

    def getTipo(self):
        return self.tipo

    def get_id(self):
        return self.idUsuario

    def validar(self, email, password):
        user=Usuarios.query.filter_by(email=email, estatus='Activo').first()
        if user!=None:
            if user.validarPassword(password):
                return user
            else:
                return None
        else:
            return None

    alumnos = relationship('Alumno', backref='usuario', lazy='dynamic')
    docentes = relationship('Docente', backref='usuario', lazy='dynamic')

class Alumnos(db.Model):
    __tablename__ = 'Carreras'
    nocontrol = Column(Integer, primary_key=True)
    nousuario = Column(Integer, ForeignKey(Usuarios.nousuario), unique=True)
    semestre = Column(Integer)
    idcarrera = Column(Integer, ForeignKey(Carreras.idcarrera))

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        alumno = self.consultaIndividual()
        db.session.delete(alumno)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.nocontrol)
    equipos=relationship('Equipo',backref='alumno',lazy='dynamic')

    pass

class Docentes(db.Model):
    __tablename__ = 'Docentes'
    nodocente = Column(Integer, primary_key=True)
    nousuario = Column(String, ForeignKey(Usuarios.nousuario), unique=True)
    escolaridad = Column(String)
    especialidad= Column(String)
    cedula=Column(Integer,unique=True)
    idcarrera=Column(Integer,ForeignKey(Carreras.idcarrea))

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        docente = self.consultaIndividual()
        db.session.delete(docente)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.nodocente)
    equipos=relationship('equipo', backref='docente', lazy='dynamic')

    pass

class Edicion_Eventos(db.Model):
    __tablename__ = 'Edicion_Eventos'
    idevento = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)
    fecharegistro = Column(Date)
    fechaevento = Column(Date)
    horainicio = Column(Time)
    horafin = Column(Time)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        edicion_evento = self.consultaIndividual()
        db.session.delete(edicion_evento)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.idevento)
    equipos=relationship('Equipo',backref='edicion_evento', lazy='dynamic')
    problemas_propuestos=relationship('Problema_Resuelto',backref='edicion_evento', lazy='dynamic')

    pass

class Equipos(db.Model):
    __tablename__ = 'Equipos'
    idequipo = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)
    nodocente = Column(Integer, ForeignKey('Docentes.nodocente'))
    puntosobtenidos = Column(Integer)
    problemasresueltos= Column(Integer, ForeignKey('Problemas_Resueltos.problemaresuelto'))
    nocontrolintegrante1 = Column(Integer, ForeignKey('Alumnos.nocontrol'), unique=True)
    nocontrolintegrante2 = Column(Integer, ForeignKey('Alumnos.nocontrol'), unique=True)
    nocontrolintegrante3 = Column(Integer, ForeignKey('Alumnos.nocontrol'), unique=True)
    idcategoria=Column(Integer,ForeignKey('Categorias.idcategoria'),unique=True)
    idedicion=Column(Integer,ForeignKey('Edicion_Eventos.idevento'),unique=True)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        equipo = self.consultaIndividual()
        db.session.delete(equipo)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.idequipo)
    problemas_resueltos=relationship('problema_resuelto',backref='equipo',lazy='dynamic')
    pass

class Problemas(db.Model):
    __tablename__ = 'Problemas'
    idproblema = Column(Integer, primary_key=True)
    nombreproblema = Column(String, unique=True)
    puntos = Column(Integer)
    tiempomaximo = Column(Integer)
    descripcion = Column(String,unique=True)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        problema = self.consultaIndividual()
        db.session.delete(problema)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.idproblema)
    problemas_propuestos=relationship('Problema_Propuesto', backref='problema',lazy='dynamic')

    pass

class Problemas_Propuestos(db.Model):
    __tablename__ = 'Problemas_Propuestos'
    noproblemas = Column(Integer, ForeignKey(Problemas.idproblema))
    noproblemaspropuestos = Column(Integer, primary_key=True, unique=True)
    noedicion = Column(Integer, ForeignKey(Edicion_Eventos.idevento))
    #color = Column(color)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        problema_propuesto = self.consultaIndividual()
        db.session.delete(problema_propuesto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.noproblemaspropuestos)
    problemas_resueltos=relationship('problema_resuelto', backref='problema_propuesto', lazy='dynamic')

    pass

class Problemas_Resueltos(db.Model):
    __tablename__ = 'Problemas_Resueltos'
    problemaresuelto = Column(Integer, primary_key=True, unique=True)
    tiempoejecucion = Column(Integer)
    noequipo = Column(Integer, ForeignKey('Equipos.idequipo'))
    puntos=Column(Integer)
    noproblemaspropuestos=Column(Integer, ForeignKey('Problemas_Propuestos.noproblemaspropuestos'),unique=True)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        problema_resuelto = self.consultaIndividual()
        db.session.delete(problema_resuelto)
        db.session.commit()

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self):
        return self.query.get(self.problemaresuelto)

    pass
