import os
import sys

# Adiciona o diretório pai ao sys.path para permitir a importação de módulos da pasta 'app'
pasta_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(pasta_pai)

from app.funcionario import Funcionario
from ferramentas.funcoes_auxiliares import gerador_de_cpf
def testar_classe_funcionario():
    """
    Função de teste para a classe Funcionario.

    Este teste cobre os seguintes pontos:
    - Criação de um objeto da classe Funcionario
    - Uso de métodos setters para modificar atributos
    - Uso de métodos getters para recuperar valores
    - Impressão dos dados pessoais formatados do funcionário
    """

    # Criação de um funcionário com dados fictícios
    f = Funcionario("Sergio", gerador_de_cpf(), "X@4asdA9", "Ajudante de Obras", 2_857.69)

    print("\nExibir Dados Pessoais")
    dados = f.mostrar_dados()  # Método que retorna informações formatadas do funcionário
    print(dados)
    print()

    # Testando modificações de atributos via setters
    print("Alterar Nome do Funcionário")
    f.set_nome("Sergio Ribeiro")
    print()

    print("Alterar Documento do Funcionário")
    f.set_documento("07845179914")
    print()

    print("Alterar Cargo do Funcionário")
    f.set_cargo("Meio Oficial de Obras")
    print()

    print("Alterar Salário do Funcionário")
    f.set_salario(3_057.75)
    print()

    # Recuperando valores com getters
    nome = f.get_nome()
    documento = f.get_documento()
    cargo = f.get_cargo()
    salario = f.get_salario()

    print("\nExibindo valores atualizados:")
    print("Nome:", nome)
    print("Documento:", documento)
    print("Cargo:", cargo)
    print("Salário:", salario)

# Executa o teste apenas se o arquivo for rodado diretamente
if __name__ == "__main__":
    testar_classe_funcionario()
