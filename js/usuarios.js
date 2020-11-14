var arrayUsuarios=[];
class Usuario{
  constructor(id,nombreCompleto,sexo,telefono,email,estatus,tipoUsuario) //Aquí van los parametros de entrada,(las variables necesarias para construir la clase)
  {
      this.id=id;
      this.nombreCompleto=nombreCompleto;
      this.sexo=sexo;
      this.telefono=telefono;
      this.email=email;
      this.estatus=estatus;
      this.tipoUsuario=tipoUsuario;
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
