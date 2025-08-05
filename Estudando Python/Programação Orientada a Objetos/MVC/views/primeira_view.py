def pagina_introducao():
    mensagem = """
    * Sistema de cadastro

    1. cadastrar pessoa
    2. buscar pessoa por nome
    3. sair
    """
    print(mensagem)
    return input("Escolha: ")

if __name__ == "__main__":
    pagina_introducao()