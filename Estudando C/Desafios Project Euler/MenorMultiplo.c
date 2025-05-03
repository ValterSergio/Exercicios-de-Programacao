/*
2520 é o menor numero que pode ser dividido por cada um dos numeros de 1 a 10 sem qualquer resto.

Qual é o menor número positivo que é uniformemente divisível por todos os números de 1 a 20?
*/

# include <stdio.h>

#define MAX_FATORES 100
#define MAX_NUMS 100

// fatorar número
void fatorarNumero(int num, int fatores[], int expoentes[], int *tamanho){

    // inicia o divisor
    int divisor = 2;
    
    // controla o indice dos vetores
    *tamanho = 0;

    // enquanto o numero não for totalmente fatorado
    while (num > 1){

        // salvar o total de vezes que o numero é dividido
        int cont = 0;

        // enquanto for possivel realizar a divisão
        // com divisor atual 
        while (num % divisor == 0){
            num = num / divisor;

            // contamos quantas vezes esse divisor se repete
            cont++;

        }

        // se foi possivel realizar alguma divisão
        if (cont > 0){
            // guardamos o fator de dvisão
            fatores[*tamanho] = divisor;

            // guardamos os expoentes(as vezes que o fator se repete)
            expoentes[*tamanho] = cont;

            // pulamos para o proximo indice da lista
            (*tamanho)++;
        }

        divisor++;
    }
}

int encontrarMMC(int lista[], int tamanho_lista) {
    // Vetor que armazena os fatores primos únicos encontrados
    int fatores_gerais[MAX_FATORES] = {0};

    // Vetor que armazena o maior expoente de cada fator primo
    int expoentes_gerais[MAX_FATORES] = {0};

    // Contador para saber quantos fatores únicos já temos
    int total_fatores = 0;

    // percorre cada número da lista original
    for (int i = 0; i < tamanho_lista; i++) {

        // vetores temporários para armazenar a fatoração do número atual
        int fatores[MAX_FATORES], expoentes[MAX_FATORES];

        // quantidade de fatores únicos do número atual
        int tam_fatores = 0;

        // fatoramos o número atual e preenchemos os vetores
        fatorarNumero(lista[i], fatores, expoentes, &tam_fatores);

        // percorre os fatores da fatoração atual
        for (int j = 0; j < tam_fatores; j++) {

            int fator = fatores[j];         // fator primo atual
            int expoente = expoentes[j];   // expoente desse fator

            int encontrado = 0; // indica se o fator já está em fatores_gerais

            // verifica se o fator já está na lista de fatores gerais
            for (int k = 0; k < total_fatores; k++) {
                if (fatores_gerais[k] == fator) {
                    // se o novo expoente for maior, atualizamos
                    if (expoente > expoentes_gerais[k]) {
                        expoentes_gerais[k] = expoente;
                    }

                    // marcamos que o fator já foi encontrado
                    encontrado = 1;
                    break;
                }
            }

            // se o fator ainda não estiver na lista, adicionamos ele
            if (!encontrado) {
                fatores_gerais[total_fatores] = fator;          // adiciona o novo fator
                expoentes_gerais[total_fatores] = expoente;     // com seu expoente
                total_fatores++;                                // incrementa a contagem
            }
        }
    }

    // variável que armazenará o resultado final do MMC
    int mmc = 1;

    // multiplicamos os fatores elevados aos seus maiores expoentes
    for (int i = 0; i < total_fatores; i++) {
        for (int j = 0; j < expoentes_gerais[i]; j++) {
            mmc *= fatores_gerais[i];
        }
    }

    // retornamos o MMC calculado
    return mmc;
}

int main(){
    int mmc[20]= {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};

    int resultado = encontrarMMC(mmc, 19);
    printf("%d", resultado);
}
