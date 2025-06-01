from abc import ABC, abstractmethod

class Login(ABC):
    @abstractmethod
    def liberar_acesso(self, senha: str): pass

class Sistema(ABC):
    @abstractmethod
    def administrador(self, usuario): pass

class SistemaAluno(Sistema):
    def administrador(self, usuario: object):
        if not isinstance(usuario, Aluno):
            print("Apenas Alunos podem acessar o sistema")
            print(f"O {usuario.__class__.__name__} {usuario.nome} não pode entrar nesse sistema.")
            return False
        return usuario

class SistemaProfessor(Sistema):
    def administrador(self, usuario: object):
        if not isinstance(usuario, Professor):
            print("Apenas Professores podem acessar o sistema")
            print(f"O {usuario.__class__.__name__} {usuario.nome} não pode entrar nesse sistema.")
            return False
        print(f"Administrador: {usuario.nome.capitalize()}")
        return usuario

class Usuario(Login):
    def __init__(self, nome: str, idade: int, senha: str):
        self.nome = nome
        self.idade = idade
        self.senha = senha

    def liberar_acesso(self, senha: str):
        raise NotImplementedError("Subclasses devem implementar esse metódo")

    def __str__(self):
        return f"Eu sou um {self.__class__.__name__}, me chamo {self.nome}"

class Aluno(Usuario):
    def __init__(self, nome, idade, senha):
        super().__init__(nome, idade, senha)
        self.conectado = False

    def liberar_acesso(self, senha):
        self.conectado = self.senha == senha

    def __str__(self):
        return f"{super().__str__()}, Eu amo estudar"

class Professor(Usuario):
    def __init__(self, nome, idade, senha):
        super().__init__(nome, idade, senha)
        self.conectado = False

    def liberar_acesso(self, senha):
        self.conectado = self.senha == senha

    def __str__(self):
        return f"{super().__str__()}, Eu amo ensinar"

def validar_usuario(lista_usuarios: list[Usuario], nome: str, senha: str) -> bool|Usuario:
    usuario = False
    for usuario in lista_usuarios:
        nome_usuario = usuario.nome
        senha_usuario = usuario.senha
        nome_encontrado = nome_usuario.lower() == nome.lower()
        if not nome_encontrado: continue
        senha_encontrada = senha_usuario == senha
        if not senha_encontrada: continue
        usuario = usuario
        break

    return usuario

if __name__ == "__main__":
    p1 = Professor("profe1", 25, "profe1")
    p2 = Professor("profe2", 25, "profe2")
    a1 = Aluno("aluno1", 15, "aluno1")
    a2 = Aluno("aluno2", 15, "aluno2")

    sistema_aluno = SistemaAluno()
    sistema_professor = SistemaProfessor()

    lista_usuarios = [p1, p2, a1, a2]

    # Teste 1: Professor com login correto
    print("\n Teste 1: Professor com login correto")
    nome = "profe1"
    senha = "profe1"
    usuario = validar_usuario(lista_usuarios, nome, senha)
    if usuario:
        usuario.liberar_acesso(senha)
        administrador = sistema_professor.administrador(usuario)
        print(administrador)

    # Teste 2:  Professor com senha errada
    print("\n Teste 2: Professor com senha errada")
    nome = "profe2"
    senha = "errada"
    usuario = validar_usuario(lista_usuarios, nome, senha)
    if usuario:
        usuario.liberar_acesso(senha)
        administrador = sistema_professor.administrador(usuario)
        print(administrador)
    else:
        print("Acesso negado: senha ou nome incorreto")

    # Teste 3:  Aluno tentando entrar como professor
    print("\n Teste 3: Aluno tentando acessar sistema de professor")
    nome = "aluno1"
    senha = "aluno1"
    usuario = validar_usuario(lista_usuarios, nome, senha)
    if usuario:
        usuario.liberar_acesso(senha)
        administrador = sistema_professor.administrador(usuario)
        print(administrador)

    # Teste 4:  Aluno com login correto no sistema de alunos
    print("\n Teste 4: Aluno com login correto")
    nome = "aluno2"
    senha = "aluno2"
    usuario = validar_usuario(lista_usuarios, nome, senha)
    if usuario:
        usuario.liberar_acesso(senha)
        administrador = sistema_aluno.administrador(usuario)
        print(administrador)

    # Teste 5:  Aluno com nome errado
    print("\n Teste 5: Aluno não cadastrado")
    nome = "aluno3"
    senha = "aluno3"
    usuario = validar_usuario(lista_usuarios, nome, senha)
    if usuario:
        usuario.liberar_acesso(senha)
        administrador = sistema_aluno.administrador(usuario)
        print(administrador)
    else:
        print("Acesso negado: usuário não encontrado")
