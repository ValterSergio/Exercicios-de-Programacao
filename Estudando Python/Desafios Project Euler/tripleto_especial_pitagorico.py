"""
Desafio: Tripleto Pitagórico Especial

Um tripleto pitagórico consiste em três números inteiros positivos a < b < c, tal que:

    a^2 + b^2 = c^2

Existe exatamente um tripleto pitagórico para o qual:

    a + b + c = 1000

Escreva um programa em Python que encontre o valor de a, b e c que satisfazem essa condição, e imprima o produto a * b * c.
"""

def solucao_desafio_nove(n: int) -> dict: 
    for a in range(1, n // 4):
        # 'a' deve ser menor que n // 4 porque:
        # Suponha a < b < c. Como a + b + c = n,
        # e c é o maior, ele será aproximadamente n/2 (no pior caso).
        # Logo, a e b juntos precisam somar um pouco mais que n/2.
        # Então a não pode ser maior que n // 3, e podemos limitar ainda mais para otimizar.

        for b in range(a + 1, n // 2):
            # 'b' começa de a+1 para evitar combinações repetidas (a < b)
            # b < n/2 porque c = n - a - b, e c deve ser positivo

            c = n - a - b  # 'c' é o restante da soma

            # Verificamos a condição pitagórica
            if a * a + b * b != c * c:
                continue

            produto = a * b * c
            return {"A": a, "B": b, "C": c, "Produto": produto}
        
if __name__ == "__main__":
    import time
    inicio = time.time()
    print("Iniciando busca do tripleto....")
    produto = solucao_desafio_nove(1000)
    fim = time.time()
    tempo = fim - inicio
    print(f"Produto encontrado: ", produto)
    print(f"Tempo de execução: ", tempo, " segundos")