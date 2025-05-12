from controller.gerenciador import GerenciadorFaturas
from model.repositorio import RepositorioJSON, CAMINHO
import os
import sys

def segurar_menu():
    escolha = int(input("Aperte 0 para sair, aperte 1 para o menu anterior: "))
    
    if escolha == 0:
        sys.exit(0)

    if escolha == 1:
        return 
    

def cabecalho(msg: str) -> None:
    print("-"*65)
    print(f"-----\t-> {msg} <-\t-----")
    print("-"*65)

def rodape() -> None:
    print("-"*65)
    print("-----\t-> Fim <-\t-----")
    print("-"*65)

def menu() -> int:
    os.system("cls")
    cabecalho("Menu Principal")
    print("""
1 - registrar Fatura
2 - Listar todas as Faturas
3 - Listar Faturas atrasadas
4 - listar Faturas por mes
5 - listar Faturas por servico
6 - listar Faturas pagas
0 - Sair
""")
    return int(input("Informe a escolha: "))

def executar():
    dados = RepositorioJSON(CAMINHO)
    controle = GerenciadorFaturas(dados)
    print("oi")
    while True:
        
        try:
            inicio = menu()
        except Exception as erro:
            print(f"Erro: {str(erro)}")
        
        os.system("cls")
        faturas = dados.carregar_arquivo()
        match inicio:
            case 1:
                controle.repositorio.carregar_arquivo()
                try:
                    servico = input("informe o Serviço: ")
                    valor = float(input("Informe o valor: "))
                    vencimento = input("Informe a data de vencimento (dd/mm/aaaa): ")
                    cabecalho("Adicionar Fatura")
                    controle.adicionar_fatura(servico=servico, valor=valor, vencimento_str=vencimento)
                    rodape()
                    faturas = controle.listar_faturas()
                    segurar_menu()

                except Exception as erro:
                    print(f"Erro: {str(erro)}\n --- Tente Novamente ---")
                    break

            case 2:
                cabecalho("Exibindo Faturas")
                controle.repositorio.carregar_arquivo()
                for conta in controle.listar_faturas():
                    print(conta)
                rodape()
                segurar_menu()

            case 3:
                cabecalho("Faturas Atrasadas")
                controle.repositorio.carregar_arquivo()
                for conta in controle.listar_faturas_atrasadas():
                    print(conta)
                rodape()
                segurar_menu()
                

            case 4:
                cabecalho("Localizar Faturas ( Mês )")
                try:
                    mes = int(input("Informe o mês ( numero ): "))
                    if not isinstance(mes, int):
                        print("Numero invalido")
                        break
                    
                    controle.repositorio.carregar_arquivo()
                    for conta in controle.listar_faturas_por_mes(mes):
                        print(conta)
                except Exception as erro:
                    print(f"Erro: {str(erro)}")
                    break
                    
                rodape()
                segurar_menu()

            case 5:
                cabecalho("Localizar Faturas ( Serviço )")
                try:
                    encontrar_servico = input("Digite o servico que está buscando: ")
                    if all([letra for letra in encontrar_servico if not letra.isnumeric()]):
                        for conta in controle.listar_faturas_por_servico(encontrar_servico):
                            print(conta)
                    rodape()
                    segurar_menu()

                except Exception as erro:
                    print(f"Erro: {str(erro)}")
                    break
            
            case 6:
                cabecalho("Localizar Faturas Pagas")
                controle.repositorio.carregar_arquivo()
                for conta in controle.listar_faturas_pagas():
                    print(conta)
                rodape()
                segurar_menu()
            
            case 0:
                cabecalho("Encerrando ....")
                controle.repositorio.salvar_arquivo(faturas)
                os.system("cls")
                sys.exit(0)
