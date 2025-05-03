from app.funcionario import Funcionario

class Gerente(Funcionario):
    """
    Classe que representa um gerente, herdando de Funcionario.

    Adiciona um atributo específico de bonificação (bonus).
    """

    def __init__(self, nome: str, documento, senha_portal, cargo, salario, bonus=None):
        """
        Inicializa um gerente com todos os atributos de um funcionário + bônus.

        Args:
            nome (str): Nome do gerente.
            documento (str): Documento (CPF).
            senha_portal (str): Senha de acesso.
            cargo (str): Cargo ocupado.
            salario (float): Salário atual.
            bonus (float, opcional): Porcentagem de bonificação.
        """
        super().__init__(nome, documento, senha_portal, cargo, salario)
        self.__bonus = bonus  # Bonificação do gerente

    def get_bonus(self) -> str:
        """
        Retorna a porcentagem de bonificação do gerente.

        Returns:
            str: Valor do bônus.
        """
        return self.__bonus

    def set_bonus(self, novo):
        """
        Define um novo valor de bonificação, se for maior que zero.

        Args:
            novo (float): Novo valor de bônus.

        Returns:
            bool: True se o valor for aceito, False caso contrário.
        """
        if novo <= 0:
            return False
        self.__bonus = novo
        return True

    def mostrar_dados(self) -> str:
        """
        Retorna uma string com os dados do gerente, incluindo o bônus.

        Returns:
            str: Informações formatadas do gerente.
        """
        return f"{super().mostrar_dados()}\nBonificação: {self.get_bonus()}%\n{'-'*65}"

    def aplicar_bonus(self) -> float:
        """
        Aplica o bônus ao salário e retorna o novo valor com o aumento.

        Returns:
            float: Salário com o bônus aplicado.
        """
        return self.aumentar_salario(self.get_bonus())
