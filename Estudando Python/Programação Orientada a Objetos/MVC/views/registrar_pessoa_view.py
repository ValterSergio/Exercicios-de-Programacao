from os import system

class RegistrarPessoaView:
    def registrar_pessoa_view(self):
        system("cls||clear")
        print("Registrar Pessoa\n")

        pessoa = input("Informe o nome da pessoa: ")
        idade = input("Digite a idade da pessoa: ")
        
        return {
            "nome": pessoa,
            "idade": idade
        }
    
    def registro_de_pessoa_sucesso(self, mensagem: dict):
        system("cls||clear")
        msg = f"""
        Usuario cadastrado com sucesso !

        tipo: {mensagem["mensagem"]["type"]}
        Registro: {mensagem["mensagem"]["count"]}
        infos: 
            Nome: {mensagem["mensagem"]["atributos"]["nome"]}        
            Idade: {mensagem["mensagem"]["atributos"]["idade"]}        
        """
        print(msg)
    
    def registro_pessoa_falha(self, erro: str):
        system("cls||clear")
        msg = f"""

        Falha ao cadastrar usuario !!

        Erro: {erro}

        """
        print(msg)
