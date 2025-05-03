#include <stdio.h>
#include <string.h>

/*
Problema 8 do Project Euler:

Dado um número de 1000 dígitos, o objetivo é encontrar o maior produto possível
de 13 dígitos consecutivos.

A estratégia consiste em percorrer o número, separando todas as combinações possíveis
de 13 dígitos, calcular o produto de cada uma e manter o maior valor encontrado.

Link do desafio: https://projecteuler.net/problem=8
*/

int main() {
    // Número gigante fornecido pelo problema
    char numero_grande[] =
        "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843"
        "8586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557"
        "6689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749"
        "3035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776"
        "6572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397"
        "5369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474"
        "8216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586"
        "1786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408"
        "0719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606"
        "0588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";

    int tamanho_total = strlen(numero_grande);
    int tamanho_sequencia = 13;

    unsigned long long maior_produto = 0;
    char sequencia_maior_produto[14] = "";

    for (int posicao = 0; posicao < tamanho_total; posicao++) {
        for (int deslocamento = 0; deslocamento < tamanho_total - posicao - 1; deslocamento++) {
            if (deslocamento + tamanho_sequencia > tamanho_total) {
                break;
            }

            unsigned long long produto_atual = 1;

            for (int i = 0; i < tamanho_sequencia; i++) {
                char caractere = numero_grande[deslocamento + i];
                int digito = caractere - '0';
                produto_atual *= digito;
            }

            if (produto_atual > maior_produto) {
                maior_produto = produto_atual;
                strncpy(sequencia_maior_produto, &numero_grande[deslocamento], tamanho_sequencia);
                sequencia_maior_produto[tamanho_sequencia] = '\0';
            }
        }
    }

    printf("Maior produto encontrado: %llu\n", maior_produto);
    printf("Sequência correspondente: %s\n", sequencia_maior_produto);

    return 0;
}
