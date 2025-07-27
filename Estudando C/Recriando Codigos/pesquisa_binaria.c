# include <stdio.h>

int pesquisa_binaria(int numeros[], int tamanho, int alvo)
{
    int inicio = 0;
    int fim = tamanho - 1;

    while (inicio <= fim)
    {
        int metade = (inicio + fim) / 2;
        int comparar = numeros[metade];
        if (comparar == alvo){
            return metade;
        } else if (comparar < alvo)
        {
            inicio = metade + 1;
        } else
        {
            fim = metade - 1;
        }
        
        

    }
    return -1;
}

int main(){
    int numeros[300];

    // obter tamanho do vetor
    int tamanho = sizeof(numeros) / sizeof(numeros[0]);
    
    // prencher vetor para testar pesquisa binaria
    for (int i = 0; i <= tamanho; i++){
        numeros[i] = i * 2 + 3;
    }

    // um alvo aleatorio
    int alvo = 99;

    int localizar = pesquisa_binaria(numeros, tamanho, alvo);

    if (localizar == -1){
        printf("Numero %d nao encontrado.", alvo);
    } else {
        printf("Numero localizado na posicao %d.", localizar);
    }

    printf("\nValor alvo: %d", alvo);
    printf("\nValor encontrado na posicao %d: %d", localizar, numeros[localizar]);

}