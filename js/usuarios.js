function validar(form)
{
        cad=validarNoUsuario(form.nousuario.value);
        cad+=validarNombre(form.nombre.value);
        cad+=validarSexo(form.sexo.value);
        cad+=validarTelefono(form.telefono.value);
        cad+=validarEmail(form.email.value);
        cad+=validarEstatus(form.estatus.value);
        cad+=validarTipoUsuario(parseInt(form.tipousuario.options[form.tipousuario.options.selectedIndex].value));
        cad+=validarPasssword(form.password.value,form.pwdrepite.value);
        if(cad!=''){
            document.getElementById("notificaciones").innerHTML='<p>'+cad+'</p>';
            return false;
        }
        else{
           var op="c";
           realizarOperacion();
           return true;
        }
}

function validarNoUsuario(cad)
{
    if(cad>=1)
    {
        return '';
    }
    else
    {
        return "Número de usuario invalido <br>"
    }
}

function validarNombre(cad)
{
    if(cad.length==0)
    {
        return 'Debes informar el nombre de la persona <br>';
    }
    else
    {
        return '';
    }
}

function validarSexo(cad)
{
    if(cad.length==0)
    {
        return 'Debes elegir un sexo<br>';
    }
    return '';
}

function validarTelefono(cad)
{
    var ban=false;
    if(cad.length==12)
    {
       var patron=/\d{3}-\d{3}-\d{4}/;
       if(patron.test(cad))
       {
           return '';
       }
       else
       {
            return 'El número de telefono no cumple el patrón ###-###-####.<br>';
       }
    }
    else{
        return 'El telefono debe ser de 12 caracteres. <br>'
    }
}

function validarEmail(cad)
{
    var patron=/[a-z]\w*@\w+.\w+.*/;
    if(patron.test(cad))
    {
        return '';
    }
    else
    {
        return "La cuenta de correo electrónico no tiene el formato correcto. <br>";
    }
}

function validarEstatus(cad)
{
    if(cad.length==0)
    {
        return 'Debes informar el estatus.<br>';
    }
    else
    {
        return '';
    }
}

function validarTipoUsuario(cad)
{
    if(cad==0)
    {
        return 'Debes elegir un tipo de usuario<br>';
    }
    return '';
}

function validarPasssword(pwd1,pwd2){
    if(pwd1!=pwd2){
        return "Las contraseñas no coinciden. <br>";
    }
    else{
        return '';
    }
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////---Aquí se crea el objeto---////////////////////////////////////////////
var arrayUsuarios=[];
class Usuario{
  constructor(id,nombreCompleto,sexo,telefono,email,estatus,tipoUsuario,password,pwdrepite) //Aquí van los parametros de entrada,(las variables necesarias para construir la clase)
  {
      this.id=id;
      this.nombreCompleto=nombreCompleto;
      this.sexo=sexo;
      this.telefono=telefono;
      this.email=email;
      this.estatus=estatus;
      this.tipoUsuario=tipoUsuario;
      this.password=password;
      this.pwdrepite=pwdrepite;
  }

  toString() //Aquí se crea el método ToString
  {
    return "ID: " + this.id + ", Nombre: " + this.nombreCompleto + ", Sexo: " + this.sexo + ", Telefono: " + this.telefono + ", Email: " + this.email + ", Estatus: " + this.estatus + ", tipoUsuario: " + this.tipoUsuario;
  }

  guardar()
  {
      //Almacenará el objeto en la BD
      arrayUsuarios.push(this)
  }

  actualizar()
  {
      for(i=0;i<arrayUsuarios.length;i++)
      {
          if(arrayUsuarios[i].id == this.id)
          {
              arrayUsuarios[i]=this;
          }
      }
  }

  eliminar()
  {
      for(i=0;i<arrayUsuarios.length;i++)
      {
          if(arrayUsuarios[i].id==this.id)
          {
              //delete arrayEdificios[i];
              arrayUsuarios.splice(i,1);
          }
      }
  }

  consultar()
  {
      for(i=0;i<arrayUsuarios.length;i++)
      {
          if(arrayUsuarios[i].id==this.id)
          {
              return arrayUsuarios[i];
          }
      }
      return null;
  }
}
///////////////////////////////////////////---Aquí se crea el objeto---///////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
