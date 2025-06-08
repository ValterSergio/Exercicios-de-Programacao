from os.path import exists

def criar_arquivo_txt(nome: str) -> None:
    """
    Cria um arquivo de texto com o nome especificado e escreve uma lista de números no arquivo.

    Args:
        nome (str): O nome do arquivo a ser criado (sem a extensão .txt).
    
    Exemplo:
        criar_arquivo_txt('arquivo_exemplo')
    """
    nome_txt = f"{nome + '.txt'}"
    criar = open(nome_txt, 'w')
    criar.write(f"{[str(x) for x in range(10**6)]}")
    criar.close()
    print("Arquivo criado com sucesso: ", nome)

def verficar_se_existe_txt(nome: str) -> None:
    """
    Verifica se o arquivo de texto com o nome especificado existe.

    Args:
        nome (str): O nome do arquivo a ser verificado (sem a extensão .txt).
    
    Exemplo:
        verficar_se_existe_txt('arquivo_exemplo')
    """
    nome_txt = f"{nome + '.txt'}"
    if exists(nome_txt):
        print("O arquivo existe")
    else:
        print("O arquivo não existe")


if __name__ == "__main__":
    from time import sleep
    from os import remove
    nome = 'exemplo'

    print("Criando arquivo TXT")
    criar_arquivo_txt(nome)
    sleep(30)

    print("Confirmando existência do arquivo.")
    verficar_se_existe_txt(nome)
    print("Verificação concluída.")
    
    # apagando arquivo criado
    remove(nome + '.txt')
