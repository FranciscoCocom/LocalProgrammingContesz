function validar(form){
    var cad=validarIdCategoria(form.idcategoria.value);
        cad+=validarNombre(form.nombre.value);
        cad+=validarSemestreLimite(form.semestrelimite.value);
    var accion = form.accion.value;
    if(cad!=''){
        document.getElementById("notificaciones" + accion).innerHTML='<p>'+cad+'</p>';
        return false;
    } else{
        var accion = form.accion.value;
        if (accion == "crear"){
          alert("Crear");
        }else {
          alert("Editar")
        }
       return true;
    }
}

function validarIdCategoria(cad)
{
    if(cad==1 || cad==2){
        return '';
    }else{
        return "Id de categoria no valido <br>";
    }
}

function validarNombre(cad)
{
    if(cad.length==0){
        return 'Debes informar el nombre de la Categoria <br>';
    }else
    {
        return '';
    }
}

function validarSemestreLimite(cad)
{
    if(validarIdCategoria==1){
        if(cad>=1 && cad<=4){
            return " ";
        }else{
            return "Excediste el semestre limite para la categoria seleccionada";
        }
    }else if(validarIdCategoria==2){
        if(cad>=5 && cad<=12){
            return " ";
        }else{
            return " Excediste el semestre limite para la categoria(minimo 5°)"
        }
    }else{
        return "Número de semestre invalido <br>";
    }
}
///////////////////////////////////Aquí termina la validación///////////////////

//////////////////////////////////Aquí empieza la creación del objeto///////////
var arrayCategorias=[];
class Categoria
{
    constructor(idcategoria,nombre,semestrelimite)
    {
        this.idcategoria=idcategoria;
        this.nombre=nombre;
        this.semestrelimite=semestrelimite;
    }
    toString(){
        return "Id Categoria: "+this.idcategoria+", Nombre: "+this.nombre +
         ", semestre Limite: " + this.semestrelimite;
    }

    guardar() {
        //Almacenará el objeto en la BD
        arrayCategorias.push(this)
    }
    actualizar() {
        for(i=0;i<arrayCategorias.length;i++){
            if(arrayCategorias[i].id==this.id){
                arrayCategorias[i]=this;
            }
        }
    }

    eliminar(){
      alert("hola delete");
        for(i=0;i<arrayCategorias.length;i++){
            if(arrayCategorias[i].id==this.id){
                arrayCategorias.splice(i,1);
            }
        }
    }
    consultar()
    {
        for(i=0;i<arrayCategorias.length;i++){
            if(arrayCategorias[i].id==this.id){
                return arrayCategorias[i];
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