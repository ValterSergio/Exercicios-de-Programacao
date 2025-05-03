# Um número palíndromo é aquele que pode ser lido da mesma forma em ambos os sentidos.
# O maior palíndromo formado pelo produto de dois números de 2 dígitos é 9009 = 91 × 99.

# Encontre o maior palíndromo formado pelo produto de dois números de 3 dígitos.

num = 100 # base 
palindromo = 0  

while num <= 999:
    mult = num
    while mult <= 999:
        produto = str(num * mult)
        inverter = produto[::-1]
        if produto == inverter:
            _palindromo = int(produto)
            if _palindromo > palindromo:
                palindromo = _palindromo
        mult += 1
    num += 1

print("O maior palindromo formado pelo produto de 2 números de 3 digitos é : ", palindromo)