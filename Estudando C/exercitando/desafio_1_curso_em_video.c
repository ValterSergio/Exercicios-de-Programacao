/*
    Crie um scrípt que leia o nome de uma pessoa e mostre uma mensagem de boas vindas de acordo com o valor digitado
*/

# include <stdio.h>

int main(void){
    char nome[15];

    printf("Digite seu Nome: ");
    scanf("%s", nome);

    printf("Ola, seja bem-vindo %s :) ", nome);
}