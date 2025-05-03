import os
import sys

# Adiciona o diretório pai ao sys.path para permitir a importação de módulos externos
pasta_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(pasta_pai)

from app.pessoa import Pessoa
from ferramentas.funcoes_auxiliares import gerador_de_cpf

def teste_classe_pessoa():
    """
    Executa testes manuais na classe Pessoa, demonstrando a criação de objetos,
    uso de getters e setters, e validação de dados (CPF, nome e senha).
    """

    # Instanciando a classe com dados iniciais
    p1 = Pessoa("Valter", "016-9940*90+2.8/7,6.54>45", "@Vs12345678")

    # Exibe os dados iniciais obtidos pelos getters
    print("-" * 70)
    print("\nExibindo Getters com dados Iniciais\n")
    print("-" * 70)
    print(f"Nome : {p1.get_nome()}")
    print(f"CPF  : {p1.get_documento()}")
    print(f"Senha: {p1.get_senha_portal()}")
    print("-" * 70)

    # Realiza alterações nos atributos usando os setters
    print("\nUsando Setter para trocar os atributos\n")
    print("-" * 70)
    trocar_nome = p1.set_nome("Valter Sergio Ribeiro Tertuliano")
    trocar_cpf = p1.set_documento(gerador_de_cpf())
    troca_senha = p1.set_senha_portal("@Sr12345678")
    print("-" * 70)
    print("Atributos trocados")
    print("-" * 70)

    # Exibe os dados atualizados
    print("\nExibindo os novos atributos\n")
    print("-" * 70)
    print(f"Nome : {p1.get_nome()}")
    print(f"CPF  : {p1.get_documento()}")
    print(f"Senha: {p1.get_senha_portal()}")
    print("-" * 70)

    print("Metodo exibir dados")
    dados = p1.mostrar_dados()
    print(dados)
    # Remove o objeto da memória
    del p1
    print("Objeto deletado com sucesso.")


# Executa o teste somente se o arquivo for executado diretamente
if __name__ == "__main__":
    teste_classe_pessoa()