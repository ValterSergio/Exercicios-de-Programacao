from pathlib import Path

# Pegando o caminho da pasta do projeto
print("-" * 79)

# Usamos a variável __file__ para pegar o caminho do arquivo que está em execução
caminho_do_arquivo_sendo_executado = __file__
print(f"Caminho completo do arquivo sendo executado (inclui o nome do arquivo): {caminho_do_arquivo_sendo_executado}")

print("-" * 79)

# Usamos a classe Path para representar o caminho de forma mais legível e manipulável
caminho_do_arquivo_atual = Path(caminho_do_arquivo_sendo_executado)
print(f"Caminho do arquivo obtido utilizando a classe Path: {caminho_do_arquivo_atual}")

print("-" * 79)

# Uma maneira mais concisa e legível de pegar o caminho do arquivo é utilizar Path diretamente
caminho_path = Path(__file__)
print(f"Caminho obtido de maneira mais legível e concisa com Path: {caminho_path}")

print("-" * 79)

# Podemos "subir" na hierarquia de pastas usando o método .parent da classe Path
caminho_projeto = caminho_path.parent  # Ou podemos fazer Path(__file__).parent diretamente
print(f"Caminho da pasta onde o arquivo está localizado (diretório atual): {caminho_projeto}")

print("-" * 79)

# Para obter o caminho absoluto do local do projeto, podemos usar o método .absolute() do Path
caminho_absoluto = Path().absolute()
print(f"Caminho absoluto do diretório onde o projeto está sendo executado: {caminho_absoluto}")

print("-" * 79)

# Podemos subir uma pasta na hierarquia do sistema de arquivos para obter a pasta acima do projeto
raiz_acima_do_projeto = caminho_absoluto.parent
print(f"Caminho da pasta imediatamente acima do diretório do projeto: {raiz_acima_do_projeto}")

print("-" * 79)

# E podemos continuar subindo para mais pastas acima, utilizando o .parent novamente
print(f"Caminho da pasta ainda mais acima do diretório do projeto (subindo mais um nível): {raiz_acima_do_projeto.parent}")
print("-" * 79)
