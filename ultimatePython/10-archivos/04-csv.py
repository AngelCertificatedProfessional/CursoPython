import csv

with open("10-archivos/archivos.csv", "w") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["twit_id", "user_id", "text"])
    writer.writerow([1000, 1, "este es un twit"])
    writer.writerow([1001, 2, "otro twit!"])
