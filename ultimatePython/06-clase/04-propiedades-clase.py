class Perro:
    patas = 4

    def __init__(self, nombre, edad):  # indica la estructura de la instancia
        self.nombre = nombre  # parametro con la palabra nombre
        self.edad = edad  # parametro con la palabra nombre

    def habla(self):  # el primer parametro siempre sera self
        print(f"{self.edad} dice: Guau!")


Perro.patas = 3
mi_perro = Perro("Jaime", 1)
mi_perro2 = Perro("Felipe", 1)
mi_perro.patas = 5
print(Perro.patas)
print(mi_perro.patas)
print(mi_perro2.patas)
