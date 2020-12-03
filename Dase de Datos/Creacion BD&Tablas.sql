create database ConTESZ;
use ConTESZ;

/*creacion de tablas*/
create table Carreras(
idCarrera int not null,
nombre varchar(100),
sigla varchar(5),
constraint pk_Carreras primary key(idCarrera)
);
/*TERMINA TABLA CARRERAS*/

create table Docentes(
noDocente int not null,
idUsusario int not null,
idCarrera int not null,
escolaridad varchar(50) not null,
especialidad varchar(50) not null,
cedula varchar(50) not null,
constraint pk_Docentes primary key(noDocente)
);
/*TERMINA LA TABLA DOCENTES*/

create table Usuarios(
idUsuario int not null,
nombreCompleto varchar (50) not null,
sexo char not null,
telefono int,
correo varchar(50) not null,
estatus varchar(50) not null,
tipoUsuario varchar (10) not null,
contraseña varchar (50) not null,
constraint pk_Usuarios primary key(idUsuario)
);
/*TERMINA TABLA USUARIOS*/

create table Alumnos(
noControl varchar(8) not null,
idUsuario int not null,
semestre int not null,
idCarrera int not null,
constraint pk_Alumnos primary key(noControl)
);
/*TERMINA LA TABLA ALUMNOS*/

create table Categorias(
idCategoria int not null,
nombre varchar(50) not null,
semestreLimite int not null,
constraint pk_Categorias primary key(idCategoria)
);
/*TERMINA TABLA CATEGORIAS*/

create table Equipos(
idEquipo int not null,
nombre varchar(50) not null,
noDocente int not null,
puntosObtenidos float not null,
problemasResueltos int,
noEquipo int not null,
alu_noControl1 varchar(8) not null,
alu_noControl2 varchar(8) not null,
alu_noControl3 varchar(8) not null,
idCategoria int not null,
idEdicion int not null,
constraint pk_Equipos primary key(idEquipo)
);
/*TERMINA TABLA EQUIPOS*/

create table Edicion_Eventos(
idEdicion int not null,
nombre varchar(50),
fechaRegistro date not null,
fechaEvento date not null,
horaInicio time not null,
horaFin time,
constraint pk_EdicionEventos primary key(idEdicion)
);
/*TERMINA LA TABLA EDICION EVENTOS*/

create table Problemas_Propuestos(
idProblemas int not null,
idProblemasPropuestos int not null,
idEdicion int not null,
idCategoria int not null,
color varchar(10) not null,
constraint pk_ProblemasPropuestos primary key(idProblemasPropuestos)
);
/*TERMINA LA TABLA PROBLEMAS PROPUESTOS*/

create table Problemas(
idProblemas int not null,
nombre varchar(200) not null,
puntos float not null,
tiempoMax int not null,
descripcion varchar(200) not null,
constraint pk_Problemas primary key(idProblemas)
);
/*TERMINA LA TABLA DE PROBLEMAS*/

create table Problemas_Resueltos(
problemaResuelto int not null,
tiempoEjecucion int not null,
idEquipo int not null,
puntos float not null,
idProblemasPropuestos int not null,
constraint pk_Problemas_Resueltos primary key(ProblemaResuelto)
);

/* --------------------RESTRICCIONES-------------------------------*/

alter table Carreras add constraint chk_sigla check (sigla='ISC' or sigla='ITICS');
alter table Carreras add constraint uk_idCarrera unique(idCarrera);


alter table Docentes add constraint fk_Docentes_Usuarios foreign key(idUsusario) references Usuarios(idUsuario);
alter table Docentes add constraint fk_Docentes_Carreras foreign key(idCarrera) references Carreras(idCarrera);
alter table Docentes add constraint uk_noDocente unique (noDocente);
alter table Docentes add constraint uk_cedula unique (cedula);

alter table Usuarios add constraint chk_email check (correo like '%@%.%');
alter table Usuarios add constraint chk_tipo check (tipoUsuario in('Alumno','Docente','Administrador'));
alter table Usuarios add constraint chk_estatus check (estatus='Activo' or estatus='Inactivo');
alter table Usuarios add constraint chk_telefono check (telefono like '[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]');
alter table Usuarios add constraint chk_sexo check(Sexo in('F','M'));
alter table Usuarios add constraint uk_idUsuario unique (idUsuario);
alter table Usuarios add constraint uk_telefonoUsuario unique (telefono);

alter table Alumnos add constraint fk_Alumnos_Usuarios foreign key(idUsuario) references Usuarios(idUsuario);
alter table Alumnos add constraint fk_Alumnos_Carreras foreign key(idCarrera) references Carreras(idCarrera);
alter table Alumnos add constraint chk_noControl check(noControl like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]');
alter table Alumnos add constraint chk_semestre check(semestre like '[1-12]');
alter table Alumnos add constraint uk_noControl unique (noControl);

alter table Categorias add constraint uk_categorias unique (idCategoria);

alter table Equipos add constraint fk_Equipos_Alumnos foreign key(alu_noControl1) references Alumnos(noControl);
alter table Equipos add constraint fk_Equipos_Alumnos2 foreign key(alu_noControl2) references Alumnos(noControl);
alter table Equipos add constraint fk_Equipos_Alumnos3 foreign key(alu_noControl3) references Alumnos(noControl);
alter table Equipos add constraint fk_Equipos_Categorias foreign key(idCategoria) references Categorias(idCategoria);
alter table Equipos add constraint fk_Equipos_EdicionEventos foreign key(idEdicion) references Edicion_Eventos(idEdicion);
alter table Equipos add constraint fk_Equipos_Docentes foreign key(noDocente) references Docentes(noDocente);
alter table Equipos add constraint uk_Equipo unique (idEquipo);
alter table Equipos add constraint uk_nombreEquipo unique (nombre);

alter table Edicion_Eventos add constraint chk_horaInicioFin check (horaInicio<horaFin);
alter table Edicion_Eventos add constraint uk_Eventos unique (idEdicion);

alter table Problemas_Propuestos add constraint fk_ProblemasPropuestos foreign key(idProblemas) 
references Problemas(idProblemas);
alter table Problemas_Propuestos add constraint fk_ProPropuestosEdicion foreign key(idEdicion) 
references Edicion_Eventos(idEdicion);
alter table Problemas_Propuestos add constraint fk_ProPropuestosCateg foreign key(idCategoria) 
references Categorias(idCategoria);
alter table Problemas_Propuestos add constraint uk_ProblePropuesto unique (idProblemasPropuestos);

alter table Problemas add constraint chk_puntos check(puntos like '[0-100]');
alter table Problemas add constraint chk_tiempoMax check(tiempoMax<'1:00:00');
alter table Problemas add constraint uk_Problemas unique (idProblemas);

alter table Problemas_Resueltos add constraint fk_ProblemasRes_ProbPropuesto foreign key(idProblemasPropuestos)
references Problemas_Propuestos(idProblemasPropuestos);
alter table Problemas_Resueltos add constraint fk_ProblemaResuelto_Equipos foreign key(idEquipo) 
references Equipos(idEquipo);
alter table Problemas_Resueltos add constraint uk_ProbResuelto unique (ProblemaResuelto);
