class Perro:
    def habla(self):  # el primer parametro siempre sera self
        print("Guau!")


mi_perro = Perro()
# print(type(mi_perro))
mi_perro.habla()
print(isinstance(mi_perro, Perro))
