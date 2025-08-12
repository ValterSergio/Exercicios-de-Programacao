from view.menu_view import MenuView
from controller.menu_controller import MenuController

def exibir_menu():
    view = MenuView()
    controller = MenuController()

    # chamar a interface
    resposta_usuario = view.exibir_menu()
    resposta_processamento = controller.validar_escolha(resposta_usuario)

    return {
            "mensagem": resposta_processamento['mensagem'],
            "resposta": resposta_processamento['resposta'],
            "caminho": resposta_processamento['caminho'],
            "objeto": resposta_processamento['objeto'],
            "metodo": resposta_processamento['metodo']
        }

    


if __name__ == "__main__":
    exibir_menu()
    
