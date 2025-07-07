# include <stdio.h>

int main(){
    int tempos[3];
    int contador = 0;

    for (int i = 0; i < 3; i++)
    {
        printf("Informe o tempo do atleta em segundos: ");
        
        short int validar = scanf("%d", &tempos[i]);

        if (validar != 1){
            printf("Erro: Informe um numero inteiro.\n");
            return -1;
        }

        if (tempos[i] < 0){
            printf("Erro: Valor informado deve ser Maior ou Igual a Zero ( Em caso de falha tecnica)");
            return -1;
        }

        contador += tempos[i];
    }

    float media = (float) contador / 3;
    
    if (media > 20){
        printf("Atleta Desclassificado.\t\nTempo Medio: %.2f segundos.\n", media);
    } else if (media > 15 && media <= 20){
        printf("Atleta Categoria Bronze.\t\nTempo Medio: %.2f segundos\n", media);
    } else if (media > 10 && media <= 15){
        printf("Atleta Categoria Prata.\t\nTempo Medio: %.2f segundos.\n", media);
    } else if (media <= 10){
        printf("Atleta Categoria Ouro.\t\nTempo Medio: %.2f segundos.\n", media);
    }

    
}