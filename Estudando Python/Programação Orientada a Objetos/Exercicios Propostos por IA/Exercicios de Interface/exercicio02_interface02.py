from abc import ABC, abstractmethod

class Autentificar(ABC):
    @abstractmethod
    def liberar_acesso(self, senha: str): pass


class UsuarioSistema(Autentificar):
    def __init__(self, nome: str, senha: str):
        self.nome = nome
        self.senha = senha
        
    def liberar_acesso(self, senha):
        return senha == "sistema"

class UsuarioCliente(Autentificar):
    def __init__(self, nome: str, senha: str):
        self.nome = nome
        self.senha = senha

    def liberar_acesso(self, senha):
        return senha == "cliente1"

if __name__ == "__main__":
    adm = UsuarioSistema("adm", "sistema")
    cliente = UsuarioCliente("cliente", "cliente1")
    usuarios = [adm, cliente]
    senhas = ["sistema", "cliente1"]
    for x in range(len(usuarios)):
        liberado = usuarios[x].liberar_acesso(senhas[x])
        print(f"Usuario: {usuarios[x].__class__.__name__} -> Acesso: {"Liberado" if liberado else "Acesso Negado"}")
    
    
