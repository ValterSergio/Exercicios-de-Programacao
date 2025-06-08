from os import mkdir, replace
from shutil import rmtree

def criar_pasta(nome_pasta: str) -> None:
    """
    Cria uma pasta para armazenar arquivos.

    Parâmetros:
    nome_pasta (str): O nome da pasta a ser criada.
    
    Retorno:
    None
    """
    mkdir(nome_pasta)

def criar_arquivo(nome: str, conteudo: str) -> None:
    """
    Cria um arquivo e escreve um conteúdo dentro dele.

    Parâmetros:
    nome (str): O nome do arquivo a ser criado.
    conteudo (str): O conteúdo a ser escrito no arquivo.
    
    Retorno:
    None
    """
    with open(nome, 'w') as arquivo:
        arquivo.write(conteudo)

def mover_arquivo(nome: str, destino: str) -> None:
    """
    Move um arquivo para um diretório específico.

    Parâmetros:
    nome (str): O nome do arquivo a ser movido.
    destino (str): O diretório de destino.
    
    Retorno:
    None
    """
    replace(nome, f'{destino}/{nome}')

def apagar_pasta(nome_pasta: str) -> None:
    """
    Apaga uma pasta e todo o seu conteúdo.

    Parâmetros:
    nome_pasta (str): O nome da pasta a ser removida.
    
    Retorno:
    None
    """
    rmtree(nome_pasta)

def main() -> None:
    """
    Função principal que cria uma pasta, gera arquivos dentro dela
    e depois remove a pasta gerada.
    """
    nome_pasta = 'pasta_de_arquivos'
    
    # Criar a pasta
    criar_pasta(nome_pasta)

    # Criar e mover arquivos para a pasta
    for x in range(5):
        nome_arquivo = f'arquivo{x+1}.txt'
        conteudo = str([f'{str(y + 1)} ' for y in range(10**6)])  # Gera uma lista de números como string
        
        criar_arquivo(nome_arquivo, conteudo)  # Cria o arquivo
        mover_arquivo(nome_arquivo, nome_pasta)  # Move para a pasta

    # Apagar a pasta criada
    apagar_pasta(nome_pasta)

if __name__ == "__main__":
    main()
