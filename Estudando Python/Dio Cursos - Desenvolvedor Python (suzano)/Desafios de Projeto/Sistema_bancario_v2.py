from datetime import datetime
from sys import exit

# Função principal para acessar a conta de um cliente
def acessar_conta(cpf: str, conta: dict, cliente: dict):
    if not isinstance(conta, dict):
        print("Conta não encontrada")
        return


    while True:
        # Recupera informações principais da conta
        saldo = conta.get("saldo", 0)
        limite_diario_saque = conta["limite_diario_saque"] - conta["numero_saques"]
        limite_saque = conta.get("limite_saque", 500)
        transacoes = conta.get("transacoes", [])
        
        exibir_menu_cliente(saldo, limite_diario_saque)
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            valor = float(input("Informe o valor para depósito: "))
            registrar_extrato(
                cpf_cliente=cpf,
                conta_cliente=conta,
                lista_registros=transacoes,
                funcao=depositar,
                saldo=saldo,
                valor=valor
            )

        elif escolha == 2:
            valor = float(input("Informe o valor para saque: "))
            registrar_extrato(
                cpf_cliente=cpf,
                conta_cliente=conta,
                lista_registros=transacoes,
                funcao=sacar,
                saldo=saldo,
                valor=valor,
                limite_saque=limite_saque,
                numero_saques=conta["numero_saques"] + 1,
                limite_diario_saque=limite_diario_saque
            )

        elif escolha == 3:
            exibir_extrato(transacoes)

        elif escolha == 4:
            print("Saindo da conta...")
            break

        elif escolha == 5:
            print("Finalizando o Programa")
            exit()

        else:
            print("Informe um número válido")

# Exibe o menu do cliente durante o acesso à conta
def exibir_menu_cliente(saldo: float, limite_diario_saque: int):
    print(f"""
{'-'*65}
                    --- Banco Python ---
{'-'*65}
                    --- Resumo Geral ---
{'-'*65}
Saldo Atual: R$ {saldo:,.2f}
Limite de Saques Restantes: {limite_diario_saque}
{'-'*65}
1 - Depositar
2 - Sacar
3 - Consultar Extrato
4 - Sair da Conta
5 - Encerrar Programa
{'-'*65}
""")

# Realiza o saque com validações de limite e saldo
def sacar(*, saldo, valor, limite_saque, numero_saques, limite_diario_saque):
    if saldo <= 0:
        print("Erro: Saldo negativo.")
        return saldo
    if valor <= 0:
        print("Erro: Valor inválido.")
        return saldo
    if valor > limite_saque:
        print("Erro: Valor acima do limite permitido.")
        return saldo
    if numero_saques >= limite_diario_saque:
        print("Erro: Limite diário de saques atingido.")
        return saldo
    if valor > saldo:
        print("Erro: Saldo insuficiente.")
        return saldo

    print("Saque realizado com sucesso!")
    return saldo - valor

# Realiza um depósito, validando o valor
def depositar(saldo=0, valor=0):
    if valor <= 0:
        print("Erro: Valor do depósito deve ser positivo.")
        return saldo

    print("Depósito realizado com sucesso!")
    return saldo + valor

# Registra uma transação (depósito ou saque) no extrato da conta
def registrar_extrato(cpf_cliente="xxx.xxx.xxx-xx", conta_cliente=None, lista_registros=[], funcao=None, **kwargs):
    if not funcao or not conta_cliente:
        print("Erro ao registrar operação.")
        return

    extrato = {"cpf": cpf_cliente}
    operacao = funcao.__name__.capitalize()

    extrato["Tipo de Operação"] = operacao

    for chave, valor in kwargs.items():
        extrato[chave] = valor

    if operacao == "Depositar":
        saldo_atual = conta_cliente["saldo"]
        novo_saldo = funcao(saldo_atual, kwargs["valor"])
        conta_cliente["saldo"] = novo_saldo
        extrato["Saldo atualizado"] = novo_saldo

    elif operacao == "Sacar":
        saldo_atual = conta_cliente["saldo"]
        novo_saldo = funcao(**kwargs)
        if novo_saldo != saldo_atual:
            conta_cliente["saldo"] = novo_saldo
            conta_cliente["numero_saques"] += 1
            extrato["Saldo atualizado"] = novo_saldo
        else:
            return  # Não registra transação se saque foi negado

    lista_registros.append(extrato)
    conta_cliente["transacoes"] = lista_registros

# Cria um dicionário com os dados do cliente
def criar_cliente(**dados_cliente):
    return {chave.lower(): valor for chave, valor in dados_cliente.items()}

