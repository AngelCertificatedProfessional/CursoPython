import json
from pathlib import Path

# escribir json
productos = [
    {"id": 1, "name": "Surfboard"},
    {"id": 2, "name": "Bicicleta"},
    {"id": 3, "name": "Skate"},
]

data = json.dumps(productos)
Path("10-archivos/productos.json").write_text(data)

# leer json
data = Path("10-archivos/productos.json").read_text(encoding="utf-8")
productos2 = json.loads(data)
productos2[0]["name"] = "Chanchitlo feliz"
Path("10-archivos/productos.json").write_text(json.dumps(productos2))
