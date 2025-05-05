class Conectar:
    def __init__(self, local="localhost"):
        # Método construtor (método comum): chamado automaticamente quando um objeto é criado.
        self.local = local
        self.usuario = None
        self.senha = None

    def set_usuario(self, usuario):
        # MÉTODO COMUM: recebe 'self', ou seja, uma instância da classe.
        # Pode acessar e modificar os atributos do objeto específico.
        self.usuario = usuario

    def set_senha(self, senha):
        # Outro MÉTODO COMUM: também atua sobre um objeto (instância) específico.
        self.senha = senha

    @classmethod
    def criar_com_autenticacao(cls, usuario, senha):
        # MÉTODO DE CLASSE: recebe 'cls' em vez de 'self', ou seja, a própria CLASSE.
        # Útil para criar instâncias de forma alternativa, como uma fábrica de objetos.
        conectar = cls()  # Cria um novo objeto da classe usando o construtor padrão
        conectar.usuario = usuario
        conectar.senha = senha
        return conectar  # Retorna o novo objeto configurado

    @staticmethod
    def validar_senha(senha):
        # MÉTODO ESTÁTICO: não recebe 'self' nem 'cls'.
        # Serve como uma função auxiliar relacionada à classe.
        # Aqui, valida se a senha tem mais de 3 caracteres.
        return len(senha) > 3

    @staticmethod
    def validar_nome(nome):
        # Outro MÉTODO ESTÁTICO: também independente da instância ou classe.
        # Apenas verifica o tamanho do nome.
        return len(nome) > 3

    def __str__(self):
        # Método especial que define como o objeto será impresso
        return f"Classe: {self.__class__.__name__}\n{ {x: y for x, y in vars(self).items()} }"


# Dados fornecidos para login
senha = "123456789"
usuario = "abcdefg"

# Chamando MÉTODOS ESTÁTICOS diretamente pela classe
# Isso é possível porque eles não dependem da instância nem da classe em si
senha_valida = Conectar.validar_senha(senha)
nome_valido = Conectar.validar_nome(usuario)

if senha_valida and nome_valido:
    # Se os dados forem válidos, usamos um MÉTODO DE CLASSE para criar o objeto
    conectar = Conectar.criar_com_autenticacao(usuario, senha)

# Quando imprimimos o objeto, o método __str__ exibe os atributos atuais
print(conectar)
