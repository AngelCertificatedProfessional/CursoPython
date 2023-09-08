import sqlite3

with sqlite3.connect("11-bdsqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Chanchito feliz"),
        (3, "Chanchito triste")
    ]
    cursor.executemany(
        """
            INSERT INTO usuarios values (?,?) 
        """,
        usuarios
    )
