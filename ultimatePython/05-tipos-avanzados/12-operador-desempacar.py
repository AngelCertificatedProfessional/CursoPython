lista = [1, 2, 3, 4]
print(1, 2, 3, 4)
print(*lista)

lista = (1, 2, 3, 4)
print(1, 2, 3, 4)
print(*lista)

lista1 = [1, 2, 3, 4]
lista2 = [5, 6]

combinada = ["Hola", *lista1, "mundo", *lista2, "chanchito"]
print(combinada)

punto1 = {"x": 19, "lala": "holamundo", "y": "hola", "z": "mundo"}
punto2 = {"y": 15}

nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
