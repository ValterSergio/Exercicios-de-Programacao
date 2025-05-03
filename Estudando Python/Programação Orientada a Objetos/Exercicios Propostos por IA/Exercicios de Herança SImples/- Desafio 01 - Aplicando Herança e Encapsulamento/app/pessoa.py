import os
import sys

# Adiciona o diretório pai ao sys.path para permitir a importação de módulos externos
pasta_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(pasta_pai)

"""
Desafio: Sistema de Funcionários com Controle de Acesso

Cenário:
Sistema simples de cadastro de funcionários para uma empresa.
O objetivo é proteger dados sensíveis dos colaboradores, permitindo que 
outras partes do sistema interajam com segurança e controle sobre essas informações.
"""

from ferramentas.funcoes_auxiliares import limpar_cpf, validar_cpf, validar_nome, validar_senha


class Pessoa:
    """
    Classe que representa uma pessoa com nome, CPF e senha de acesso a um sistema interno.
    """

    def __init__(self, nome: str, documento: str, senha_portal: str):
        """
        Construtor da classe Pessoa.

        Args:
            nome (str): Nome completo da pessoa.
            documento (str): CPF da pessoa, possivelmente com caracteres especiais.
            senha_portal (str): Senha de acesso ao sistema.
        """
        self.nome = nome
        self._documento = limpar_cpf(documento)  # Armazena apenas os números do CPF
        self.__senha_portal = senha_portal       # Armazena a senha de forma privada

    def get_nome(self) -> str:
        """
        Retorna o nome atual da pessoa.

        Returns:
            str: Nome completo da pessoa.
        """
        return self.nome

    def set_nome(self, nome: str) -> bool:
        """
        Define um novo nome para a pessoa, se for um nome completo válido.

        Args:
            nome (str): Novo nome completo.

        Returns:
            bool: True se o nome for válido e alterado com sucesso, False caso contrário.
        """
        if validar_nome(nome):
            self.nome = nome
            return True
        return False

    def get_documento(self) -> str:
        """
        Retorna o CPF (documento) da pessoa.

        Returns:
            str: CPF com apenas os números.
        """
        return self._documento

    def set_documento(self, novo: str) -> bool:
        """
        Define um novo CPF para a pessoa, após validar sua estrutura e autenticidade.

        Args:
            novo (str): Novo CPF, com ou sem caracteres especiais.

        Returns:
            bool: True se o CPF for válido e atualizado com sucesso, False caso contrário.
        """
        cpf = limpar_cpf(novo)
        if validar_cpf(cpf):
            self._documento = cpf
            return True
        return False

    def get_senha_portal(self) -> str:
        """
        Retorna a senha atual da pessoa.

        Returns:
            str: Senha do portal.
        """
        return self.__senha_portal

    def set_senha_portal(self, senha: str) -> bool:
        """
        Define uma nova senha para o portal, caso atenda aos critérios de segurança.

        Args:
            senha (str): Nova senha desejada.

        Returns:
            bool: True se a senha for válida e atualizada, False caso contrário.
        """
        if validar_senha(senha):
            self.__senha_portal = senha
            return True
        return False

    def mostrar_dados(self) -> str:
        """Exibe nome e indentidade da Pessoa"""
        return f"{"-"*65}\nDados Pessoais\n{"-"*65}\nNome: {self.get_nome()}\nIndentidade: {self.get_documento()}\n{"-"*65}"

