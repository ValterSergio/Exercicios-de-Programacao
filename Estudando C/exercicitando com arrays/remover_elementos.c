# include <stdio.h>

int main(void)
{
    // prencher um vetor com 100 numeros
    int matriz[100];

    for (int i = 0; i < 100; i++)
    {
        matriz[i] = i + 1;
    }
    // exibir matriz e seus valores
    printf("Todos os numeros: { ");
    for (int i = 0; i < 100; i++)
    {
        printf("%i, ", matriz[i]);
    }
    printf("... }\n");
    
    // não temos metodos para remover arrays
    // devemos criar um novo array e copiar os elementos
    int matriz_pares[100];

    int indice = 0;
    for (int i = 0; i < 100; i++)
    {
        // vamos remover os valores impares
        if (matriz[i] % 2 == 0){
            matriz_pares[indice] = matriz[i];
            indice++;
        }
    }

    // exibe os valores salvo na nova matriz de elementos pares
    printf("\n\nRemovendo os numeros IMPARES da matriz\n\n");
    printf("\nNumeros pares: { ");
    for (int i = 0; i < indice; i++)
    {
        printf("%i, ", matriz_pares[i]);
    }
    printf("... }");
}