/*
    Faça um programa que lê as duas notas de um aluno, calcula a 
    media entre elas e exibe o resultado
*/
# include <stdio.h>

int main(void){
    float n1;
    float n2;
    printf("\nDigite a 1° nota: ");
    scanf("%f", &n1);

    printf("\nDigite a 2° nota: ");
    scanf("%f", &n2);

    float media = (n1 + n2) / 2;
    printf("\nAluno teve media: %.2f", media);

    return 0;
}