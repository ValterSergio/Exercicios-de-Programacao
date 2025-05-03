import os
import sys

# Adiciona o diretório pai ao sys.path para permitir a importação de módulos da pasta 'app'
pasta_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(pasta_pai)

# Importações de classes necessárias para compor o teste
from app.departamento import Departamento
from app.funcionario import Funcionario
from app.gerente import Gerente
from app.estagiario import Estagiario
from app.terceirizado import Terceirizado

from ferramentas.funcoes_auxiliares import gerador_de_cpf

def testar_classe_departamento_com_funcionario():
    """
    Função de teste para a classe Departamento.

    Esse teste cria uma instância de Departamento e adiciona múltiplos funcionários a ele.
    Em seguida, exibe a lista de funcionários cadastrados no departamento.

    Objetivo:
    - Verificar o funcionamento do método `adicionar_funcionario`.
    - Verificar se o método `listar_funcionarios` exibe corretamente os dados.

    Observações:
    - Utiliza objetos da classe Funcionario como dependência.
    """

    # Criação de três funcionários com dados fictícios
    funcionario1 = Funcionario("Valter", gerador_de_cpf(), "dçaksçdkaskda", "Desenvolvedor Jr", 2_906.36)
    funcionario2 = Funcionario("Wando", gerador_de_cpf(), "dçaksçdkaskda", "Desenvolvedor Jr", 2_906.36)
    funcionario3 = Funcionario("Wagner", gerador_de_cpf(), "dçaksçdkaskda", "Desenvolvedor Jr", 2_906.36)

    # Criação do departamento de Tecnologia da Informação (T.I)
    departamento = Departamento("T.I")

    # Lista de funcionários para serem adicionados ao departamento
    funcionarios = [funcionario1, funcionario2, funcionario3]

    # Adiciona cada funcionário à instância do departamento
    print("Adicionando Funcionarios no departamento")
    for funcionario in funcionarios:
        departamento.adicionar_funcionario(funcionario)
        print(funcionario.mostrar_dados())
    print()
    
    # Exibe todos os funcionários cadastrados no departamento
    departamento.listar_funcionarios()

def testar_classe_departamento_com_todos_funcionarios():
    gerente = Gerente("Louiis", gerador_de_cpf(), "9878564", "Gerente de Vendas", 6952.48, 5)

    estagio = Estagiario("Guri", gerador_de_cpf(), "kjdaskd,dsmn", "Assistente administrativo", 0, 12, 1650)

    tercerizado = Terceirizado("red", gerador_de_cpf(), "09iukmn", "Limpador de Vidros",  1958.49, "vidros S.A")
    
    lista = [gerente, estagio, tercerizado]
    for pessoa in lista:
        print(pessoa.mostrar_dados())

# Executa o teste somente se o arquivo for executado diretamente
if __name__ == "__main__":
    testar_classe_departamento_com_funcionario()
    print()
    testar_classe_departamento_com_todos_funcionarios()