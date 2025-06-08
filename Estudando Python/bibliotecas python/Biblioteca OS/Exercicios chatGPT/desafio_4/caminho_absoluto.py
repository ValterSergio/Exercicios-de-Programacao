from os.path import abspath

def informar_caminho_absoluto(caminho: str) -> str:
    """
    Retorna o caminho absoluto de um arquivo ou diretório.

    Esta função recebe um caminho relativo e retorna o caminho absoluto correspondente.

    Args:
        caminho (str): O caminho do arquivo ou diretório (pode ser relativo ou absoluto).
    
    Returns:
        str: O caminho absoluto do arquivo ou diretório especificado.
    
    Exemplo:
        informar_caminho_absoluto('arquivo_teste.txt')
        # Retorna algo como: '/home/usuario/projeto/arquivo_teste.txt'
    """
    return abspath(caminho)

if __name__ == "__main__":
    from os import remove
    nome_arquivo = 'arquivo_teste.txt'
    
    # criando arquivo de teste
    criar = open(nome_arquivo, 'w')
    criar.close()

    caminho = informar_caminho_absoluto(nome_arquivo)
    print(f"O caminho absoluto do arquivo {nome_arquivo}:")
    print("-" * 79)
    print(f'Caminho: ', caminho)
    print("-" * 79)

    # apaga o arquivo criado
    remove(caminho)
