import sqlite3

from pathlib import Path

# salvando o diretorio raiz
ROOT_DIR = Path(__file__).parent

# Nome do arquivo de dados
DB_NAME = "db.sqlite3"

# caminho do arquivo
DB_FILE = ROOT_DIR / DB_NAME

# Definindo nome da tabel
TABLE_NAME = "customers"

print("Iniciando conexão")

# iniciando conexão
connection = sqlite3.connect(DB_FILE)

print("Iniciando Cursor")

# iniciando cursor
cursor = connection.cursor()

print("Criando Tabela de dados")

# Usando cursor para criar tabela
cursor.execute(
    # verificar se a tabela não existe
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "name TEXT,"
    "peso REAL"
    ")"
)

print("Comitando banco de dados")

# realizando commit com connection
connection.commit()

print("Fechando conexão")

# sempre devemos fechar o cursor e o banco de dados
cursor.close()
connection.close()
