class Pessoa:
    """Representa uma pessoa com nome e email."""

    def __init__(self, nome: str, email: str):
        """Inicializa uma instância de Pessoa."""
        self._nome = nome
        self._email = email

    def get_nome(self) -> str:
        """Retorna o nome da pessoa."""
        return self._nome

    def set_nome(self, novo_nome: str) -> None:
        """Atualiza o nome da pessoa."""
        self._nome = novo_nome

    def get_email(self) -> str:
        """Retorna o email da pessoa."""
        return self._email

    def set_email(self, novo_email: str) -> None:
        """Atualiza o email da pessoa."""
        self._email = novo_email

    def exibir_dados(self) -> str:
        """Retorna os dados da pessoa formatados."""
        return f"Nome: {self.get_nome()}\nEmail: {self.get_email()}\n"


class Funcionario(Pessoa):
    """Representa um funcionário com cargo e salário."""

    def __init__(self, cargo: str, salario: float | int, **kwargs):
        """Inicializa uma instância de Funcionario."""
        super().__init__(**kwargs)
        self._salario = salario
        self._cargo = cargo

    def get_salario(self) -> int | float:
        """Retorna o salário do funcionário."""
        return self._salario

    def set_salario(self, novo_salario: int|float) -> None:
        """Atualiza o salário do funcionário."""
        self._salario = novo_salario

    def get_cargo(self) -> str:
        """Retorna o cargo do funcionário."""
        return self._cargo

    def set_cargo(self, novo_cargo: str) -> None:
        """Atualiza o cargo do funcionário."""
        self._cargo = novo_cargo

    def exibir_dados(self) -> str:
        """Retorna os dados completos do funcionário."""
        return f"{super().exibir_dados()}\nCargo: {self.get_cargo()}\nSalario: {self.get_salario()}\n"


class Freelancer(Pessoa):
    """Representa um freelancer com projeto e valor por projeto."""

    def __init__(self, projeto: str, valor_projeto: float, **kwargs):
        """Inicializa uma instância de Freelancer."""
        super().__init__(**kwargs)
        self._projeto = projeto
        self._valor_projeto = valor_projeto

    def get_projeto(self) -> str:
        """Retorna o nome do projeto atual."""
        return self._projeto

    def set_projeto(self, novo_projeto: str) -> None:
        """Atualiza o nome do projeto."""
        self._projeto = novo_projeto

    def get_valor_projeto(self) -> int | float:
        """Retorna o valor do projeto."""
        return self._valor_projeto

    def set_valor_projeto(self, novo_valor: str) -> None:
        """Atualiza o valor do projeto (erro: deveria atualizar _valor_projeto)."""
        self._valor_projeto = novo_valor 

    def exibir_dados(self) -> str:
        """Retorna os dados do freelancer formatados."""
        return f"{super().exibir_dados()}Projeto: {self.get_projeto()}\nPagamento por Projeto: {self.get_valor_projeto()}\n"


class ColaboradorHibrido(Funcionario, Freelancer):
    """Representa um colaborador que atua como funcionário e freelancer."""

    def __init__(self, nome, email, cargo, salario, projeto, valor_projeto):
        """Inicializa uma instância de ColaboradorHibrido."""
        super().__init__(nome=nome, email=email, cargo=cargo, salario=salario, projeto=projeto, valor_projeto=valor_projeto)

    def exibir_dados(self) -> None:
        """Exibe todas as informações do colaborador de forma formatada."""
        print("-" * 65)
        print("Informações do Colaborador")
        print("-" * 65)
        print("Nome do Colaborador(a): ", self.get_nome())
        print("Cargo do Funcionario: ", self.get_cargo())
        print("Salario Fixo: R$", self.get_salario(), "Reais")
        print("-" * 65)
        print("Projetos Ativos: ", self.get_projeto())
        print("Pagamento por Projeto: ", self.get_valor_projeto())
        print("-" * 65)


if __name__ == "__main__":
    # Exemplo de uso
    colaborador1 = ColaboradorHibrido("@nome", "@Email", "@cargo", 123.45, "@projeto", 123.45)
    colaborador1.exibir_dados()
