class Perro:

    # los metiodos magicos inician con dos guines y terminan con dos guiones
    # nuestro constructor es un metodo magico
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Propiedad privada
        self.edad = edad

    def __del__(self):
        print(f"Chao perro :( {self.nombre}")

    def __str__(self):  # tiene estructura del objeto cuando se manda a llamar la instancia de una clase
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} fice: Guau!")


perro = Perro("Chanchito", 7)

print(perro)
texto = str(perro)
print(texto)

del perro
