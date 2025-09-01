# include <stdio.h>

int main(void)
{
    // criar  matriz de 10 elementos
    int n = 20;
    int matriz[n];

    // preencher a matriz
    for (int i = 0; i < n; i++){
        matriz[i] = 1 + i;
    }

    // exiba a matriz criada
    printf("\nMatriz inicial: { ");
    for (int i = 0; i < n; i++){
        printf("%i, ", matriz[i]);
    }
    printf("...}\n");

    // remover varios elementos impares sem copiar a matriz
    int reescrever_posicao = 0;
    for (int i = 0; i < n; i++)
    {
        if (matriz[i] % 2 != 0)
        {
            matriz[reescrever_posicao] = matriz[i];
            reescrever_posicao++;
        }
    }
    n = reescrever_posicao;

    // exiba a matriz criada
    printf("\nMatriz com todos os pares removidos: { ");
    for (int i = 0; i < n; i++){
        printf("%i, ", matriz[i]);
    }
    printf("...}\n");

}