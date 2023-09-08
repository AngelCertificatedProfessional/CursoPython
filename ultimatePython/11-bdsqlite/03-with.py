import sqlite3

# creamos la conexion con with que mandara a llamar la funcion de exit al final
# de la consulta que mandara internamente al close y al commit
with sqlite3.connect("11-bdsqlite/app.db") as con:
    # generamos las consultas
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios
        (id INTEGER primary key, nombre VARCHAR(50))
        """
    )
