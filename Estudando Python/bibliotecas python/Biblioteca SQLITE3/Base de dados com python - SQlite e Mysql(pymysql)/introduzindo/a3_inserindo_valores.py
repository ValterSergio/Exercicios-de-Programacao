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

print("registrando valores nas colunas da tabela")


# Registrando com execute do cursor
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, peso)  VALUES (NULL, "Valter Sérgio", 73.5)'
)  # aqui é executado apenas um registro

print("Comitando um unico registro com execute.")
connection.commit()

print("Podemos apagar uma tabela inteira com DElETE")
# no sql tem o truncatetable - mas o sqlite não possui esse
# comando, mas tem delete

# apagando com cursor
cursor.execute(f"DELETE FROM {TABLE_NAME}")

print(
    "Todos os valores registrados até esse momento foram apagados, mas a sequencia de ID continua seguindo enfrente"
)
connection.commit()

print("Apagando o registro de sequencias -  se quiser zerar os ID   ")
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}" ')

connection.commit()

print("Registrando muitos valores.")

cursor.execute(
    f"INSERT INTO {TABLE_NAME} (id, name, peso) "
    ' VALUES (NULL, "Valter Tertuliano", 73.5), (NULL, "Sérgio Ribeiro", 70.5)'
)  # aqui é executado varios registro

print("Comitando todos os registros.")
connection.commit()


print("Fechando conexão")

# sempre devemos fechar o cursor e o banco de dados
cursor.close()
connection.close()
