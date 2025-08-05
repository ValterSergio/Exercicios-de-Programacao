from src.models.repositorio.repositorio_pessoa import RepositorioPessoas
from src.models.entidades.pessoa import Pessoa

class RegistrarPessoaController:
    def registrar(self, pessoa_info: dict, repositorio: RepositorioPessoas):
        try:
            self.__validar_pessoa(pessoa_info)
            self.__registrar_pessoa(pessoa_info, repositorio)

            resposta = self.__formatar_resposta(pessoa_info)
            return {"sucesso": True, "mensagem": resposta}
        
        except Exception as erro:
            return {"sucesso": False, "erro": str(erro)}

    def __validar_pessoa(self, pessoa: dict):
        if not isinstance(pessoa['nome'], str):
            raise Exception("Campo nome incorreto")
        
        try: int(pessoa["idade"])
        except: raise Exception("Campo idade incorreto")
    
    def __registrar_pessoa(self, pessoa_info: dict, repositorio: RepositorioPessoas):
        nome = pessoa_info["nome"]
        idade = pessoa_info["idade"]
        pessoa = Pessoa(nome, idade)
        repositorio.registrar_pessoa(pessoa)

    def __formatar_resposta(self, pessoa: dict):
        return {
            "count": 1,
            "type": "Pessoa",
            "atributos": pessoa
        }