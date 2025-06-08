from os import mkdir, rmdir

def criar_pasta(nome: str):
    """
    Cria uma nova pasta com o nome especificado.

    Args:
        nome (str): O nome da pasta a ser criada.
    
    Exemplo:
        criar_pasta('nova_pasta')
    """
    mkdir(nome)
    print("Pasta criada com sucesso: ", nome)


def remover_pasta(nome: str) -> None:
    """
    Remove a pasta especificada.

    Args:
        nome (str): O nome da pasta a ser removida.
    
    Exemplo:
        remover_pasta('pasta_antiga')
    """
    rmdir(nome)
    print("Pasta removida com sucesso: ", nome)

if __name__ == "__main__":

    # queremos ver a pasta sendo criada
    from time import sleep

    nome = 'diretorio_teste'
    criar_pasta(nome)
    sleep(10)
    remover_pasta(nome)
    print("\nFim da execução do programa.")
