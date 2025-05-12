/*
    Crie um script que leia dois numeros e tente mostrar
    a soma entre eles
*/
# include <stdio.h>

int main(void){

    float valorA;
    float valorB;


    printf("--- Bem vindo ----\n\n");
    printf("Digite o valor de A: ");
    scanf("%f", &valorA);
    printf("\nDigite o valor de B: ");
    scanf("%f", &valorB);

    float resultado = valorA + valorB;

    printf("\nResultado FInal: %.2f", resultado);
}