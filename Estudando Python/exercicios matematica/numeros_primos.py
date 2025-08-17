"""
Crie um algortimo que indentifique se um numero é primo.
"""

def indentificar_numero_primo(n: int) -> bool:
    divisor = 1
    divisores = []
    while divisor <= n:
        if n % divisor == 0:
            divisores.append(divisor)
        
        # se passa de dois divisores corta o loop
        if len(divisores) > 2:
            return False
        
        divisor += 1
    
    # se não encerrar antes é porque é primo
    return True

if __name__ == "__main__":
    n = 13 # esse é primo
    if indentificar_numero_primo(n):
        print(f"O valor {n} é primo.")
    else:
        print(f"O valor {n} é composto.")