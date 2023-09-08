from pathlib import Path
from time import ctime

# para que esto corra bien tiene que ser de la carpeta de ultimate python
archivo = Path("10-archivos/archivo-prueba.txt")
print(archivo.stat())  # sirve para ver todas las estadisticas del archivo
# sirve para ver la fecha de acceso a este archivo entregando un timestamp
print("acceso", ctime(archivo.stat().st_atime))
print("creacion", ctime(archivo.stat().st_ctime))
print("modificacion", ctime(archivo.stat().st_mtime))
