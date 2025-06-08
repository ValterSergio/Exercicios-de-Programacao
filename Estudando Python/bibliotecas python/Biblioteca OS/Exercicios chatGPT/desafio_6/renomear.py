from os import rename

def renomear_arquivo(antigo: str, novo: str) -> None:
    return rename(antigo, renomear)


if __name__ == "__main__":
    from os import remove

    nome = "novo_arquivo.txt"
    arquivo = open(nome, 'w')
    arquivo.close()

    renomear = 'arquivo_renomeado.txt'
    renomear_arquivo(nome, renomear)

    # apagar o arquivo
    remove(renomear)