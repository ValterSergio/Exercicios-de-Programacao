"""
Desafio: Tripleto Pitagórico Especial

Um tripleto pitagórico consiste em três números inteiros positivos a < b < c, tal que:

    a^2 + b^2 = c^2

Existe exatamente um tripleto pitagórico para o qual:

    a + b + c = 1000

Escreva um programa em Python que encontre o valor de a, b e c que satisfazem essa condição, e imprima o produto a * b * c.
"""

def encontrar_produto():
    for a in range(1, 1000):
        for b in range(a+1, 1000):
            c = 1000 - a - b
            if a * a + b * b == c * c:
                print(f"Tripleto encontrado: A={a} -> B={b} -> C={c}")
                print("Produto de A x B x c: ", a * b * c)
                return 

if __name__ == "__main__":
    encontrar_produto()