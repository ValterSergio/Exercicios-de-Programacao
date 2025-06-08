from os import listdir

def listar_arquivos_e_diretorios() -> None:
    """
    Lista os arquivos e diretórios presentes no diretório atual.

    A função percorre todos os objetos no diretório atual e os exibe 
    com seus respectivos índices.

    Exemplo de saída:
        Total de objetos : nome do objeto
        0: arquivo1.txt
        1: pasta1
        2: arquivo2.csv
    """
    print("Total de objetos : nome do objeto")
    for num, item in enumerate(listdir()):
        print(f'{num}: {item}')

if __name__ == "__main__":

    listar_arquivos_e_diretorios()
