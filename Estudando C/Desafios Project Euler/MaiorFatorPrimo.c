// Os fatores primos de 13195 são 5, 7, 13 e 29.

// Qual é o maior fator primo do número 600851475143?

#include <stdio.h>

int main() {
    long long numero = 600851475143;
    long long fator = 2, MaiorFatorPrimo = 0;

    while (numero > 1) {
        if (numero % fator == 0) {
            MaiorFatorPrimo = fator;
            numero /= fator;
        } else {
            fator++; 
        }
    }

    printf("O maior fator primo: %lld\n", MaiorFatorPrimo);
    return 0;
}
