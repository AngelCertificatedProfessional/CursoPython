punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto)

# print(punto, punto["lala"]) marca error
if "lala" in punto:
    print("encontre lala", punto["lala"])

print(punto.get("x"))
print(punto.get("lala"))  # regresa None
print(punto.get("lala", 97))  # le asignamos un valor si no existe
del punto["x"]  # elimina la key
del punto["y"]  # elimina la key

print(punto)
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {
        "id": 1,
        "nombre": "Chanchito"
    },
    {
        "id": 2,
        "nombre": "Feliz"
    },
    {
        "id": 3,
        "nombre": "Nicolas"
    },
    {
        "id": 4,
        "nombre": "Felipe"
    }
]

for usuario in usuarios:
    print(usuario["nombre"])
