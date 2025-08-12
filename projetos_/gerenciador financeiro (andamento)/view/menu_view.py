from util.limpar_terminal import limpar_terminal

class MenuView:
    def exibir_menu(self):
        print("\n Menu Principal \n")
        print("1. Criar Registro")
        print("2. Remover Registro")
        print("3. Exibir todos os Registros")
        print("4. Sair do programa.")
        return input("Escolha uma opção: ")
    
    def exibir_menu_falha(self, mensagem: str):
        limpar_terminal()
        print(f"{mensagem.capitalize()}")
    
    def exibir_menu_sucesso(self, mensagem: str):
        limpar_terminal()
        print(f"{mensagem.capitalize()}")
    