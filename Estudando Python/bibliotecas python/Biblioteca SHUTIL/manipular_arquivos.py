import shutil
import os

# Função para criar arquivos com conteúdo
def criar_arquivo(nome):
    with open(nome, 'w') as criar:
        criar.write("testando biblioteca shutil.")

# Definindo caminho de origem do arquivo 
caminho_origem = 'arquivo_teste.txt'

# Definindo pasta de destino do arquivo
caminho_destino = 'destino_teste'
os.mkdir(caminho_destino)

# Criando um arquivo na raiz da pasta
criar_arquivo(caminho_origem)

# Movendo o arquivo para a pasta de destino
shutil.move(caminho_origem, caminho_destino)

# Criando arquivo com metadados
copiar_metadados = 'copiar_metadados.txt'
criar_arquivo(copiar_metadados)

# Copiando o arquivo com os metadados
shutil.copy2(copiar_metadados, caminho_destino)

# Criando e copiando apenas o conteúdo de um arquivo
copiar_conteudo_sem_metados = 'copiar_conteudo.txt'
with open(copiar_conteudo_sem_metados, 'w') as escrever:
    escrever.write("Testando a copia de conteudo de arquivo")

receber_copia_de_conteudo = 'receber_conteudo.txt'
with open(receber_copia_de_conteudo, 'w') as receber:
    pass  # Cria o arquivo vazio

# Copiando o conteúdo de um arquivo para outro sem os metadados
shutil.copyfile(copiar_conteudo_sem_metados, receber_copia_de_conteudo)

# Copiando as permissões de um arquivo
copiar_permissao = 'copiar_permissao.txt'
with open(copiar_permissao, 'w') as novo:
    novo.write("Copiando as permissoes do arquivo")

receber_copia_permissao = 'receber_permissao.txt'
criar_arquivo(receber_copia_permissao)

shutil.copymode(copiar_permissao, receber_copia_permissao)

# Exibindo o espaço de disco utilizado pela pasta 'destino_teste'
memoria_usada = shutil.disk_usage(caminho_destino)
print(f'Tipo de dado de saida: {type(memoria_usada)}')
print(f'Saida: {memoria_usada}')

# Limpando os arquivos e pastas criados
# Apagando a pasta de destino e todos os arquivos dentro dela
shutil.rmtree(caminho_destino)

# Removendo os arquivos criados na raiz do diretório
os.remove(copiar_metadados)
os.remove(copiar_conteudo_sem_metados)
os.remove(receber_copia_de_conteudo)
os.remove(copiar_permissao)
os.remove(receber_copia_permissao)
