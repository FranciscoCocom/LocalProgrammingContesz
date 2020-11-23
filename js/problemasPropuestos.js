function validar(form){
    var cad=validarNoProblemas(form.noproblemas.value);
        cad+=validarNoProblemasPropuestos(form.noproblemaspropuestos.value);
        cad+=validarNoEdicion(form.noedicion.value);
        cad+=validarColor(form.color.value);
    var accion = form.accion.value;
    if(cad!=''){
        document.getElementById("notificaciones" + accion).innerHTML='<p>'+cad+'</p>';
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

function validarNoProblemas(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "Número de problema invalido <br>";
    }
}

function validarNoProblemasPropuestos(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "Número de problema propuesto invalido <br>";
    }
}

function validarNoEdicion(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "Número de problema invalido <br>";
    }
}

function validarColor(cad)
{
  if(cad==0)
  {
      return 'Debes elegir un color<br>';
  }
  return '';
}
