def get_producto(**datos):
    print(datos)
    print(datos["id"], datos["name"])


get_producto(id="23", name="iPhone", desc="Esto es un iphone")
