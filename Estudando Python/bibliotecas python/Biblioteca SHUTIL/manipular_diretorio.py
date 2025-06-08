import shutil
import os

try:
    # Definição da estrutura de diretórios (árvore de pastas)
    arvore_de_pastas = 'pasta1/pasta2/pasta3/pasta4'

    # Criando a estrutura de diretórios definida acima
    # `exist_ok=True` evita erro caso a pasta já exista
    os.makedirs(arvore_de_pastas, exist_ok=True)

    # Copiando toda a pasta 'pasta1' e seu conteúdo para 'destino_teste2'
    shutil.copytree('pasta1', 'destino_teste2')

    # Apagando toda a pasta 'destino_teste2' (cópia feita anteriormente)
    shutil.rmtree('destino_teste2')

    # Apagando a pasta original 'pasta1' e toda a sua estrutura interna
    shutil.rmtree('pasta1')

    # Criando e compactando arquivos

    # Função para criar arquivos com conteúdo de texto
    def criar_arquivo(nome, texto):
        with open(nome, 'w') as criar:
            criar.write(texto)

    # Criando um diretório para armazenar os arquivos que serão compactados
    compactar = 'compactando_arquivos'
    os.mkdir(compactar)

    # Criando 1000 arquivos de texto dentro da pasta 'compactando_arquivos'
    for x in range(1000):
        nome = f'teste{x}.txt'  # Nome do arquivo
        texto = f'{str(x) * x}'  # Conteúdo do arquivo: repete o número 'x', 'x' vezes
        criar_arquivo(nome, texto)  # Cria o arquivo
        shutil.move(nome, compactar)  # Move o arquivo criado para a pasta de compactação

    # Compactando a pasta 'compactando_arquivos' em um arquivo ZIP chamado 'compactados.zip'
    shutil.make_archive('compactados', 'zip', compactar)

    # Criando um diretório onde os arquivos serão extraídos
    extrair = 'extraindo_arquivos'
    os.mkdir(extrair)

    # Extraindo os arquivos do ZIP recém-criado para a pasta 'extraindo_arquivos'
    shutil.unpack_archive('compactados.zip', extrair)

except FileExistsError:
    # Se os arquivos ou pastas já existirem, exibe uma mensagem de erro
    print("Arquivos já existem")

finally:
    # Removendo o arquivo ZIP após a extração
    os.remove('compactados.zip')

    # Removendo a pasta com os arquivos originais compactados
    shutil.rmtree(compactar)

    # Removendo a pasta com os arquivos extraídos
    shutil.rmtree(extrair)
