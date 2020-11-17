var op="";

function nuevo(){
    op="c";
}

function realizarOperacion()
{
    var obj;
    switch(op){
        case "c":
            obj=new Usuario(
                document.getElementById("nousuario").value,
                document.getElementById("nombre").value,
                document.getElementById("sexo").value,
                document.getElementById("telefono").value,
                document.getElementById("email").value,
                document.getElementById("estatus").value,
                document.getElementById("tipousuario").value,
                document.getElementById("password").value,
                document.getElementById("pwdrepite").value);
            obj.guardar();
            consultaGeneral();
            break;
        case "u":
            obj=new Edificio(
              document.getElementById("nousuario").value,
              document.getElementById("nombre").value,
              document.getElementById("sexo").value,
              document.getElementById("telefono").value,
              document.getElementById("email").value,
              document.getElementById("estatus").value,
              document.getElementById("tipousuario").value,
              document.getElementById("password").value,
              document.getElementById("pwdrepite").value);
            obj.actualizar();
            consultaGeneral();
            break;
    }
}


function consultaGeneral(){
    var table=document.getElementById("datos");
    //eliminarTabla();
    for(i=0;i<arrayUsuarios.length;i++){
        var tr=document.createElement("tr");
        var objeto=arrayUsuarios[i];
        for(p in objeto){
           var td=document.createElement("td");
           var txt=document.createTextNode(objeto[p]);
           td.appendChild(txt);
           tr.appendChild(td);

        }
        var link=crearLink(arrayUsuarios[i].id,"editar");
        var td=document.createElement("td");
        td.appendChild(link);
        tr.appendChild(td)
        link=crearLink(arrayUsuarios[i].id,"eliminar");
        td=document.createElement("td");
        td.appendChild(link);
        tr.appendChild(td)
        table.appendChild(tr);
    }
}

function crearLink(id,operacion){
    var link=document.createElement("a");
    var img=document.createElement("img");
    img.setAttribute("src","../Imagenes/"+operacion+".png");
    link.appendChild(img);
    link.setAttribute("href","javascript:"+operacion+"("+id+")");
    return link;
}

function editar(id){
    op="u";
    var obj=new Usuario(id,"","","","","","","","");
    var obj2=obj.consultar();
    document.getElementById("id").value=obj2.id;
    document.getElementById("nombre").value=obj2.nombre;
    document.getElementById("sexo").value=obj2.sexo;
    document.getElementById("telefono").value=obj2.telefono;
    document.getElementById("email").value=obj2.email;
    document.getElementById("estatus").value=obj2.estatus;
    document.getElementById("tipousuario").value=obj2.tipoUsuario;
    document.getElementById("password").value=obj2.password;
    document.getElementById("pwdrepite").value=obj2.pwdrepite;
}
