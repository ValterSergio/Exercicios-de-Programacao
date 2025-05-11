from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.now().strftime("%Y"))
    
    def __init__(self, nome, ano_nascimento):
        self.nome = nome 
        self.ano_nascimento = ano_nascimento
        self.idade = self.obter_idade()

    def obter_idade(self):
       return Pessoa.ano_atual - self.ano_nascimento

if __name__ == "__main__":
    p = Pessoa("valter", 1994)
    print(p.obter_idade())