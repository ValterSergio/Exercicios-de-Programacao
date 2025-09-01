#include <stdio.h>

int main() {
    int n1;
    printf("Digite um numero inteiro: ");
    scanf("%d", &n1);
    
    if (n1 < 0) {
        printf("O numero %d é Negativo!\n");
    } else if (n1 > 0) {
        printf("O numero %d e Positivo!\n");
    } else {
        printf("O numero informado %d (zero)");
    }

    return 0;
}