# include <stdio.h>

// função para concatenar strings

char *concatenar(char *str_destino, char *str_origem)
{
    // Contar o total de caracteres dentro da string de origem
    int i = 0;

    // trasferir os caracteres da string de origem para destino
    int j = 0;

    // incrementar o contador de caracteres até o caracter nulo '\0'
    while (str_destino[i] != '\0')
    {
        i++;
    }

    // como já sabemos o total de caracter, podemos começar a transferir os caracteres
    while (str_origem[j] != '\0')
    {
        // Unimos as strings j(join) começa com 0 aqui, enquanto i(contador de caracteres) começa com o total de caracteres na string original
        str_destino[i] = str_origem[j];

        // incrementa ambas variaveis
        i++;
        j++;
    }

    // não se pode esquecer do caracter nulo, que representa o fim (algo extremamente importante em C)
    str_destino[i] = '\0';

    // retorna a string concatenada
    return str_destino;
}

// bloco main para testar a função
int main()
{
    // a string de destino deve ter espaço suficiente para receber a string de origem
    char str_destino[50] = "Minha primeira Funcao para ";
    char str_origem[] = "concatenar strings em C.";

    // exibir o resultado e descobrir se deu bom rs
    printf("%s", concatenar(str_destino, str_origem));
    return 0;

}