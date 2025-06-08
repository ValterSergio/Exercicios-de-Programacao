import os
from shutil import rmtree

def mover_arquivo(arquivo: str, destino: str) -> None:
    """
    Move um arquivo para o diretório de destino, substituindo caso já exista.

    Parâmetros:
    arquivo (str): O nome do arquivo que será movido.
    destino (str): O diretório para onde o arquivo será movido.

    Retorno:
    None
    """
    os.replace(arquivo, f'{destino}/{arquivo}')  # Move o arquivo para o diretório especificado

if __name__ == '__main__':
    # Nome do arquivo a ser criado e movido
    nome = "mover_arquivo.txt"

    # Cria um arquivo vazio
    with open(nome, 'w') as arquivo:
        pass  # Apenas cria o arquivo sem escrever nada

    # Cria um diretório chamado "destino" para armazenar o arquivo
    os.mkdir('destino')

    # Move o arquivo recém-criado para o diretório "destino"
    mover_arquivo(nome, 'destino')

    # Remove o diretório "destino" e seu conteúdo
    rmtree('destino')
