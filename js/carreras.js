function validar(form){
    var cad=validarIdCarrera(form.idcarrera.value);
        cad+=validarNombre(form.nombre.value);
        cad+=validarSiglas(form.siglas.value);
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


function validarIdCarrera(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "Id de carrera invalido invalido <br>";
    } 
}

function validarNombre(cad)
{
    if(cad.length==0)
    {
        return 'Debes informar el nombre de la carrera <br>';
    }
    else
    {
        return '';
    }
}

function validarSiglas(cad)
{
    if(cad>=1 && cad<=5)
    {
        return '';
    }
    else{
        return "Ingrese las siglas correctaas de la carrera <br>";
    }
}

///////////////////////////////////Aquí termina la validación///////////////////
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////Aquí empieza la creación del objeto///////////
var arrayCarreras=[];
class Carrera
{
    constructor(idcarrera,nombre,siglas)
    {
        this.idcarrera=idcarrera;
        this.nombre=nombre;
        this.siglas=siglas;
    }
    toString()
    {
        return "Id Carrera: "+this.idcarrera+", Nombre: "+this.nombre + ", Siglas: " + this.siglas;
    }

    guardar()
    {
        //Almacenará el objeto en la BD
        arrayCarreras.push(this)
    }
    actualizar()
    {
        for(i=0;i<arrayCarreras.length;i++){
            if(arrayCarreras[i].id==this.id){
                arrayCarreras[i]=this;
            }
        }
    }

    eliminar()
    {
      alert("hola delete");
        for(i=0;i<arrayCarreras.length;i++){
            if(arrayCarreras[i].id==this.id){
                arrayCarreras.splice(i,1);
            }
        }
    }
    consultar()
    {
        for(i=0;i<arrayCarreras.length;i++){
            if(arrayCarreras[i].id==this.id){
                return arrayCarreras[i];
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