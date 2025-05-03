# Crie uma classe Motorista com método dirigir() e uma classe
# Cantor com método cantar(). Depois, crie a classe
# ArtistaUber que herda das duas e pode tanto cantar quanto 
# dirigir

class Motorista:
    def __init__(self):
        pass

    def dirigir(self):
        print("Dirigindo...")

class Cantor:
    def __init__(self):
        pass

    def cantar(self):
        print("Cantando...")
    
class ArtistaUber(Motorista, Cantor):
    def __init__(self):
        Motorista.__init__(self)
        Cantor.__init__(self)

    def cantar_e_dirigir(self):
        self.cantar()
        self.dirigir()


if __name__ == "__main__":
    uber = ArtistaUber()
    uber.cantar_e_dirigir()