from datetime import datetime

class Pessoa:
    ano = int(datetime.now().strftime("%Y"))
    total_instanciada = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.contar_total_instancias()        
    
    @classmethod
    def contar_total_instancias(cls):
        cls.total_instanciada += 1
        return cls.total_instanciada
    
    @classmethod
    def metodo_de_classe(cls):
        print("Método da classe chamado")
        print(f"Ano atual armazenado na classe: {cls.ano}")
    
    @classmethod
    def criar_pessoa_10_anos(cls, nome):
        print("Criando um novo objeto com idade fixa de 10 anos")
        return cls(nome, 10)

    @classmethod
    def criar_pessoa_anonima(cls, idade):
        print("Criando uma pessoa anônima com idade informada")
        return cls("Anônimo", idade)

if __name__ == "__main__":
    # Criando uma instância normalmente
    p = Pessoa("Carlos", 32)
    print(f"Pessoa criada: nome={p.nome}, idade={p.idade}")
    
    # Acessando atributo da classe diretamente
    print(f"Ano da classe: {Pessoa.ano}")  # Ex: 2025
    
    # Chamando método de classe pela instância
    p.metodo_de_classe()
    
    # Criando pessoa anônima com idade definida
    p1 = Pessoa.criar_pessoa_anonima(23)
    print(f"Pessoa 1: nome={p1.nome}, idade={p1.idade}")
    
    # Criando pessoa com idade fixa de 10 anos
    p2 = Pessoa.criar_pessoa_10_anos("Julia")
    print(f"Pessoa 2: nome={p2.nome}, idade={p2.idade}")

    # Demonstrando que diferentes chamadas retornam instâncias diferentes
    print(f"p1 é instância de Pessoa? {'Sim' if isinstance(p1, Pessoa) else 'Não'}")
    print(f"p2 é instância de Pessoa? {'Sim' if isinstance(p2, Pessoa) else 'Não'}")

    # Fabricando muitos objetos
    lista_pessoas = [Pessoa.criar_pessoa_anonima((x + x*3)) for x in range(10)]

    # foram instanciado 3 objetos
    print(f"A classe Pessoa já foi instanciada {Pessoa.total_instanciada} vezes")
    
    # exibindo objetos Fabricados
    for pessoa in lista_pessoas:
        print(pessoa.nome, pessoa.idade)