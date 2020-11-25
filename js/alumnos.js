function validar(form){
    var cad=validarNoControl(form.nocontrol.value);
        cad+=validarNoUsuario(form.nousuario.value);
        cad+=validarSemestre(form.semestre.value);
        cad+=validarIdCarrera(form.idcarrera.value);
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


function validarNoControl(cad)
{
    var patron=/\d{8}/;
    if(patron.test(cad))
    {
        return '';
    }
    else{
        return "El número de control debe ser de 8 dígitos <br>";
    }
}

function validarNoUsuario(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "Número de Usuario invalido <br>";
    }
}

function validarSemestre(cad)
{
    if(cad>=1 && cad<=9)
    {
        return '';
    }
    else{
        return "Número de semestre invalido <br>";
    }
}

function validarIdCarrera(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else{
        return "Id de carrera invalido <br>";
    }
}
///////////////////////////////////Aquí termina la validación///////////////////
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////Aquí empieza la creación del objeto///////////
var arrayAlumnos=[];
class Alumno
{
    constructor(nocontrol,nousuario,semestre,idcarrera)
    {
        this.nocontrol=nocontrol;
        this.nousuario=nousuario;
        this.semestre=semestre;
        this.idcarrera=idcarrera;
    }
    toString()
    {
        return "Número control: "+this.nocontrol+", Número usuario: "+this.nousuario + ", semestre: " + this.semestre + ", ID carrera: " + this.idcarrera;
    }

    guardar()
    {
        //Almacenará el objeto en la BD
        arrayAlumnos.push(this)
    }
    actualizar()
    {
        for(i=0;i<arrayAlumnos.length;i++){
            if(arrayAlumnos[i].id==this.id){
                arrayAlumnos[i]=this;
            }
        }
    }

    eliminar()
    {
      alert("hola delete");
        for(i=0;i<arrayAlumnos.length;i++){
            if(arrayAlumnos[i].id==this.id){
                //delete arrayEdificios[i];
                arrayAlumnos.splice(i,1);
            }
        }
    }
    consultar()
    {
        for(i=0;i<arrayAlumnos.length;i++){
            if(arrayAlumnos[i].id==this.id){
                return arrayAlumnos[i];
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
