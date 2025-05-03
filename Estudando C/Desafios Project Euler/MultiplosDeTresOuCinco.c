/*
 * Se listarmos todos os números naturais abaixo de 10
 * que são múltiplos de 3 ou 5, nós teremos 3, 5, 6 e 9 e
 * a soma desses múltiplos é 23
 * 
 * Problema: Encontre a soma de todos os multiplos de 3 ou 5
 * abaixo de 1000
 */
#include <stdio.h>

int main(){
    int somar = 0;
    for (int i =0; i < 1000; i++){
        if (i % 5 == 0 || i % 3 == 0){
            somar += i;
        }
    }
    printf("A soma dos multiplos de 3 e 5 ate mil e %d", somar);
    return 0;
}
