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

# iniciando cursor
cursor = connection.cursor()

print("Criando Tabela de dados")

# Usando cursor para criar tabela
tabela = (
    # verificar se a tabela não existe
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "name TEXT,"
    "peso REAL"
    ")"
)
cursor.execute(tabela)

# Registrando dados com execute do cursor
# essa tecnica permite separar os dados dos comando sql
sql = (
    f'INSERT INTO {TABLE_NAME}' 
    '(name, peso) ' 
    'VALUES ' 
    '(?, ?)'
)
# executemany precisa receber um iteravel 
cursor.executemany(sql, [['Valter T', 65], ['wagner', 73], ['wictor', 76]]) 

print("Comitando todos os registros.")
connection.commit()

cursor.close()
connection.close()
