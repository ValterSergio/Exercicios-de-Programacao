from os.path import getsize

def obter_tamanho_arquivo(arquivo: str) -> int:
    return getsize(arquivo)

if __name__ == '__main__':
    from os import remove

    # criando arquivo
    nome = "novo_arquivo.txt"
    arquivo = open(nome, 'w')
    arquivo.write(f'{[str(x) for x in range(10**6)]}')
    arquivo.close()

    print(f"O arquivo criado tem {obter_tamanho_arquivo(nome)} bytes")

    # removendo arquivo gerado
    remove(nome)