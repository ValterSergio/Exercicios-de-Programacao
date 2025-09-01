# include <stdio.h>
# include <stdlib.h>

int verificar_intervalo(float nota){

    if (nota >= 0 && nota <= 10){
        printf("Nota validada !\n");
        return 1;
    } else {
        printf("Erro: Nota fornecida fora do intervalo.\n");
        printf("Informe uma nota entre 0 e 10.");
        return -1;
    }
}

float obter_nota(){
    float nota;
    short int validar;
    printf("Informe o valor da nota: ");
    validar = scanf("%f", &nota);
    if (validar != 1){
        printf("Erro: Informe Apenas Numeros Válidos");
        return -1;
    }

    if (verificar_intervalo(nota) == 1){
        return nota;
    } else {
        return -1;
    }
}

float calcular_media(float a, float b, float c){
    return (a + b + c) / 3;
}

short int menu(){
    short int escolha;
    while (1)
    {
        /* Calcular Média, Sair do Programa */
        printf("Bem Vindo.\n");
        printf("Aperte 1 para comecar ou 0 para sair: ");
        short int validar_escolha = scanf("%hd", &escolha);
        if (validar_escolha != 1){
            printf("Erro: Informe Apenas Numeros.\n");
            continue;
        }

        if (escolha == 0){
            printf("Obrigado, volte sempre.\n");
            exit(0);
        }

        return 1;

    }
    
}

void verificar_situacao(float media){
    if (media >= 6){
        printf("Aluno Aprovado. Nota final: %.2f\n", media);
    } else if (media < 6 && media > 3)
    {
        printf("Aluno em Recuperacao !!!\n");
        printf("Por favor informe a nota de recuperacao abaixo. \n");
        float nota = obter_nota();
        if (nota >= 0){
            if (nota > 5){
                printf("Aluno Aprovado pela recuperacao. Nota final: %.2f\n", nota);
            } else {
                printf("Aluno Reprovado. Nota final: %.2f\n", nota);
            }
        }
    } else if (media <= 3){
        printf("Aluno Reprovado. Nota Final: %.2f\n", media);
    }    
    
    
}
int main(){
    float media;
    while (1)
    {
        printf("\n--> Calculadora de Médias <--\n");
        if (menu() == 1){
            float nota1 = obter_nota();
            float nota2 = obter_nota();
            float nota3 = obter_nota();

            if (nota1 >= 0 && nota2 >= 0 &&  nota3 >= 0){
                media = calcular_media(nota1, nota2, nota3);
                verificar_situacao(media);
            } else {
                exit(0);
            }
        }
    }
    return 0;
    
}