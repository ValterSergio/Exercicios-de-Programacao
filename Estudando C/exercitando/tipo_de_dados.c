# include <stdio.h>

int main(){

    short int idade;
    float altura;
    char nome[10];

    printf("Digite sua idade: ");
    scanf("%d", &idade);

    printf("Digite sua altura: ");
    scanf("%f", &altura);

    printf("Digite seu nome: ");
    scanf("%s", nome);

    printf("\n---> Dados Fornecidos <---\n%d, %f, %s\n--> FIM <--\n", idade, altura, nome);

    printf("---> Espaço Ocupado por cada variavel <---\n");
    printf("A variavel idade ocupa %lu de memoria.", sizeof(idade));
    printf("\nA variavel altura ocupa %lu de memoria.", sizeof(altura));
    printf("\nA variavel nome ocupa %lu de memoria.", sizeof(nome));

    // fim
    printf("\n---> FIM <---\n");
    return 0;
}