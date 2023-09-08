try:
    n1 = int(input("Ingresa el primer numero: "))
except ValueError as e:  # para validar los tipos de datos
    print("Ingrese un valor que corresponda")
except NameError as e:  # para validar que no halla errores en la aplicacion
    print("Ocurrio un error!")

# except Exception as e:
#     print(type(e))
