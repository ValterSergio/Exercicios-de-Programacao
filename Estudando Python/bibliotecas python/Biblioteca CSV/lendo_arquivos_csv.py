# https://medium.com/data-hackers/escrita-e-leitura-de-arquivos-csv-em-python-6a256c608818

from pathlib import Path
CAMINHO_CSV = Path(__file__).parent / 'arquivo_csv.csv'

import csv

print("\nExibindo no formato padrão\n")
with open(CAMINHO_CSV, 'r', encoding='utf-8') as arquivo:
    
    # o reader retorna um objeto para ser interado 
    # o delimitador com virgula é para delimitar as colunas
    leitor = csv.reader(arquivo, delimiter=',')

    # leitor.__next__() # usa para pular o cabeçalho

    
    for linha in leitor:
        print(linha)

print("\nExibindo em formato chave-valor\n")
with open(CAMINHO_CSV, 'r', encoding='utf-8') as arquivo:
    
    # o reader retorna um objeto para ser interado 
    # o delimitador com virgula é para delimitar as colunas
    leitor = csv.DictReader(arquivo)

    # leitor.__next__() # usa para pular o cabeçalho

    
    for linha in leitor:
        print(linha)