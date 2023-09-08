numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# feo!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, segundo, tercero, *otros = numeros
print(primero, segundo, tercero)

primero, seg, *otros, pen, ultimo = numeros
print(primero, seg, otros, pen, ultimo)
