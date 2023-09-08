from pathlib import Path

path = Path("09-rutas-directorios")
# path.exists()  # verificamos que exista
# path.mkdir()  # crea la carpeta
# path.rmdir()  # elimina la carpeta pero no debe haber archivos en la carpeta
# path.rename("test")  # cambiar el nombre del directorio

# for p in path.iterdir():  # regresa un metodo acumlador
#     print(p)

archivos = [p for p in path.iterdir() if not p.is_dir()]
print(archivos)

archivos = [p for p in path.glob('*.py')]
print(archivos)

# todos los arhcivos que estan en el nivel del una carpeta anterior
archivos = [p for p in path.glob('**/*.py')]
print(archivos)


# lo mismo que el anterior
archivos = [p for p in path.rglob('*.py')]
print(archivos)
