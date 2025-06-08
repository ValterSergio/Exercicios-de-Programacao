from os.path import isfile

def verificar_caminho(caminho: str) -> str:
    """
    Verifica se o caminho fornecido corresponde a um arquivo ou a um diretório.

    Parâmetros:
    caminho (str): O caminho a ser verificado.

    Retorno:
    str: "Arquivo" se for um arquivo, "Diretorio" se for um diretório.
    """
    if isfile(caminho):
        return "Arquivo"
    return   "Diretorio"

if __name__ == "__main__":

    # Definição de caminhos para teste
    caminho1 = 'desafio_6'
    caminho2 = f'{caminho1}/renomear.py'
    
    # Exibe se os caminhos são arquivos ou diretórios
    print("O primeiro caminho é um", verificar_caminho(caminho1))
    print("O segundo caminho é um", verificar_caminho(caminho2))
