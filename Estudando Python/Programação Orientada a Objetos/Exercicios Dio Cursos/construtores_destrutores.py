class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Construindo o Objeto...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Destruindo o Objeto ")

    def latir(self):
        print("auau")
    
    def acordar(self):
        self.acordado = True
        print(f"{self.nome} está acordado.")
    
    def dormir(self):
        self.acordado = False
        print(f"{self.nome} está dormindo")
    
    def exibir_cachorro(self):
        print(f"\nOlá sou o {self.__class__.__name__} {self.nome}")
        print(f"Eu sou da cor {self.cor}")
        print(f"Estou {'Acordado' if self.acordado else 'Dormindo'}\n")

if __name__ == "__main__":
    c1 = Cachorro("DOG", "AZUL", False)
    c1.exibir_cachorro()
