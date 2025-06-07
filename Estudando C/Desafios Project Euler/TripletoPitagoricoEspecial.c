/*
 Desafio: Tripleto Pitagórico Especial

 Um tripleto pitagórico consiste em três números inteiros positivos a < b < c, tal que:
     a^2 + b^2 = c^2

 Existe exatamente um tripleto pitagórico para o qual:
     a + b + c = 1000

 Escreva um programa em C que encontre os valores de a, b e c que satisfazem essa condição,
 e imprima o produto a * b * c.
*/

#include <stdio.h>

int main(void) {
    int a, b, c;

    for (a = 1; a < 1000; a++) {
        for (b = a + 1; b < 1000 - a; b++) {
            c = 1000 - a - b;
            if (a * a + b * b == c * c) {
                printf("Tripleto encontrado: a = %d, b = %d, c = %d\n", a, b, c);
                printf("Produto abc = %d\n", a * b * c);
                return 0;
            }
        }
    }

    return 0;
}
