# Os fatores primos de 13195 são 5, 7, 13 e 29.
# Qual é o maior fator primo do número 600851475143?


num = 600_851_475_143
fator = 2
maiorFator = 0

while num > 1:
    
    if num % fator == 0:
        maiorFator = fator
        num /= fator
    else:
        fator += 1
        
print("O maior fator primo: ", maiorFator)
