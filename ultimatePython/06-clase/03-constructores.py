class Perro:

    def __init__(self, nombre, edad):  # indica la estructura de la instancia
        self.nombre = nombre  # parametro con la palabra nombre
        self.edad = edad  # parametro con la palabra nombre

    def habla(self):  # el primer parametro siempre sera self
        print(f"{self.edad} dice: Guau!")


mi_perro = Perro("Jaime", 1)
mi_perro2 = Perro("Felipe", 2)
mi_perro.habla()
mi_perro2.habla()
