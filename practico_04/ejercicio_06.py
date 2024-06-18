"""Base de Datos SQL - Creación de tablas auxiliares"""

import sqlite3

from ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    db = sqlite3.connect("my_db.db")

    cursor = db.cursor()
    cadenaSQL = """CREATE TABLE PersonaPeso (
        IdPersona INTEGER,
        Fecha DATE,
        Peso INTEGER,
        FOREIGN KEY(IdPersona) REFERENCES Persona(IdPersona)
    )"""

    cursor.execute(cadenaSQL)
    db.commit()
    db.close()


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    pass # Completar


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
