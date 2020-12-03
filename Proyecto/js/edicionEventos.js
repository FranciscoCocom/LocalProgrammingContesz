function validar(form){
    var cad=validarIdEvento(form.idevento.value);
        cad+=validarNombreEvento(form.nombre.value);
        cad+=validarFechaRegistro(form.fecharegistro.value);
        cad+=validarFechaEvento(form.fechaevento.value);
        cad+=validarHoraInicio(form.horainicio.value);
        cad+=validarHoraFin(form.horafin.value);
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

function validarIdEvento(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "Número de evento invalido <br>";
    }
}

function validarNombreEvento(cad)
{
    if(cad.length==0)
    {
        return 'Debes informar el nombre del evento <br>';
    }
    else
    {
        return '';
    }
}

function validarFechaRegistro(cad)
{
  if (cad==0)
  {
      return 'Debes informar la fecha de registro <br>';
  }else
  {
      return '';
  }
}

function validarFechaEvento(cad)
{
  if (cad==0)
  {
      return 'Debes informar la fecha del evento <br>';
  }else
  {
      return '';
  }
}

function validarHoraInicio(cad)
{
  if (cad==0)
  {
      return 'Debes informar la hora de inicio <br>';
  }else
  {
      return '';
  }
}

function validarHoraFin(cad)
{
  if (cad==0)
  {
      return 'Debes informar la hora de terminación <br>';
  }else
  {
      return '';
  }
}

function mostrarDiv(){
    document.getElementById("modalEliminacion").style.display="block";
}
function ocultarDiv(){
    document.getElementById("modalEliminacion").style.display="none";
}
