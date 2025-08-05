from os import system 

class BuscarPessoaView:
    def buscar_pessoa_view(self):
        system("cls||clear")
        print("buscar pessoa\n")
        nome = input("Informe o nome da pessoa para busca: ")

        info_pessoa = {
            "nome": nome
        }
        return info_pessoa
    
    def buscar_pessoa_sucesso(self, mensagem: dict):
        msg = f"""

        Pessoa encontrada com Sucesso !

        tipo: {mensagem["mensagem"]["type"]}
        Registros: {mensagem["mensagem"]["count"]}
        Infos: 
            Nome: {mensagem["mensagem"]["info"]["nome"]}
        """
        print(msg)
    
    def buscar_pessoa_falha(self, erro: str):
        msg = f"""
        
        Usuario Não encontrado !!!

        Erro: {erro}

        """
        print(msg) 