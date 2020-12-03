function validar(form)
{
        cad=validarIdProblema(form.idproblema.value);
        cad+=validarNombreProblema(form.nombreproblema.value);
        cad+=validarPuntos(form.puntos.value);
        cad+=validarTiempoMaximo(form.tiempomaximo.value);
        cad+=validarDescripcionProblema(form.descripcionproblema.value);
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

function validarIdProblema(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else
    {
        return "Id de problema invalido <br>"
    }
}

function validarNombreProblema(cad)
{
    if(cad.length==0)
    {
        return 'Debes informar el nombre del problema <br>';
    }
    else
    {
        return '';
    }
}

function validarPuntos(cad)
{
    if(cad>=0 || cad<=100)
    {
        return '';
    }
    return 'Debes dar los puntos en el rango de 0 a 100<br>';
}

function validarTiempoMaximo(cad)
{
    if(cad>=0 && cad<=60){
        return ' ';
    }else{
        return 'Se ha excedido de tiempo, ingrese tiempo valido';
    }
}

function validarDescripcionProblema(cad)
{
    if(cad.length==0)
    {
        return 'Debes colocar la descripcion del problema<br>';
    }
    return '';
}

///////////////////////////////////////////---Aquí se crea el objeto---////////////////////////////////////////////
var arrayProblemas=[];
class Problema{
  constructor(idProblema,nombreProblema,puntos,tiempoMaximo,descripcionProblema) //Aquí van los parametros de entrada,(las variables necesarias para construir la clase)
  {
      this.idProblema=idProblema;
      this.nombreProblema=nombreProblema;
      this.puntos=puntos;
      this.descripcionProblema=descripcionProblema;
  }

  toString() //Aquí se crea el método ToString
  {
    return "Id Problema: " + this.idProblema + 
    ", Nombre del Problema: " + this.nombreProblema + 
    ", Puntos: " + this.puntos + 
    ", Descripcion del problema: " + this.descripcionProblema;
  }

  guardar()
  {
      //Almacenará el objeto en la BD
      arrayProblemas.push(this)
  }

  actualizar()
  {
      for(i=0;i<arrayProblemas.length;i++)
      {
          if(arrayProblemas[i].id == this.id)
          {
              arrayProblemas[i]=this;
          }
      }
  }

  eliminar()
  {
      for(i=0;i<arrayProblemas.length;i++)
      {
          if(arrayProblemas[i].id==this.id)
          {
              arrayProblemas.splice(i,1);
          }
      }
  }

  consultar()
  {
      for(i=0;i<arrayProblemas.length;i++)
      {
          if(arrayProblemas[i].id==this.id)
          {
              return arrayProblemas[i];
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
