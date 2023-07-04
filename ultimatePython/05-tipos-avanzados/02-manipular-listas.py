mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas[0])
mascotas[0] = "Bicho"
print(mascotas)
print(mascotas[:3])
print(mascotas[-1])
# pares toma el primero, saltate el siguiente y ve al tercero
print(mascotas[::2])
# pares toma el indice 1, saltate el siguiente y ve al tercero
print(mascotas[1::2])
numeros = list(range(21))
print(numeros[::2])  # pares
print(numeros[1::2])  # impares
