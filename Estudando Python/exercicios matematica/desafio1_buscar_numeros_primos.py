"""
Crie um algoritmo que localize todos os numeros primos até n
"""

def verificar_primos(n: int) -> bool:
    # 0 e 1 não são primos
    if n < 2:
        return False
    
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        
        divisor += 1
    return True

def localizar_primos(n: int) -> tuple:
    contador = 2
    primos = []

    while contador <= n:
        if verificar_primos(contador):
            primos.append(contador)
        contador += 1
    return tuple(primos)

if __name__ == "__main__":
    # quantos primos encontramos de 1 até mil?
    n = 1000
    primos_encontrados = localizar_primos(n)
    print(f"Todos os numeros primos encontrados até o {n:,}: ", primos_encontrados)