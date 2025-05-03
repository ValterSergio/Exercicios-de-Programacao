import os
import sys

# Adiciona o diretório pai ao sys.path para permitir a importação de módulos externos
pasta_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(pasta_pai)

from app.pessoa import Pessoa
from ferramentas.funcoes_auxiliares import validar_nome, validar_salario, calcular_aumento_salarial

class Funcionario(Pessoa):
    """
    Representa um funcionário da empresa, herdando os atributos e métodos da classe Pessoa.
    
    Atributos adicionais:
        - cargo (str): Cargo ou função do funcionário.
        - salario (float): Salário atual do funcionário.
    """

    def __init__(self, nome: str, documento: str, senha_portal: str, cargo: str, salario: float):
        """
        Inicializa uma instância de Funcionario, utilizando a base da classe Pessoa.

        Args:
            nome (str): Nome completo do funcionário.
            documento (str): CPF do funcionário.
            senha_portal (str): Senha de acesso ao sistema.
            cargo (str): Cargo ocupado pelo funcionário.
            salario (float): Salário atual do funcionário.
        """
        super().__init__(nome, documento, senha_portal)
        self._cargo = cargo                  # Atributo protegido
        self.__salario = salario             # Atributo privado

    def get_cargo(self) -> str:
        """
        Retorna o cargo atual do funcionário.

        Returns:
            str: Cargo ocupado.
        """
        return self._cargo

    def get_salario(self) -> float:
        """
        Retorna o salário atual do funcionário.

        Returns:
            float: Valor atual do salário.
        """
        return self.__salario

    def set_cargo(self, cargo: str) -> bool:
        """
        Define um novo cargo para o funcionário, validando se é uma string plausível.

        Obs: A função `validar_nome` está sendo utilizada para validar o nome do cargo,
        assumindo que o cargo deve conter ao menos uma estrutura básica de texto.

        Args:
            cargo (str): Novo cargo a ser atribuído.

        Returns:
            bool: True se o cargo for alterado com sucesso, False caso contrário.
        """
        if validar_nome(cargo):
            self._cargo = cargo
            print("Cargo alterado com sucesso.")
            return True
        print("Cargo inválido.")
        return False

    def set_salario(self, salario: float) -> bool:
        """
        Define um novo salário para o funcionário, validando se é um valor positivo.

        Args:
            salario (float): Novo valor salarial.

        Returns:
            bool: True se o salário for válido, False caso contrário.
        """
        if validar_salario(salario):
            self.__salario = salario
            print("Salário atualizado com sucesso.")
            return True
        print("Salário inválido.")
        return False

    def aumentar_salario(self, porcentagem: int) -> None:
        """
        Aplica um aumento salarial com base em uma porcentagem fornecida.

        Args:
            porcentagem (int): Porcentagem de aumento a ser aplicada (ex: 10 para 10%).

        Returns:
            None
        """
        novo_valor = calcular_aumento_salarial(self.get_salario(), porcentagem)
        self.__salario = novo_valor
        print(f"Aumento de {porcentagem}% aplicado com sucesso.")
    
    def mostrar_dados(self):
        return f"{"-"*65}\nDados Pessoais\n{"-"*65}\nNome: {self.get_nome()}\nIndentidade: {self.get_documento()}\nCargo: {self.get_cargo()}\n{"-"*65}"
