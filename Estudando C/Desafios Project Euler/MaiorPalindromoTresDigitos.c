/* 
    Um número palíndromo é aquele que pode ser lido da mesma
forma em ambos os sentidos.
    O maior palíndromo formado pelo produto de dois números 
de 2 dígitos é 9009 = 91 × 99.
    Encontre o maior palíndromo formado pelo produto de dois
números de 3 dígitos.
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Função para inverter string
void inverterString(char str[]) {
    int inicio = 0;
    int final = strlen(str) - 1;
    char temporaria;

    while (inicio < final) {
        temporaria = str[inicio];
        str[inicio] = str[final];
        str[final] = temporaria;

        inicio++;
        final--;
    }
}

int main() {
    int num = 100;
    int mult, produto;
    char produtostr[10];
    char copia[10];
    int palindromo = 0;
    int palindromoTemp = 0;

    while (num <= 999) {
        mult = num;
        while (mult <= 999) {
            // Obtendo o produto de dois números
            produto = num * mult;

            // Convertendo o produto para string
            sprintf(produtostr, "%d", produto);

            // Criando uma cópia para comparação
            strcpy(copia, produtostr);

            // Invertendo a string
            inverterString(produtostr);
            
            // Verifica se a string original e a invertida são iguais
            if (strcmp(copia, produtostr) == 0) {
                // Converte string para inteiro
                palindromoTemp = atoi(copia);

                // Atualiza o maior palíndromo encontrado
                if (palindromoTemp > palindromo) {
                    palindromo = palindromoTemp;
                }
            }
            mult++;  
        }
        num++;
    }

    // Exibir o maior palíndromo encontrado
    printf("Maior palíndromo: %d\n", palindromo);

    return 0;
}
