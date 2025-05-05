class caneta:
    def __init__(self, cor):
        self.cor = cor
        self._tampada = False

    # getter classico
    def get_cor(self):
        print("Getter Classico")
        return self.cor

    @property # getter Pythonico
    def tampada(self):
        print("Getter Pythonico")
        return self._tampada


caneta = caneta("VERDE")
print(caneta.get_cor())
print(caneta.tampada)
    