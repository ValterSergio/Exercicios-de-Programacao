import os
import sys

# Adiciona o diretório pai ao sys.path para permitir importações de módulos na pasta 'app'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.gerente import Gerente
from ferramentas.funcoes_auxiliares import gerador_de_cpf

def testar_classe_gerente():
    """
    Função de teste para a classe Gerente.

    Testa:
    - Criação de um gerente
    - Exibição de dados
    - Aplicação de bônus no salário
    - Modificação do valor de bônus
    """

    # Cria uma instância de Gerente com valores iniciais
    g = Gerente("Edward", gerador_de_cpf(), "#4admsaçdmA", "Porteiro chefe", 1950.65, 5)

    # Exibe os dados atuais do gerente
    dados = g.mostrar_dados()
    print(dados)

    # Aplica o bônus e mostra o impacto no salário
    salario_anterior = g.get_salario()
    g.aplicar_bonus()
    novo_salario = g.get_salario()
    print(salario_anterior, novo_salario)

    # Altera o valor do bônus
    g.set_bonus(3)
    
    # Exibe os dados atualizados com o novo bônus
    dados = g.mostrar_dados()
    print(dados)

if __name__ == "__main__":
    testar_classe_gerente()