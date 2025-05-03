"""
2520 é o menor numero que pode ser dividido por cada um dos numeros de 1 a 10 sem qualquer resto.

Qual é o menor número positivo que é uniformemente divisível por todos os números de 1 a 20?
"""

# fatora o numero
def fatoracaoNumeroPrimo(num):
    # definimos o dividendo o numero a ser fatorado
    dividendo = num

    # primeiro numero primo da fatoração
    divisor = 2 

    # armazena a quantidade de vezes que o divisor se repete
    fatores = {}

    # enquanto o numero a ser fatorado não for 1
    while dividendo > 1:

        # se a divisão for perfeita
        if dividendo % divisor == 0:

            # fatoramos ele dividindo ele pelo divisor
            # e o dividendo recebe o quociente da divisão
            dividendo = dividendo // divisor

            # guardamos o divisor no dicionario
            if divisor in fatores:
                fatores[divisor] += 1
            else:
                fatores[divisor] = 1
        else:

            # se não for possivel o fatoramento passamos para o proximo numero 
            divisor += 1

    return fatores

def encontrarMMC(lista_fatores: list):
    # armazena a fatoração de cada número da lista
    lista_fatorados = []

    # percorre cada número da lista original
    for fator in lista_fatores:
        # fatoramos o número e adicionamos à lista
        lista_fatorados.append(fatoracaoNumeroPrimo(fator))

    # dicionário para armazenar os maiores expoentes de cada fator primo
    fatores_comuns = {}

    # percorre cada fatoração individual
    for x in range(len(lista_fatorados)):
        # para cada fator e seu expoente
        for fat, expo in lista_fatorados[x].items():

            # se o fator já estiver no dicionário, comparamos os expoentes
            if fat in fatores_comuns:
                # guardamos o maior expoente entre os existentes
                if expo > fatores_comuns[fat]:
                    fatores_comuns[fat] = expo
            else:
                # se o fator ainda não estiver no dicionário, adicionamos
                fatores_comuns[fat] = expo

    # variável que armazenará o resultado do MMC
    mult = 1

    # multiplicamos os fatores elevados aos seus maiores expoentes
    for x, y in fatores_comuns.items():
        mult *= (x ** y)

    # retornamos o MMC final
    return mult


if __name__ == "__main__":
    lista_multiplos = [x for x in range(2, 21)]
    mmc = encontrarMMC(lista_multiplos)
    print(f"O menor número divisivel por todos os números de 1 a 20 é {mmc:,}")