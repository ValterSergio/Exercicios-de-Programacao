import sqlite3
from pathlib import Path

# salvando o diretorio raiz
ROOT_DIR = Path(__file__).parent

# Nome do arquivo de dados
DB_NAME = "db.sqlite3"

# caminho do arquivo
DB_FILE = ROOT_DIR / DB_NAME


print("Iniciando conexão")
# iniciando conexão
connection = sqlite3.connect(DB_FILE)

# curso
cursor = connection.cursor()

print("Fechando conexão")
# sempre devemos fechar o cursor e o banco de dados
cursor.close()
connection.close()
