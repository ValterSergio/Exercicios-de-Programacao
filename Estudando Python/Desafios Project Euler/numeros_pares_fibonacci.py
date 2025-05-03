"""
Cada novo termo na sequencia de Fibonacci é gerado pela 
adiçao dos dois termos anteriores. Começando com 1 e 2, os 
primeiros 10 termos serão:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89

Considerando os termos na sequencia de fibonacci cujos 
valores não excedem 4 milhões, encontre a soma dos termos de valor par

"""



primeiro = 0
segundo = 1

fibo = primeiro + segundo

numeros_pares = []
while fibo < 4_000_000:
    primeiro = segundo
    segundo = fibo
    fibo = primeiro + segundo
    if fibo % 2 == 0:
        numeros_pares.append(fibo)

print("A soma dos numeros Pares de Fibo até 4 milhoes: ", sum(numeros_pares))