from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE peliculas(
    id_peliculas INTEGER,
    nombre VARCHAR(100),
    duracion VARCHAR(10),
    genero VARCHAR(100),
    PRIMARY KEY(id_peliculas AUTOINCREMENT)
  )'''
    
    try:
      conexion.cursor.execute(sql)
      conexion.cerrar()
      titulo='Crear Registro'
      mensaje='Se Creo la tabla correctamente'
      messagebox.showinfo(titulo, mensaje)
    except:
      titulo='Crear Registro'
      mensaje='La tabla ya está creada'
      messagebox.showwarning(titulo, mensaje)
        


def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE peliculas'

    try:
      conexion.cursor.execute(sql)
      conexion.cerrar()
      titulo='Borrar Registro'
      mensaje='Se Borro la tabla'
      messagebox.showinfo(titulo, mensaje)
    except:
      titulo='Borrar Registro'
      mensaje='No hay tabla para borrar'
      messagebox.showerror(titulo, mensaje)

class Peliculas:
   def __init__(self, nombre, duracion, genero):
      self.id_peliculas = None
      self.nombre = nombre
      self.duracion = duracion
      self.genero = genero

   def __str__(self):
        return f'Peliculas[{self.nombre}, {self.duracion}, {self.genero}]'
   
def guardar(peliculas):
    conexion = ConexionDB()

    sql = f"""INSERT INTO peliculas(nombre, duracion, genero)
    VALUES('{peliculas.nombre}', '{peliculas.duracion}', '{peliculas.genero}')"""

    try:
       conexion.cursor.execute(sql)
       conexion.cerrar()
    except:
       titulo = 'Conexion al Registro'
       mensaje = 'La tabla no esta creada '
       messagebox.showerror(titulo,mensaje)

def listar():
    conexion = ConexionDB()

    lista_peliculas =[]
    sql = 'SELECT * FROM peliculas'

    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
      titulo='Conexion al Registro'
      mensaje='Crea la tabla en la Base de Datos'
      messagebox.showwarning(titulo, mensaje)

    return lista_peliculas

def editar(peliculas, id_peliculas):
   conexion = ConexionDB()

   sql = f"""UPDATE peliculas
   SET nombre = '{peliculas.nombre}', duracion= '{peliculas.duracion}', genero= '{peliculas.genero}'
   WHERE id_peliculas = {id_peliculas}"""

   try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
   except:
      titulo='Edicion de datos'
      mensaje='No se ha podido editar este registro'
      messagebox.showerror(titulo,mensaje)

def eliminar(id_peliculas):
   conexion = ConexionDB()
   sql = f'DELETE FROM peliculas WHERE id_peliculas = {id_peliculas}'

   try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
   except:
      titulo='Eliminar datos'
      mensaje='No se pudo eliminar el registro'
      messagebox.showerror(titulo,mensaje)
   