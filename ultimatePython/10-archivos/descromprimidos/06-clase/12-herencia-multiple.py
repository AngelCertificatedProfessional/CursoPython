class Animal:
    def comer(self):
        print("comiendo")


class Perro:
    def pasear(self):
        print("paseando")

# Herencia de multinivel


class Chanchito(Perro, Animal):

    def programar(self):
        print("Programar")


chanchito = Chanchito()
chanchito.programar()
chanchito.comer()
chanchito.pasear()
