import secrets

# agora tenhosegurança na geração de numeros aleatorios
# indicado para segurança, senhas, criptografia e etc.
random = secrets.SystemRandom()

# posso copiar o outro arquivo tranquilo
# que funciona como o random 
# Gerando números aleatórios 
num_aleatorio = random.randrange(0, 100, 2) # Um número aleatório que seja par entre 0 a 100
print(f'Número aleatório (intervalo de 0 a 100, apenas números pares): {num_aleatorio}')

# Gerar número sem passos
num_alea_int = random.randint(0, 100) # Sem passos
print(f'Número aleatório (intervalo de 0 a 100): {num_alea_int}')

# Gerando números flutuantes
num_alea_flutuante = random.uniform(1, 2)
print(f'Número aleatório floats (intervalo de 1 a 2): {num_alea_flutuante}')

# Podemos escolher um número aleatório dentro de iteráveis
lista = [x for x in range(10)]
escolha_aleatoria = random.choice(lista)
print(f'Número aleatório escolhido em um iterável: {escolha_aleatoria}')

# Podemos embaralhar essa lista
print("Observe que a lista está ordenada: ", lista)
random.shuffle(lista)
print("Agora ela não está mais: ", lista)

# Podemos separar pedaços de um iterável com sample
# Ele gera um novo iterável, com uma quantidade de elementos definida
# Separa aleatoriamente, e não permite repetição
numeros_separados = random.sample(lista, 3)
print("Pegando um pedaço da lista: ", numeros_separados)

# Podemos usar choices que também separa partes de um iterável
# Podemos sortear um número maior de elementos que do iterador original
# Podemos especificar pesos para cada elemento
# Parâmetro weight recebe uma lista de valores para peso
# PARÂMETRO WEIGHT - os números 1 e 3 terão mais chance de aparecer
# Detalhe: a lista definida para a "pesagem" deve ter a mesma quantia de elementos do iterador original
pesos = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]

# A lista tem 10 itens, vamos dobrar o tamanho dela
sorteio_controlado = random.choices(population=lista, weights=pesos, k=12) 
print("Controlando o sorteio de elementos: ", sorteio_controlado)
 