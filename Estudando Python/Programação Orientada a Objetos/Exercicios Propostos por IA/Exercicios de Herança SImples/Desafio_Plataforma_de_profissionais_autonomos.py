class Pessoa:
    """
    Representa uma pessoa com nome e e-mail.
    """
    def __init__(self, nome: str, email: str):
        """
        Inicializa uma pessoa com nome e e-mail.

        :param nome: Nome da pessoa.
        :param email: Endereço de e-mail da pessoa.
        """
        self.nome = nome
        self.email = email

    def mostrar_dados(self) -> str:
        """
        Retorna os dados da pessoa formatados.

        :return: String com nome e e-mail.
        """
        return f"Nome: {self.nome}  \nEmail: {self.email}"


class Programador(Pessoa):
    """
    Representa um programador que sabe programar em várias linguagens.
    """
    def __init__(self, linguagens: list, nome: str, email: str):
        """
        Inicializa um programador com linguagens, nome e e-mail.

        :param linguagens: Lista de linguagens de programação.
        :param nome: Nome do programador.
        :param email: E-mail do programador.
        """
        Pessoa.__init__(self, nome=nome, email=email)
        self.linguagens = linguagens

    def programar(self):
        """
        Imprime as linguagens nas quais o programador está trabalhando.
        """
        print(f"Eu sou o {self.nome}")
        for linguagem in self.linguagens:
            print(f"Estou programando em {linguagem}")


class Designer(Pessoa):
    """
    Representa um designer que utiliza ferramentas gráficas.
    """
    def __init__(self, nome: str, email: str, ferramentas: list):
        """
        Inicializa um designer com nome, e-mail e ferramentas.

        :param nome: Nome do designer.
        :param email: E-mail do designer.
        :param ferramentas: Lista de ferramentas que o designer usa.
        """
        Pessoa.__init__(self, nome, email)
        self.ferramentas = ferramentas

    def desenhar(self):
        """
        Imprime as ferramentas com as quais o designer está criando.
        """
        print(f"Eu sou o {self.nome}")
        for ferramenta in self.ferramentas:
            print(f"Estou criando um design com {ferramenta}.")


class Freelancer(Programador, Designer):
    """
    Representa um profissional freelancer que é tanto programador quanto designer.
    """
    def __init__(self, nome: str, email: str, linguagens: list, ferramentas: list):
        """
        Inicializa um freelancer com nome, e-mail, linguagens e ferramentas.

        :param nome: Nome do freelancer.
        :param email: E-mail do freelancer.
        :param linguagens: Lista de linguagens de programação.
        :param ferramentas: Lista de ferramentas de design.
        """
        Programador.__init__(self, linguagens, nome, email)
        Designer.__init__(self, nome, email, ferramentas)

    def trabalhar(self):
        """
        Realiza tanto atividades de programação quanto de design.
        """
        self.programar()
        self.desenhar()


class Projeto:
    """
    Representa um projeto que envolve um profissional (designer, programador ou freelancer).
    """
    def __init__(self, titulo: str, professinal: object):
        """
        Inicializa um projeto com um título e um profissional associado.

        :param titulo: Nome do projeto.
        :param professinal: Objeto do tipo profissional (Designer, Programador ou Freelancer).
        """
        self.titulo = titulo
        self.professional = professinal

    def executar(self):
        """
        Executa o trabalho do profissional de acordo com seu tipo (classe).
        """
        print(f"Projeto: {self.titulo}")
        profissional = self.professional
        classe = profissional.__class__.__name__

        print(f"Executando metodo de trabalho do {classe}")

        if classe == "Designer":
            profissional.desenhar()
        elif classe == "Programador":
            profissional.programar()
        elif classe == "Freelancer":
            profissional.trabalhar()

    def exibir_professional(self):
        """
        Exibe os dados do profissional envolvido no projeto.
        """
        dados = self.professional.mostrar_dados()
        print(f"Cargo: {self.professional.__class__.__name__} \n{dados}")


if __name__ == "__main__":
    # ferramentas e linguagens para os objetos
    linguagens = ["java", "python", "C"]
    ferramentas = ["Photoshop", "Gimp", "Canvas"]

    # criar um programador para trabalhar no projeto casa
    programador = Programador(linguagens, "Wagner", "wagner@email.com")
    casa = Projeto("Casa", programador)
    casa.exibir_professional()
    casa.executar()

    print()  # quebra de linha

    # Criar um designer para o frontend de uma loja
    designer = Designer("wanderley", "wanderley@email.com", ferramentas)
    front = Projeto("Loja", designer)
    front.exibir_professional()
    front.executar()

    print()  # quebra de linha

    # criar um freelancer para o projeto basico
    fre = Freelancer("Valter", "valter@email.com", linguagens, ferramentas)
    basico = Projeto("basico", fre)
    basico.exibir_professional()
    basico.executar()
