usuarios = [[4, "Chanchito"], [1, "Felipe"], [5, "Pulga"]]

nombres = []
for usuario in usuarios:
    nombres.append(usuario[1])
print(nombres)

# nombres = [expression for item in items]
# map simulacion compresion de listas
nombres = [usuario[1] for usuario in usuarios]
print(nombres)
# filtrar - filter
nombres = [usuario for usuario in usuarios if usuario[0] > 2]
print(nombres)
# filtrar y transofrmar
nombres = [usuario[1] for usuario in usuarios if usuario[0] > 2]
print(nombres)

# ------------programacion funcional-------------------
nombres = list(map(lambda usuario: usuario[1], usuarios))
print(nombres)

menosUsuarios = list(filter(lambda usuario: usuario[0] > 2, usuarios))
print(menosUsuarios)
