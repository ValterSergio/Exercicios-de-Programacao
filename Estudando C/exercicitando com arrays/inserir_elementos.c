# include <stdio.h>

int main(void)
{
    int n;
    // pergunte quantos valores vao ser adicionados na matriz
    printf("Informe o total de numeros a ser adicionado na matriz: ");
    scanf("%i", &n);
    
    // declare a matriz com tamanho definido pelo usuario
    int matriz[n];

    // acrescente os valores na matriz
    for (int i = 0; i < n; i++)
    {
        printf("Informe o valor a ser guardado na matriz: ");
        scanf("%i", &matriz[i]);
        printf("Valor %i adicionado com sucesso !!!\n", matriz[i]);
    }

    // exiba os valores na matriz
    printf("\n\nValores Adicionados na matriz !!!\n\n");
    for (int i = 0; i < n; i++){
        printf("Item %i: %i\n", i, matriz[i]);
    }

    printf("\nFim !!!");
}