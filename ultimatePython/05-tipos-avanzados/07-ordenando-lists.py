numeros = [2, 4, 1, 45, 75, 22]

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

numeros2 = sorted(numeros)  # crea una nueva lista
print(numeros2)
numeros2 = sorted(numeros, reverse=True)  # crea una nueva lista
print(numeros2)


def ordena(elemento):
    return elemento[1]


usuarios = [[4, "Chanchito"], [1, "Felipe"], [5, "Pulga"]]
usuarios.sort()  # va a ordenar por el id siendo el primer valor
print(usuarios)
usuarios.sort(key=ordena)  # va a ordenar por el valor indicado
print(usuarios)
# usuarios.sort(key=lambda parametros:valorRestorno)  # va a ordenar por el valor indicado
usuarios.sort(key=lambda el: el[1])  # va a ordenar por el valor indicado
print(usuarios)
