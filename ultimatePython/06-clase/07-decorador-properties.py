class Perro:

    def __init__(self, nombre):  # indica la estructura de la instancia
        self.nombre = nombre  # Propiedad privada

    @property  # indica el metodo para que se convierta en una propiedad
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Choclo")
print(perro.nombre)
