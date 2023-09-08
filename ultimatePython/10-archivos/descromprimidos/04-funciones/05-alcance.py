saludo = "Saludo global"


def saludar():
    global saludo  # mala practica no usar variables globales
    saludo = "Hola Mundo"
    print(saludo)


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


print(saludo)
saludar()
saludaChanchito()
saludar()
print(saludo)
