function validar(form)
{
        cad=validarNoDocente(form.nodocente.value);
        cad+=validarNoUsuario(form.nousuario.value);
        cad+=validarEscolaridad(form.escolaridad.value);
        cad+=validarEspecialidad(form.especialidad.value);
        cad+=validarCedula(form.cedula.value);
        cad+=validarIdCarrera(form.idcarrera.value);
        if(cad!=''){
            document.getElementById("notificaciones").innerHTML='<p>'+cad+'</p>';
            return false;
        }
        else{
           return true;
        }
}

function validarNoDocente(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else
    {
        return "Número de Docente invalido <br>"
    }
}

function validarNoUsuario(cad)
{
    if(cad>=1) {
        return '';
    }else
    {
        return "Número de Usuario invalido <br>"
    }
}

function validarEscolaridad(cad)
{
    if(cad.length==0) {
        return 'Debes informar la escolaridad <br>';
    }else
    return '';
}

function validarEspecialidad(cad)
{
    if(cad.length==0)
    {
        return 'Debes informar la Especialidad del Docente <br>';
    }
    else
    {
        return '';
    }
}

function validarCedula(cad)
{
    if(cad.length==7 || cad.length==8)
    {
        return '';
    }
    else
    {
        return "Introduce una cedula valida. <br>";
    }
}

function validarIdCarrera(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else
    {
        return "Id de carrera invalido <br>"
    }
}

//---------------------------------------------------------------------------------------
var arrayDocentes=[];
class Docente{
  constructor(noDocente,noUsuario,escolaridad,especialidad,cedula,idCarrera) //Aquí van los parametros de entrada,(las variables necesarias para construir la clase)
  {
      this.noDocente=noDocente;
      this.noUsuario=noUsuario;
      this.escolaridad=escolaridad;
      this.especialidad=especialidad;
      this.cedula=cedula;
      this.idCarrera=idCarrera;
  }

  toString() //Aquí se crea el método ToString
  {
    return "NoDocente: " + this.noDocente + ", NoUsuario: " + this.noUsuario + ", Escolaridad: " 
    + this.escolaridad + ", Especialidad: " + this.especialidad + ", Cedula: " + this.cedula
     + ", IdCarrera: " + this.idCarrera;
  }

  guardar()
  {
      arrayDocentes.push(this)
  }

  actualizar()
  {
      for(i=0;i<arrayDocentes.length;i++)
      {
          if(arrayDocentes[i].noDocente == this.noDocente)
          {
              arrayDocentes[i]=this;
          }
      }
  }

  eliminar()
  {
      for(i=0;i<arrayDocentes.length;i++)
      {
          if(arrayDocentes  [i].noDocente==this.noDocente)
          {
              arrayDocentes.splice(i,1);
          }
      }
  }

  consultar()
  {
      for(i=0;i<arrayDocentes.length;i++)
      {
          if(arrayDocentes[i].noDocente==this.noDocente)
          {
              return arrayDocentes[i];
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
