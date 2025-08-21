# include <stdio.h>

int main(void)
{

    short colunas = 10;
    short linhas = 10;

    // criar um vetor
    int vetor[colunas][linhas];

    printf("\nCriando vetor bidimensional !!!\n");
    
    int contador = 0;
    for (int i = 0; i < linhas; i++)
    {
        for (int j = 0; j < colunas; j++)
        {
            contador++;
            vetor[i][j] = contador;
            printf(" %i ", vetor[i][j]);
        }
        printf("\n");
    }

    /* 
     * todo numero que for divisivel por 3 deve 
     * ser substituido por -1, e todo numero que
     * for divisivel por 5 deve ser substituido
     * por -2 todo numero que for divisivel por 3
     * e 5 deve ser substituido por 0
     * 
     */
     printf("\n\nModificando o vetor !!!\n\n");
     for (int i = 0; i < linhas; i++)
     {
        for (int j = 0; j < colunas; j++)
        {
            int valor = vetor[i][j];
            
            // é divisivel por 3 e 5 ?
            if (valor % 3 == 0 && valor % 5 == 0)
            {
                // modifica o valor para 0
                vetor[i][j] = 0;
            } else if (valor % 3 == 0)
            {
                // modifica o valor para -1
                vetor[i][j] = -1;
            } else if (valor % 5 == 0)
            {
                // modifica o valor para -2
                vetor[i][j] = -2;
            }

            // até aqui o vetor ja foi modificado
            printf(" %i ", vetor[i][j]);
        }
        printf("\n");
     }
    

}