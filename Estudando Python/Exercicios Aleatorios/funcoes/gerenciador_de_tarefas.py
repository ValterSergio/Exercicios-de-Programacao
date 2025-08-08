CAMINHO = "tarefas.txt"

# funções auxiliares

def salvar_tarefa(tarefa):
    with open(CAMINHO, "a", encoding="utf-8") as file:
        formatar_tarefa = f""" Tarefa: {tarefa['tarefa']}, Detalhes da Tarefa: {tarefa['detalhes']}, Data da Tarefa: {tarefa['data']}, Hora da Tarefa: {tarefa['hora']}"""
        try:
            file.write(formatar_tarefa + "\n")
            return {"mensagem": True, "resposta": "Tarefa Registrada Com Sucesso !!!"}
        except Exception as erro:
            return {"mensagem": False, "resposta": str(erro)}

def obter_tarefas() -> dict:
    tarefas = []
    try:
        with open(CAMINHO, "r", encoding="utf-8") as file:
            for linha in file:
                tarefas.append(linha)
        return {"mensagem": True, "resposta": tarefas}
    except Exception as erro:
        return {"mensagem": False, "resposta": str(erro)}

def indexar_tarefas(lista_tarefas: list[str]) -> None:
    print("\nTarefas registradas\n")
    
    n = len(lista_tarefas)
    if n == 0:
        print(f"Não tem tarefas registradas")
        return
    
    # marcar indice para cada tarefa
    indice = 0
    for tarefa in lista_tarefas:
        print(f"ID: {indice} | Tarefa: {tarefa}")
        indice += 1
    

def reescrever_arquivo(lista_tarefas: list[str]) -> dict:
    try:
        with open(CAMINHO, 'w') as file:
            for tarefa in lista_tarefas:
                file.write(tarefa + "\n")
    except Exception as erro:
        return {'mensagem': False, 'resposta': str(erro)}
    else:
        return {'mensagem': True, 'resposta': 'Arquivo Modificado'}            

# criar tarefa
def criar_tarefa_view() -> dict:
    return {
        'tarefa': input("Informe o nome da tarefa: ").replace(",", ""),
        'detalhes': input("Informe os detalhes da tarefa: ").replace(",", ""),
        'data': input("Informe a data da tarefa (dd/mm/aaaa): "),
        'hora': input("Informe a hora da tarefa (hh:mm): ")
    }

def criar_tarefa_controller(view):
    try:
        resposta = view
        return salvar_tarefa(resposta) # retorna um dicionario 
    except Exception as erro:
        return {"mensagem": False, "resposta": str(erro)}

def criar_tarefa():
    view = criar_tarefa_view()
    resposta = criar_tarefa_controller(view)
    print(resposta['resposta'])

# listar tarefas
def exibir_tarefas_view(tarefa: str):
    # separar os dados pela virgula
    dados = tarefa.split(",")
    print("-"*15, "Tarefa", "-"*15)
    for dado in dados:
        print(dado)


def exibir_tarefas_controller():
    try:
        resposta = obter_tarefas()
    except Exception as erro:
        print("Erro: ", str(erro))
    else:
        dados = resposta['resposta']
        if len(dados) > 0:
            for tarefa in dados:
                exibir_tarefas_view(tarefa)
            print("-"*15, "Todas as Tarefas foram exibidas", "-"*15)
        else:
            print("Não tem tarefas registradas !!!")

def exibir_tarefas():
    exibir_tarefas_controller()

# remover tarefa
def remover_tarefa_view(lista_tarefas: str):
    indexar_tarefas(lista_tarefas=lista_tarefas)
    return input("Digite o ID da tarefa para remover: ")

def remover_tarefa_controller(view) -> dict:
    try:
        # coletar os dados necessarios
        dados = obter_tarefas()
        resposta = view(dados['resposta'])

        # verificar se a resposta é para sair
        if resposta.lower() == 'sair':
            return {"mensagem": False, "resposta": "Operação Cancelada"}
        
        # converter para inteiro
        resposta = int(resposta)
    except Exception as erro:
        return {'mensagem': False, 'resposta': str(erro)}
    
    # a resposta é um inteiro que indentifica o indice da tarefa na lista
    try:
        dados['resposta'].pop(resposta)
        # retorna o dicionario de sucesso ou falha
        arquivo =  reescrever_arquivo(dados['resposta'])
        if arquivo['mensagem']:
            return {"mensagem": True, "resposta": arquivo['resposta']}
        else:
            return {"mensagem": False, "resposta": arquivo['resposta']}
    except Exception as erro:
        return {'mensagem': False, 'resposta': str(erro)}
    
def remover_tarefa():
    remover_view = remover_tarefa_view
    remover_controller = remover_tarefa_controller(remover_view)
    if remover_controller['mensagem']:
        print(f"Tarefa Removida com sucesso: {remover_controller['resposta']}")
    else:
        print(f"\n{remover_controller['resposta']}\n")

# menu principal
def menu_view():
    print("- "*30)
    print("\n", "-"*10, "\tGerenciador de Tarefas\t", "-"*10, "\n")
    print("- "*30)
    print("1. Adicionar Tarefa ")
    print("2. Remover Tarefa")
    print("3. Exibir Tarefas")
    print("4. Sair")
    print("- "*30)
    return input("Digite um número para escolher: ")

def menu_controller(view):
    # tente converter o numero
    try:
        resposta = int(view)
    except Exception as erro:
        return {"mensagem": False, "resposta": str(erro)}
    
    # verifique se é menor que 1 e menor que 4
    if resposta < 1 or resposta > 4:
        return {"mensagem": False, "resposta": "Números fora do intervalo (1 a 4)"}
    
    # se chegou até aqui está tudo certo
    return {"mensagem": True, "resposta": resposta}

def menu():
    while True:
        view = menu_view()
        controller = menu_controller(view)
        if controller['mensagem']:
            resposta = controller['resposta']
            match resposta:
                case 1:
                    criar_tarefa()
                case 2:
                    remover_tarefa()
                case 3:
                    exibir_tarefas()
                case 4:
                    print("Saindo....")
                    break
        else:
            print(controller['resposta'])

if __name__ == "__main__":
    menu()