from src.models.repositorio.repositorio_pessoa import RepositorioPessoas
from src.models.entidades.pessoa import Pessoa

class BuscarPessoaController:
    def buscar_por_nome(self, pessoa_info: dict, repositorio: RepositorioPessoas):
        try:
            self.__validar_nome(pessoa_info)
            pessoa = self.__buscar_pessoa(pessoa_info, repositorio)
            resposta = self.__formatar_resposta(pessoa)
            return {"sucesso": True, "mensagem": resposta}
        except Exception as erro:
            return {"sucesso": False, "erro": str(erro)}
    
    def __validar_nome(self, pessoa_info: dict):
        if not isinstance(pessoa_info["nome"], str):
            raise Exception("Campo de nome invalido!")
    
    def __buscar_pessoa(self, pessoa_info: dict, repositorio: RepositorioPessoas):
        nome = pessoa_info['nome']
        pessoa = repositorio.buscar_pessoa(nome)
        if not pessoa: raise Exception("Pessoa não encontrada")
        return pessoa

    def __formatar_resposta(self, pessoa: Pessoa):
        return {
            "count": 1,
            "type": "Pessoa",
            "info": {
                "nome": pessoa.nome,
                "idade": pessoa.idade
            }
        }