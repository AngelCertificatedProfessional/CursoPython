class MiError(ZeroDivisionError):
    "Esta clase es para representar mi error"

    def __ini__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f"{self.mensaje} - codigo: {self.codigo}"


def division(n=0):
    if n == 0:
        raise MiError("No se puede dividir por 0", 800)
    # es como el throw de java
    return 5/n


try:
    division()
except MiError as e:
    print(e.codigo)
