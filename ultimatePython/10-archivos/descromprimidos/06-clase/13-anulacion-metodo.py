class Ave:

    def __init__(self):
        self.volador = True

    def vuela(self):
        print("vuela ave")


class Pato(Ave):
    def __init__(self):
        super().__init__()  # correr contructor de la dependencia padre
        self.nada = True

    def vuela(self):
        print("vuela pato")
        # super().vuela()  # obtiene el metodo de la herencia


pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)
