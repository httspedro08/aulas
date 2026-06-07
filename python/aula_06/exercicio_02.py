class Instrumento:
    def tocar(self):
        pass


class Violao(Instrumento):
    def tocar(self):
        print("Plim plim")


class Bateria(Instrumento):
    def tocar(self):
        print("Tum tum")


class Piano(Instrumento):
    def tocar(self):
        print("Dó ré mi")


instrumentos = [Violao(), Bateria(), Piano()]

for instrumento in instrumentos:
    instrumento.tocar()