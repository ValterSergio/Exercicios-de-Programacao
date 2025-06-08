import sys


# sabe que modulos que fazem parte do nucleo do python e são
# carregados diretamente na memoria do python possue ( built-in ) 

# modulos congelados são modulos escritos em python, mas 
# compilados e incluidos dentro do interpretador para
# inicialização rapida

# Modulos carregados de arquivos, são modulos normais que são 
# importados de arquivos .py do sistema

def analisar_modulos_carregados():
    print("Conhecendo os modulos já carregados:")
    # cria uma copia por segurança
    modulos = sys.modules.copy()

    # vemos que isso é um dcionario
    print(type(modulos))

    # vamos fazer uma iteração simples apenas para observar
    for modulo in modulos:
        print(modulo, end=', ')

    # vamos olhar melhor esse dicionario
    print()
    for chave, valor in modulos.items():
        print("Chave: ", chave, "\tValor: ", str(valor))
        if '(built-in)' in str(valor):
            print("Modulo internos ( padrão )\n")
        elif '(frozen)' in str(valor):
            print("Modulo Congelado ( intepertrador )\n")
        elif '.py' in str(valor):
            print("Modulo Normais ( importados de arquivo '.py'\n )\n")
        else:
            print("Tipo de modulo desconhecido")


