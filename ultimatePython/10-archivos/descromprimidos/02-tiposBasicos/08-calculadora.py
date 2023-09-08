n1 = input("Ingrese primer numero: ")
n2 = input("Ingrese segundo numero: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2}
El resultado de la suma es {suma}
El resultado de la resta es {resta}
El resultado de la multiplicacion es {multiplicacion}
El resultado de la division es {div}
"""
print(mensaje)
