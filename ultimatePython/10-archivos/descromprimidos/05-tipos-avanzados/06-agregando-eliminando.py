mascotas = ["Rayo", "Pelusa", "Pulga", "Felipe", "Pulga",  "Chanchito Feliz"]
mascotas.insert(1, "Melvin")  # agrega en este caso en la posico9on 1
mascotas.append("Chanchito Triste")  # agrega al final
mascotas.remove("Pulga")  # No va el indice
mascotas.pop()            # elimina el ultiomo
mascotas.pop(1)           # indice a eliminar
del mascotas[0]           # otra manera de eliminar
mascotas.clear()          # limpiar todo el arreglo
print(mascotas)
