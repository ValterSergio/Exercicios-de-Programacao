class Pessoa:
    def __init__(self, nome, **kwargs):
        self.nome = nome
        super().__init__(**kwargs)
    
    def exibir(self):
        for x, y in self.__dict__.items():
            print(f"Atributo: {x} | Valor do atributo: {y}")

class Funcionario:
    def __init__(self, salario, **kwargs):
        self.salario = salario
        super().__init__(**kwargs)

class Colaborador(Pessoa, Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome=nome, salario=salario)

colaborador = Colaborador("Valter", 1565)
