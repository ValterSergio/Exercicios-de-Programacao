/*
    Program que lê um número inteiro e exibe sua tabuada (multiplicações de 1 a 10)

*/

#include <stdio.h>

int main(void){

    int n;

    printf("Digite um numero para a tabuada: ");
    scanf("%d", &n);

    printf("\n%d * 1: %d", n, n * 1);
    printf("\n%d * 2: %d", n, n * 2);
    printf("\n%d * 3: %d", n, n * 3);
    printf("\n%d * 4: %d", n, n * 4);
    printf("\n%d * 5: %d", n, n * 5);
    printf("\n%d * 6: %d", n, n * 6);
    printf("\n%d * 7: %d", n, n * 7);
    printf("\n%d * 8: %d", n, n * 8);
    printf("\n%d * 9: %d", n, n * 9);
    printf("\n%d * 10: %d", n, n * 10);

    return 0;
}