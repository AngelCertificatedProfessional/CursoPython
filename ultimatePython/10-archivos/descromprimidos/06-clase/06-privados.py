class Perro:
    patas = 4

    def __init__(self, nombre, edad):  # indica la estructura de la instancia
        self.__nombre = nombre  # Propiedad privada
        self.edad = edad  # parametro con la palabra nombre

    def habla(self):
        print(f"{self.__nombre} dice:Guau!")

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    @classmethod  # transformar en un metodo propio de la clase perro
    # tambien puede considerarse como un static en java
    def factory(cls):
        return cls("Chancioto feliz", 4)


perro1 = Perro.factory()
perro1.habla()
print(perro1.get_nombre())
print(perro1.__dict__)
