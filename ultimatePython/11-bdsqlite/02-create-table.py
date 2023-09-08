import sqlite3

# creamos la conexion
con = sqlite3.connect("11-bdsqlite/app.db")

# generamos las consultas
cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios
    (id INTEGER primary key, nombre VARCHAR(50))
    """
)
# No sirve la consulta a menos que se ejecute el commit
con.commit()

con.close()
