/*
    Crie um script que leia o dia, o mes e o ano de nascimento
    de uma pessoa e mostre uma mensagem com a data formatada
*/

# include <stdio.h>

int main(void){
    int anoNascimento;
    int mesNascimento;
    int diaNascimento;

    printf("\nInforme dia do nascimento: ");
    scanf("%d", &diaNascimento);
    
    printf("\nInforme mes do nascimento: ");
    scanf("%d", &mesNascimento);
    
    printf("\nInforme ano do nascimento: ");
    scanf("%d", &anoNascimento);

    printf("\nData de Nascimento: %d/%d/%d", diaNascimento, mesNascimento, anoNascimento);

    
}