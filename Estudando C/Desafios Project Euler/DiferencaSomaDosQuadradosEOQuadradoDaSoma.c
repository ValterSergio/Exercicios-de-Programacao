/*
Encontre a diferença entre:
O quadrado da soma dos primeiros "n" numeros naturais
e a soma dos quadrados dos primeiros "n" numeros naturais
*/

#include <stdio.h>

int main(){
    int n = 100;
    int soma = n * (n + 1) / 2;
    int quadrado_da_soma = soma * soma;
    int soma_dos_quadrados = n * (n +1) * (2 * n + 1) / 6;
    int diferenca = quadrado_da_soma - soma_dos_quadrados;

    printf("A diferenca: %d", diferenca);
    return 0;
}