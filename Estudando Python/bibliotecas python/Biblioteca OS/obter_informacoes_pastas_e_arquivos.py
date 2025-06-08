import os

def obter_informacoes_arquivos(caminho: str) -> None:
    info = os.stat(caminho)
    # Exibe todas as informações coletadas
    print(f"Modo de permissões: {oct(info.st_mode)}")
    print(f"Inode: {info.st_ino}")
    print(f"ID do dispositivo: {info.st_dev}")
    print(f"Número de hard links: {info.st_nlink}")
    print(f"UID (dono): {info.st_uid}")
    print(f"GID (grupo): {info.st_gid}")
    print(f"Tamanho: {info.st_size} bytes")
    print(f"Último acesso (timestamp): {info.st_atime}")
    print(f"Última modificação (timestamp): {info.st_mtime}")
    print(f"Última mudança de metadados (Unix) ou criação (Windows) (timestamp): {info.st_ctime}")


if __name__ == "__main__":
    # definimos um caminho relativo
    caminho = "arquivo.txt"

    # criamos um arquivo para fins de teste
    arquivo = open(caminho, "w")
    arquivo.write("Conhecendo stats")
    arquivo.close()

    # obtemos o caminho absoluto do arquivo criado
    caminho_absoluto = os.path.abspath(caminho)

    obter_informacoes_arquivos(caminho_absoluto)

    # apagando arquivo de teste
    os.remove(caminho_absoluto)
