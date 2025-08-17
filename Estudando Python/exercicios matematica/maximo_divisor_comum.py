"""
Cie um algoritmo que calcule o máximo divisor comum entre 2 números.
"""

def calcular_mdc(a: int, b: int) -> int:
    # definimos o maior valor como dividendo
    if a > b:
        dividendo = a
        divisor = b
    elif a < b:
        dividendo = b
        divisor = a
    else:
        print("Ambos os valores são iguais")
        return -1
    
    while True:
        print(f"Dividindo {dividendo} / {divisor} = {dividendo / divisor}")
        resto = dividendo % divisor
        print("Resto: ", resto)
        if resto == 0:
            return divisor
        elif resto > 0:
            dividendo = divisor
            divisor = resto

if __name__ == "__main__":
    n1 = 32
    n2 = 48

    print(f"O mdc de {n1, n2} é: {calcular_mdc(n1, n2)}")