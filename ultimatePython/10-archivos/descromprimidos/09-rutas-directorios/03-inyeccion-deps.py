from pathlib import Path
# import db
# import graphql
# import api

path = Path()  # obtienes la ruta actual
# obtienes un ciclo de todas las carpetas separadas
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "base de datos",
    "api": "esta es la api",
    "graphql": "esto es graphql"
}


def load(p):
    # print(str(p))
    # esto ayuda a remplazar lo que esta dentro de las subcarpetas por el punto
    # print(str(p).replace("/", "."))
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene funcion init")


list(map(load, paths))
