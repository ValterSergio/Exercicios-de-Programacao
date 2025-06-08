import os

"""
os.fsencode(filename)
Codifica o objeto caminho ou similar filename para tratador de erros e codificação do sistema de arquivos; retorna bytes inalterados.
"""


# podemos converter um caminho, objeto os similar de string para bytes
def codificar_caminho_para_bytes(caminho):
    # vamos usar fs ENCODE para converter a str para bytes
    caminho_em_bytes = os.fsencode(caminho)

    print(f"Caminho em Bytes: {caminho_em_bytes}")

    return caminho_em_bytes


def decodificar_caminho_para_bytes(caminho):
    # vamos usar fs DECODE para passar os bytes para str

    bytes_para_str = os.fsdecode(caminho)

    print(f"Bytes para str: {bytes_para_str}")

    return bytes_para_str


if __name__ == "__main__":
    # vamos pegar o caminho raiz do sistema
    caminho = os.environ["systemroot"]
    caminho_bytes = codificar_caminho_para_bytes(caminho)
    caminho_str = decodificar_caminho_para_bytes(caminho_bytes)
