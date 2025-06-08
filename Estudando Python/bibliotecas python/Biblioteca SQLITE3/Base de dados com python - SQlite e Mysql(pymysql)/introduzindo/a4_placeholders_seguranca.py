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
cursor.execute(sql, ['Valter T', 65])  # aqui é executado apenas um registro

sql_varios_dados = (
    f'INSERT INTO {TABLE_NAME} ' 
    '(id, name, peso) '
    ' VALUES '
    '(NULL, "Valter Tertuliano", 73.5), (NULL, "Sérgio Ribeiro", 70.5)'
)
cursor.execute(sql_varios_dados)  # aqui é executado varios registro

print("Comitando todos os registros.")
connection.commit()

# sempre devemos fechar o cursor e o banco de dados
print("Fechando conexão")
cursor.close()
connection.close()
