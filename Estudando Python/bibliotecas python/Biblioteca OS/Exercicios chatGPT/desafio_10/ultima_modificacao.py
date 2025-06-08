from os.path import getmtime
from datetime import datetime

def obter_ultima_modificacao(arquivo: str) -> float:
    """
    Obtém o timestamp da última modificação de um arquivo.

    Parâmetros:
    arquivo (str): O caminho do arquivo.

    Retorno:
    float: O timestamp UNIX da última modificação do arquivo.
    """
    return getmtime(arquivo)

def converter_data(tempo_de_arquivo: float) -> str:
    """
    Converte um timestamp UNIX em uma data e hora formatadas.

    Parâmetros:
    tempo_de_arquivo (float): O timestamp UNIX.

    Retorno:
    str: A data e hora formatadas como "DD-MM-YYYY - HH:MM:SS".
    """
    return datetime.fromtimestamp(tempo_de_arquivo).strftime("%d-%m-%Y - %H:%M:%S")

def main() -> None: 
    """
    Função principal que obtém e exibe a última modificação de um arquivo.
    """
    # Caminho do arquivo a ser verificado
    caminho = './desafio_1/criar_e_remover_diretorio.py'

    # Obtém o timestamp da última modificação do arquivo
    data = obter_ultima_modificacao(caminho)

    # Converte o timestamp para um formato legível e exibe
    print("A data da última modificação:", converter_data(data))

if __name__ == "__main__":
    main()