# Cria uma nova conta associada a um cliente
def criar_conta(total_de_contas, cliente, **dados_adicionais):
    try:
        nova_conta = {
            "cliente": cliente,
            "cpf": cliente.get("cpf"),
            "conta": total_de_contas + 1,
            "agencia": "0001",
            "saldo": 0,
            "transacoes": [],
            "numero_saques": 0
        }
        nova_conta.update(dados_adicionais)
        print("Conta criada com sucesso!")
        return nova_conta
    except Exception as erro:
        print("Erro ao criar conta:", erro)

# Exibe o extrato de uma conta
def exibir_extrato(lista_extrato):
    cabecalho("Histórico de Transações")

    if not lista_extrato:
        print("Nenhuma transação registrada.")
    else:
        for i, transacao in enumerate(lista_extrato, 1):
            print(f"\nTransação {i}")
            for chave, valor in transacao.items():
                print(f"{chave}: {valor}")

    rodape()

# Registra uma nova conta em uma lista
def registrar_conta(lista_conta, conta):
    lista_conta.append(conta)

# Busca um cliente ou conta pelo CPF
def buscar_cpf(lista, cpf):
    cpf_limpo = limpar_cpf(cpf)
    for item in lista:
        if item.get("cpf") == cpf_limpo:
            return item
    print("CPF não encontrado.")
    return None

# Cria uma data formatada de nascimento
def criar_data_nascimento(dia, mes, ano):
    return datetime(ano, mes, dia).strftime("%d/%m/%Y")

# Remove caracteres não numéricos do CPF
def limpar_cpf(cpf):
    return "".join(c for c in cpf if c.isdigit())

# Valida se o CPF possui 11 dígitos
def validar_cpf(cpf):
    return len(limpar_cpf(cpf)) == 11

# Registra um novo cliente, se CPF não estiver duplicado
def registrar_cliente(lista_clientes):
    nome = input("Digite seu nome completo: ")
    cpf = limpar_cpf(input("Digite seu CPF: "))

    if any(cliente["cpf"] == cpf for cliente in lista_clientes):
        print("Erro: CPF já cadastrado.")
        return False

    if not validar_cpf(cpf):
        print("CPF inválido.")
        return False

    dia = int(input("Dia de nascimento: "))
    mes = int(input("Mês de nascimento: "))
    ano = int(input("Ano de nascimento: "))
    data_nascimento = criar_data_nascimento(dia, mes, ano)

    logradouro = input("Endereço (rua, número e bairro): ")
    cidade_estado = input("Cidade e Estado (ex: São Paulo, SP): ")

    novo_cliente = criar_cliente(
        nome=nome,
        saldo=0,
        cpf=cpf,
        data_nascimento=data_nascimento,
        endereco=f"{logradouro.strip().capitalize()}, {cidade_estado.strip().capitalize()}"
    )

    lista_clientes.append(novo_cliente)
    return novo_cliente

# Menu inicial do programa
def menu_inicial():
    return int(input(
        "\n--- Bem-vindo ao Banco Python ---\n"
        "1 - Cadastrar Cliente\n"
        "2 - Acessar Conta\n"
        "3 - Encerrar Programa\n"
        "Escolha uma opção: "
    ))

# Exibe um cabeçalho visual
def cabecalho(msg):
    print("-" * 65)
    print(f"{msg.center(65)}")
    print("-" * 65)

# Exibe um rodapé visual
def rodape():
    print("-" * 65)
    print("Fim da Operação".center(65))
    print("-" * 65)

# Execução principal
if __name__ == "__main__":
    lista_clientes = []
    lista_contas = []

    while True:
        opcao = menu_inicial()

        if opcao == 1:
            cabecalho("Cadastro de Cliente")
            cliente = registrar_cliente(lista_clientes)
            if cliente:
                nova_conta = criar_conta(
                    total_de_contas=len(lista_contas),
                    cliente=cliente,
                    limite_saque=500,
                    limite_diario_saque=3
                )
                registrar_conta(lista_contas, nova_conta)
                rodape()

        elif opcao == 2:
            cabecalho("Acesso à Conta")
            cpf_input = input("Digite o CPF da conta: ")
            if not validar_cpf(cpf_input):
                print("CPF inválido.")
                continue

            cpf = limpar_cpf(cpf_input)
            conta = buscar_cpf(lista_contas, cpf)
            cliente = buscar_cpf(lista_clientes, cpf)

            if conta and cliente:
                acessar_conta(cpf, conta, cliente)

        elif opcao == 3:
            print("Encerrando programa.")
            break

        else:
            print("Opção inválida.")
