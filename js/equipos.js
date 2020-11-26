function validar(form)
{//FALTA HACER CADA UNA DE LAS FUNCIONES Y VERFIFICAR LOS HTML
        cad=validarIdEquipo(form.idequipo.value);
        cad+=validarNombre(form.nombre.value);
        cad+=validarNoDocente(form.nodocente.value);
        cad+=validarPuntosobtenidos(form.puntosobtenidos.value);
        cad+=validarProblemaResuelto(form.problemaresuelto.value);
        cad+=validarNoControlIntegrante1(form.NoControlIntegrante1.value);
        cad+=validarNoControlIntegrante2(form.NoControlIntegrante2.value);
        cad+=validarNoControlIntegrante3(form.NoControlIntegrante3.value);
        cad+=validarIdCategoria(form.idcategoria.value);
        cad+=validarIdEdicion(form.idedicion.value);
        var accion = form.accion.value;
        if(cad!=''){
            document.getElementById("notificaciones").innerHTML='<p>'+cad+'</p>';
            return false;
        }
        else{
          var accion = form.accion.value;
          if (accion == "crear")
          {
            alert("Crear");
          }else {
            alert("Editar")
          }
         return true;
        }
}

function validarIdEquipo(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else
    {
        return "Id de Equipo invalido <br>"
    }
}

function validarNombre(cad)
{
    if(cad.length==0)
    {
        return 'Debes informar el nombre del equipo <br>';
    }
    else
    {
        return '';
    }
}

function validarNoDocente(cad)
{
    if(cad>=1)
    {
        return ' ';
    }
    return 'Debes ingresar un No de Docente ';
}

function validarPuntosobtenidos(cad)
{
    var ban=false;
    if(cad>=0 && cad<=100)
    {
       
           return '';
    }
    else{
        return 'Solo se puede dar un maximo de calificacion de 100. <br>'
    }
}

function validarProblemaResuelto(cad)
{
    if(cad.length==0)
    {
        return 'Debes informar el problema que se resolvio.<br>';
    }
    else
    {
        return '';
    }
}

function validarNoControlIntegrante1(cad)
{
    var patron=/\d{8}/;
    if(patron.test(cad))
    {
        if(cad==validarNoControlIntegrante2.cad || cad==validarNoControlIntegrante3.cad){
            return 'Deben ser No de control diferentes ';
        }else{
            return ' ';
        }
    }
    else{
        return "El número de control debe ser de 8 dígitos <br>";
    }
}

function validarNoControlIntegrante2(cad)
{
    var patron=/\d{8}/;
    if(patron.test(cad))
    {
        if(cad==validarNoControlIntegrante1.cad || cad==validarNoControlIntegrante3.cad){
            return 'Deben ser No de control diferentes ';
        }else{
            return ' ';
        }
    }
    else{
        return "El número de control debe ser de 8 dígitos <br>";
    }
}

function validarNoControlIntegrante3(cad){
    var patron=/\d{8}/;
    if(patron.test(cad))
    {
        if(cad==validarNoControlIntegrante2.cad || cad==validarNoControlIntegrante1.cad){
            return 'Deben ser No de control diferentes ';
        }else{
            return ' ';
        }
    }
    else{
        return "El número de control debe ser de 8 dígitos <br>";
    }
}

function validarIdEdicion(){
    if(cad>=1)
    {
        return '';
    }
    else
    {
        return "Id de Edicion invalido <br>"
    }
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////---Aquí se crea el objeto---////////////////////////////////////////////
var arrayEquipos=[];
class Equipo{
  constructor(idEquipo,nombre,noDocente,puntosObtenidos,problemasResueltos,NoControlIntegrante1,NoControlIntegrante2,NoControlIntegrante3,idCategoria,idEdicion) //Aquí van los parametros de entrada,(las variables necesarias para construir la clase)
  {
      this.idEquipo=idEquipo;
      this.nombre=nombre;
      this.noDocente=noDocente;
      this.puntosObtenidos=puntosObtenidos;
      this.problemasResueltos=problemasResueltos;
      this.NoControlIntegrante1=NoControlIntegrante1;
      this.NoControlIntegrante2=NoControlIntegrante2;
      this.NoControlIntegrante3=NoControlIntegrante3;
      this.idCategoria=idCategoria;
      this.idEdicion=idEdicion;
  }

  toString() //Aquí se crea el método ToString
  {
    return "Id Equipo: " + this.idEquipo + ", Nombre: " + this.nombre + 
    ", No Docente: " + this.noDocente + ", Puntos Obtenidos: " + this.puntosObtenidos
    + ", Problemas Resueltos: " + this.problemasResueltos + ", No Control Integrante1: " + this.NoControlIntegrante1
    + ", No Control Integrante2: " + this.NoControlIntegrante2+", No Control Integrante3: "+this.NoControlIntegrante3
    +", Id Categoria: "+this.idCategoria+", Id Edicion: "+this.idEdicion;
  }

  guardar()
  {
      //Almacenará el objeto en la BD
      arrayEquipos.push(this)
  }

  actualizar()
  {
      for(i=0;i<arrayEquipos.length;i++)
      {
          if(arrayEquipos[i].id == this.id)
          {
              arrayEquipos[i]=this;
          }
      }
  }

  eliminar()
  {
      for(i=0;i<arrayEquipos.length;i++)
      {
          if(arrayEquipos[i].id==this.id)
          {
              arrayEquipos.splice(i,1);
          }
      }
  }

  consultar()
  {
      for(i=0;i<arrayEquipos.length;i++)
      {
          if(arrayEquipos[i].id==this.id)
          {
              return arrayEquipos[i];
          }
      }
      return null;
  }
}

function mostrarDiv(){
    document.getElementById("modalEliminacion").style.display="block";
}
function ocultarDiv(){
    document.getElementById("modalEliminacion").style.display="none";
}
///////////////////////////////////////////---Aquí se crea el objeto---///////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
