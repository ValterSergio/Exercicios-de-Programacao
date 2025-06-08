import os
from shutil import rmtree

principal = 'principal'

# o bloco try é apenas para garantir que o programa não vai travar, por fileExistError, e nem ter que ficar apagando pasta manualmente
try:
    # criar pasta principal
    os.mkdir(principal)
except Exception as Error:
    print(f"Erro: {str(Error)}")
    rmtree(principal)   
finally:
    os.mkdir(principal)


# entrar na pasta principal criada
os.chdir(principal)

# checar se estamos na pasta criada
print(os.getcwd())

# definindo nome padrão para pastas
subpastas = 'subpasta'

# automatizando criação de pastas
for x in range(3):
    nome_pasta = f'{subpastas}{str(x+1)}'
    os.mkdir(nome_pasta)

# listando diretorio principal
for pasta in os.listdir():
    print("Pasta: ", pasta)

# apagando pastas geradas

os.chdir('..') # voltando para pasta raiz
rmtree(principal) # apagando pasta criada