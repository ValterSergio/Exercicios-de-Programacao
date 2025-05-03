class Funcionario:
    """
    Classe base que representa um funcionário genérico.
    """

    def __init__(self, nome, id, salario):
        """
        Inicializa um novo funcionário.

        Args:
            nome (str): Nome do funcionário.
            id (int): Identificador único do funcionário.
            salario (float): Salário atual do funcionário.
        """
        self.nome = nome
        self.id = id
        self.salario = salario

    def aumentar_salario(self, porcentagem):
        """
        Aumenta o salário do funcionário com base em uma porcentagem.

        Args:
            porcentagem (float): Porcentagem a ser adicionada ao salário.
        """
        self.salario += self.salario * (porcentagem / 100)

    def exibir_informacoes(self):
        """
        Retorna as informações básicas do funcionário.

        Returns:
            str: Informações formatadas.
        """
        return f"Funcionário: {self.nome} | ID: {self.id} | Salário: {self.salario:.2f}"


class FuncionarioTI(Funcionario):
    """
    Representa um funcionário da área de TI, herdando de Funcionario.
    """

    def __init__(self, nome, id, salario, linguagens_programacao=None):
        """
        Inicializa um funcionário de TI.

        Args:
            nome (str): Nome do funcionário.
            id (int): Identificador do funcionário.
            salario (float): Salário do funcionário.
            linguagens_programacao (list, opcional): Lista de linguagens que o funcionário conhece.
        """
        super().__init__(nome, id, salario)
        if linguagens_programacao is None:
            linguagens_programacao = []
        self.linguagens_programacao = linguagens_programacao

    def adicionar_linguagem(self, linguagem):
        """
        Adiciona uma nova linguagem à lista do funcionário de TI.

        Args:
            linguagem (str): Linguagem a ser adicionada.
        """
        if linguagem not in self.linguagens_programacao:
            self.linguagens_programacao.append(linguagem)

    def remover_linguagem(self, linguagem):
        """
        Remove uma linguagem da lista do funcionário de TI.

        Args:
            linguagem (str): Linguagem a ser removida.
        """
        if linguagem in self.linguagens_programacao:
            self.linguagens_programacao.remove(linguagem)

    def exibir_informacoes(self):
        """
        Retorna as informações do funcionário de TI, incluindo linguagens de programação.

        Returns:
            str: Informações formatadas.
        """
        informacoes = super().exibir_informacoes()
        linguagens = ', '.join(self.linguagens_programacao)
        return f"{informacoes}\nLinguagens de programação: {linguagens}"


class FuncionarioFinanceiro(Funcionario):
    """
    Representa um funcionário da área financeira.
    """

    def __init__(self, nome, id, salario, especialidade):
        """
        Inicializa um funcionário financeiro.

        Args:
            nome (str): Nome do funcionário.
            id (int): Identificador do funcionário.
            salario (float): Salário do funcionário.
            especialidade (str): Especialidade do funcionário.
        """
        super().__init__(nome, id, salario)
        self.especialidade = especialidade

    def alterar_especialidade(self, nova_especialidade):
        """
        Altera a especialidade do funcionário financeiro.

        Args:
            nova_especialidade (str): Nova especialidade.
        """
        self.especialidade = nova_especialidade

    def exibir_informacoes(self):
        """
        Retorna as informações do funcionário financeiro, incluindo a especialidade.

        Returns:
            str: Informações formatadas.
        """
        informacoes = super().exibir_informacoes()
        return f"{informacoes}\nEspecialidade: {self.especialidade}"


# Testes das classes
if __name__ == "__main__":
    # Criando um Funcionário TI
    funcionario_ti = FuncionarioTI("João Silva", 1234, 3000, ["Python", "Java"])
    funcionario_ti.aumentar_salario(10)
    funcionario_ti.adicionar_linguagem("C++")         # Nova linguagem
    funcionario_ti.remover_linguagem("Java")          # Remover linguagem existente

    # Criando um Funcionário Financeiro
    funcionario_financeiro = FuncionarioFinanceiro("Maria Oliveira", 5678, 3500, "Contabilidade")
    funcionario_financeiro.aumentar_salario(5)
    funcionario_financeiro.alterar_especialidade("Auditoria")  # Mudando a especialidade

    # Exibindo informações
    print(funcionario_ti.exibir_informacoes())
    print()
    print(funcionario_financeiro.exibir_informacoes())
