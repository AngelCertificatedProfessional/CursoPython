from io import open

# escritura
texto = "Hola mundo2!"
# si no existe lo crea
archivo = open("10-archivos/hola-mundo.txt", "w")
archivo.write(texto)
archivo.close()

# lectura
archivo = open("10-archivos/hola-mundo.txt", "r")
texto = archivo.read()
archivo.close()
print(texto)

# lectura como lista
archivo = open("10-archivos/hola-mundo.txt", "r")
texto = archivo.readlines()
archivo.close()
print(texto)

# with y seek
with open("10-archivos/hola-mundo.txt", "r") as archivo:
    print(archivo.readlines())  # carga todo el archivo en memoria
    archivo.seek(0)  # regresar al primer caracter
    for linea in archivo:  # busca unalinea por linea
        print(linea)

# agregar sin eliminar
archivo = open("10-archivos/hola-mundo.txt", "+a")
archivo.write("Chao mundo :(")
archivo.close()

# lectura y escritura
with open("10-archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito feliz"
    archivo.writelines(texto)
