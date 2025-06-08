# documentação
# https://docs.python.org/pt-br/3.13/library/os.html

import os

"""
Este mapeamento pode ser usado para modificar o ambiente, 
além de consultá-lo. putenv() será chamado automaticamente 
quando o mapeamento for modificado

No Windows, as chaves são convertidas em maiúsculas. Isso 
também se aplica ao obter, definir ou excluir um item. Por 
exemplo, environ['monty'] = 'python' mapeia a chave 'MONTY' 
para o valor 'python'
"""


def exibir_variaveis_de_ambiente() -> dict:
    variaveis_ambiente = (
        os.environ
    )  # retorna um dicionário representando o ambiente do processo(computador)

    # consulta todas variaveis de ambiente e suas informações
    for variavel, informacoes in variaveis_ambiente.items():
        print(f"Nome: {variavel}\t Informações: {informacoes}")

    return variaveis_ambiente


# checa se o tipo de sistema operacional nativo esta em bytes
def checar_sistema_nativo() -> bool:
    if os.supports_bytes_environ:
        print("\nSistema Nativo está em bytes.\n")
        return True

    print("\nSistema Nativo NÃO está em bytes.\n")
    return False


# se sim podemos verificar as variaveis de ambiente em bytes
def exibir_variaveis_em_bytes(sinal: bool) -> None:
    if sinal:
        for x, y in os.environb.items():
            print(f"Nome: {x}\t Informações: {y}")


if __name__ == "__main__":
    exibir_variaveis_de_ambiente()
    sinal = checar_sistema_nativo()
    exibir_variaveis_em_bytes(sinal)
