from pathlib import Path

# Path(r"")  # El r windows para que no tome los caracteres del bash \
Path("/usr/bin")  # crea una ruta para este directorio
Path()  # crea una ruta de la posicion actual de la aplicacion
Path.home()  # ruta al home
Path("one/__init__.py")  # ruta relativa crea el archivo  o abrirlo

path = Path("hola-mundo/mi-archivo.py")
path.is_file()  # ayuda a detectar si la ruta tiene un archivo
path.is_dir()  # ayuda a detectar si la ruta tiene un folder
path.exists()  # si el archivo o la carpeta existe

print(
    path.name,  # el nombre del archivo con su extencion
    path.stem,  # el nombre del archivo sin su extencion
    path.suffix,  # la externcion del archivo
    path.parent,  # el directorio padre de donde se origina
    path.absolute()  # la ruta completa de donde se originaria este PAD
)

# cambia el nombre del archivo y la extencion
p = path.with_name("chanchito.exe")
print(p)
p = path.with_suffix(".bat")  # cambia la extencion del archivo
print(p)
p = path.with_stem("feliz")  # cambia el nombre del archivo
