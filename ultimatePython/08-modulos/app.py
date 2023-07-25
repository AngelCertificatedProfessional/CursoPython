# from usuarios.acciones import guardar, pagar_impuestos
# from usuarios.acciones.utilidades import guardar, pagar_impuestos
from usuarios.impuestos.utilidades import pagar_impuestos
import usuarios
print(dir(usuarios))  # obtiene los elementos del paquete y subpaquete
print(usuarios.__name__)
print(usuarios.__package__)
print(usuarios.__path__)
print(usuarios.__file__)
# pagar_impuestos()
