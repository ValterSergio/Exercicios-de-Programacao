"""
2520 é o menor numero que pode ser dividido por cada um dos numeros de 1 a 10 sem qualquer resto.

Qual é o menor número positivo que é uniformemente divisível por todos os números de 1 a 20?
"""
from os import system

def executar():
    limite = 50
    resultado = encontrar_menor_numero(limite)
    system("cls||clear")
    print(f"Resultado: {int(resultado)}")

def encontrar_menor_numero(limite):
    resultado = 1
    for x in range(2, limite + 1):
        resultado = MMC(resultado, x)  # Agora está correto
        print(f"MMC -> Resultado: {resultado} | Valor Atual: {x}")
    return resultado

def MDC(a, b):
    if a > b: 
        dividendo = a 
        divisor = b
    else: 
        dividendo = b 
        divisor = a 
        
    while True: 
        resto = dividendo % divisor 
        if resto == 0: 
            return divisor 
        elif resto > 0: 
            dividendo = divisor 
            divisor = resto
    

def MMC(a, b):
    return (a * b) // MDC(a, b)  # Usa divisão inteira


if __name__ == "__main__":
    executar()