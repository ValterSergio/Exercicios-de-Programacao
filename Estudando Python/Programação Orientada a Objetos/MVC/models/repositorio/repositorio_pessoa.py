from src.models.entidades.pessoa import Pessoa

class RepositorioPessoas:
    def __init__(self):
        self.__pessoas = []
    
    def registrar_pessoa(self, pessoa: Pessoa):
        self.__pessoas.append(pessoa)
    
    def buscar_pessoa(self, nome: str):
        for pessoa in self.__pessoas:
            if pessoa.nome.lower() == nome.lower():
                return pessoa
    
