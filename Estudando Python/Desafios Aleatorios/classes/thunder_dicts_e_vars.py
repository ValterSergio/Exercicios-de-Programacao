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
    def exibir_atributos(p):
        for atributo, valor in p.__dict__.items():
            print(f"Atributo: {atributo} | Valor: {valor}")
        print()

    p = Pessoa("valter", 1994)
    print(p.obter_idade())
    
    # adicionar email
    p.__dict__["email"] = "valter@email.com"

    # alterar nome
    p.__setattr__("nome", "Sergio")

    # exibir tudo
    exibir_atributos(p)

    # remover email
    del p.__dict__["email"]
    
    # remover idade
    p.__delattr__("idade")

    # conferindo mudanças
    exibir_atributos(p)

    print(vars(p)) # vars retorna dicionario com todos os atributos
    

    

