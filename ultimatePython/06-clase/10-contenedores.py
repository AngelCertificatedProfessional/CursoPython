class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"


class Categoria:
    productos = []

    def __init__(self, nombre, producto):
        self.nombre = nombre
        self.productos = producto

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


kayak = Producto("Kajack", 1000)
bicicleta = Producto("Bicicleta", 750)
surfboard = Producto("SurfBoard", 500)
deportes = Categoria("Deportes", [kayak, bicicleta])
deportes.agregar(surfboard)
deportes.imprimir()
