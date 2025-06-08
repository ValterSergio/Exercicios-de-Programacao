# https://docs.python.org/3/library/csv.html

from pathlib import Path
CAMINHO_CSV = Path(__file__).parent / 'escrever_arquivo.csv'
CAMINHO_CSV_DICT = Path(__file__).parent / 'escrever_arquivo_dict.csv'

import csv

lista_dicionario = [
    {'nome': 'valter', 'idade':30, 'peso': 73},
    {'nome': 'wagner', 'idade':32, 'peso': 62},
    {'nome': 'wictor', 'idade':28, 'peso': 52},
]

print("\nEscrevendo CSV com WRITER\n")

with open(CAMINHO_CSV, 'w', encoding='utf-8') as arquivo:
    
    # passar o nome das colunas
    colunas = lista_dicionario[0].keys()

    # chamamos o escritor
    escritor = csv.writer(arquivo, lineterminator='\n')

    # escrevemos essas colunas no arquivo
    escritor.writerow(colunas)
    escritor.writerow('')

    # percorremos a lista de dicionarios
    for id in lista_dicionario:
        escritor.writerow(id.values())

print("\nEscrevendo CSV com DICTWRITER\n")

with open(CAMINHO_CSV_DICT, 'w', encoding='utf-8') as arquivo:
    
    # passar o nome das colunas
    colunas = lista_dicionario[0].keys()

    # chamamos o escritor DictWriter e passamos o arquivo( f ) a coluna( fieldnames) e a formatação( dialect )
    escritor = csv.DictWriter(f=arquivo, fieldnames=colunas, dialect='excel', lineterminator='\n')

    # podemos adicionar o cabeççalho ( opcional )
    escritor.writeheader()

    # percorremos a lista de dicionarios
    for id in lista_dicionario:
        escritor.writerow(id)
