#include <stdio.h>
#include <stdbool.h>

/*
Desafio 7 do Project Euler:

Ao enumerar os primeiros seis números primos: 2, 3, 5, 7, 11 e 13,
podemos ver que o 6º número primo é 13.

A tarefa é encontrar qual é o 10.001º número primo.
*/

// Função que verifica se um número é primo
bool checar_primo(int num) {
    if (num < 2)
        return false;
    if (num == 2)
        return true;
    if (num % 2 == 0)
        return false;

    int i = 3;
    while (i * i <= num) {
        if (num % i == 0)
            return false;
        i += 2;
    }
    return true;
}

int main() {
    int num = 2;
    int contador = 0;

    while (contador < 10001) {
        num++;
        if (checar_primo(num)) {
            contador++;
        }
    }

    printf("O primo que fica na posição 10001° é %d\n", num);
    return 0;
}
