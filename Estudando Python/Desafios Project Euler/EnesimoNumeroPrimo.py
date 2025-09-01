"""
Desafio 7 do Project Euler:

Ao enumerar os primeiros seis números primos: 2, 3, 5, 7, 11 e 13,
podemos ver que o 6º número primo é 13.

A tarefa é encontrar qual é o **10.001º número primo**.
"""

def checar_primo(num):
    """
    Esta função verifica se um número é primo.

    Um número primo é um número maior que 1 que só pode ser dividido
    por 1 e por ele mesmo, sem sobrar resto.
    Exemplo: 2, 3, 5, 7, 11, 13, ...
    """

    # Se o número for menor que 2, não é primo (por definição)
    if num < 2:
        return False

    # 2 é o único número par que é primo
    if num == 2:
        return True

    # Se o número for par (e diferente de 2), ele não pode ser primo
    if num % 2 == 0:
        return False

    # Vamos testar apenas números ímpares a partir do 3
    i = 3

    # Só precisamos testar divisores até a raiz quadrada do número.
    # Isso é mais rápido do que testar todos os números até num.
    while i * i <= num:
        # Se num for divisível por i, então não é primo
        if num % i == 0:
            return False
        # Pulamos para o próximo número ímpar
        i += 2

    # Se não achamos nenhum divisor, o número é primo
    return True

# Começar com o número 2 (o primeiro número primo)
num = 1
# Contador de primos encontrados
contador = 0

while contador < 10_001:
    num += 1  # Vamos testar o próximo número
    if checar_primo(num):  # Se ele for primo
        contador += 1      # Contamos ele como mais um primo

# Quando o laço termina, encontramos o 10.001º primo!
print(f"O primo que fica na posição 10001° é {num:,}")
