"""
Cria um algoritmo que indentifique todos os divisores naturais de n.
"""

def encontrar_divisores_naturais(n: int) -> tuple:
    contador = 1
    divisores = []
    while contador <= n:
        if n % contador == 0:
            divisores.append(contador)
        contador += 1
    return tuple(divisores)

if __name__ == "__main__":
    n = 150
    
    print(f"Divisores de {n} encontrados: ", encontrar_divisores_naturais(n)) 