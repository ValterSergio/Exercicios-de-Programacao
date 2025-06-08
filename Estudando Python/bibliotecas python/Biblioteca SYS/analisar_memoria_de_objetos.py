import sys


def obter_tamanho_do_objeto_si(objeto):
    print(f"O objeto {type(objeto)} tem {sys.getsizeof(objeto)} bytes - multiplos de 8 ( bit )")
    return sys.getsizeof(objeto)

# listas armazenam referencias aos objetos ( o endereço da 
# memoria e não o valor em si)
lista = list(range(10**6))

# conjuntos usam tabelas de hash (podem ser mais eficientes 
# em alguns casos)
conjunto = set(range(10**6))

tamanho_lista = obter_tamanho_do_objeto_si(lista)
tamanho_conjunto = obter_tamanho_do_objeto_si(conjunto)

# isso nos ajuda a encontrar as estruturas de dados mais 
# eficientes para trabalhar
if tamanho_conjunto < tamanho_lista:
    print("\nUsar o conjunto, ocupa menos memoria que usar listas")
else:
    print("\nUsar lista, ocupa menos memoria que usar conjuntos")

