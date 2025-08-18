# include <stdio.h>

int main(void)
{
    // criar uma matriz de 10 elementos
    int n = 10;
    int matriz[n];

    // preencher matriz
    for (int i = 0; i < n; i++ )
    {
        matriz[i] = i + 1;
    }

    // definir o alvo da busca
    int alvo = 5;

    // buscar elemento
    int posicao_elemento = -1;
    for (int i = 0; i < n; i++)
    {
        if (matriz[i] == alvo){
            posicao_elemento = i;
            break;
        }
    }

    if (posicao_elemento != -1)
    {
    printf("\nAlvo localizado na posicao %i\n", posicao_elemento);
    printf("valor encontrado: %i\n\n", matriz[posicao_elemento]);
    } else {
        printf("\nElemento não encontrado\n");
    }
}