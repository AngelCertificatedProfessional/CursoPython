buscar = 10

for numero in range(5):
    print(numero)
    if numero == buscar:
        print('encontrado', buscar)
        break
else:  # else se llama cuando no se manda a llmar el else
    print('no encontre el numero indicado')

for char in "Ultimate python":
    print(char)
