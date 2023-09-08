from pathlib import Path
from zipfile import ZipFile
# escritura
# with ZipFile("10-archivos/comprimidos.zip", "w") as zip:
#     # curso-py
#     for path in Path().rglob("*.*"):
#         if str(path) != "archivos/comprimidos.zip":
#             zip.write(path)
# lectura
with ZipFile("10-archivos/comprimidos.zip") as zip:
    # imprimimos el listado de archivos
    print(zip.namelist())
    info = zip.getinfo("10-archivos/06-comprimidos.py")
    # muestra el peso de los archivos
    print(
        info.file_size,
        info.compress_size
    )
    # descomprime los archivos
    zip.extractall("10-archivos/descromprimidos")
