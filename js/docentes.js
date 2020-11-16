var arrayDocentes=[];
class Docente{
  constructor(noDocente,noUsuario,escolaridad,especialidad,cedula,idCarrera) //Aquí van los parametros de entrada,(las variables necesarias para construir la clase)
  {
      this.noDocente=noDocente;
      this.noUsuario=noUsuario;
      this.escolaridad=escolaridad;
      this.especialidad=especialidad;
      this.cedula=cedula;
      this.idCarrera=idCarrera;
  }

  toString() //Aquí se crea el método ToString
  {
    return "NoDocente: " + this.noDocente + ", NoUsuario: " + this.noUsuario + ", Escolaridad: " + this.escolaridad + ", Especialidad: " + this.especialidad + ", Cedula: " + this.cedula + ", IdCarrera: " + this.idCarrera;
  }

  guardar()
  {
      //Almacenará el objeto en la BD
      arrayDocentes.push(this)
  }

  actualizar()
  {
      for(i=0;i<arrayDocentes.length;i++)
      {
          if(arrayDocentes[i].noDocente == this.noDocente)
          {
              arrayDocentes[i]=this;
          }
      }
  }

  eliminar()
  {
      for(i=0;i<arrayDocentes.length;i++)
      {
          if(arrayDocentes  [i].noDocente==this.noDocente)
          {
              arrayDocentes.splice(i,1);
          }
      }
  }

  consultar()
  {
      for(i=0;i<arrayDocentes.length;i++)
      {
          if(arrayDocentes[i].noDocente==this.noDocente)
          {
              return arrayDocentes[i];
          }
      }
      return null;
  }


}
