# include <stdio.h>

int main(void)
{
    // crie uma matriz com 10 elementos
    int n = 10;
    int matriz[n];

    // prenche a matriz
    for (int i = 0; i < n; i++)
    {
        matriz[i] = i + 1;
    }

    // exiba a matrix criada
    printf("\nMatriz inicial: { ");
    for (int i = 0; i < n; i++){
        printf("%i, ", matriz[i]);
    }
    printf("...}\n");

    // escolhe um numero qualquer para remover
    int remover;
    printf("\nEscolha um numero de 1 a %i para remover: ", n);
    scanf("%i", &remover);

    // encontre a posição do valor a ser removido
    int posicao = -1;
    for (int i = 0; i < n; i++)
    {
        if (matriz[i] == remover){
            posicao = i;
            break;
        }
    }

    // verifica se realmente foi encontrado
    if (posicao == -1)
    {
        printf("\nvalor não encontrado !!!\n");
    } else {
        for (int i = posicao; i < n - 1; i++){
            matriz[i] = matriz[i + 1];
        }
        n--;
    }
    
    // exibir o matriz com o valore removido
   // exiba a matrix criada
    printf("\nMatriz com valor removido: { ");
    for (int i = 0; i < n; i++){
        printf("%i, ", matriz[i]);
    }
    printf("...}\n");

}