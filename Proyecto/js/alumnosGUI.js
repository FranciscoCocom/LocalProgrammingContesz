var op="";

function delete() {
  alert("metodo delete");
op="d";

}

function realizarOperacion(){
    var obj;
    switch(op){
        case "c":
        obj=new Alumno(
          document.getElementById("nocontrol").value,
          document.getElementById("nousuario").value,
          document.getElementById("semestre").value,
          document.getElementById("idcarrera").value);
            obj.guardar();
            break;
        case "u":
        obj=new Alumno(
          document.getElementById("nocontrol").value,
          document.getElementById("nousuario").value,
          document.getElementById("semestre").value,
          document.getElementById("idcarrera").value);
            obj.actualizar();
            break;
        case "d":
            obj=new Alumno(
              document.getElementById("nocontrol").value,
              document.getElementById("nousuario").value,
              document.getElementById("semestre").value,
              document.getElementById("idcarrera").value);
            obj.eliminar();
              break;
    }
}
