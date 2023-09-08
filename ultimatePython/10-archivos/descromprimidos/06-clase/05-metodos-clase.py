class Perro:
    patas = 4

    def __init__(self, nombre, edad):  # indica la estructura de la instancia
        self.nombre = nombre  # parametro con la palabra nombre
        self.edad = edad  # parametro con la palabra nombre

    @classmethod  # transformar en un metodo propio de la clase perro
    def habla(cls):  # es lo mismo que escribieramos lo mismo que perro
        print("Guau!")

    @classmethod  # transformar en un metodo propio de la clase perro
    def factory(cls):
        return cls("Chancioto feliz", 4)


Perro.habla()
perro1 = Perro("Chancito", 2)
perro2 = Perro("Felipe", 3)
perro3 = Perro.factory()
print(perro3.nombre, perro3.edad)
