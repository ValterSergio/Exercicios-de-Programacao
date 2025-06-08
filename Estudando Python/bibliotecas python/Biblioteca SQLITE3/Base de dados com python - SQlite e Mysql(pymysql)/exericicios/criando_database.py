from pathlib import Path
import sqlite3
import string
import random
import os

DIRETORIO_RAIZ =    Path(__file__).parent
BANCO_DE_DADOS = 'db.sqlite3'
CAMINHO_DADOS = DIRETORIO_RAIZ / BANCO_DE_DADOS


# função para geração de dados ficticios
def gerar_dados(total=100):
    lista_principal = []

    def criar_nome_peso():
        # criando sublista para receber as letras
        sublista = []

        # escolher 5 letras para simular nomes
        for _ in range(5):
            
            sublista.append(random.choice(string.ascii_lowercase))

        # escolher um numero aleatorio para simular o exemplo de peso
        numero = random.choice(range(60, 120))

        # unir as letras na sublista para formar as palavras
        nome = ''.join(sublista)

        # adicionar o nome e o numero criando uma lista de lista dentro da lista principal
        lista_principal.append([nome, numero])

    # podemos criar quantos dados agente quiser
    for x in range(total):
        criar_nome_peso()
    
    return lista_principal


if __name__ == "__main__":
    conectar = sqlite3.connect(CAMINHO_DADOS)
    cursor = conectar.cursor()

    # primeiro vamos gerar dados ficticios
    dados = gerar_dados(total=10_000) # vamos adicionar os dados

    # vamos escolher um nomepara tabela
    NOME_TABELA ='TABELA_FAKE'

    # Vamos criar essa tabela
    cursor.execute(
        # verificamos se a tabela não existe ANTES DE CRIAR
        f"CREATE TABLE IF NOT EXISTS {NOME_TABELA} ("
        # definimos o id com um inteiro para a chave primaria, com auto incremento
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "

        # Definimos agora as colunas da tabela
        "nome TEXT, "
        "peso REAL"

        ")"
    )

    # agora vamos adicionar dados a essas colunas
    adicionar_dados = (

        # COMO PARA INSERIR DADOS NA TABELA INDICADA
        f"INSERT INTO {NOME_TABELA}"

        # JOGAMOS DENTRO DE UMA "TUPLA" O NOME DAS COLUNAS
        "(nome, peso)"

        # agora informamos os valores
        "VALUES"
        "(?, ?)"

    )

    # agora vamos adicionar os dados gerados dentro da tabela
    cursor.executemany(adicionar_dados, dados)

    # fazemos o comit para salvar os registros
    conectar.commit()

    # fechando banco de dados
    cursor.close()
    conectar.close()

    # por mera curiosidade qual tamano do arquivo de dados
    # Verificar o tamanho do arquivo de banco de dados em MB
    tamanho_bytes = os.path.getsize(CAMINHO_DADOS)
    tamanho_mb = tamanho_bytes / (1024 * 1024)

    print(f"O arquivo de banco de dados tem: {tamanho_mb:.2f} Megabytes")