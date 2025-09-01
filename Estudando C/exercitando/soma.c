# include <stdio.h>

int main(void){
    int n1;
    printf("Digite a: ");
    scanf("%d", &n1);

    int n2;
    printf("Digite b: ");
    scanf("%d", &n2);

    int soma = n1 + n2;
    printf("A soma de %d + %d = %d", n1, n2, soma);

    return 0;

}