import os

# obtendo caminho de trabalho atual
print("-" * 30)
print("\nObtendo local de trabalho atual...\n")
local_de_trabalho_atual = os.getcwd()
print("Localização atual:\n", local_de_trabalho_atual)
print("\n", "-" * 30)

# podemos facilitar a munipulação de diretorios com path.join

print("Manipulando os caminhos...\n")
adicionar_nome = "valter_treinando_OS"
print("Podemos concatenar qualquer string em qualquer caminho:\n")
print("String definida para um novo caminho:\n", adicionar_nome)
print("\nO caminho está montado e pronto para qualquer uso que seja necessario")

# agora podemos montar o novo caminho
novo_caminho = os.path.join(local_de_trabalho_atual, adicionar_nome)
print("\nCaminho criado com JOIN:\n", novo_caminho)
print("-" * 30)

# podemos pegar o caminho absoluto de um arquivo relativo
# criamos um arquivo simples
nome_caminho_relativo = "arquivo_caminho_relativo.txt"
arquivo = open(nome_caminho_relativo, "w")
arquivo.close()

# temos a variavel com o caminho relativo do arquivo criado
# mas queremos o caminho absoluto dele
caminho_absoluto = os.path.abspath(nome_caminho_relativo)

print("\nCaminho absoluto de um arquivo com caminho relativo:")
print("Caminho: ", caminho_absoluto)

print("\nObtendo a extensão de um arquivo:")

# splittext pode fornecer o nome e a extensão do arquivo
nome, ext = os.path.splitext(caminho_absoluto)
print(f"Extensão do arquivo: ", ext)

# podemos remover o caminho usando esse mesmo caminho
os.remove(caminho_absoluto)

# uma boa pratica é checar a existencia do arquivo antes de qualquer manipulação
# no caso atual vamos apenas checar se ele foi apagado
print("-" * 30)
print("\nVerificando existencia de arquivos/diretorios\n")
apagado = not os.path.exists(caminho_absoluto)
if apagado:
    print(f"Arquivo {nome_caminho_relativo} apagado com sucesso.")
else:
    print("Arquivo não foi apagado.")
print()
print("-" * 30)
