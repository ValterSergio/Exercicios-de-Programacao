from constructor.menu_constructor import exibir_menu
from constructor.criar_registro_construtor import CriarRegistroConstructor
from util.limpar_terminal import limpar_terminal

def executar_programa():
    escolha = 0
    while escolha != 4:
        menu = exibir_menu()
        if menu['mensagem']:
            escolha = menu['resposta']
            match escolha:
                case 1:
                    limpar_terminal()
                    #função para criar o registro
                    CriarRegistroConstructor().criar_registro()
                case 2:
                    # criar a função para remover o registro
                    continue
                case 3:
                    # criar função exibir todos os registros
                    continue
                case 4:
                    print("saindo do programa")
                    break
        else:
            limpar_terminal()
            print("-"* 65)
            print("ERRO: Tente Novamente")
            print("-"* 65)
            print(f"Detalhes de Erro: {menu['resposta']}")
            print("-"* 65)
            continue

if __name__ == "__main__":
    executar_programa()