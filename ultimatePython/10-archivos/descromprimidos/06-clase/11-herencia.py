class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):
    def pasear(self):
        print("paseando")

# Herencia de multinivel


class Chanchito(Perro):

    def programar(self):
        print("Programar")


chanchito = Chanchito()
chanchito.programar()

perro = Perro()
perro.comer()
