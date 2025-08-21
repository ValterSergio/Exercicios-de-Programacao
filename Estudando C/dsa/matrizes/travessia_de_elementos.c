# include <stdio.h>
/* Atravessando todas as letras do alfabeto */
int main(void)
{
    // quantas letras maiusculas temos ?
    int maiusculas = 90 - 65/ 
    
    // soma mais um para o caractere nulo
    maiusculas++;

    char string_maiusculas[maiusculas];
    
    int contador = 0;
    for (int i = 65; i <= 90; i++)
    { 
        
        // forçar a conversão do int para char
        char letra = (char) i;
      
        // usar o contador para o indice da matriz
        // guardar a letra maiuscula dentro da matriz de carateres
        string_maiusculas[contador] = letra;
        
        // incrementar contador
        contador++;
      
        printf("Total de letras: %i | Letra: %c\n", contador, letra);
    }

    string_maiusculas[contador] = '\0';
    
    // exibe a string_maiusculas
    printf("\nLetras maiusculas: %s\n\n", string_maiusculas);

    // obter uma string com todas as minusculas
    int primeira_letra = 97;
    int ultima_letra = 122; 

    // contador esta com o total de letras
    char string_minusculas[contador];

    // posso zerar o contador
    contador = 0;
    for (int i = primeira_letra; i <= ultima_letra; i++)
    {
        // printf("\n-> %i valor de i", i);
        char letra = (char) i;
        string_minusculas[contador] = letra;
        contador++;
    }

    string_minusculas[contador] = '\0';
    printf("\nLetras minusculas: %s \n\n", string_minusculas);
    printf("%i", contador);
}