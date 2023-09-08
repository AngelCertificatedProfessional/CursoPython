# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2
# ciclo hasta que encuentre la palabra salir manera 1
# comando = ""
# while comando.lower() != "salir":
#     comando = input("$ ")
#     print(comando)
# ciclo hasta que encuentre la palabra salir manera 2
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
