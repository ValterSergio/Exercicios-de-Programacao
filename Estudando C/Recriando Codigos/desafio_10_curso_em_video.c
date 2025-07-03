/*
    Programa que lê o valor em reais e converte para dólares
    com base na cotação   
*/
# include <stdio.h>

int main(void){
    
    // valor do dolar atualmente
    float dolar = 3.27;
    float totalReais;


    // entrada - precisa saber o total em reais para dolar
    printf("\n\t--- Converter de Dolar para Real \n");
    printf("\nInforme a quantia em reais: ");
    scanf("%f", &totalReais);

    // faz a conversão do real para o dólar
    float totalDolar = totalReais / dolar;

    // exibe
    printf("%.2f reais compra -> %.2f dolares", totalReais, totalDolar);


}