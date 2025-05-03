"""
Se listarmos todos os números naturais abaixo de 10
que são múltiplos de 3 ou 5, nós teremos 3, 5, 6 e 9 e
a soma desses múltiplos é 23.

Problema: Encontre a soma de todos os múltiplos de 3 ou 5
abaixo de 1000.
"""

somar = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)

print("A soma dos multiplos de 3 e 5 até mil é:", somar)