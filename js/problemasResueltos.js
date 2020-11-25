function validar(form){
    var cad=validarProblemaResuelto(form.problemaresuelto.value);
        cad+=validarTiempoEjecución(form.tiempoejecucion.value);
        cad+=validarNoEquipo(form.noequipo.value);
        cad+=validarPuntos(form.puntos.value);
        cad+=validarNoProblemasPropuestos(form.noproblemaspropuestos.value);
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

function validarProblemaResuelto(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "Número de problema resuelto invalido <br>";
    }
}

function validarTiempoEjecución(cad)
{
    if(cad>=0)
    {
        return '';
    }
    else{
        return "Tiempo de ejecución invalido <br>";
    }
}

function validarNoEquipo(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "Número de equipo invalido <br>";
    }
}

function validarPuntos(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "Número de puntos invalido <br>";
    }
}

function validarNoProblemasPropuestos(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "Número de problemas propuestos invalido <br>";
    }
}
function mostrarDiv(){
    document.getElementById("modalEliminacion").style.display="block";
}
function ocultarDiv(){
    document.getElementById("modalEliminacion").style.display="none";
}
