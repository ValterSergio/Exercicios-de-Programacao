/*
    Crie um programa que lê um número inteiro e exibe o seu antecessor e sucessor
*/

# include <stdio.h>

int main(void){
    int n;
    printf("Digite um numero Inteiro: ");
    scanf("%d", &n);

    int antecessor = n - 1;
    int sucessor = n + 1;
    printf("\nO antecessor de %d: %d", n, antecessor);
    printf("\nO sucessor de %d: %d", n, sucessor);

    return 0;
}
