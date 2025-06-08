import os

# conseguimos obter o diretorio de trabalho atual
local_de_trabalho = os.getcwd()  # retorna uma str com o caminho
print("\nLocal de trabalho atual: ", local_de_trabalho)

# podemos alterar o diretorio de trabalho
os.chdir("C:\\Users\\valte\\Desktop\\")  # vamos mudar para desktop
print("\nMudando local de trabalho: ", os.getcwd())

# podemos listar todas as pastas e arquivos no local de trabalho atual
obter_arquivos_e_diretorios = os.listdir(".")  # nesse momento estamos no desktop

print("\nArquivos do Desktop: ", obter_arquivos_e_diretorios)

# podemos criar pasta
criar_pasta = f"{str(os.getcwd())}\\pasta_criada_com_mkdir"  # estou montando o caminho antes de criar a pasta
print("\nCaminho para nova pasta: ", criar_pasta)

# checamos se a pasta não existe
if not os.path.exists(criar_pasta):
    print("\nPasta sendo criada...")
    os.mkdir(criar_pasta)
    print("Confirmando nova pasta: ", os.listdir("."))
else:
    print("\nPasta já foi criada anteriormente")

# podemos criar uma estrutura mas completa com varias pastas
criar_pastas_sequencias = f"{criar_pasta}\\um\\dois\\tres"
os.makedirs(criar_pastas_sequencias, exist_ok=True)

# podemos buscar todos os arquivos e diretorios recursivamente
for raiz, pasta, arquivo in os.walk(criar_pasta):
    print(f"Caminho das pastas criadas: ", raiz)

print()

# podemos apagar pastas vazias usando OS, no caso precisei de um loop para apagar as que foram criadas anteriormente
while os.path.exists(criar_pasta):
    for raiz, pasta, arquivo in os.walk(criar_pasta):
        try:
            os.rmdir(raiz)
            print("Pasta apagada: ", raiz)
        except:
            continue

print(f"\nConfirmando deletamento: ", os.listdir("."))

# podemos voltar para o local de trabalho inicial agora
os.chdir(local_de_trabalho)
print("\nLocal de origem: ", os.getcwd())
