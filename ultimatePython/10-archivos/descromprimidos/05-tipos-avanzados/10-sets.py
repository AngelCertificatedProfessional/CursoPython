# set significa grupo o conjunto de coleccion de datos que no puede repetirse y no esta ordenada
primer = {
    1, 1, 2, 2, 3, 4
}
primer.add(5)
primer.remove(1)  # elimina los 1 hasta los duplicados
print(primer)

segundo = [3, 4, 5]
segundo = set(segundo)  # convierte la lista en un set
print(segundo)

print(primer | segundo)  # union del primero y segundo
# interseccion del primer set y del segundo set donde los dos valores existen
print(primer & segundo)
# diferencia, muestra los valores que estan de la derecha a la izquierda
print(primer - segundo)
# diferencia simetrica, devolver los valores que esten entre la primera y segunda pero elimina duplicados
print(primer ^ segundo)

if 5 in segundo:
    print("hola mundo")
