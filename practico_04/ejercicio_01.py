"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    db = sqlite3.connect("my_db.db")

    cursor = db.cursor()
    cadenaSQL = """CREATE TABLE Persona (
        IdPersona INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre CHAR(30),
        FechaNacimiento DATE,
        DNI INTEGER,
        Altura INTEGER
    )"""

    cursor.execute(cadenaSQL)
    db.commit()
    db.close()

def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    db = sqlite3.connect("my_db.db")

    cursor = db.cursor()
    cadenaSQL = """DROP TABLE Persona"""
    cursor.execute(cadenaSQL)

    cadenaSQL = """DROP TABLE PersonaPeso"""
    cursor.execute(cadenaSQL)
    db.commit()
    db.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
# borrar_tabla()