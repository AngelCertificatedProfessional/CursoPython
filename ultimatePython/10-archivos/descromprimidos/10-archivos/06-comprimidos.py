from pathlib import Path
from zipfile import ZipFile

with ZipFile("10-archivos/comprimidos.zip", "w") as zip:
    # curso-py
    for path in Path().rglob("*.*"):
        if str(path) != "archivos/comprimidos.zip":
            zip.write(path)
