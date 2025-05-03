"""
Problema 8 do Project Euler:

Dado um número de 1000 dígitos, o objetivo é encontrar o maior produto possível
de 13 dígitos consecutivos.

A estratégia consiste em percorrer o número, separando todas as combinações possíveis
de 13 dígitos, calcular o produto de cada uma e manter o maior valor encontrado.

Link do desafio: https://projecteuler.net/problem=8
"""

# Número gigante fornecido no problema
numero_grande = """7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"""

# Tamanho total do número
tamanho_total = len(numero_grande)

# Variável para armazenar o maior produto encontrado
maior_produto = 0

# Variável para guardar a sequência de 13 dígitos que gerou o maior produto
sequencia_maior_produto = ""

# Percorre cada possível posição inicial no número
for posicao_atual in range(tamanho_total):
    for deslocamento in range(tamanho_total - posicao_atual - 1):
        # Extrai uma sequência de 13 dígitos consecutivos
        sequencia_13_digitos = numero_grande[deslocamento:deslocamento + 13]

        # Garante que a sequência tem 13 dígitos completos
        if len(sequencia_13_digitos) < 13:
            continue

        # Calcula o produto dos 13 dígitos
        produto_atual = 1
        for caractere in sequencia_13_digitos:
            produto_atual *= int(caractere)

        # Atualiza o maior produto e a sequência correspondente, se necessário
        if produto_atual > maior_produto:
            maior_produto = produto_atual
            sequencia_maior_produto = sequencia_13_digitos

# Exibe os resultados finais
print("Resultado do maior produto encontrado:", maior_produto)
print("Sequência que resulta nesse produto:", sequencia_maior_produto)