#include <stdio.h>

int main(void){
    char meu_char = 'z' ; // 'A' tem valor ASCII 65
    int ascii_a = (int) meu_char;

    char guardar_resto[9]; // 8 bits + '\0'
    guardar_resto[8] = '\0'; // marca fim da string

    int valor = ascii_a;
    int pos = 7;

    while (pos >= 0) {
        int resto = valor % 2;
        guardar_resto[pos] = resto + '0'; // converte 0/1 para '0'/'1'
        valor = valor / 2;
        pos--;
    }

    printf("Representacao binaria de '%c' (ASCII %d): %s\n", meu_char, ascii_a, guardar_resto);

    return 0;
}
