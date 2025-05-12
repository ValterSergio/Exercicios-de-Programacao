/*
    Crie um programa qu lê um numero inteiro digitado pelo usuario
    e exiba o dobro, o triplo, e a raiz quadrada desse numero
*/

#include <stdio.h>
#include <math.h>

int main(void) {
    int n1;
    printf("Digite um numero inteiro: ");
    scanf("%d", &n1);

    int dobro = n1 * 2;
    int triplo = n1 * 3;
    double raizQuadrada = sqrt(n1);

    printf("\nO dobro de %d: %d", n1, dobro);
    printf("\nO triplo de %d: %d", n1, triplo);
    printf("\nA raiz quadrada de %d: %.2f", n1, raizQuadrada);
    return 0;
}