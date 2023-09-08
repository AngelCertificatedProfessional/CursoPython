from pprint import pprint

string = "Hola mundo este es mi string"


def quita_espacios(texto):
    return [char for char in texto if char != " "]


def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


sin_espacios = quita_espacios(string)
print(sin_espacios)

contados = cuenta_caracteres(sin_espacios)
pprint(contados, width=1)


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],  # sorteo por el valor 1
        reverse=True
    )


ordenados = ordena(contados)
print(ordenados)


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


mayores = mayores_tuplas(ordenados)
print(mayores)


def crea_mensaje(diccionario):
    mensaje = "Los que mas se reptiten son \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje


mensaje = crea_mensaje(mayores)
print(mensaje)
