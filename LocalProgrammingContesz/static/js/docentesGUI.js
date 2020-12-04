var op="";

function nuevo(){
    op="c";
}

function realizarOperacion()
{
    var obj;
    switch(op){
        case "c":
            obj=new Docente(
                document.getElementById("nodocente").value,
                document.getElementById("nousuario").value,
                document.getElementById("escolaridad").value,
                document.getElementById("especialidad").value,
                document.getElementById("cedula").value,
                document.getElementById("idcarrera").value;
            obj.guardar();
            consultaGeneral();
            break;
        case "u":
            obj=new Docente(
                document.getElementById("nodocente").value,
                document.getElementById("nousuario").value,
                document.getElementById("escolaridad").value,
                document.getElementById("especialidad").value,
                document.getElementById("cedula").value,
                document.getElementById("idcarrera").value;
             obj.actualizar();
            consultaGeneral();
            break;
    }
}


function consultaGeneral(){
    var table=document.getElementById("datos");
    //eliminarTabla();
    for(i=0;i<arrayDocentes.length;i++){
        var tr=document.createElement("tr");
        var objeto=arrayDocentes[i];
        for(p in objeto){
           var td=document.createElement("td");
           var txt=document.createTextNode(objeto[p]);
           td.appendChild(txt);
           tr.appendChild(td);

        }
        var link=crearLink(arrayDocentes[i].id,"editar");
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
    var obj=new Docente(nodocente,"","","","","");
    var obj2=obj.consultar();
    document.getElementById("nodocente").value=obj2.nodocente;
    document.getElementById("nousuario").value=obj2.nousuario;
    document.getElementById("escolaridad").value=obj2.escolaridad;
    document.getElementById("especialidad").value=obj2.especialidad;
    document.getElementById("cedula").value=obj2.cedula;
    document.getElementById("idcarrera").value=obj2.idcarrera;
    }
