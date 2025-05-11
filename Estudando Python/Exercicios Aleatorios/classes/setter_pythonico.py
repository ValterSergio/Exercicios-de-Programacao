class Cerveja:
    def __init__(self, marca, preco):
        self.marca = marca
        self._preco = preco

    @property
    def preco(self):
        print("Getter com property")
        return self._preco

    @preco.setter
    def preco(self, valor):
        print("Setter pythonico")
        self._preco = valor

if __name__ == "__main__":
    c = Cerveja("Skol", 1.96)
    c.preco = 2.56
    print(c.preco)
