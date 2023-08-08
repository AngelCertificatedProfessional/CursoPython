import csv
import os
# escribir
# with open("10-archivos/archivos.csv", "w") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([1000, 1, "este es un twit"])
#     writer.writerow([1001, 2, "otro twit!"])
# leer
# with open("10-archivos/archivos.csv") as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     # volvermos a aredigigirnos al iniciopara que lo pueda leer
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)

# actualizar csv
with open("10-archivos/archivos.csv") as r, open("10-archivos/archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000, 1, "texto modificado"])
        else:
            writer.writerow(linea)
    os.remove("10-archivos/archivos.csv")
    os.rename("10-archivos/archivo_temp.csv", "10-archivos/archivos.csv")
