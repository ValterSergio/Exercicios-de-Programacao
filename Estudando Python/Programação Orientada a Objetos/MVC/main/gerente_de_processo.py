from src.main.construtor.processo_de_introducao import processo_introducao
from src.main.construtor.buscar_pessoa_construtor import buscar_pessoa_construtor
from src.main.construtor.registrar_pessoa_construtor import registrar_pessoa_construtor
from src.models.repositorio.repositorio_pessoa import RepositorioPessoas
def iniciar():
    repositorio = RepositorioPessoas()
    while True:
        escolha = processo_introducao()

        if escolha == "1": registrar_pessoa_construtor(repositorio)
        elif escolha == "2": buscar_pessoa_construtor(repositorio)
        elif escolha == "3": 
            print("comando 3 acionado - saindo")
            exit()
        else: print("Comando não encontrado")
