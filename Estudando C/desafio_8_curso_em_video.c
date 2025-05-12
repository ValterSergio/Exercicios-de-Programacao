/*
    Faça um programa que lê um valor em metros e exibe suas conversões para
    varias unidades de medida.
    Este programa deve converter de Metros para quilometro, hectometros, decametros
    metros, decimetros, centimetros e milimetros
*/

#include <stdio.h>

int main(void){
    float metro;
    printf("Digite Total em Metros: ");
    scanf("%f", &metro);
    
    // metro 1
    float quilometro = metro / 1000; // 1 km igual a 1000 metros
    float hectometro = metro / 100; // 1 hectometro igual 100 metros 
    float decametro = metro / 10; // 1 decametro igual 10 metros
    float decimetro = metro * 10; // 1 metro tem 10 Decimetros
    float centimetro = metro * 100; // 1 metro tem 100 centimetros
    float milimetros = metro * 1000; // 1 metro tem 1000 centimetros
    

    // saida
    printf("\nConversões:\n");
    printf("Quilômetros: %.3f km\n", quilometro);
    printf("Hectômetros: %.2f hm\n", hectometro);
    printf("Decâmetros : %.2f dam\n", decametro);
    printf("Metros     : %.2f m\n", metro);
    printf("Decímetros : %.0f dm\n", decimetro);
    printf("Centímetros: %.0f cm\n", centimetro);
    printf("Milímetros : %.0f mm\n", milimetros);

    return 0;

}