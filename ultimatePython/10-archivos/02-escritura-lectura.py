from pathlib import Path
archivo = Path("10-archivos/archivo-prueba.txt")
# codificacion utf-08 para los caracteres de tipo espanol.
texto = archivo.read_text("utf-8").split('\n')
texto.insert(3, "Hola Mundo")
# une los caracteres para no guardar el \n
archivo.write_text("\n".join(texto), "utf-8")
# print(texto)
