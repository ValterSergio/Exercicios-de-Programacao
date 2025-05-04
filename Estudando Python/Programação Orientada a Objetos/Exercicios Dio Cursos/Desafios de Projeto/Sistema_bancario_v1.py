SALDO_INICIAL = 10
LIMITE_VALOR_SAQUE = 500
LIMITE_SAQUES = 3
OPERACOES = []

def exibir_menu(saldo: float):
    menu  = f"""
{"-"*65}
    --- Banco Python ---
{"-"*65}
    ---     Resumo geral     ---
{"-"*65}
Saldo Atual: R$ {saldo:,.2f}
Limite de Saques Permitidos: {LIMITE_SAQUES}
{"-"*65}
1 - Depositar
2 - Sacar
3 - Consultar Extrato
4 - Encerrar
{"-"*65}
"""
    print(menu)

def validar_deposito(saldo: float, valor: float) -> bool:
    deposito_positivo = True if valor > 0 else False
    if not deposito_positivo:print("Erro: Valor de deposito deve ser positivo")

    return deposito_positivo
  
def validar_saque(saldo: float, valor: float) -> float:
    saldo_positivo = True if saldo > 0 else False
    valor_positivo = True if valor > 0 else False
    saldo_suficiente = True if saldo > valor else False
    limite_de_saques = True if LIMITE_SAQUES > 0 else False
    limite_de_valor = True if valor <= LIMITE_VALOR_SAQUE else False
    validar_saque = saldo_positivo and valor_positivo and saldo_suficiente and limite_de_saques and limite_de_valor

    if not saldo_suficiente:print("ERRO: Saldo Insuficiente")
    if not valor_positivo:print("ERRO: Valor de saque deve ser positivo")
    if not saldo_positivo:print("ERRO: Saque só é possivel com saldo positivo")
    if not limite_de_saques: print("ERRO: Limite diario de saques esgotado.")
    if not limite_de_valor: print(f"ERRO: Valor maximo para saque: R$ {LIMITE_VALOR_SAQUE:,.2f}")
    
    return validar_saque

def depositar(saldo: float, valor: float) -> float:
        novo_saldo = saldo + valor
        print(f"Deposito liberado novo saldo: R$ {novo_saldo:,.2f}")
        return novo_saldo
  
def sacar(saldo: float, valor: float):
    global LIMITE_SAQUES
    novo_saldo = saldo - valor
    print(f"Saque liberado, novo saldo: R$ {novo_saldo:,.2f}")
    LIMITE_SAQUES -= 1
    return novo_saldo

def exibir_extrato() -> None:
    global OPERACOES
    print("-"*65)
    print("-----     REGISTRO DE MOVIMENTAÇÂO     -----")
    for historio in OPERACOES:
        print("-"*65)
        for operacao, valor in historio.items():
            print(f"Operação: {operacao} | Valor: {valor}")
    print("-"*65)

def registrar_extrato(operacao: dict) -> None:
    global OPERACOES
    OPERACOES.append(operacao)

def realizar_deposito(saldo_cliente: float):
    
    print("\n--- Realizando deposito ---\n")
    valor = float(input("Digite o valor para deposito: "))
    
    if validar_deposito(saldo_cliente, valor):
        saldo_cliente = depositar(saldo_cliente, valor) 
    
        registrar = {
        "Deposito": f"R$ {valor:,.2f}",
        "Saldo Atualizado": f"R$ {saldo_cliente:,.2f}"
        }
        registrar_extrato(registrar)
        return saldo_cliente
    
    return saldo_cliente

def realizar_saque(saldo_cliente: float):
    print("\n--- Realizando deposito ---\n")
    valor = float(input("Digite o valor para depositop: "))
    
    if validar_saque(saldo_cliente, valor):
        saldo_cliente = sacar(saldo_cliente, valor) 
        
        registrar = {
        "Saque": f"R$ {valor:,.2f}",
        "Saldo Atualizado": f"R$ {saldo_cliente:,.2f}",
        "Limite de Saques": LIMITE_SAQUES,
        "Valor maximo de Saque": f"R$ {LIMITE_VALOR_SAQUE:,.2f}"
        }
        registrar_extrato(registrar)
        return saldo_cliente

    return saldo_cliente

def executar_transacoes(saldo_cliente: float=SALDO_INICIAL):

    while True:
        exibir_menu(saldo=saldo_cliente)
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            saldo_cliente = realizar_deposito(saldo_cliente=saldo_cliente)
        elif escolha == 2:
            saldo_cliente = realizar_saque(saldo_cliente=saldo_cliente)
        elif escolha == 3:
            exibir_extrato()
        elif escolha == 4:
            print("encerrando...")
            break

if __name__ == "__main__":
    executar_transacoes(250)