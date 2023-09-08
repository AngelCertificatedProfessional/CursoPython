pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
pila.pop()
ultimoElemento = pila.pop()
print(ultimoElemento)
print(pila)
print(pila[-1])
if not pila:
    print("pila vacia")
pila.pop()
if not pila:
    print("pila vacia")
