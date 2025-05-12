/*
    Programa que lê uma entrada do teclado e exibe 
    informações sobre ela.
    Inclui verificações de tipo e características da string.
    Mostra o tipo primitivo do dado inserido 
*/
#include <stdio.h>
#include <ctype.h>

int main(void) {
    char c;
    printf("\nDigite um caractere: ");
    scanf("%c", &c);

    printf("\n\tInformacoes da Entrada\n\n");

    if (isdigit(c)) {
        // isdigit - Numeros de 0 a 9
        // retorna 1 se verdadeiro, 0 se falso
        printf("Eu sou um numero.\n");
    }

    if (isalpha(c)) {
        // isalpha - Qualquer letra (a-z ou A-Z)
        printf("Eu sou uma letra.\n");
    }

    if (isalnum(c)) {
        // isalnum - Alfanumerico (letra OU numero)
        printf("Eu sou alfanumerico.\n");
    }

    if (isspace(c)) {
        // isspace - Qualquer espaco em branco (espaço, tab, \n, etc)
        printf("Eu sou um espaco em branco.\n");
    }

    if (isupper(c)) {
        // isupper - Qualquer letra maiuscula
        printf("Eu sou uma letra maiuscula.\n");
    }

    if (islower(c)) {
        // islower - Qualquer letra minuscula
        printf("Eu sou uma letra minuscula.\n");
    }

    if (ispunct(c)) {
        // ispunct - Qualquer simbolo de pontuacao (ex: ! ? . , ; : etc)
        printf("Eu sou um simbolo de pontuacao.\n");
    }

    if (isxdigit(c)) {
        // isxdigit - Digitos hexadecimais (0-9, a-f, A-F)
        printf("Eu sou um digito hexadecimal.\n");
    }

    if (isprint(c)) {
        // isprint - Qualquer caractere imprimivel (exclui os de controle)
        printf("Eu sou um caractere imprimivel.\n");
    }

    if (isgraph(c)) {
        // isgraph - Qualquer caractere visivel (imprimivel, exceto espaco)
        printf("Eu sou um caractere visivel (nao sou espaco).\n");
    }

    return 0;
}
